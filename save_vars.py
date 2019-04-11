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
fsave = np.savez(os.path.join(path_dir,fname), r=ff.x, phi=ff.y, z=ff.z, rhop=ff.rhop, rho=ff.rho, vort=ff.vort)



