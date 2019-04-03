import pencil as pc
from pylab import *

epsi = 1e-4
ny = 1024; nz = 32

# Function to return variables for desired data file
def Disk(ivar):
    ff = pc.read_var(trimall=True, ivar=ivar, quiet=True)
    global  x, y, rhop, res
    r2d, p2d = meshgrid(ff.x, ff.y) # r, phi
    x = r2d*cos(p2d)
    y = r2d*sin(p2d)
    rhop = ff.rhop
    lg_rhop_xy = log10(rhop[int(nz/2),...] + epsi)
    res = linspace(lg_rhop_xy.max()-4, lg_rhop_xy.max(), 256)
    return lg_rhop_xy

# Plot xy and xz planes of the disk side by side
def diskxy_xz(a):
    lg_rhop_xy = Disk(a)
    #z = var.read_var(trimall=True, ivar=1).z
    lg_rhop_xz = log10(rhop[:,int(ny/2),:] + epsi)
    resxz = linspace(lg_rhop_xz.max()-4, lg_rhop_xz.max(), 256)
    fig, ax = subplots(1, 2)
    fig.suptitle('Dust Density at t = %s Orbits' % a)
    ax[0].contourf(x, y, lg_rhop_xy, resxy)
    ax[0].set_xlim([x.min(), x.max()])
    ax[0].set_ylim([y.min(), y.max()])
    ax[0].set_title('x-y');     ax[0].set_ylabel('y')
    ax[1].contourf(r, z, lg_rhop_xz, resxz)
    ax[1].set_xlim([r.min(), r.max()])
    ax[1].set_ylim([z.min(), z.max()])
    ax[1].set_title('x-z');     ax[1].set_ylabel('z')
    for i in range(len(ax)):
        ax[i].set_facecolor('black')
        ax[i].set_xlabel('x')
        ax[i].set_aspect('equal')
    show()
# Return 1xn subplots of dust density contour at each orbit
def disk_plot(*args):
    times = [*args]
    rhops = [Disk(t) for t in times]
    fig, axs = subplots(1, len(args))
    fig.suptitle(r'Dust Density: $\log_{10}(\rho_{p})$')
    for i in range(len(axs)):
        axs[i].contourf(x, y, rhops[i], res)
        axs[i].set_facecolor('black')
        axs[i].set_xlabel('x')
        axs[i].set_ylabel('y')
        axs[i].set_title('t = %s' % times[i])
        axs[i].set_aspect('equal')
        #cbar = fig.colorbar(p1, ax=axs, orientation='horizontal')
    show()
# Vorticity plot
def vort_plot(ivar):
    ff = pc.read_var(trimall=True, ivar=ivar, magic=["vort"])
    r = ff.x; phi = ff.y; z = ff.z
    vort_z = ff.vort[2,...]
    rhop = log10(ff.rhop[int(nz/2),...] + epsi)
    rho = log10(ff.rho[int(nz/2),...] + epsi)
    res = linspace(rhop.max()-4, rhop.max(), 256)
    fig, ax = subplots(1, 2)
    ax[0].contourf(r, phi, mean(vort_z, axis=0), linspace(-1, 1, 256))
    ax[1].contourf(r, phi, rhop/rho, res) 
    ax[0].set_title('Vorticity')
    ax[1].set_title(r'$\rho_{p}/\rho_{g}$')
    ax[1].set_facecolor('black')
    for i in range(len(ax)):
        ax[i].set_xlabel('r')
        ax[i].set_ylabel(r'$\phi$')
    show() #84
disk_plot(2, 3, 4, 5)
#vort_plot(21)    
#diskxy_xz(21)
#disk_plot_3(2, 15, 21) #30.5, 29.9, 30.5
#disk_plot_6(2, 3, 8, 12, 15, 21) #87


#        fig, axs = subplots(2, 3)
#        for i, row in enumerate(axs):
#            for j, ax in enumerate(row):
#                axs[i,j].set_facecolor('black')
#                axs[i,j].contourf(x, y, rhops[i,j], res)
