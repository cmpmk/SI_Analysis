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



#### Return coordinates of most massive clump:
ff = pc.read_var(trimall=True, ivar = 21)
dim = pc.read_dim()

nz = dim.nz
# Determine the location of the n-largest masses in the disk
#[ 987. 1001. 1053. 1054. 1088. 1098. 1134. 1374. 1865. 2053.]

r = ff.x
phi = ff.y
z = ff.z
N = ff.np#[16,...]
MM = where(N==N.max())
print(MM)
ix=MM[2]
iy=MM[1]
iz=MM[0]

print(N[31, 26, 160])
adj = 0.03
def return_coors(X, Y, Z):
    print(r[X], phi[Y], z[Z])

    
    
return_coors(26, 160, 31)

#contourf(r, z, N[:,int(1024/2),:], 256)
#contourf(r, phi, N[int(iz),...], 256)
#xlim(r[ix]-adj, r[ix]+adj)
#ylim(phi[iy]-adj, phi[iy]+adj)
#show()


def stack_rhops():
#    rp = []
    for i in range(nz):
        rp = sum(
#    print(shape(rp))
#    contourf(r, phi, rp, 256)
    show()
    
stack_rhops()




#M = N.flatten()
#n = 10 # n highest values
#M = (M[argsort(M)[-n:]])
#print(M)
#X = array([])
#Y = array([])
#for i in M:
#    y, x = where(N==i)
#    X = append(X,r[x])
#    Y = append(Y,phi[y])


# pos = 8
# fig, ax = subplots(1,4)
# adj = 0.02;
# print(X)
# print(Y)
# for i in range(4):
#     ax[i].contourf(r, phi, N, 256)
#     ax[i].set_xlim(X[i]-adj, X[i]+adj)
#     ax[i].set_ylim(Y[i]-adj, Y[i]+adj)
#show()
#ax.contourf(r, phi, N, 256)
# nz = 32
# def plot_mass():
#     fig, axs = subplots(1, 2)
#     P1 = axs[0].contourf(ff.x, ff.y, ff.np[int(nz/2),...], 256)
#     cbar = colorbar(P1, orientation='horizontal')
#     adj = 0.03
#     axs[1].contourf(x, y, N, 256)
#     axs[1].set_xlim([x_loc-adj, x_loc+adj])
#     axs[1].set_ylim([y_loc-adj, y_loc+adj])
#     show()
#plot_mass()

#x_loc = X[pos]
#y_loc = Y[pos]
#ax.set_xlim(x_loc-adj, x_loc+adj)
#ax.set_ylim(y_loc-adj, y_loc+adj)
#show()

