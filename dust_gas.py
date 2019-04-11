from pylab import *
import pencil as pc

svar = load('saved/var21.npz')
nz = 32
with load('saved/var21.npz') as svar:
    r = svar['r']
    phi = svar['phi']
    z = svar['z']
    rhop = svar['rhop']
    rho = svar['rho']
    vort = svar['vort']
    
rhop = log10(rhop[int(nz/2),...] + 1e-4)
rho = log10(rho[int(nz/2),...] + 1e-4)
dtog = rhop/rho
vort_z = vort[2,...]

resp = linspace(rhop.max()-4, rhop.max(), 256)
resg = linspace(rho.min(), rho.max(), 256)
rese = linspace(-1, 1, 256)

fig, ax = subplots(nrows=2, ncols=2)
# Dust density
ax[0,0].set_facecolor('black')
ax[0,0].set_xlabel('r'); ax[0,0].set_ylabel(r'$\phi$')
ax[0,0].set_title(r'$\rho_{p}$')
A1 = ax[0,0].contourf(r, phi, rhop, resp)
cbar = colorbar(A1, ax=ax[0,0], orientation='vertical')
cbar.set_ticks(linspace(0, amax(rhop), num=5))

# Gas density
ax[0,1].set_facecolor('black')
ax[0,1].set_xlabel('r'); ax[0,1].set_ylabel(r'$\phi$')
ax[0,1].set_title(r'$\rho_{g}$')
A2 = ax[0,1].contourf(r, phi, rho, resg)

# Dust to Gas ratio density
ax[1,0].set_facecolor('black')
ax[1,0].set_xlabel('r'); ax[1,0].set_ylabel(r'$\phi$')
ax[1,0].set_title(r'$\rho_{p}/\rho_{g}$')
A3 = ax[1,0].contourf(r, phi, dtog, rese)

# Vorticity
ax[1,1].set_facecolor('black')
ax[1,1].set_xlabel('r'); ax[1,1].set_ylabel(r'$\phi$')
ax[1,1].set_title('Vorticity')
A4 = ax[1,1].contourf(r, phi, mean(vort_z, axis=0), rese)

show()
