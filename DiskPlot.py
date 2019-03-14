from pylab import *
import pencil as pc

datadir='/media/cmp/Storage/research/Streaming3D/data'
dim = pc.read_dim()

def ffread(var):
    ff = pc.read_var(trimall=True, datadir=datadir, ivar=var)
    rhop = ff.rhop
    r = ff.x;    phi = ff.y;    z = ff.z
    epsi = 1e-4
    orbit = str(var)
    lg_rhop_xy = log10(rhop[int(dim.nz/2.),...] + epsi)
    r2d, p2d = meshgrid(r, phi)
    x = r2d*cos(p2d)
    y = r2d*sin(p2d)
    res = linspace(lg_rhop_xy.max()-4, lg_rhop_xy.max(), 256)
    return x, y, res, lg_rhop_xy, orbit

#lg_rhop_xz = log10(rhop[:,dim.ny/2,:] + epsi)
x, y, res, lg_rhop_xy1,orbit = ffread(10)
x, y, res, lg_rhop_xy20,orbit = ffread(21)

print(orbit)
style.use('dark_background')
fig, (ax1, ax2) = subplots(1,2)
ax1.contourf(x, y, lg_rhop_xy1, res)
ax1.title('Title = %s', str(orbit))
ax2.contourf(x, y, lg_rhop_xy20, res)
ax2.title('Title = ', orbit)
show()
