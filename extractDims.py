import pencil as pc
from pylab import *

# Assign datadir to the path of your data directory
#datadir='/media/cmp/Storage/research/Streaming3D/data'
datadir='./data'
ivar = 21

# Data variables:
ff = pc.read_var(trimall=True, datadir=datadir, ivar=ivar)
r = ff.x
phi = ff.y
z = ff.z
rhop = ff.rhop
NP = ff.np
np_max = amax(NP)
np_min = amin(NP)

# Assign npar variable
from pencil.files import pdim
npar = pdim.read_pdim().npar

from pencil.files import dim
nx = dim.read_dim().nx
ny = dim.read_dim().ny
nz = dim.read_dim().nz
# Parameters:
par = pc.read_param(datadir=datadir)
cs0 = par.cs0
pd = par.dustdensity_powerlaw
pg = par.density_power_law
eps0 = par.eps_dtog # Dust to gas ratio

# Grid variables:
from pencil.files import grid
Lx = grid.read_grid().Lx
Ly = grid.read_grid().Ly
Lz = grid.read_grid().Lz

r_int = round(amin(grid.read_grid().x), 3) # Inner boundary
r_ext = round(amax(grid.read_grid().x), 3) # Outer boundary

#grids = {"Lx":Lx, "Ly":Ly, "Lz":Lz,
#         "dx":grid.dx, "dy":grid.dy, "dz":grid.dx}


######################################################
# Assign multiple variables for each data file (experimental):
# ff = []
# ivar = [2, 4, 21] # Array containing the var number you want to read in
# for ivar in ivar:
#     var = pc.read_var(trimall=True, ivar=ivar)
#     ff.append(var)

# ff21 = ff[2]
# AA = amax(ff21.np)
# A = amax(ff[2].np)

