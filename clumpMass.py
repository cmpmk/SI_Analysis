from extractDims import *

print('np_min, np_max = %s, %s' % (np_min, np_max))
print('npar =', npar)
print('Disk Radius = ', Lx)
print('Dust, Gas Density Power Law = %s, %s' % ( pd, pg))
np_max = 1053
# Minimum mass solar nebula
#
# Sigma = 1500 (r/AU)**(-1.5) g/cm3
# T = 280/sqrt(r/AU) K
#

sigma0 = 1500.
# T0 = 280.
# cs0 =
# Omega0 = sqrt(G*Msun/AU**1.5)
# H0 = cs0/Omega0
# rho0 = sigma0/H0

unit_length = 1.49e13 # AU
unit_column_density = 1500 # g/cm3
dust_to_gas_ratio = 1e-4

r_ext = 2.5 * unit_length
r_int = 0.4 * unit_length

r0 = 1.0 * unit_length   # (AU) Reference radius
rho0 = 1.0 * unit_length # Initial density
#sigma0 = rho0 * Lz
Mdisk = 2*pi/(2-pd) * sigma0 * (r0**(pd))*(r_ext**(2-pd) - r_int**(2-pd))

#
# Specify what the global dust_to_gas ratio is
#

# Check if mass of gas, disk, and dust are proportional
Mgas = Mdisk
Mdust = Mgas * dust_to_gas_ratio

Mp = Mdust/npar
Mclump = np_max*Mp

print('Mass of disk: ', round(Mdisk, 3))
print('Mp = ', "{:2e}".format(Mp))
print('Mass of clump = ', "{:.2e}".format(Mclump))
Mceres = 8.958e23
print('Mass of clump (ceres)=', "{:.2e}".format(Mclump/Mceres))
# Return index of max NP value:
# ff.np shape is [32, 1024, 384]
# index returns [31, 26, 160]
# NP[31, 26, 160] = 2053, so this is the correct location

#### Return coordinates of most massive clump:
x = ff.x; y = ff.y
N = ff.np[int(nz/2),...] 
#N = ff.np[31,...]  # 0.86, -2.979
index = unravel_index(argmax(N, axis=None), N.shape)
x_loc = x[index[1]] #0.852
y_loc = y[index[0]] #-2.936
#x_loc = 0.843782
#y_loc = -0.23623
print('Largest value found: ', (N[index]))
print('x, y coordinates %s, %s' % (round(x_loc, 3),round(y_loc, 3)))


# #fig, ax = subplots(1, 1)
# fig.suptitle(r'Largest Located Clump ~$10^{22}g$')
# p1 = ax.contourf(ff.x, ff.y, ff.np[int(nz/2),...], 256)
# cbar = colorbar(p1, orientation='vertical')
# adj = 0.03
# #ax.contourf(x, y, N, 256)
# ax.set_xlim([x_loc-adj, x_loc+adj])
# ax.set_ylim([y_loc-adj, y_loc+adj])
# ax.set_xlabel('r')
# ax.set_ylabel(r'$\phi$')
# show()
#     
# def plot_mass():
#     fig, axs = subplots(1, 2)
#     fig.suptitle('Largest Located Clump 10^20 - 10^22 kg')
#     P1 = axs[0].contourf(ff.x, ff.y, ff.np[int(nz/2),...], 256)
#     cbar = colorbar(P1, orientation='horizontal')
#     adj = 0.03
#     axs[1].contourf(x, y, N, 256)
#     axs[1].set_xlim([x_loc-adj, x_loc+adj])
#     axs[1].set_ylim([y_loc-adj, y_loc+adj])
#     for i in range(len(axs)):
#         axs[i].set_xlabel('r')
#         axs[i].set_ylabel(r'$\phi$')
#     show()
# plot_mass()

# Determine the location of the n-largest masses in the disk

#n = 10  # Number of returns

#ff = pc.read_var(trimall=True, ivar=21)
#N = ff.np[16,...]
#M = N.flatten()
#index = unravel_index(N[argsort(N)[-n:]])
#print(index)
#y, x = where(N==M[i])
#x = ff.x; y = ff.y  
#N = ff.np[16,...]
#index = unravel_index(N[argsort(N)[-n:]])
#print(index)
#N.sort(); print(N)
