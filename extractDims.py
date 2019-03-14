import pencil as pc

#ivar = 21
datadir='/media/cmp/Storage/research/Streaming3D/data'
# Load in objects:
#ff = pc.read_var(trimall=True, datadir=datadir, ivar=ivar)
dim = pc.read_dim(datadir=datadir)
par = pc.read_param(datadir=datadir)
grid = pc.read_grid(datadir=datadir)

# Parameters:
cs0 = par.cs0
pd = par.dustdensity_powerlaw
pg = par.density_power_law
eps0 = par.eps_dtog # Dust to gas ratio

# Grid variables:
grids = {"Lx":grid.Lx, "Ly":grid.Ly, "Lz":grid.Lz,
         "dx":grid.dx, "dy":grid.dy, "dz":grid.dx}
#for key, val in grids.items():
#    print(key, ' ', val)
