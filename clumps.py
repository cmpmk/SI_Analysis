# clumpMass
from extractDims import *

print('np_min, np_max = %s, %s' % (np_min, np_max))
print('npar =', npar)
print('Disk Radius = ', Lx)
print('Dust, Gas Density Power Law = %s, %s' % ( pd, pg))

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

print('Mass of disk: ', round(Mdisk, 3))
print('Mp = ', "{:2e}".format(Mp))
print('Mass of clump = ', "{:.2e}".format(Mclump))
print('Mass of clump (ceres)=', "{:.2e}".format(Mclump/Mceres))

#### Return coordinates of most massive clump:
N = NP[int(nz/2),...] 
index = unravel_index(argmax(N, axis=None), N.shape)
x_loc = r[index[1]] 
y_loc = phi[index[0]] 

print('Largest value found: ', (N[index]))
print('x, y coordinates %s, %s' % (round(x_loc, 3),round(y_loc, 3)))

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

    
########## allclumps ##########
def allClumps():
    import pencil as pc

    ### Return coordinates of most massive clump:
    ff = pc.read_var(trimall=True, ivar = 21)
    epsi = 1e-4
    # Determine the location of the n-largest masses in the disk
    #[ 987. 1001. 1053. 1054. 1088. 1098. 1134. 1374. 1865. 2053.]

    r, phi, z = ff.x, ff.y, ff.z
    N = ff.np
    MM = where(N==N.max())
    print(MM)
    ix, iy, iz = MM[2], MM[1], MM[0]
    
    def return_coors(X, Y, Z):
        print(r[X], phi[Y], z[Z])
        
    return_coors(ix, iy, iz)

    def stack_rhops():
        rp = zeros((1024, 384))
        for i in arange(0, nz):
            rp += ff.rhop[i,...]
        contourf(r, phi, rp, 256)
        show()
    stack_rhops()
allClumps()
# 173            
