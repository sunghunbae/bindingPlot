import numpy as np
import matplotlib.pyplot as plt
import sys

L=np.logspace(-8,-1,num=50,endpoint=True) # 1e-8 ... 1e-1

def pBound(Kd) :
  a=P+L+Kd 
  b=P*L
  x=0.5*a-np.sqrt(0.25*a*a-b)
  return 100*x/P

P=10e-9
plt.subplot(3,1,1)
plt.grid()
plt.xscale('log')
plt.xlabel('log[L]')
plt.ylabel('P(10nM) bound(%)')
plt.yticks(np.arange(0,110,10))
plt.plot(L,pBound(Kd=10e-6)) 
plt.plot(L,pBound(Kd=100e-6)) 
plt.plot(L,pBound(Kd=1000e-6)) 
plt.legend(["Kd=10uM","Kd=100uM","Kd=1000uM"],loc=2,prop={'size':8})

P=1e-6
plt.subplot(3,1,2)
plt.grid()
plt.xscale('log')
plt.xlabel('log[L]')
plt.ylabel('P(1uM) bound(%)')
plt.yticks(np.arange(0,110,10))
plt.plot(L,pBound(Kd=10e-6)) 
plt.plot(L,pBound(Kd=100e-6)) 
plt.plot(L,pBound(Kd=1000e-6)) 
plt.legend(["Kd=10uM","Kd=100uM","Kd=1000uM"],loc=2,prop={'size':8})

P=100e-6
plt.subplot(3,1,3)
plt.grid()
plt.xscale('log')
plt.xlabel('log[L]')
plt.ylabel('P(100uM) bound(%)')
plt.yticks(np.arange(0,110,10))
plt.plot(L,pBound(Kd=10e-6)) 
plt.plot(L,pBound(Kd=100e-6)) 
plt.plot(L,pBound(Kd=1000e-6)) 
plt.legend(["Kd=10uM","Kd=100uM","Kd=1000uM"],loc=2,prop={'size':8})

plt.savefig('protein-observed-L.png')
plt.show()
