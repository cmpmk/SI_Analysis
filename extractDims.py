import pencil as pc

# Load in objects:
ff = pc.read_var(trimall=True, datadir='/media/cmp/Storage/SIMovie/data')
dim = pc.read_dim(datadir='/media/cmp/Storage/SIMovie/data')
par = pc.read_param(datadir='/media/cmp/Storage/SIMovie/data')
grid = pc.read_grid(datadir='/media/cmp/Storage/SIMovie/data')

# Parameters:
cs0 = par.cs0
pd = par.dustdensity_powerlaw
pg = par.density_power_law
eps0 = par.eps_dtog # Dust to gas ratio

# Grid variables:

grids = {"Lx": grid.Lx, "Ly":grid.Ly, "Lz": grid.Lz,
         "dx": grid.dx, "dy":grid.dy, "dz":grid.dx}

print(grids)
