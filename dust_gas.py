from pylab import *
import pencil as pc

svar = load('saved/var21.npz')
mnz = int(32/2)
#with load('saved/var21.npz') as svar:
r = svar['r']
phi = svar['phi']
z = svar['z']
rhop = svar['rhop']
rho = svar['rho']
vort = svar['vort']

# Objects for contours:
lg_rhop = log10(rhop[mnz,...] + 1e-4)
lg_rho = log10(rho[mnz,...] + 1e-4)
lg_dtog = lg_rhop/lg_rho
vort_z = vort[2,...]

# Original Data:
rhop = rhop[mnz,...]
rho = rho[mnz,...]
dtog = rhop/rho

# For contour levels:
resp = linspace(lg_rhop.max()-4, lg_rhop.max(), 256)
resg = linspace(lg_rho.min(), lg_rho.max(), 256)
rese = linspace(-1, 1, 256)

nrows = 2; ncols = 2
fig, ax = subplots(nrows=2, ncols=2)
# Dust density
ax[0,0].set_title(r'$\rho_{p}$')
A1 = ax[0,0].contourf(r, phi, lg_rhop, resp)
cbar = colorbar(A1, ax=ax[0,0], orientation='vertical')
ax00_ticks = ["{:0.0f}".format(i)
              for i in linspace(amin(rhop), amax(rhop), 9)]
cbar.ax.set_yticklabels(ax00_ticks)
            
# Gas density
ax[0,1].set_title(r'$\rho_{g}$')
A2 = ax[0,1].contourf(r, phi, lg_rho, resg)
cbar = colorbar(A2, ax=ax[0,1], orientation='vertical')
ax01_ticks = ["{:0.2f}".format(i)
        for i in linspace(amin(rho), amax(rho), 9)]
cbar.ax.set_yticklabels(ax01_ticks)

# Dust to Gas ratio density
ax[1,0].set_title(r'$\rho_{p}/\rho_{g}$')
A3 = ax[1,0].contourf(r, phi, lg_dtog, rese)
cbar = colorbar(A3, ax=ax[1,0], orientation='vertical')
ax10_ticks = ["{:0.2f}".format(i)
        for i in linspace(amin(dtog), amax(dtog), 9)]
cbar.ax.set_yticklabels(ax10_ticks)

# Vorticity
ax[1,1].set_title('Vorticity')
A4 = ax[1,1].contourf(r, phi, mean(vort_z, axis=0), rese)
cbar = colorbar(A4, ax=ax[1,1], orientation='vertical')
vvv = mean(vort_z, axis=0)
ax11_ticks = ["{:0.2f}".format(i)
        for i in linspace(amin(vvv), amax(vvv), 9)]
cbar.ax.set_yticklabels(ax11_ticks)

for i in range(nrows):
    for j in range(ncols):
        ax[i,j].set_facecolor('black')
        ax[i,j].set_xlabel('r'); ax[i,j].set_ylabel(r'$\phi$')
show()
