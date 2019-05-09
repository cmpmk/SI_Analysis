########## allclumps ##########
## Full disk clump analysis ##
from pylab import *

consts = load('saved/constants.npz')
xyz = load('saved/xyz.npz')
dat = load('saved/var21.npz')

r, phi, z = xyz['r'], xyz['phi'], xyz['z'] # Load box arrays

nx, ny, nz = consts['nx'], consts['ny'], consts['nz'] # Load grid resolution
npar = consts['npar'] # Load number of particles

np = dat['NP']        # Load particle density (np) vals
rhop = dat['rhop']    # Load particle density

# Stack all the np levels
def stack_nps():
    nofp = zeros((ny, nx))
    for i in arange(0, nz):
        nofp += np[i,...]
    return nofp

# Stack all the rhop levels
def stack_rhops():
    nrhop = zeros((ny, nx))
    for i in arange(0, nz):
        nrhop += rhop[i,...]
    return nrhop

nrhop = stack_rhops()
nofp = stack_nps()

def largest_locs(Array, n):
    flat = Array.flatten()
    indices = argpartition(flat, -n)[-n:]
    indices = indices[argsort(-flat[indices])]
    return unravel_index(indices, Array.shape)

cl_np = asarray(largest_locs(nofp, 10)) # assign the ff.np return as an array
cl_rhop = asarray(largest_locs(nrhop, 10)) # assign the ff.rhop return as an array

rloc = cl_np[1] # r-coordinates
ploc = cl_np[0] # phi-coordinates


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

def Hill_Radius(Mclump):
    M0 = 2000 # Solar mass in code units
    R = 0.5 # Testing purposes
    Rh = R*(Mclump/(3.* M0))**(1./3)
    return Rh


# Determine roche densities 
def Roche_Limit(R):
    M0 = 2000 # Solar mass in code units
    rhor = (3/(2*pi))*(M0 / R**3)
    return rhor

rhor = Roche_Limit(r) # Create an array of roche densities for each point along the radius
print(rhor)

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

