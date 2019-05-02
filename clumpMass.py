# clumpMass
from extractDims import *

print('np_min, np_max, npar = %s, %s, %s' % (np_min, np_max, npar))
print('Disk Radius = ', Lx)
print('Dust, Gas Density Power Law = %s, %s' % (pd, pg))
np_max = 2053
# Minimum mass solar nebula
#
# Sigma = 1500 (r/AU)**(-1.5) g/cm3
# T = 280/sqrt(r/AU) K
    
sigma0 = 1500.
# T0 = 280.
# Omega0 = sqrt(G*Msun/AU**1.5)
# H0 = cs0/Omega0
# rho0 = sigma0/H0

unit_length = 1.49e13 # AU
unit_column_density = 1500 # g/cm3
dust_to_gas_ratio = 1e-4

r_ext = r_ext * unit_length
r_int = r_int * unit_length

r0 = 1.0 * unit_length   # (AU) Reference radius
rho0 = 1.0 * unit_length # Initial density
Mdisk = 2*pi/(2-pd) * sigma0 * (r0**(pd))*(r_ext**(2-pd) - r_int**(2-pd))

#
# Specify what the global dust_to_gas ratio is
#

# Check if mass of gas, disk, and dust are proportional
Mgas = Mdisk
Mdust = Mgas * dust_to_gas_ratio
    
Mp = Mdust/npar
Mclump = np_max*Mp

print('Mass of disk = ', "{:.2e}".format(Mdisk))
print('Mass per particle = ', "{:2e}".format(Mp))
print('Mass of clump (g) = ', "{:.2e}".format(Mclump))
print('Mass of clump (ceres)=', "{:.2e}".format(Mclump/Mceres))

#### Return coordinates of most massive clump:
N = NP[int(nz/2),...] 
index = unravel_index(argmax(N, axis=None), N.shape)
x_loc = r[index[1]] 
y_loc = phi[index[0]] 

def plot_mass():
    adj = 0.03
    fig, axs = subplots(1, 2)
    fig.suptitle('Largest Located Clump 10^20 - 10^22 kg')
    P1 = axs[0].contourf(r, phi, NP[int(nz/2),...], 256)
    cbar = colorbar(P1, orientation='horizontal')
    axs[1].contourf(r, phi, N, 256)
    axs[1].set_xlim([x_loc-adj, x_loc+adj])
    axs[1].set_ylim([y_loc-adj, y_loc+adj])
    for i in range(len(axs)):
        axs[i].set_xlabel('r')
        axs[i].set_ylabel(r'$\phi$')
    show()
