import pencil as pc
from pylab import *

ff = pc.read_var(trimall=True, ivar=21, magic=["vort"])
r, phi = meshgrid(ff.x, ff.y)
omega = 1./r**1.5
vort_k = omega/2
nz = 32/2
res = linspace(-1, 1, 256)
vort_z = ff.vort[2,...]
#A = mean(vort_z, axis=0)
#print(A.min()); print(A.max())
suptitle('Vorticity')
contourf(r, phi, mean(vort_z, axis=0), res, cmap='tab20')
title('t = %s orbits' % round(ff.t/(2*pi),2))
xlabel('x')
ylabel('y')
#colorbar(p1)
show()

#vortz_mid = ff1.vort[2, int(dim.nz/2),...]
#print(vortz_mid.min(), vortz_mid.max())
