# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from time import clock  
from sympy import *
from __future__ import division

x = Symbol('x')

# <codecell>

def asec(x):
    return acos(1/x)

# <codecell>

Charlwood = dict()
Charlwood[ 1] = (asin(x)*log(x),-2*sqrt(1-x**2)+atanh(sqrt(1-x**2))-x*asin(x)*(1-log(x))+sqrt(1-x**2)*log(x))
Charlwood[ 2] = (x*asin(x)/sqrt(1-x**2),x-sqrt(1-x**2)*asin(x))
Charlwood[ 3] = (asin(sqrt(x+1)-sqrt(x)),((sqrt(x)+3*sqrt(1+x))*sqrt(-x+sqrt(x)*sqrt(1+x)))/(4*sqrt(2))-(Rational(3,8)+x)*asin(sqrt(x)-sqrt(1+x)))
Charlwood[ 4] = (log(1+x*sqrt(1+x**2)),-2*x+sqrt(2*(1+sqrt(5)))*atan(sqrt(-2+sqrt(5))*(x+sqrt(1+x**2)))-sqrt(2*(-1+sqrt(5)))*atanh(sqrt(2+sqrt(5))*(x+sqrt(1+x**2)))+x*log(1+x*sqrt(1+x**2)))
Charlwood[ 5] = (cos(x)**2/sqrt(cos(x)**4+cos(x)**2+1),x/3+Rational(1,3)*atan((cos(x)*(1+cos(x)**2)*sin(x))/(1+cos(x)**2*sqrt(1+cos(x)**2+cos(x)**4))))
Charlwood[ 6] = (tan(x)*sqrt(1+tan(x)**4),(-Rational(1,2))*asinh(tan(x)**2)-atanh((1-tan(x)**2)/(sqrt(2)*sqrt(1+tan(x)**4)))/sqrt(2)+Rational(1,2)*sqrt(1+tan(x)**4))
Charlwood[ 7] = (tan(x)/sqrt(1+sec(x)**3),(-Rational(2,3))*atanh(sqrt(1+sec(x)**3)))
Charlwood[ 8] = (sqrt(tan(x)**2+2*tan(x)+2),asinh(1+tan(x))+sqrt(Rational(1,2)*(1+sqrt(5)))*atan((-sqrt(-1+sqrt(5))+sqrt(1+sqrt(5))*tan(x))/(sqrt(2)*sqrt(2+tan(x)*(2+tan(x)))))-sqrt((1/2)*(-1+sqrt(5)))*atanh((sqrt(1+sqrt(5))+sqrt(-1+sqrt(5))*tan(x))/(sqrt(2)*sqrt(2+tan(x)*(2+tan(x))))))
Charlwood[ 9] = (sin(x)*atan(sqrt(sec(x)-1)),Rational(1,2)*atan(sqrt(-1+sec(x)))-atan(sqrt(-1+sec(x)))*cos(x)+Rational(1,2)*cos(x)*sqrt(-1+sec(x)))
Charlwood[10] = (x**3*exp(asin(x))/sqrt(1-x**2),Rational(1,10)*exp(asin(x))*(3*x+x**3-3*sqrt(1-x**2)-3*x**2*sqrt(1-x**2)))
Charlwood[11] = ((x*log(1+x**2)*log(x+sqrt(1+x**2)))/sqrt(1+x**2),4*x-2*atan(x)-2*sqrt(1+x**2)*log(x+sqrt(1+x**2))+log(1+x**2)*(-x+sqrt(1+x**2)*log(x+sqrt(1+x**2))))
Charlwood[12] = (atan(x+sqrt(1-x**2)),-(asin(x)/2)+Rational(1,4)*sqrt(3)*atan((-1+sqrt(3)*x)/sqrt(1-x**2))+Rational(1,4)*sqrt(3)*atan((1+sqrt(3)*x)/sqrt(1-x**2))-Rational(1,4)*sqrt(3)*atan((-1+2*x**2)/sqrt(3))+x*atan(x+sqrt(1-x**2))-Rational(1,4)*atanh(x*sqrt(1-x**2))-Rational(1,8)*log(1-x**2+x**4))
Charlwood[13] = (x*atan(x+sqrt(1-x**2))/sqrt(1-x**2),-(asin(x)/2)+Rational(1,4)*sqrt(3)*atan((-1+sqrt(3)*x)/sqrt(1-x**2))+Rational(1,4)*sqrt(3)*atan((1+sqrt(3)*x)/sqrt(1-x**2))-Rational(1,4)*sqrt(3)*atan((-1+2*x**2)/sqrt(3))-sqrt(1-x**2)*atan(x+sqrt(1-x**2))+Rational(1,4)*atanh(x*sqrt(1-x**2))+Rational(1,8)*log(1-x**2+x**4))
Charlwood[14] = (asin(x)/(1+sqrt(1-x**2)),((-1+sqrt(1-x**2))*asin(x))/x+asin(x)**2/2-log(1+sqrt(1-x**2)))
Charlwood[15] = (log(x+sqrt(1+x**2))/(1-x**2)**Rational(3,2),(-Rational(1,2))*asin(x**2)+(x*log(x+sqrt(1+x**2)))/sqrt(1-x**2))
Charlwood[16] = (asin(x)/(1+x**2)**Rational(3,2),(x*asin(x))/sqrt(1+x**2)-asin(x**2)/2)
Charlwood[17] = (log(x+sqrt(x**2-1))/(1+x**2)**Rational(3,2),(-Rational(1,2))*acosh(x**2)+(x*log(x+sqrt(-1+x**2)))/sqrt(1+x**2))
Charlwood[18] = (log(x)/(x**2*sqrt(x**2-1)),sqrt(-1+x**2)/x-atanh(x/sqrt(-1+x**2))+(sqrt(-1+x**2)*log(x))/x)
Charlwood[19] = (sqrt(1+x**3)/x,(2*sqrt(1+x**3))/3-Rational(2,3)*atanh(sqrt(1+x**3)))
Charlwood[20] = (x*log(x+sqrt(x**2-1))/sqrt(x**2-1),-x+sqrt(-1+x**2)*log(x+sqrt(-1+x**2)))
Charlwood[21] = (x**3*(asin(x)/sqrt(1-x**4)),Rational(1,4)*x*sqrt(1+x**2)-Rational(1,2)*sqrt(1-x**4)*asin(x)+asinh(x)/4)
Charlwood[22] = (x**3*(asec(x)/sqrt(x**4-1)),-(sqrt(-1+x**4)/(2*sqrt(1-1/x**2)*x))+Rational(1,2)*sqrt(-1+x**4)*asec(x)+Rational(1,2)*atanh((sqrt(1-1/x**2)*x)/sqrt(-1+x**4)))
Charlwood[23] = (x*atan(x)*log(x+sqrt(1+x**2))/sqrt(1+x**2),(-x)*atan(x)+Rational(1,2)*log(1+x**2)+sqrt(1+x**2)*atan(x)*log(x+sqrt(1+x**2))-Rational(1,2)*log(x+sqrt(1+x**2))**2)
Charlwood[24] = (x*log(1+sqrt(1-x**2))/sqrt(1-x**2),sqrt(1-x**2)-(1+sqrt(1-x**2))*log(1+sqrt(1-x**2)))
Charlwood[25] = (x*log(x+sqrt(1+x**2))/sqrt(1+x**2),-x+sqrt(1+x**2)*log(x+sqrt(1+x**2)))
Charlwood[26] = (x*log(x+sqrt(1-x**2))/sqrt(1-x**2),sqrt(1-x**2)+atanh(sqrt(2)*x)/sqrt(2)-atanh(sqrt(2)*sqrt(1-x**2))/sqrt(2)-sqrt(1-x**2)*log(x+sqrt(1-x**2)))
Charlwood[27] = (log(x)/(x**2*sqrt(1-x**2)),-(sqrt(1-x**2)/x)-asin(x)-(sqrt(1-x**2)*log(x))/x)
Charlwood[28] = (x*atan(x)/sqrt(1+x**2),-asinh(x)+sqrt(1+x**2)*atan(x))
Charlwood[29] = (atan(x)/(x**2*sqrt(1-x**2)),-((sqrt(1-x**2)*atan(x))/x)-atanh(sqrt(1-x**2))+sqrt(2)*atanh(sqrt(1-x**2)/sqrt(2)))
Charlwood[30] = (x*atan(x)/sqrt(1-x**2),-asin(x)-sqrt(1-x**2)*atan(x)+sqrt(2)*atan((sqrt(2)*x)/sqrt(1-x**2)))
Charlwood[31] = (atan(x)/(x**2*sqrt(1+x**2)),-((sqrt(1+x**2)*atan(x))/x)-atanh(sqrt(1+x**2)))
Charlwood[32] = (asin(x)/(x**2*sqrt(1-x**2)),-((sqrt(1-x**2)*asin(x))/x)+log(x))
Charlwood[33] = (x*log(x)/sqrt(x**2-1),-sqrt(-1+x**2)+atan(sqrt(-1+x**2))+sqrt(-1+x**2)*log(x))
Charlwood[34] = (log(x)/(x**2*sqrt(1+x**2)),-(sqrt(1+x**2)/x)+asinh(x)-(sqrt(1+x**2)*log(x))/x)
Charlwood[35] = (x*asec(x)/sqrt(x**2-1),sqrt(x**2-1)*asec(x)-(sqrt(1-1/x**2)*x*log(x))/sqrt(x**2-1))
Charlwood[36] = (x*log(x)/sqrt(1+x**2),-sqrt(1+x**2)+atanh(sqrt(1+x**2))+sqrt(1+x**2)*log(x))
Charlwood[37] = (sin(x)/(1+sin(x)**2),-(atanh(cos(x)/sqrt(2))/sqrt(2)))
Charlwood[38] = ((1+x**2)/((1-x**2)*sqrt(1+x**4)),(1/sqrt(2))*atanh(sqrt(2)*(x/sqrt(1+x**4))))
Charlwood[39] = ((1-x**2)/((1+x**2)*sqrt(1+x**4)),atan((sqrt(2)*x)/sqrt(1+x**4))/sqrt(2))
Charlwood[40] = (log(sin(x))/(1+sin(x)),-x-atanh(cos(x))-(cos(x)*log(sin(x)))/(1+sin(x)))
Charlwood[41] = (log(sin(x))*sqrt(1+sin(x)),(4*cos(x))/sqrt(1+sin(x))-(2*cos(x)*log(sin(x)))/sqrt(1+sin(x))-4*atanh(cos(x)/sqrt(1+sin(x))))
Charlwood[42] = (sec(x)/sqrt(sec(x)**4-1),-(atanh((cos(x)*cot(x)*sqrt(sec(x)**4-1))/sqrt(2))/sqrt(2)))
Charlwood[43] = (tan(x)/sqrt(1+tan(x)**4),-(atanh((1-tan(x)**2)/(sqrt(2)*sqrt(1+tan(x)**4)))/(2*sqrt(2))))
Charlwood[44] = (sin(x)/sqrt(1-sin(x)**6),atanh((sqrt(3)*cos(x)*(1+sin(x)**2))/(2*sqrt(1-sin(x)**6)))/(2*sqrt(3)))
Charlwood[45] = (sqrt(sqrt(sec(x)+1)-sqrt(sec(x)-1)),sqrt(2)*(sqrt(-1+sqrt(2))*atan((sqrt(-2+2*sqrt(2))*(-sqrt(2)-sqrt(-1+sec(x))+sqrt(1+sec(x))))/(2*sqrt(-sqrt(-1+sec(x))+sqrt(1+sec(x)))))-sqrt(1+sqrt(2))*atan((sqrt(2+2*sqrt(2))*(-sqrt(2)-sqrt(-1+sec(x))+sqrt(1+sec(x))))/(2*sqrt(-sqrt(-1+sec(x))+sqrt(1+sec(x)))))-sqrt(1+sqrt(2))*atanh((sqrt(-2+2*sqrt(2))*sqrt(-sqrt(-1+sec(x))+sqrt(1+sec(x))))/(sqrt(2)-sqrt(-1+sec(x))+sqrt(1+sec(x))))+sqrt(-1+sqrt(2))*atanh((sqrt(2+2*sqrt(2))*sqrt(-sqrt(-1+sec(x))+sqrt(1+sec(x))))/(sqrt(2)-sqrt(-1+sec(x))+sqrt(1+sec(x)))))*cot(x)*sqrt(-1+sec(x))*sqrt(1+sec(x)))
Charlwood[46] = (x*log(x**2+1)*atan(x)**2,(-x)*atan(x)*(-3+log(1+x**2))+Rational(1,4)*(-6+log(1+x**2))*log(1+x**2)+Rational(1,2)*atan(x)**2*(-3-x**2+(1+x**2)*log(1+x**2)))
Charlwood[47] = (atan(x*sqrt(1+x**2)),Rational(1,2)*atan(sqrt(1+x**2)/x**2)+x*atan(x*sqrt(1+x**2))+Rational(1,2)*sqrt(3)*atanh((sqrt(3)*sqrt(1+x**2))/(2+x**2)))
Charlwood[48] = (atan(sqrt(x+1)-sqrt(x)),sqrt(x)/2+(1+x)*atan(sqrt(1+x)-sqrt(x)))
Charlwood[49] = (asin(x/sqrt(1-x**2)),x*asin(x/sqrt(1-x**2))+atan(sqrt(1-2*x**2)))
Charlwood[50] = (atan(x*sqrt(1-x**2)),x*atan(x*sqrt(1-x**2))-sqrt(Rational(1,2)*(1+sqrt(5)))*atan(sqrt(Rational(1,2)*(1+sqrt(5)))*sqrt(1-x**2))+sqrt(Rational(1,2)*(-1+sqrt(5)))*atanh(sqrt(Rational(1,2)*(-1+sqrt(5)))*sqrt(1-x**2)))

