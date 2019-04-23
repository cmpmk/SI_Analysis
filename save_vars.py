import os
import numpy as np
import pencil as pc
import argparse

# Define path of new directory to save npz files to
path_dir = './saved/'
# Make the directory if it doesn't already exists
if not os.path.exists(path_dir):
    os.makedirs(path_dir)

# Grab VAR number from CLI input:
parser = argparse.ArgumentParser()
parser.add_argument("datafile", type=int, help='Input var file')
var = parser.parse_args().datafile

datadir='./data'

# Assing data to object
ff = pc.read_var(trimall=True, datadir=datadir, ivar=var, magic=["vort"])
fname = ('var%02d' % var)
fsave = np.savez_compressed(os.path.join(path_dir,fname), r=ff.x, phi=ff.y, z=ff.z, rhop=ff.rhop, rho=ff.rho, vort=ff.vort, NP=ff.np)


def constants():
    from pencil.files import pdim
    npar = pdim.read_pdim().npar
    # Get grid dimensions
    from pencil.files import dim
    nx = dim.read_dim().nx
    ny = dim.read_dim().ny
    nz = dim.read_dim().nz

    # Get parameters:
    par = pc.read_param(datadir=datadir)
    cs0 = par.cs0
    pd = par.dustdensity_powerlaw
    pg = par.density_power_law
    eps0 = par.eps_dtog

    # Box size:
    from pencil.files import grid
    Lx = grid.read_grid().Lx
    Ly = grid.read_grid().Ly
    Lz = grid.read_grid().Lz

    r_int = round(np.amin(grid.read_grid().x), 1)
    r_ext = round(np.amax(grid.read_grid().x), 1)

    fname = 'constants'
    fsave = np.savez_compressed(os.path.join(path_dir,fname), npar=npar,
                                nx=nx, ny=ny, nz=nz, cs0=cs0, pd=pd, pg=pg, eps0=eps0,
                                Lx = Lx, Ly = Ly, Lz = Lz, r_int = r_int, r_ext = r_ext)
#constants()
