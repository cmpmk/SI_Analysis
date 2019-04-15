import pencil as pc
from pylab import *

#### Return coordinates of most massive clump:
ff = pc.read_var(trimall=True, ivar = 21)
dim = pc.read_dim()

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

print(N[31, 26, 160])
adj = 0.03
def return_coors(X, Y, Z):
    print(r[X], phi[Y], z[Z])

    
    
return_coors(26, 160, 31)

#contourf(r, z, N[:,int(1024/2),:], 256)
#contourf(r, phi, N[int(iz),...], 256)
#xlim(r[ix]-adj, r[ix]+adj)
#ylim(phi[iy]-adj, phi[iy]+adj)
#show()


def stack_rhops():
#    rp = []
    for i in range(nz):
        rp = sum(
#    print(shape(rp))
#    contourf(r, phi, rp, 256)
    show()
    
stack_rhops()




#M = N.flatten()
#n = 10 # n highest values
#M = (M[argsort(M)[-n:]])
#print(M)
#X = array([])
#Y = array([])
#for i in M:
#    y, x = where(N==i)
#    X = append(X,r[x])
#    Y = append(Y,phi[y])


# pos = 8
# fig, ax = subplots(1,4)
# adj = 0.02;
# print(X)
# print(Y)
# for i in range(4):
#     ax[i].contourf(r, phi, N, 256)
#     ax[i].set_xlim(X[i]-adj, X[i]+adj)
#     ax[i].set_ylim(Y[i]-adj, Y[i]+adj)
#show()
#ax.contourf(r, phi, N, 256)
# nz = 32
# def plot_mass():
#     fig, axs = subplots(1, 2)
#     P1 = axs[0].contourf(ff.x, ff.y, ff.np[int(nz/2),...], 256)
#     cbar = colorbar(P1, orientation='horizontal')
#     adj = 0.03
#     axs[1].contourf(x, y, N, 256)
#     axs[1].set_xlim([x_loc-adj, x_loc+adj])
#     axs[1].set_ylim([y_loc-adj, y_loc+adj])
#     show()
#plot_mass()

#x_loc = X[pos]
#y_loc = Y[pos]
#ax.set_xlim(x_loc-adj, x_loc+adj)
#ax.set_ylim(y_loc-adj, y_loc+adj)
#show()

