import pencil as pc
from pylab import *


# Function to return variables for desired data file
def Disk(ivar):
    ff = pc.read_var(trimall=True, ivar=ivar, quiet=True)
    global  x, y, z, rhop, res, ny, nz, epsi
    r2d, p2d = meshgrid(ff.x, ff.y)            # r, phi
    x, y, z = r2d*cos(p2d), r2d*sin(p2d), ff.z # Coordinates
    ny, nz = 1024, 32                          # Grid resolutions
    epsi = 1e-4
    rhop = ff.rhop
    lg_rhop_xy = log10(rhop[int(nz/2),...] + epsi) # log10 dust density
    res = linspace(lg_rhop_xy.max()-3.5, lg_rhop_xy.max(), 256)
    return lg_rhop_xy

# Return 1xn subplots of dust density contour at each orbit
def disk_plot(*args):
    times = [*args]
    rhops = [Disk(t) for t in times]
    
    if len(args) == 1:
        fig, axs = subplots(1, 1)
        axs.contourf(x, y, rhops[0], res)
        axs.set_facecolor('black')
        xy_label(axs, 'x', 'y')
        axs.set_title('t = %s' % times[0])
    else:
        fig, axs = subplots(1, len(args), figsize=(10, 8))
        fig.suptitle(r'Dust Density: $\log_{10}(\rho_{p})$')
        for i in range(len(axs)):
            axs[i].contourf(x, y, rhops[i], res)
            axs[i].set_facecolor('black')
            xy_label(axs[i], 'x', 'y')
            axs[i].set_title('t = %s' % times[i])
    show()

# Plot x-z profile
def disk_xz(ivar):
    lg_rhop_xz = log10(rhop[:,int(ny/2),:] + epsi)
    resxz = linspace(lg_rhop_xz.max()-4, lg_rhop_xz.max(), 256)
    
    fig, ax = subplots(1, 1)
    ax.contourf(r, z, lg_rhop_xz, resxz)
    ax.set_xlim([r.min(), r.max()])
    ax.set_ylim([z.min(), z.max()])
    ax.set_title('x-z, t = %s' % ivar)
    xy_label(ax, 'x', 'z')
    ax.set_aspect('equal')
    show()
    
# Vorticity plot
def vort_plot(ivar):
    ff = pc.read_var(trimall=True, ivar=ivar, magic=["vort"])
    vort_z = ff.vort[2,...]
    
    fig, ax = subplots(1, 1)
    ax.contourf(ff.x, ff.y, mean(vort_z, axis=0), linspace(-1, 1, 256))
    ax.set_title('Vorticity')
    xy_label(ax, 'r', r'$\phi$')
    show() #84

def xy_label(obj, xlab, ylab): # Return x, y labels (reduces lines)
    return obj.set_xlabel(str(xlab)), obj.set_ylabel(str(ylab))

disk_plot(21)
#vort_plot(21)    
#disk_xz(21)
