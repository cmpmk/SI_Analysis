import pencil as pc
from pylab import *
style.use('dark_background')

epsi = 1e-4
ny = 1024
nz = 32
# Function to return variables for a specific data file
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
    t = str(round(ff.t/(2*pi),2))
    return x, y, res, lg_rhop_xy, t

def diskxy_xz():
    ff = pc.read_var(trimall=True, ivar=21)
    r = ff.x
    phi = ff.y
    z = ff.z
    rhop = ff.rhop
    lg_rhop_xy = log10(rhop[int(nz/2),...] + epsi)
    lg_rhop_xz = log10(rhop[:,int(ny/2),:] + epsi)
    r2d, p2d = meshgrid(r, phi)
    x = r2d*cos(p2d)
    y = r2d*sin(p2d)
    resxy = linspace(lg_rhop_xy.max()-4, lg_rhop_xy.max(), 256)
    resxz = linspace(lg_rhop_xz.max()-4, lg_rhop_xz.max(), 256)
    fig, ax = subplots(1, 2)
    fig.suptitle('Dust Density at t = 21 Orbits')
    ax[0].contourf(x, y, lg_rhop_xy, resxy)
    ax[1].contourf(r, z, lg_rhop_xz, resxz)
    ax[0].set_xlim([x.min(), x.max()])
    ax[0].set_ylim([y.min(), y.max()])
    ax[1].set_xlim([r.min(), r.max()])
    ax[1].set_ylim([z.min(), z.max()])
    ax[0].set_title('x-y')
    ax[1].set_title('x-z')
    for i in range(len(ax)):
        ax[i].set_xlabel('x')
        ax[i].set_aspect('equal')
    ax[0].set_ylabel('y')
    ax[1].set_ylabel('z')
    show()

#diskxy_xz()

def disk_plot_3(a, b, c):
    x, y, res, lg_rhop_xya, ta = Disk(a)
    x, y, res, lg_rhop_xyb, tb = Disk(b)
    x, y, res, lg_rhop_xyc, tc = Disk(c)
    times = [ta, tb, tc]
    fig, axs = subplots(1, 3)
    fig.suptitle('Dust Density')
    axs[0].contourf(x, y, lg_rhop_xya, res)
    axs[1].contourf(x, y, lg_rhop_xyb, res)
    axs[2].contourf(x, y, lg_rhop_xyc, res)
    for i in range(len(axs)):
        axs[i].set_xlabel('x')
        axs[i].set_ylabel('y')
        axs[i].set_title('t = %s' % times[i])
    show()
#   cbar = fig.colorbar(p1, ax=axs, orientation='horizontal')
#disk_plot_3(5, 12, 20)
def disk_plot_6(a, b, c, d, e, f):
    x, y, res, lg_rhop_xya, ta = Disk(a)
    x, y, res, lg_rhop_xyb, tb = Disk(b)
    x, y, res, lg_rhop_xyc, tc = Disk(c)
    x, y, res, lg_rhop_xyd, td = Disk(d)
    x, y, res, lg_rhop_xye, te = Disk(e)
    x, y, res, lg_rhop_xyf, tf = Disk(f)
    fig, axs = subplots(2, 3)
    axs[0,0].contourf(x, y, lg_rhop_xya, res)
    axs[0,1].contourf(x, y, lg_rhop_xyb, res)
    axs[0,2].contourf(x, y, lg_rhop_xyc, res)
    axs[1,0].contourf(x, y, lg_rhop_xyd, res)
    axs[1,1].contourf(x, y, lg_rhop_xye, res)
    axs[1,2].contourf(x, y, lg_rhop_xyf, res)
    times = [ta, tb, tc, td, te, tf]
    for i in range(len(axs)+1):
        axs[0,i].set_title('t = %s' % times[i])
        axs[1,i].set_title('t = %s' % times[i+3])
    show()
#   axs[0,0].colorbar()
disk_plot_6(1, 3, 5, 8, 10, 11)
