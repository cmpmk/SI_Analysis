import pencil as pc
from pylab import *

ffa = pc.read_var(trimall=True, ivar=2, magic=["vort"])
ffb = pc.read_var(trimall=True, ivar=10, magic=["vort"])
ffc = pc.read_var(trimall=True, ivar=21, magic=["vort"])

#vortz_mid = ff1.vort[2, int(dim.nz/2),...]
#print(vortz_mid.min(), vortz_mid.max())

r, phi = meshgrid(ffa.x, ffa.y)
omega = 1./r**1.5
vort_k = omega/2
nz = 32/2
vort_avg = mean(mean(ffa.vort, axis=0), axis=0)
res = linspace(-2.5, 2.5, 256)

# fig, axs = subplots(1,2)
# axs[0].contourf(r, phi, vort_avg, res)
# axs[1].contourf(r, phi, ffb.vort[2, int(nz),...]/vort_k, res)
# show()

def vort_avg(x):
    return mean(mean(x, axis=0), axis=0)

def VortAvg():
    r, phi = meshgrid(ffa.x, ffa.y)
    res = linspace(-1, 1, 256)
    fig, axs = subplots(1,3)
    fig.suptitle('Vorticity')
    axs[0].contourf(r, phi, vort_avg(ffa.vort), res)
    axs[1].contourf(r, phi, vort_avg(ffb.vort), res)
    axs[2].contourf(r, phi, vort_avg(ffc.vort), res)
    axs[0].set_title('t = 2 (orbits)')
    axs[1].set_title('t = 10 (orbits)')
    axs[2].set_title('t = 21 (orbits)')
    axs[0].set_xlabel('x')
    axs[1].set_xlabel('x')
    axs[2].set_xlabel('x')
    axs[0].set_ylabel('y')
    axs[1].set_ylabel('y')
    axs[2].set_ylabel('y')
    show()
VortAvg()
    
def VortMulti():
    ff15 = pc.read_var(trimall=True, ivar=15, magic=["vort"])
    ff18 = pc.read_var(trimall=True, ivar=18, magic=["vort"])
    ff20 = pc.read_var(trimall=True, ivar=21, magic=["vort"])

    fig, axs = subplots(2, 3, sharex=True, sharey=True)
    fig.suptitle('Vorticity')
    axs[0,0].contourf(r, phi, ff1.vort[2, int(nz),...]/vort_k, res)
    axs[0,1].contourf(r, phi, ff5.vort[2, int(nz),...]/vort_k, res)
    axs[0,2].contourf(r, phi, ff10.vort[2, int(nz),...]/vort_k, res)
    axs[1,0].contourf(r, phi, ff15.vort[2, int(nz),...]/vort_k, res)
    axs[1,1].contourf(r, phi, ff18.vort[2, int(nz),...]/vort_k, res)
    axs[1,2].contourf(r, phi, ff20.vort[2, int(nz),...]/vort_k, res)
