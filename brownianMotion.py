import sys
import scipy.stats
import scipy.integrate
import scipy.special
import math
from scipy import inf


# ---------------- Calcuation--------------
def pdflp(x, p0, v, t1):
    return scipy.stats.norm(
        math.log(p0), math.sqrt(t1) * v / math.sqrt(365.2425 * 24)
    ).pdf(x)


def cdfmaxlp(x, v, t1, t2):
    return 1 - scipy.special.erf(
        x / (v * math.sqrt(t2 - t1) / math.sqrt(24 * 365.2425 / math.sqrt(2.0)))
    )


def upandin(p0, v, p1, p2, t1, t2):
    integrand = lambda x: (pdflp(x, p0, v, t1) * cdfmaxlp(math.log(p1) - x, v, t1, t2))
    return scipy.integrate.quad(integrand, -inf, math.log(p1))


def hitleftedge(p0, v, p1, p2, t1, t2):
    integrand = lambda x: (pdflp(x, p0, v, t1) * 1)
    return scipy.integrate.quad(integrand, math.log(p1), math.log(p2))


def downandin(p0, v, p1, p2, t1, t2):
    integrand = lambda x: (pdflp(x, p0, v, t1) * cdfmaxlp(x - math.log(p2), v, t1, t2))
    return scipy.integrate.quad(integrand, math.log(p2), inf)


def probabilitytouch(p0, v, p1, p2, t1, t2):
    return (
        upandin(p0, v, p1, p2, t1, t2)
        + hitleftedge(p0, v, p1, p2, t1, t2)
        + downandin(p0, v, p1, p2, t1, t2)
    )

def dayDistanceCal(targetDate1,targetDate2):
    delta = -1
    delta = targetDate2-targetDate1
    return delta.days