import pencil as pc
from pylab import *

ff = pc.read_var(trimall=True, ivar=5, magic=["vort"])
dim = pc.read_dim()

#contourf(ff.x, ff.y, ff.vort[2, int(dim.nz/2),...], 256) # Plots a low resolution image

vortz_mid = ff.vort[2, int(dim.nz/2),...]
print(vortz_mid.min())
print(vortz_mid.max())

#contourf(ff.x, ff.y, ff.vort[2, int(dim.nz/2),...], linspace(-1, 1, 256))

r, phi = meshgrid(ff.x, ff.y)
omega = 1./r**1.5
vort_k = omega/2

#contourf(ff.x, ff.y, ff.vort[2, int(dim.nz/2),...]/vort_k, linspace(-1, 1, 256))
contourf(r, phi, ff.vort[2, int(dim.nz/2),...]/vort_k, linspace(-1, 1, 256))

show()
