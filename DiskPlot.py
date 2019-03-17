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
#x, y, res, lg_rhop_xy1, orbit1 = Disk(10)
#x, y, res, lg_rhop_xy2, orbit2 = Disk(20)

style.use('dark_background')
# fig, (ax1, ax2) = subplots(1,2)
# ax1.contourf(x, y, lg_rhop_xy1, res)
# ax1.set_title('t = %s' % (orbit1))
# ax2.contourf(x, y, lg_rhop_xy2, res)
# ax2.set_title('t = %s' % (orbit2))
# show()

def disk_plot_3(a, b, c):
    x, y, res, lg_rhop_xya, orbita = Disk(a)
    x, y, res, lg_rhop_xyb, orbitb = Disk(b)
    x, y, res, lg_rhop_xyc, orbitc = Disk(c)
    fig, axs = subplots(1, 3)
    fig.suptitle('Dust Density')
    p1=axs[0].contourf(x, y, lg_rhop_xya, res)
    axs[1].contourf(x, y, lg_rhop_xyb, res)
    axs[2].contourf(x, y, lg_rhop_xyc, res)
    axs[0].set_title('t = %s' % (orbita))
    axs[1].set_title('t = %s' % (orbitb))
    axs[2].set_title('t = %s' % (orbitc))
    cbar = fig.colorbar(p1, ax=axs, orientation='horizontal')
    axs[0].set_xlabel('x')
    axs[1].set_xlabel('x')
    axs[2].set_xlabel('x')
    axs[0].set_ylabel('y')
    axs[1].set_ylabel('y')
    axs[2].set_ylabel('y')
    show()

def disk_plot_6(a, b, c, d, e, f):
    x, y, res, lg_rhop_xya, orbita = Disk(a)
    x, y, res, lg_rhop_xyb, orbitb = Disk(b)
    x, y, res, lg_rhop_xyc, orbitc = Disk(c)
    x, y, res, lg_rhop_xyd, orbitd = Disk(d)
    x, y, res, lg_rhop_xye, orbite = Disk(e)
    x, y, res, lg_rhop_xyf, orbitf = Disk(f)
    fig, axs = subplots(2, 3)
    axs[0,0].contourf(x, y, lg_rhop_xya, res)
    axs[0,1].contourf(x, y, lg_rhop_xyb, res)
    axs[0,2].contourf(x, y, lg_rhop_xyc, res)
    axs[1,0].contourf(x, y, lg_rhop_xyd, res)
    axs[1,1].contourf(x, y, lg_rhop_xye, res)
    axs[1,2].contourf(x, y, lg_rhop_xyf, res)
    axs[0,0].colorbar()
    axs[0,0].set_title('t = %s' % (orbita))
    axs[0,1].set_title('t = %s' % (orbitb))
    axs[0,2].set_title('t = %s' % (orbitc))
    axs[1,0].set_title('t = %s' % (orbitd))
    axs[1,1].set_title('t = %s' % (orbite))
    axs[1,2].set_title('t = %s' % (orbitf))
    show()

disk_plot_3(12, 17, 21)
