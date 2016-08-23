import numpy as np
import matplotlib.pyplot as plt
import sys

Kd=np.logspace(-8,-1,num=50,endpoint=True) # 1e-9 ... 1e-1

def lBound(Kd) :
  a=P+L+Kd 
  b=P*L
  x=0.5*a-np.sqrt(0.25*a*a-b)
  return 100*x/L

P=1e-6 # 1uM
plt.subplot(3,1,1)
plt.grid()
plt.xscale('log')
plt.xlabel('Kd')
plt.ylabel('L([P]=1uM) bound(%)')
L=1e-6 
plt.plot(Kd,lBound(Kd)) 
L=10e-6
plt.plot(Kd,lBound(Kd)) 
L=100e-6
plt.plot(Kd,lBound(Kd)) 
plt.legend(["[L]=1uM","[L]=10uM","[L]=100uM"],loc=1,prop={'size':12})

P=10e-6 # 10uM
plt.subplot(3,1,2)
plt.grid()
plt.xscale('log')
plt.xlabel('Kd')
plt.ylabel('L([P]=10uM) bound(%)')
L=1e-6 
plt.plot(Kd,lBound(Kd)) 
L=10e-6
plt.plot(Kd,lBound(Kd)) 
L=100e-6
plt.plot(Kd,lBound(Kd)) 
plt.legend(["[L]=1uM","[L]=10uM","[L]=100uM"],loc=1,prop={'size':12})

P=40e-6 # 40uM
plt.subplot(3,1,3)
plt.grid()
plt.xscale('log')
plt.xlabel('Kd')
plt.ylabel('L([P]=40uM) bound(%)')
L=1e-6 
plt.plot(Kd,lBound(Kd)) 
L=10e-6
plt.plot(Kd,lBound(Kd)) 
L=100e-6
plt.plot(Kd,lBound(Kd)) 
plt.legend(["[L]=1uM","[L]=10uM","[L]=100uM"],loc=1,prop={'size':12})

plt.savefig('ligand-observed-Kd.png')
plt.show()
