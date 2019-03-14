import time
start = time.time()
import pencil as pc
from pylab import *

epsi = 1e-4
nz = 32
def Disk(ivar):
    ff = pc.read_var(trimall=True, ivar=ivar)
    r = ff.x
    phi = ff.y
    z = ff.z
    rhop = ff.rhop
    lg_rhop_xy = log10(rhop[int(nz/2),...] + epsi)
    r2d, p2d = meshgrid(r, phi)
    x = r2d*cos(p2d)
    y = r2d*sin(p2d)
    res = linspace(lg_rhop_xy.max()-4, lg_rhop_xy.max(), 256)
    orbit = ivar
    return x, y, res, lg_rhop_xy, orbit

#lg_rhop_xz = log10(rhop[:,dim.ny/2,:] + epsi)
x, y, res, lg_rhop_xy1, orbit1 = Disk(10)
x, y, res, lg_rhop_xy2, orbit2 = Disk(20)

orbit1 = str(orbit1)
style.use('dark_background')
fig, (ax1, ax2) = subplots(1,2)
ax1.contourf(x, y, lg_rhop_xy1, res)
ax1.set_title('Orbit %s' % (orbit1))
ax2.contourf(x, y, lg_rhop_xy2, res)
ax2.set_title('Orbit  %s' % (orbit2))
end = time.time()
print(round(end-start, 3))
show()

# 21.01, 28.07

