### clumpMass ###
from extractDims import *

def clumpMass(npval):
    from extractDims import r_ext, r_int
    # Minimum mass solar nebula
    # Sigma = 1500 (r/AU)**(-1.5) g/cm3
    # T = 280/sqrt(r/AU) K
    sigma0 = 1500.
    # T0 = 280, Omega0 = sqrt(G*Msun/AU ** 1.5), H0 = cs0/Omega0, rho0 = sigma0/H0

    unit_length = 1.49e13       # AU
    unit_column_density = 1500  # g/cm3
    dust_to_gas_ratio = 1e-4

    r_ext = r_ext * unit_length # Outer disk boundary
    r_int = r_int * unit_length # Inner disk boundary

    r0 = 1.0 * unit_length      # (AU) Reference radius
    rho0 = 1.0 * unit_length    # Initial density

    Mdisk = 2*pi/(2-pd) * sigma0 * (r0**(pd))*(r_ext**(2-pd) - r_int**(2-pd))
        
    # Check if mass of gas, disk, and dust are proportional
    Mgas = Mdisk
    Mdust = Mgas * dust_to_gas_ratio
    
    Mp = Mdust/npar
    Mclump = np_max*Mp

    print('Mass of disk = ', "{:.2e}".format(Mdisk))
    print('Mass per particle = ', "{:2e}".format(Mp))
    print('Mass of clump (g) = ', "{:.2e}".format(Mclump))
    print('Mass of clump (ceres)=', "{:.2e}".format(Mclump/Mceres))

Clump1 = clumpMass(2053)

def plot_mass():
    #### Return coordinates of most massive clump:
    N = NP[int(nz/2),...] 
    index = unravel_index(argmax(N, axis=None), N.shape)  # Get the largest value from the ff.np array
    x_loc = r[index[1]]   # Grab the x value from the index
    y_loc = phi[index[0]] # Grab the y value from the index
    adj = 0.03 # Used to limit axes to mimic zooming into the mass

    fig, axs = subplots(1, 2)
    fig.suptitle('Largest Located Clump')
    P1 = axs[0].contourf(r, phi, NP[int(nz/2),...], 256) # Plot the entire region 
    cbar = colorbar(P1, orientation='horizontal')
    axs[1].contourf(r, phi, N, 256)                      # Plot the mass        
    axs[1].set_xlim([x_loc-adj, x_loc+adj])
    axs[1].set_ylim([y_loc-adj, y_loc+adj])
    for i in range(len(axs)):
        axs[i].set_xlabel('r')
        axs[i].set_ylabel(r'$\phi$')
    show()
plot_mass()
