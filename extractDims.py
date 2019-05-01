import pencil as pc
from pylab import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("datafile", type=int, help='Input var file')
var = parser.parse_args().datafile

# Assign datadir to the path of your data directory
datadir='./data'
cnst = load('saved/constants.npz')

# Data variables:
#ff = pc.read_var(trimall=True, datadir=datadir, ivar=var)
ff = load('saved/var%02d.npz' % var)
r = ff['r']
phi = ff['phi']
z = ff['z']
rhop = ff['rhop']
NP = ff['NP']
np_max = amax(NP)
np_min = amin(NP)

# Assign npar variable
npar = cnst['npar']

# Assign grid resolution variables
nx = cnst['nx']
ny = cnst['ny']
nz = cnst['nz']

# Grid variables:
Lx = cnst['Lx']
Ly = cnst['Ly']
Lz = cnst['Lz']

# Radial Boundaries
r_int = cnst['r_int']
r_ext = cnst['r_ext']

# Parameters:
cs0 = cnst['cs0']
pd = cnst['pd']
pg = cnst['pg']
eps0 = cnst['eps0']

# Misc:
Mceres = 8.958e23

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