# <codecell>

def test(suite, problem):
    
    integrand, antideriv = suite[problem]
    print [problem], "Charlwood"
    print "integrand :", integrand 
    print "antideriv :", antideriv
    
    try:
        start = clock()  
        solution = integrate(integrand, x)
        duration = clock() - start  
    
    except RuntimeError, e:
        print "integrator: RuntimeError:", e
        print 
        return
    except KeyboardInterrupt:
        print "time      :", round(clock() - start) 
        print "integrator: Timed out! \n"
        return
    except AttributeError, e:
        print "integrator: AttributeError:", e
        print
        return
    except ValueError, e: 
        print "integrator: ValueError:", e 
        print "comment   : Additional constraints? Assume? \n"
        return
    
    print "sympy     :", solution
          
    str_solution = str(solution)
    diffsolution = solution.diff(x) 
    matheq = 0 == simplify((integrand - diffsolution).expand())
    
    if len(str_solution) > 2*len(str(antideriv)):
        print "comment   : Solution is messy."
            
    if 'Integral' in str_solution: 
            print "comment   : Unevaluated or not an elementary solution!"
    else:
        if 'I' in str_solution: 
            print "comment   : Not a real solution!"  
            
    if 'Piecewise' in str_solution:
        print "comment   : Not a continous solution!"
    
    if not matheq:    
        print "comment   : Diffs not back to zero. (Check use of abs.)"
    
    print "time      :", round(duration)
    if duration > 60 :
        print "You are wasting my time!"
    print

