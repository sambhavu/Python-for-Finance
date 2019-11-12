import math
import numpy
from  numpy import * 


S0 = 100.0
K = 105 
T = 1.0
r= .05 
sigma = .2 

I = 100000
z = random.standard_normal(I)
ST = S0* exp((r-.5*sigma**2)*T+sigma*sqrt(T)*z)
hT = maximum(ST-K,0)
C0 = exp(-r*T)*sum(hT/I)

print(C0)

