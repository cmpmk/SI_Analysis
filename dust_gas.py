from pylab import *
import pencil as pc

ff = pc.read_var(trimall=True, ivar=21, magic=["vort"])
nz = 32
r = ff.x
phi = ff.y
z = ff.z

rhop = log10(ff.rhop[int(nz/2),...] + 1e-4)
rho = log10(ff.rho[int(nz/2),...] + 1e-4)
vort_z = ff.vort[2,...]
resp = linspace(rhop.max()-4, rhop.max(), 256)
resg = linspace(rho.min(), rho.max(), 256)

fig, ax = subplots(1, 3, sharex=True, sharey=True)
ax[0].contourf(r, phi, rhop, resp)
ax[1].contourf(r, phi, rho, resg)
ax[2].contourf(r, phi, mean(vort_z, axis=0), linspace(-1, 1, 256))
ax[0].set_title(r'$\rho_{p}$')
ax[1].set_title(r'$\rho_{g}$')
ax[2].set_title('Vorticity')
for i in range(len(ax)):
    ax[i].set_facecolor('black')
fig.tight_layout()
show()
