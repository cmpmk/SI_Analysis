import pencil as pc
from pylab import *

ff = pc.read_var(trimall=True, ivar=21, magic=["vort"])

#vortz_mid = ff1.vort[2, int(dim.nz/2),...]
#print(vortz_mid.min(), vortz_mid.max())

r, phi = meshgrid(ff.x, ff.y)
omega = 1./r**1.5
vort_k = omega/2
nz = 32/2
res = linspace(-1, 1, 256)
vort_z = ff.vort[2,...]
xlabel('x')
ylabel('y')
title('Vorticity at t = 21 Orbits')
A = mean(vort_z, axis=0)
print(A.min())
print(A.max())
p1 = contourf(r, phi, mean(vort_z,axis=0), res)
colorbar(p1)
show()

def VortAvg():
    r, phi = meshgrid(ff.x, ff.y)
    res = linspace(-1, 1, 256)
    fig, axs = subplots(1,1)
    fig.suptitle('Vorticity')
    contourf(r, phi, mean(vort_z,axis=0), res)
    axs[0].set_title('t = 2')
    axs[0].set_xlabel('x')
    axs[0].set_ylabel('y')
    show()
#VortAvg()
    
