from extractDims import *

print('np_min, np_max = %s, %s' % (np_min, np_max))
print('npar =', npar)
print('Disk Radius = ', Lx)
print('Dust, Gas Density Power Law = %s, %s' % ( pd, pg))

r0 = 1.0   # (AU) Reference radius
rho0 = 1.0 # Initial density
sigma0 = rho0 * Lz
#sigma0 = amax(rhop)
# Expression to calculate mass of disk
Mdisk = 4*pi*sigma0*(r0**(pd))*(sqrt(r_ext) - sqrt(r_int))

# Check if mass of gas, disk, and dust are proportional
if (eps0 == 1.0):
    Mgas = Mdisk
    Mdust = Mgas

Mp = Mdust/npar

Mclump = amax(NP)*Mp

sigma = sigma0 * (Lx/r0)**(-pd) #r0 = 5 

print('Mass of disk: ', round(Mdisk, 3))
print('Mp = ', "{:2e}".format(Mp))
print('Mass of clump = ', "{:.2e}".format(Mclump))

# Return index of max NP value:
# ff.np shape is [32, 1024, 384]
# index returns [31, 26, 160]
# NP[31, 26, 160] = 2053, so this is the correct location

#### Return coordinates of most massive clump:
x = ff.x; y = ff.y
N = ff.np[int(nz/2),...]
index = unravel_index(argmax(N, axis=None), N.shape)
x_loc = x[index[1]]
y_loc = y[index[0]]
print('Largest value found: ', (N[index]))
print('x, y coordinates %s, %s' % (round(x_loc, 3),round(y_loc, 3)))

def plot_mass():
    fig, axs = subplots(1, 2)
    P1 = axs[0].contourf(ff.x, ff.y, ff.np[int(nz/2),...], 256)
    cbar = colorbar(P1, orientation='horizontal')
    adj = 0.01
    axs[1].contourf(x, y, N, 256)
    axs[1].set_xlim([x_loc-adj, x_loc+adj])
    axs[1].set_ylim([y_loc-adj, y_loc+adj])
    show()
plot_mass()

# Determine the location of the n-largest masses in the disk

#n = 10  # Number of returns

#ff = pc.read_var(trimall=True, ivar=21)
#N = ff.np
#N = N.flatten()
#print(N[argsort(N)[-n:]])

#x = ff.x; y = ff.y  
#N = ff.np[16,...]
#index = unravel_index(N[argsort(N)[-n:]])
#print(index)
#N.sort(); print(N)