def test_all(suite): 
    start = clock()  
    for problem in suite.iteritems(): 
        test(suite, problem[0])
    duration = clock() - start 
    print "total time:", round(duration)

# <codecell>

test(Charlwood, 1)

# <codecell>

test(Charlwood, 2)

# <codecell>

test(Charlwood, 3)

# <codecell>

test(Charlwood, 4)

# <codecell>

test(Charlwood, 5)

# <codecell>

test(Charlwood, 6)

# <codecell>

test(Charlwood, 7)

# <codecell>

test(Charlwood, 8)

# <codecell>

test(Charlwood, 9)

# <codecell>

test(Charlwood, 10)

# <codecell>

test(Charlwood, 11)

# <codecell>

test(Charlwood, 12)

# <codecell>

test(Charlwood, 13)

# <codecell>

test(Charlwood, 14)

# <codecell>

test(Charlwood, 15)

# <codecell>

test(Charlwood, 16)

# <codecell>

test(Charlwood, 17)

# <codecell>

test(Charlwood, 18)

# <codecell>

test(Charlwood, 19)

# <codecell>

test(Charlwood, 20)

# <codecell>

test(Charlwood, 21)

# <codecell>

test(Charlwood, 22)

# <codecell>

test(Charlwood, 23)

# <codecell>

