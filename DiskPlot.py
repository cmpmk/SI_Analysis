import pencil as pc
from pylab import *

epsi = 1e-4
ny = 1024; nz = 32

# Function to return variables for desired data file
def Disk(ivar):
    ff = pc.read_var(trimall=True, ivar=ivar, quiet=True)
    global  x, y, z, rhop, res 
    r2d, p2d = meshgrid(ff.x, ff.y) # r, phi
    x = r2d*cos(p2d)
    y = r2d*sin(p2d)
    z = ff.z
    rhop = ff.rhop
    lg_rhop_xy = log10(rhop[int(nz/2),...] + epsi)
    res = linspace(lg_rhop_xy.max()-3.5, lg_rhop_xy.max(), 256)
    return lg_rhop_xy

# Return 1xn subplots of dust density contour at each orbit
def disk_plot(*args):
    times = [*args]
    rhops = [Disk(t) for t in times]
    if len(args) == 1:
        fig, axs = subplots(1,1)
        axs.contourf(x, y, rhops[0], res)
        axs.set_facecolor('black')
        axs.set_xlabel('x')
        axs.set_ylabel('y')
        axs.set_title('t = %s' % times[0])
    else:
        fig, axs = subplots(1, len(args), figsize=(10,8))
        fig.suptitle(r'Dust Density: $\log_{10}(\rho_{p})$')
        for i in range(len(axs)):
            p1 = axs[i].contourf(x, y, rhops[i], res)
            axs[i].set_facecolor('black')
            axs[i].set_xlabel('x')
            axs[i].set_ylabel('y')
            axs[i].set_title('t = %s' % times[i])
    show()

# Plot x-z profile
def diskxy_xz(a):
    lg_rhop_xz = log10(rhop[:,int(ny/2),:] + epsi)
    resxz = linspace(lg_rhop_xz.max()-4, lg_rhop_xz.max(), 256)
    fig, ax = subplots(1, 1)
    ax.contourf(r, z, lg_rhop_xz, resxz)
    ax.set_xlim([r.min(), r.max()])
    ax.set_ylim([z.min(), z.max()])
    ax.set_title('x-z, t = %s' % a) 
    ax.set_xlabel('x')
    ax.set_ylabel('z')
    ax.set_aspect('equal')
    show()
    
# Vorticity plot
def vort_plot(ivar):
    ff = pc.read_var(trimall=True, ivar=ivar, magic=["vort"])
    r = ff.x; phi = ff.y; 
    vort_z = ff.vort[2,...]
    fig, ax = subplots(1, 1)
    ax.contourf(r, phi, mean(vort_z, axis=0), linspace(-1, 1, 256))
    ax.set_title('Vorticity')
    ax.set_xlabel('r')
    ax.set_ylabel(r'$\phi$')
    show() #84

disk_plot(21)
#vort_plot(21)    
#disk_xz(21)
