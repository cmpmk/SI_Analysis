import pencil as pc

# Load in objects:
ff = pc.read_var(trimall=True, magic=['Vort'])
dim = pc.read_dim()
par = pc.read_param()
grid = pc.read_grid()

# Parameters:
cs0 = par.cs0
pd = par.dustdensity_powerlaw
pg = par.density_power_law
eps0 = par.eps_dtog # Dust to gas ratio

# Grid variables:
Lx = grid.Lx
Ly = grid.Ly
Lz = grid.Lz

dx = grid.dx
dy = grid.dy
dz = grid.dz