test(Charlwood, 24)

# <codecell>

test(Charlwood, 25)

# <codecell>

test(Charlwood, 26)

# <codecell>

test(Charlwood, 27)

# <codecell>

test(Charlwood, 28)

# <codecell>

test(Charlwood, 29)

# <codecell>

test(Charlwood, 30)

# <codecell>

test(Charlwood, 31)

# <codecell>

test(Charlwood, 32)

# <codecell>

test(Charlwood, 33)

# <codecell>

test(Charlwood, 34)

# <codecell>

test(Charlwood, 35)

# <codecell>

test(Charlwood, 36)

# <codecell>

test(Charlwood, 37)

# <codecell>

test(Charlwood, 38)

# <codecell>

test(Charlwood, 39)

# <codecell>

test(Charlwood, 40)

# <codecell>

test(Charlwood, 41)

# <codecell>

test(Charlwood, 42)

# <codecell>

test(Charlwood, 43)

# <codecell>

test(Charlwood, 44)

# <codecell>

test(Charlwood, 45)

# <codecell>

test(Charlwood, 46)

# <codecell>

test(Charlwood, 47)

# <codecell>

test(Charlwood, 48)

# <codecell>

test(Charlwood, 49)

# <codecell>

test(Charlwood, 50)

# <codecell>


