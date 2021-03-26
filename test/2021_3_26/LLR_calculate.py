#x=LLR(y)=ln[W(y|0)/W(y|1)]
#W(y|1)=1/(1+e^(-2y/&^2))
import math
y1=-0.06
t=math.exp(-2*y1)
w1=1/(t+1)
w0=1-w1
x=math.log((w0/w1))
print(x)