########## allclumps ##########
def allClumps():
    import pencil as pc
# Determine the location of the n-largest masses in the disk

    ### Return coordinates of most massive clump:
    ff = pc.read_var(trimall=True, ivar = 21)
    epsi = 1e-4

    r, phi, z = ff.x, ff.y, ff.z
    ix, iy, iz = MM[2], MM[1], MM[0]
    
    def return_coors(X, Y, Z):
        print(r[X], phi[Y], z[Z])
    return_coors(ix, iy, iz)

    def stack_rhops():
        rp = zeros((1024, 384))
        for i in arange(0, nz):
            rp += ff.rhop[i,...]
        contourf(r, phi, rp, 256)

    def stack_nps():
        nofp = zeros((1024, 384))
        for i in arange(0, nz):
            nofp += ff.np[i,...]
        return nofp
    
    nofp = stack_nps()

#allClumps()
# 173            
