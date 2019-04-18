import pencil as pc
from pylab import *

#### Return coordinates of most massive clump:
ff = pc.read_var(trimall=True, ivar = 21)
dim = pc.read_dim()
epsi = 1e-4
nz = dim.nz
# Determine the location of the n-largest masses in the disk
#[ 987. 1001. 1053. 1054. 1088. 1098. 1134. 1374. 1865. 2053.]

r = ff.x
phi = ff.y
z = ff.z
N = ff.np#[16,...]
MM = where(N==N.max())
print(MM)
ix=MM[2]
iy=MM[1]
iz=MM[0]

#print(N[31, 26, 160])
adj = 0.03
def return_coors(X, Y, Z):
    print(r[X], phi[Y], z[Z])

return_coors(ix, iy, iz)

def stack_rhops():
    rp = []
    for i in arange(0, nz):
        rp = ff.rhop[i,...]
    print(amax(rp))
    contourf(r, phi, rp, 256)
    show()

def stack_nps():
    N = []
    for i in range(0, nz):
        N = ff.np[i,...]
#    contourf(r, phi, N, 256)
    M = N.flatten()
    n = 10 # Number of values to return
    M = (M[argsort(M)[-n::]])
    print(M)
    X = array([])
    Y = array([])
    for i in M:
        y, x = where(N==i)
        X = append(X,r[x])
        Y = append(Y,phi[y])
    print('X = ', X)
    print('Y = ', Y)
    print(X[0], Y[0])


N = []
for i in range(0, nz):
    N = ff.np[i,...]

MM = where(N==N.max())
print(N.shape)
print(MM)
lg_N = log10(N + epsi)
res = linspace(amax(lg_N)-4, amax(lg_N), 256)
fig, ax = subplots(1, 1)
a = ax.contourf(r, phi, lg_N, res)
ax.set_facecolor('black')
cbar = colorbar(a,ax=ax, orientation='vertical')
cbar_ticks = ["{:0.2f}".format(i) for i in linspace(amin(N),amax(N), 9)]
cbar.ax.set_yticklabels(cbar_ticks)
show()

lg_Nz = log10(ff.np[:,int(ny/2),:] + epsi)
contourf(r, z, lg_Nz, res)
show()
#stack_rhops()
#stack_nps()
