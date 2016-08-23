import numpy as np
import matplotlib.pyplot as plt
import sys

L=np.logspace(-8,-1,num=50,endpoint=True) # 1e-8 ... 1e-1

def BoundLigandPercent(Kd) :
  a=P+L+Kd 
  b=P*L
  x=0.5*a-np.sqrt(0.25*a*a-b)
  return 100*x/L

P=1e-6
plt.subplot(3,1,1)
plt.grid()
plt.xscale('log')
plt.xlabel('[L]')
plt.ylabel('L(P=1uM) bound(%)')
plt.yticks(np.arange(0,11.,1.))
plt.plot(L,BoundLigandPercent(Kd=10e-6)) 
plt.plot(L,BoundLigandPercent(Kd=100e-6)) 
plt.plot(L,BoundLigandPercent(Kd=1000e-6)) 
plt.legend(["Kd=10uM","Kd=100uM","Kd=1000uM"],loc=2,prop={'size':8})

P=10e-6
plt.subplot(3,1,2)
plt.grid()
plt.xscale('log')
plt.xlabel('[L]')
plt.ylabel('L(P=10uM) bound(%)')
plt.yticks(np.arange(0,110.,10))
plt.plot(L,BoundLigandPercent(Kd=10e-6)) 
plt.plot(L,BoundLigandPercent(Kd=100e-6)) 
plt.plot(L,BoundLigandPercent(Kd=1000e-6)) 
plt.legend(["Kd=10uM","Kd=100uM","Kd=1000uM"],loc=2,prop={'size':8})

P=40e-6
plt.subplot(3,1,3)
plt.grid()
plt.xscale('log')
plt.xlabel('[L]')
plt.ylabel('L(P=40uM) bound(%)')
plt.yticks(np.arange(0,110,10))
plt.plot(L,BoundLigandPercent(Kd=10e-6)) 
plt.plot(L,BoundLigandPercent(Kd=100e-6)) 
plt.plot(L,BoundLigandPercent(Kd=1000e-6)) 
plt.legend(["Kd=10uM","Kd=100uM","Kd=1000uM"],loc=2,prop={'size':8})

plt.savefig('ligand-observed-L.png')
plt.show()
