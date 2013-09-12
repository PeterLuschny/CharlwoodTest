# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from time import clock  
from sympy import *
from __future__ import division

x = Symbol('x')
a = Symbol('a')
b = Symbol('b')
n = Symbol('n')

# <codecell>

Timofeev = dict()
# chapter 1
Timofeev[101] = (1/(a**2-b**2*x**2),  1/a/b*atanh(b*x/a))
Timofeev[102] = (1/(a**2+b**2*x**2),  1/a/b*atan(b*x/a))
Timofeev[103] = (sec(2*a*x), 1/(2*a)*ln(tan(pi/4+a*x)))
Timofeev[104] = (Rational(1,4)/sin(Rational(1,3)*x), Rational(3,4)*ln(tan(x/6)))
Timofeev[105] = (1/cos(Rational(3,4)*pi-2*x), Rational(1,2)*ln(tan(pi/8-x)))
Timofeev[106] = (sec(x)*tan(x), sec(x))
Timofeev[107] = (csc(x)*cot(x), -csc(x))
Timofeev[108] = (tan(x)/sin(2*x), Rational(1,2)*tan(x))
Timofeev[109] = (1/(1+cos(x)), tan(Rational(1,2)*x))
Timofeev[110] = (1/(1-cos(x)), -cot(1/2*x))
Timofeev[111] = (sin(x)/(a-b*cos(x)), 1/b*ln(a-b*cos(x)))
Timofeev[112] = (cos(x)/(a**2+b**2*sin(x)**2), 1/a/b*atan(b*sin(x)/a))
Timofeev[113] = (cos(x)/(a**2-b**2*sin(x)**2), 1/a/b*atanh(b*sin(x)/a))
Timofeev[114] = (sin(2*x)/(a**2+b**2*sin(x)**2), 1/b**2*ln(a**2+b**2*sin(x)**2)) 
Timofeev[115] = (sin(2*x)/(b**2*sin(x)**2-a**2), 1/b**2*ln(a**2-b**2*sin(x)**2))
Timofeev[116] = (sin(2*x)/(cos(x)**2*b**2+a**2), -1/b**2*ln(cos(x)**2*b**2+a**2))
Timofeev[117] = (sin(2*x)/(cos(x)**2*b**2-a**2), -1/b**2*ln(a**2-cos(x)**2*b**2))
Timofeev[118] = (1/(4-cos(x)**2), sqrt(3)/6*(atan(sin(x)*cos(x)/(2*sqrt(3)+4 -cos(x)**2))+x))
Timofeev[119] = (exp(x)/(exp(2*x)-1), -atanh(exp(x)))
Timofeev[120] = (1/x/ln(x), ln(ln(x)))
Timofeev[121] = (1/x/(1+ln(x)**2), atan(ln(x)))
Timofeev[122] = (1/x/(1-ln(x)), -ln(1-ln(x)))
Timofeev[123] = (1/x/(1+ln(x/a)), ln(1+ln(x/a)))
Timofeev[124] = ((1-x**Rational(1,2)+x)**2/x**2, 3*ln(x)+x-4*x**Rational(1,2)+4/x**Rational(1,2)-1/x )
Timofeev[125] = ((2-x**Rational(2,3))*(x+x**Rational(1,2))/x**Rational(3,2), 2*ln(x)-Rational(6,7)*x**Rational(7,6)-Rational(3,2)*x**Rational(2,3)+4*x**Rational(1,2))
Timofeev[126] = ((2*x-1)/(2*x+3), x-2*ln(2*x+3))
Timofeev[127] = ((2*x-5)/(3*x**2-2), Rational(1,3)*ln(-3*x**2+2)+Rational(5,6)*6**Rational(1,2)*atanh(Rational(1,2)*6**Rational(1,2)*x) )
Timofeev[128] = ((2*x-5)/(3*x**2+2), Rational(1,3)*ln(3*x**2+2)-Rational(5,6)*6**Rational(1,2)*atan(Rational(1,2)*6**Rational(1,2)*x))
Timofeev[129] = (sin(x)*sin(Rational(1,4)*x), Rational(2,3)*sin(Rational(3,4)*x)-Rational(2,5)*sin(Rational(5,4)*x))
Timofeev[130] = (cos(3*x)*cos(4*x), Rational(1,14)*sin(7*x)+Rational(1,2)*sin(x))
Timofeev[131] = (tan(x)*tan(a-x), 1/tan(a)*ln(1+tan(a)*tan(x))-x)
Timofeev[132] = (sin(x)**2, Rational(1,2)*x-Rational(1,2)*sin(x)*cos(x))
Timofeev[133] = (cos(x)**2, Rational(1,2)*x+Rational(1,2)*sin(x)*cos(x))
Timofeev[134] = (sin(x)*cos(x)**3, -Rational(1,4)*cos(x)**4)
Timofeev[135] = (cos(x)**3/sin(x)**4, 1/sin(x)-Rational(1,3)/sin(x)**3)
Timofeev[136] = (1/sin(x)**2/cos(x)**2, tan(x)-cot(x))
Timofeev[137] = (cot(Rational(3,4)*x)**2, -Rational(4,3)*cot(Rational(3,4)*x)-x)
Timofeev[138] = ((1+tan(2*x))**2, Rational(1,2)*tan(2*x)-ln(cos(2*x)))
Timofeev[139] = ((tan(x)-cot(x))**2, tan(x)-cot(x)-4*x)
Timofeev[140] = ((tan(x)-sec(x))**2, 2*tan(x/2-pi/4)-x)
Timofeev[141] = (sin(x)/(1+sin(x)), tan(pi/4-x/2)+x)
Timofeev[142] = (cos(x)/(1-cos(x)), -cot(Rational(1,2)*x)-x)
Timofeev[143] = ((exp(Rational(1,2)*x)-1)**3*exp(-Rational(1,2)*x), -6*exp(Rational(1,2)*x)+2*exp(-Rational(1,2)*x)+exp(x)+3*x)
Timofeev[144] = (1/(x**2-6*x+5), Rational(1,4)*ln((x-5)/(x-1)))
Timofeev[145] = (x**2/(x**6-6*x**3+13), Rational(1,6)*atan(Rational(1,2)*x**3-Rational(3,2)))
Timofeev[146] = ((x+2)/(x**2-4*x-1), Rational(1,2)*ln(1+4*x-x**2)+4/sqrt(5)*atanh((2-x)/sqrt(5)))
Timofeev[147] = (1/(1+(x+1)**Rational(1,3)), Rational(3,2)*(x+1)**Rational(2,3)-3*(x+1)**Rational(1,3)+3*ln(1+(x+1)**Rational(1,3)))
Timofeev[148] = (1/(a*x+b)/x**Rational(1,2), 2/a**Rational(1,2)/b**Rational(1,2)*atan(a**Rational(1,2)*x**Rational(1,2)/b**Rational(1,2)))
Timofeev[149] = (x**3*(x**2+1)**Rational(1,2), Rational(1,15)*(3*x**4+x**2-2)*(x**2+1)**Rational(1,2))
Timofeev[150] = (x/(a**4-x**4)**Rational(1,2), 1/2*atan(x**2/sqrt(a**4-x**4)))
Timofeev[151] = (1/x/(x**2-a**2)**Rational(1,2), 1/a*atan((x**2-a**2)**Rational(1,2)/a))
Timofeev[152] = (1/x/(a**2-x**2)**Rational(1,2), -1/a*atanh((a**2-x**2)**Rational(1,2)/a))
Timofeev[153] = (1/x/(a**2+x**2)**Rational(1,2), -1/a*atanh(a/(a**2+x**2)**Rational(1,2)))
Timofeev[154] = (1/(-x**2+x+2)**Rational(1,2), asin(Rational(2,3)*x-Rational(1,3)))
Timofeev[155] = (1/(3*x**2-4*x+5)**Rational(1,2), 1/sqrt(3)*asinh((3*x-2)/sqrt(11)))
Timofeev[156] = (1/(-x**2+x)**Rational(1,2), asin(2*x-1))
Timofeev[157] = ((2*x+1)/(-x**2+x+2)**Rational(1,2), 2*asin(Rational(2,3)*x-Rational(1,3))-2*(-x**2+x+2)**Rational(1,2))
Timofeev[158] = (1/x/(2+x-x**2)**Rational(1,2), -1/sqrt(2)*atanh(2*sqrt(2)*sqrt(2+x-x**2)/(4+x)))
Timofeev[159] = (1/(x-2)/(-x**2+x+2)**(1/2), 2*(-x**2+x+2)**(1/2)/(3*x-6))
Timofeev[160] = ((2+3*sin(x))/sin(x)/(1-cos(x)), -atanh(cos(x))+(3*sin(x)+1)/(cos(x)-1))
Timofeev[161] = (1/(2+3*cos(x)**2), Rational(1,10)*10**Rational(1,2)*(x-atan(3*sin(x)*cos(x)/(10**Rational(1,2)+2+3*cos(x)**2))))
Timofeev[162] = ((1-tan(x))/sin(2*x), Rational(1,2)*(ln(tan(x))-tan(x)))
Timofeev[163] = ((1+tan(x)**2)/(1-tan(x)**2), 1/2*ln((1+tan(x))/(1-tan(x))))
Timofeev[164] = ((a**2-4*cos(x)**2)**Rational(3,4)*sin(2*x), Rational(1,7)*(a**2-4*cos(x)**2)**Rational(7,4))
Timofeev[165] = (sin(2*x)/(a**2-4*sin(x)**2)**Rational(1,3), -Rational(3,8)*(a**2-4*sin(x)**2)**Rational(2,3))
Timofeev[166] = (1/(a**(2*x)-1)**Rational(1,2), 1/ln(a)*atan((a**(2*x)-1)**Rational(1,2)) )
Timofeev[167] = (exp(Rational(1,2)*x)/(exp(x)-1)**Rational(1,2), 2*ln((exp(x)-1)**Rational(1,2)+exp(Rational(1,2)*x)))
Timofeev[168] = (atan(x)**n/(x**2+1), 1/(n+1)*atan(x)**(n+1))
Timofeev[169] = (asin(x/a)**Rational(3,2)/(a**2-x**2)**Rational(1,2), Rational(2,5)*a/(a**2-x**2)**Rational(1,2)*(1-x**2/a**2)**Rational(1,2)*asin(x/a)**Rational(5,2))
Timofeev[170] = (1/acos(x)**3/(-x**2+1)**Rational(1,2), 1/2/acos(x)**2)
Timofeev[171] = (ln(x)**2*x, Rational(1,2)*x**2*(ln(x)**2-ln(x)+Rational(1,2)))
Timofeev[172] = (ln(x)/x**5, -Rational(1,16)*(4*ln(x)+1)/x**4)
Timofeev[173] = (x**2*ln((x-1)/x), Rational(1,3)*x**3*ln((x-1)/x)-Rational(1,3)*ln(x-1)-Rational(1,6)*x*(x+2))
Timofeev[174] = (cos(x)**5, Rational(1,15)*sin(x)*(3*cos(x)**4+4*cos(x)**2+8))
Timofeev[175] = (cos(x)**4*sin(x)**2, Rational(1,6)*sin(x)**3*cos(x)**3+Rational(1,8)*sin(x)**3*cos(x)-Rational(1,16)*sin(x)*cos(x)+Rational(1,16)*x)
Timofeev[176] = (1/sin(x)**5, -Rational(3,8)*atanh(cos(x))-3*cos(x)/(8*sin(x)**2)-cos(x)/(4*sin(x)**4))
Timofeev[177] = (sin(x)*exp(-x), -Rational(1,2)*(cos(x)+sin(x))*exp(-x))
Timofeev[178] = (exp(2*x)*sin(3*x), Rational(1,13)*exp(2*x)*(2*sin(3*x)-3*cos(3*x)))
Timofeev[179] = (a**x*cos(x), a**x/(ln(a)**2+1)*(ln(a)*cos(x)+sin(x)))
Timofeev[180] = (cos(ln(x)), Rational(1,2)*x*(cos(ln(x))+sin(ln(x))))
Timofeev[181] = (sec(x)**2*ln(cos(x)), tan(x)*ln(cos(x))+tan(x)-x)
Timofeev[182] = (x*tan(x)**2, ln(cos(x))+x*tan(x)-Rational(1,2)*x**2)
Timofeev[183] = (asin(x)/x**2, -asin(x)/x-atanh(sqrt(1-x**2)))
Timofeev[184] = (asin(x)**2, x*asin(x)**2+2*asin(x)*(-x**2+1)**Rational(1,2)-2*x)
Timofeev[185] = (x**2*atan(x)/(x**2+1), x*atan(x)-Rational(1,2)*atan(x)**2-Rational(1,2)*ln(x**2+1))
Timofeev[186] = (acos((x/(x+1))**Rational(1,2)), (x+1)*(acos((x/(x+1))**Rational(1,2))+(1/(x+1))**(1/2)*(x/(x+1))**Rational(1,2)))
# chapter 3
Timofeev[301] = (1/((x-2)**3*(x+1)**2), (2*x**2-5*x-1)/(18*(x+1)*(x-2)**2)+Rational(1,27)*log((x-2)/(x+1)) )
Timofeev[302] = (1/((x+2)**3*(x+3)**4), (60*x**4+630*x**3+2450*x**2+4175*x+2627)/(6*(x+2)**2*(x+3)**3)+10*log((x+2)/(x+3)) )
Timofeev[303] = (x**5/(3+x)**2,  Rational(1,4)*x**4-2*x**3+Rational(27,2)*x**2-108*x+243/(x+3)+405*log(x+3) )
Timofeev[304] = (x/(3+6*x+2*x**2), Rational(1,4)*log(-(3+6*x+2*x**2))+sqrt(3)/2*atanh((3+2*x)/sqrt(3)) )
Timofeev[305] = ((2*x-3)/(3+6*x+2*x**2)**3, -(8*x**3+36*x**2+44*x+13)/(4*(2*x**2+6*x+3)**2)+1/sqrt(3)*atanh((3+2*x)/sqrt(3)) )
Timofeev[306] = ((x-1)/(x**2+5*x+4)**2, (7*x+13)/(9*(x**2+5*x+4))+Rational(7,27)*log((x+1)/(x+4)) )
Timofeev[307] = (1/(x**2+3*x+2)**5, (2*x+3)/(4*(x**2+3*x+2)**4)*(-1+Rational(14,3)*(x**2+3*x+2)-Rational(70,3)*(x**2+3*x+2)**2+140*(x**2+3*x+2)**3)+70*log((x+1)/(x+2)) )
Timofeev[308] = (1/(x**3*(7-6*x+2*x**2)**2), -1/(98*x**2)-12/(343*x)+2*(41-9*x)/(1715*(7-6*x+2*x**2))+Rational(80,2401)*log(x)-Rational(40,2401)*log(7-6*x+2*x**2)+234*sqrt(5)/60025*atan((2*x-3)/sqrt(5)) )
Timofeev[309] = (x**9/(x**2+3*x+2)**5, -(25*x**8+35292*x**7+369950*x**6+1632276*x**5+3919731*x**4+5527800*x**3+4578216*x**2+2063520*x+390960)/(24*(x**2+3*x+2)**4)+1472*log(x+2)-1471*log(x+1) )
Timofeev[310] = ((1+2*x)**2/(3+5*x+2*x**2)**5, -(11+10*x)/(4*(2*x**2+5*x+3)**4)+31*(5+4*x)/(6*(2*x**2+5*x+3)**3)*(1-10*(2*x**2+5*x+3)+120*(2*x**2+5*x+3)**2)+2480*log((x+1)/(2*x+3)) )
Timofeev[311] = ((a-b*x**2)**3/x**7, -a**3/(6*x**6)+3*a**2*b/(4*x**4)-3*a*b**2/(2*x**2)-b**3*log(x) )
Timofeev[312] = (x**13/(a**4+x**4)**5, x**2*(15*x**12-73*a**4*x**8-55*a**8*x**4-15*a**12)/(768*a**4*(x**4+a**4)**4)+5/(256*a**6)*atan(x**2/a**2) )
# chapter 7
Timofeev[701] = (x**2*cos(x)**5, Rational(1,200)*x*cos(5*x)+(Rational(1,80)*x**2-Rational(1,1000))*sin(5*x)+Rational(5,72)*x*cos(3*x)+(Rational(5,48)*x**2-Rational(5,216))*sin(3*x)+Rational(5,4)*x*cos(x)+(Rational(5,8)*x**2-Rational(5,4))*sin(x) )
Timofeev[702] = (x**3*sin(x)**3, Rational(1,12)*(x**3-Rational(2,3)*x)*cos(3*x)-Rational(1,12)*(x**2-Rational(2,9))*sin(3*x)-Rational(3,4)*(x**3-6*x)*cos(x)+Rational(9,4)*(x**2-2)*sin(x) )
Timofeev[703] = (x**2*sin(x)**6, Rational(5,48)*x**3-1/192*(x**2-Rational(1,18))*sin(6*x)-Rational(1,576)*x*cos(6*x)+Rational(3,64)*(x**2-Rational(1,8))*sin(4*x)+Rational(3,128)*x*cos(4*x)-Rational(15,64)*(x**2-Rational(1,2))*sin(2*x)-Rational(15,64)*x*cos(2*x) )
Timofeev[704] = (x**2*sin(x)**2*cos(x), Rational(1,3)*x**2*sin(x)**3-Rational(1,18)*x*cos(3*x)+Rational(1,54)*sin(3*x)+Rational(1,2)*x*cos(x)-Rational(1,2)*sin(x) )
Timofeev[705] = (x*cos(x)**4/sin(x)**2, -x*cos(x)*(Rational(1,2)*sin(x)+1/sin(x))+Rational(1,4)*sin(x)**2+log(sin(x))-Rational(3,4)*x**2 )
Timofeev[706] = (x*sin(x)**3/cos(x)**4, x*(1/(3*cos(x)**3)-1/cos(x))-sin(x)/(6*cos(x)**2)+Rational(5,6)*atanh(sin(x)) )
Timofeev[707] = (x*sin(x)/cos(x)**3, x/(2*cos(x)**2)-Rational(1,2)*tan(x) )
Timofeev[708] = (x*sin(x)**3/cos(x), Rational(1,4)*x*cos(2*x)-Rational(1,8)*sin(2*x)+integrate(x*tan(x),x) )
Timofeev[709] = (x*sin(x)**3/cos(x)**3, x/(2*cos(x)**2)-Rational(1,2)*tan(x)-integrate(x*tan(x),x) )
Timofeev[710] = ((2*x+sin(2*x))/(x*sin(x)+cos(x))**2, -2*cos(x)/(x*sin(x)+cos(x)) )
Timofeev[711] = ((x/(x*cos(x)-sin(x)))**2, (x*sin(x)+cos(x))/(x*cos(x)-sin(x)) )

# <codecell>

def test(suite, problem):
    
    integrand, antideriv = suite[problem]
    print [problem], "Timofeev"
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

test_all(Timofeev)

# <codecell>
