import pencil as pc
from pylab import *
style.use('dark_background')

epsi = 1e-4
ny = 1024; nz = 32
# Function to return variables for desired data file
def Disk(ivar):
    ff = pc.read_var(trimall=True, ivar=ivar)
    global r, x, y, z, rhop
    r = ff.x
    phi = ff.y
    z = ff.z
    rhop = ff.rhop;
    r2d, p2d = meshgrid(r, phi)
    x = r2d*cos(p2d)           
    y = r2d*sin(p2d)           
    lg_rhop_xy = log10(rhop[int(nz/2),...] + epsi)
    res = linspace(lg_rhop_xy.max()-4, lg_rhop_xy.max(), 256)
    return res, lg_rhop_xy

def diskxy_xz(a):
    resxy, lg_rhop_xy = Disk(a)
    lg_rhop_xz = log10(rhop[:,int(ny/2),:] + epsi)
    resxz = linspace(lg_rhop_xz.max()-4, lg_rhop_xz.max(), 256)
    fig, ax = subplots(1, 2)
    fig.suptitle('Dust Density at t = %s Orbits' % a)
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

def disk_plot_3(a, b, c):
    res, lg_rhop_xya = Disk(a)
    res, lg_rhop_xyb = Disk(b)
    res, lg_rhop_xyc = Disk(c)
    times = [a, b, c]
    rhops = [lg_rhop_xya, lg_rhop_xyb, lg_rhop_xyc]
    fig, axs = subplots(1, 3)
    fig.suptitle('Dust Density')
    for i in range(len(axs)):
        p1=axs[i].contourf(x, y, rhops[i], res)
        axs[i].set_xlabel('x')
        axs[i].set_ylabel('y')
        axs[i].set_title('t = %s' % times[i])
    cbar = fig.colorbar(p1, ax=axs, orientation='horizontal')
    show()

def disk_plot_6(a, b, c, d, e, f):
    res, rhopa = Disk(a)
    res, rhopb = Disk(b)
    res, rhopc = Disk(c)
    res, rhopd = Disk(d)
    res, rhope = Disk(e)
    res, rhopf = Disk(f)
    times = [a, b, c, d, e, f]
    rhops = [rhopa, rhopb, rhopc, rhopd, rhope, rhopf]
    fig, axs = subplots(2, 3)
    for i in range(len(axs)+1):
        axs[0,i].contourf(x, y, rhops[i], res)
        axs[1,i].contourf(x, y, rhops[i+3], res)
        axs[0,i].set_title('t = %s' % times[i])
        axs[1,i].set_title('t = %s' % times[i+3])
#    axs[0,0].colorbar()
    show()
#diskxy_xz(21)
disk_plot_3(5, 12, 20)
#disk_plot_6(1, 3, 5, 8, 10, 21)
