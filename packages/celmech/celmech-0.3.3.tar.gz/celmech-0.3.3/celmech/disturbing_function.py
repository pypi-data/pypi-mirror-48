from sympy import S, diff, lambdify, symbols, sqrt, cos,sin, numbered_symbols, simplify,binomial, hyper, hyperexpand, Function, factorial,elliptic_k,elliptic_e, expand_trig
from . import clibcelmech
from ctypes import Structure, c_double, POINTER, c_float, c_int, c_uint, c_uint32, c_int64, c_long, c_ulong, c_ulonglong, c_void_p, c_char_p, CFUNCTYPE, byref, create_string_buffer, addressof, pointer, cast
from scipy.integrate import quad
import math
import numpy as np
from scipy.optimize import leastsq


def laplace_coefficient(s,j,n,a):
    """
    Calculates nth derivative with respect to a (alpha) of Laplace coefficient b_s^j(a).
    Code due to Jack Wisdom. Changed notation to match Murray & Dermott (Eq. 6.67)
    
    Arguments
    ---------
    s : float 
        half-integer parameter of Laplace coefficient. 
    j : int 
        integer parameter of Laplace coefficient. 
    n : int 
        return nth derivative with respect to a of b_s^j(a)
    a : float
        semimajor axis ratio a1/a2 (alpha)
    """    
    clibcelmech.laplace.restype = c_double
    return clibcelmech.laplace(c_double(s), c_int(j), c_int(n), c_double(a))

def general_order_coefficient(res_j, order, epower, a):
    clibcelmech.GeneralOrderCoefficient.restype = c_double
    return clibcelmech.GeneralOrderCoefficient(c_int(res_j), c_int(order), c_int(epower), c_double(a))

# Vector of resonance coefficients
def get_res_coeff_vector(j,k):
    """Returns a vector comprised of all sub-resonance coefficients for the j:j-k mean motion resonance""" 
    res_pratio = float(j - k) /float(j)
    alpha = res_pratio**(2./3.)
    Cjkl = general_order_coefficient
    return np.array([Cjkl(j,k,l,alpha) for l in range(k+1)],dtype=np.float64)

def get_fg_coeffs(res_j,res_k):
    """Get 'f' and 'g' coefficients for approximating the disturbing function coefficients associated with an MMR."""
    res_pratio = float(res_j - res_k) /float(res_j)
    alpha = res_pratio**(2./3.)
    vec = get_res_coeff_vector(res_j,res_k)
    resids_vec_fn = lambda fg: vec - np.array([binomial(res_k,l) * fg[0]**(l) * fg[1]**(res_k-l) for l in range(res_k+1)],dtype=np.float64)
    ex = (1-alpha)
    f0 = -1 / ex
    g0 = 1 / ex
    f,g = leastsq(resids_vec_fn,(f0,g0))[0]
    return f,g

def Xlm0(l,m,e):
    """ 
        Get the closed-form expression for the Hansen coefficient X^(l,m)_0
        which appears in the secular component of the disturbing function (e.g., Mardling 2013) 
    """
    a =  (m-l-1) / S(2)
    b = a + 1/ S(2)
    c = m + 1
    fn = hyperexpand(hyper([a,b],[c],e*e))
    return (-e / 2)**m * binomial(l+m+1,m) * fn

def secular_eps_l_Df_m(l,m,e,e1):
    """
        Get the secularly-averaged value of 
            eps^l * exp[ i*m*(f'-f) ] 
        where l and m are integers, f' and f are true anamolies, and
            eps =  (r/a) / (r'/a')  - 1
        where r and a are radial distance and semi-major axis.
    """
    s = 0
    for i in range(l+1):
        s = s + binomial(l,i)*(-1)**(l-i) * Xlm0(i,m,e) * Xlm0(-i-1,m,e1)
    return s
def secular_DF_harmonic_term(e,e1,dw,m,order):
    s = 0
    b = Function('b') 
    alpha = symbols('alpha')
    if order%2==0:
        maxk = order + 1
    else:
        maxk=order
    for i in range(maxk):
     s = s + alpha**i *  b(1/S(2),m,i,alpha) / factorial(i) * secular_eps_l_Df_m(i,m,e,e1)
    if m==0:
        s=s / S(2)
    return s * cos(m*dw)
def secular_DF(e,e1,w,w1,order):
    """ 
    Return the secular component of the disturbing function for coplanet planets up to
    the specified order in the planets' eccentricities for an inner plaent with eccentricity 
    and longitude of periapse (e,w) and outer planet eccentricity/longitude of periape (e1,w1)
    """
    s = 0
    dw = w1 - w
    # Introduce `eps' as order parameter multiplying eccentricities. 
    # 'eps' is set to 1 at teh end of calculation.
    eps = S('epsilon')
    maxM = int( np.floor( order / 2.) )
    for i in range(maxM+1):
        term = secular_DF_harmonic_term(eps*e,eps*e1,dw,i,order) 
        term = term.series(eps,0,order+1).removeO()
        s = s + expand_trig(term) 
    return s.subs(eps,1)
def secular_DF_full(e,e1,w,w1,order):
    """ 
    Same as 'secular_DF' but uses the full expression for the Hansen coefficients that enter
    the disturbing function. While these expressions are typically more complicated when written
    in terms of eccentricity, they may be simpler when written in terms of canoncial momenta.
    """
    s = 0
    dw = w1 - w
    maxM = int( np.floor( order / 2.) )
    for i in range(maxM+1):
        s = s + secular_DF_harmonic_term(e,e1,dw,i,order) 
    return s

class laplace_B(Function):
    nargs=4
    @classmethod
    def eval(cls, s,j,n,alpha):
    # laplace coeffcients don't evaluate well with the C code
    # for large n, therefore I've substituted the exact expression
    # in terms of the elliptic K function when j=0
        if j is S.Zero:
            x = S('x')
            exprn = 4 / np.pi * diff(elliptic_k(x*x),x,n)
            return exprn.subs(x,alpha)
        elif j is S.One:
            x = S('x')
            exprn0 =  4 / np.pi *  (elliptic_k(x*x) - elliptic_e(x*x) ) / x 
            exprn = diff(exprn0, x ,n)
            return exprn.subs(x,alpha)
        else:
            return laplace_coefficient(s,j,n,alpha)/ alpha**n
