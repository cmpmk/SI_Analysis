from extractDims import *

print('np_min = ', amin(NP))
print('np_max = ', amax(NP))
print('npar =', npar)
print('Disk Radius = ', Lx)
print('Dust Density Power Law = ', pd)
print('Gas Density Power Law = ', pg)

r0 = 1.0 # (AU) Reference radius
rho0 = 1.0
sigma0 = rho0 * Lz
Mdisk = 4*pi*sigma0*(r0**(pd))*(sqrt(r_ext) - sqrt(r_int))

print('Mass of disk: ', round(Mdisk, 3))

if (eps0 == 1.0):
    Mgas = Mdisk
    Mdust = Mgas

Mp = Mdust/npar
print(Mp)

Mclump = amax(NP)*Mp
print('Mass of clump = ', "{:.2e}".format(Mclump))

#r0 = 5
sigma = sigma0 * (Lx/r0)**(-pd)

# def np_plot(x):
#     ff = pc.read_var(trimall=True, ivar=x)
#     dim = pc.read_dim()
#     r = ff.x
#     phi = ff.y
#     z = ff.z
#     r2d, p2d = meshgrid(r, phi)
#     x = r2d*cos(p2d)
#     y = r2d*sin(p2d)
#     P1= contourf(ff.x, ff.y, ff.np[int(dim.nz/2),...], 256)
#     xlabel('x')
#     ylabel('y')
#     title('Mass Clump Formed')
#     cbar = colorbar(P1, orientation='horizontal')
#     show()
# #np_plot(21)
