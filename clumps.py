########## allclumps ##########
## Full disk clump analysis ##
import time
start = time.time()
from pylab import *

consts = load('saved/constants.npz')
xyz = load('saved/xyz.npz')
dat = load('saved/var21.npz')

r, phi, z = xyz['r'], xyz['phi'], xyz['z'] # Load box arrays

nx, ny, nz = consts['nx'], consts['ny'], consts['nz'] # Load grid resolution
npar = consts['npar'] # Load number of particles

np = dat['NP']        # Load particle density (np) vals


# Stack all the np levels
def stack_nps():
    nofp = zeros((ny, nx))
    for i in arange(0, nz):
        nofp += np[i,...]
    return nofp

nofp = stack_nps()
print(amax(nofp))

def largest_locs(Array, n):
    flat = Array.flatten()
    indices = argpartition(flat, -n)[-n:]
    indices = indices[argsort(-flat[indices])]
    return unravel_index(indices, Array.shape)

cl_np = asarray(largest_locs(nofp, 10)) # assign the return as an array

rloc = cl_np[1]
ploc = cl_np[0]

# Compare the stacked and unstacked np values to reassure the difference
def plot_compare():
    r2d, p2d = meshgrid(r, phi)
    x = r2d*cos(p2d)
    y = r2d*sin(p2d)
    fig, ax = subplots(1,2)
    nofp10 = log10(nofp + 1e-4)
    ax[0].contourf(x, y, nofp, 256)
    ax[0].set_aspect('equal')
    ax[1].contourf(x, y, np[16,...], 256)
    ax[1].set_aspect('equal')
    show()

# Convert code units to physical units for clumps
def clump_mass(npval):
    pd = consts['pd']
    sigma0 = 1500.

    unit_length = 1.49e13      # AU
    unit_column_density = 1500 # g/cm3
    dtog = 1e-4                # Assign dust to gas ratio

    r_ext = consts['r_ext'] * unit_length # Outer disk boundary
    r_int = consts['r_int'] * unit_length # Inner disk boundary

    r0 = 1.0*unit_length   # (AU) Reference radius
    rho0 = 1.0*unit_length # Initial density

    Mdisk = 2*pi/(2-pd) *sigma0 * (r0**(pd))*(r_ext**(2-pd) - r_int**(2-pd))

    # Check if mass of gas, disk, and dust are proportional
    Mgas = Mdisk
    Mdust = Mgas * dtog

    Mp = Mdust / npar # Mass per particle
    Mclump = npval*Mp # Mass of clump (for input)

    print('Mass of disk = ', "{:.2e}".format(Mdisk))
    print('Mass per particle = ', "{:.2e}".format(Mp))
    print('Mass of clump (g))', "{:.2e}".format(Mclump))
    print('Mass of clump (ceres) = ', "{:.2e}".format(Mclump/Mceres))

    return Mclump

def plot_mass():
    ### Return coordinates of most massive clump:
    N = NP[]

# Determine roche for clump
def Roche_Limit(mass):
    M = 1.989e33 # (g), solar mass
    m = clump_mass(mass)
    au_to_km = 1.496e8
    R = 695.5e6 # m
    d = R*(2*(M/m))**(1./3)
    return d


end = time.time()
print('Time taken = ', round(end-start, 3))
