########## allclumps ##########
from pylab import *
import pencil as pc
consts = load('saved/constants.npz')

# Determine the location of the n-largest masses in the disk

ff = pc.read_var(trimall=True, ivar = 21)
epsi = 1e-4

r, phi, z, nz = ff.x, ff.y, ff.z, 32
pd = consts['pd']
npar = consts['npar']
#ix, iy, iz = MM[2], MM[1], MM[0]

### Return coordinates of most massive clump:
def return_coors(X, Y, Z):
    print(r[X], phi[Y], z[Z])
    return_coors(ix, iy, iz)

# Stack all the np levels    
def stack_nps():
    nofp = zeros((1024, 384))
    for i in arange(0, nz):
        nofp += ff.np[i,...]
    return nofp

nofp = stack_nps()
r2d, p2d = meshgrid(ff.x, ff.y)
x = r2d*cos(p2d)
y = r2d*sin(p2d)
fig, ax = subplots(1,2)
nofp10 = log10(nofp + 1e-4)
ax[0].contourf(x, y, nofp, 256)
ax[0].set_aspect('equal')
ax[1].contourf(x, y, ff.np[16,...], 256)
ax[1].set_aspect('equal')
show()
A = list(map(max, nofp))

# Convert code units to physical units for clumps
def clump_mass(npval):
    unit_length = 1.49e13      # AU
    unit_column_density = 1500 # g/cm3
    dtog = 1e-4
    sigma0 = 1500.
    r_ext = consts['r_ext']*unit_length
    r_int = consts['r_int']*unit_length
    r0 = 1.0*unit_length   # AU
    rho0 = 1.0*unit_length # Initial density
    Mdisk = 2*pi/(2-pd) *sigma0 * (r0**(pd))*(r_ext**(2-pd) - r_int**(2-pd))
    Mgas = Mdisk
    Mdust = Mgas * dtog
    Mp = Mdust / npar
    Mclump = npval*Mp
    return Mclump

# Determine roche for clump
def Roche_Limit(mass):
    M = 1.989e33 # (g), solar mass
    m = clump_mass(mass)
    au_to_km = 1.496e8
    R = 695.5e6 # m
    d = R*(2*(M/m))**(1./3)
    return d

#a = Roche_Limit(2053)

#print(a/(1.496e8))

