import pencil as pc
from pylab import *

ffa = pc.read_var(trimall=True, ivar=1, magic=["vort"])
ffb = pc.read_var(trimall=True, ivar=3, magic=["vort"])
ffc = pc.read_var(trimall=True, ivar=7, magic=["vort"])

#vortz_mid = ff1.vort[2, int(dim.nz/2),...]
#print(vortz_mid.min())
#print(vortz_mid.max())

r, phi = meshgrid(ffa.x, ffa.y)
omega = 1./r**1.5
vort_k = omega/2
nz = 32/2
res = linspace(-1, 1, 256)

fig, axs = subplots(1, 3)
fig.suptitle('Vorticity')
axs[0].contourf(r, phi, ffa.vort[2, int(nz),...]/vort_k, res)
axs[1].contourf(r, phi, ffb.vort[2, int(nz),...]/vort_k, res)
axs[2].contourf(r, phi, ffc.vort[2, int(nz),...]/vort_k, res)
show()
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

#contourf(ff.x,ff.y,ff.vort[2,int(dim.nz/2),...], linspace(-1, 1, 256))
#contourf(ff.x,ff.y,ff.vort[2,int(dim.nz/2),...]/vort_k, linspace(-1,1,256))
