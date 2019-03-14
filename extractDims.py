import pencil as pc
from pylab import *

ivar = 21
# Assign datadir to the path of your data directory
#datadir='/media/cmp/Storage/research/Streaming3D/data'
datadir='./data'

# Data variables:
ff = pc.read_var(trimall=True, datadir=datadir, ivar=ivar)
NP = ff.np
r = ff.x
phi = ff.y
z = ff.z
rhop = ff.rhop

# Assign npar variable
pdim = pc.read_pdim(datadir=datadir)
npar = pdim.npar

dim = pc.read_dim(datadir=datadir)
# Parameters:
par = pc.read_param(datadir=datadir)
cs0 = par.cs0
pd = par.dustdensity_powerlaw
pg = par.density_power_law
eps0 = par.eps_dtog # Dust to gas ratio

# Grid variables:
grid = pc.read_grid(datadir=datadir)
Lx = grid.Lx
Ly = grid.Ly
Lz = grid.Lz

r_int = round(amin(grid.x), 3) # Inner boundary
r_ext = round(amax(grid.x), 3) # Outer boundary

grids = {"Lx":grid.Lx, "Ly":grid.Ly, "Lz":grid.Lz,
         "dx":grid.dx, "dy":grid.dy, "dz":grid.dx}


######################################################
# Assign multiple variables for each data file (experimental):
ff = []
ivar = [2, 4, 21] # Array containing the var number you want to read in
for ivar in ivar:
    var = pc.read_var(trimall=True, ivar=ivar)
    ff.append(var)

ff21 = ff[2]
AA = amax(ff21.np)
A = amax(ff[2].np)

