import math
from scipy.integrate import quad

INTEGRAL_EPS = math.pow(10, -4)

def integral(f, a: float, b: float, eps=INTEGRAL_EPS) -> float:
    result, _ = quad(f, a, b)
    return result