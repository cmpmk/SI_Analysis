from extractDims import *

print('np_min, np_max = %s, %s' % (np_min, np_max))
print('npar = ', npar)
print('Disk Radius = ', Lx)
print('Dust, Gas Density Power Law = %s, %s' % (pd, pg))

# Minimum mass solar nebula:
# Sigma = 1500 (r/AU)**(-1.5) g/cm3
# T = 280/sqrt(r/AU) K
# T0 = 280., Omega0 = sqrt(G*Msun/AU**1.5), H0 = cs0/Omega0
# rho0 = sigma0/H0, sigma0 = rho0*Lz

unit_length = 1.49e13 # AU
unit_column_density = 1500 # g/cm3
dust_to_gas_ratio = 1e-4

# Inner and Outer radial boundaries
r_int = 0.4 * unit_length
r_ext = 2.5 * unit_length

r0 = 1.0 * unit_length # Reference radius (AU)
rho0 = 1.0 * unit_length  # Initial density

# Mass of disk:
Mdisk = 2*pi/(2-pd) * sigma0 * (r0**(pd))*\
        (r_ext**(2-pd) - r_int**(2-pd))

# Check if mass of gas, disk, and dust are proportional:
Mgas = Mdisk
Mdust = Mgas * dust_to_gas_ratio

# Mass per particle:
Mp = Mdust/npar
# Mass of clump(s):
Mclump = np_max*Mp

Mceres = 8.958e23

print('Mass of disk: ', round(Mdisk, 3))
print('Mass of particle(s): ', "{:2e}".format(Mp))
print('Mass of clump: ', "{:.2e}".format(Mclump/Mceres))
print('Mass of clump (ceres) = ', "{:.2e}".format(Mclump/Mceres))

########## Return coordinates of most massive clump:

x = ff.x; y = ff.y
N = ff.np[int(nz/2),...]
index = 
