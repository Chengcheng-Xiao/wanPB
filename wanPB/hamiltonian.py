import sys
import numpy as np
from wanPB.w90_parser import *
import pybinding as pb
import matplotlib.pyplot as plt
pb.pltutils.use_style()

def progressbar(it, prefix="", size=60, file=sys.stdout):
    '''
    progress bar function from https://stackoverflow.com/a/34482761/12660859
    '''
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), j, count))
        file.flush()
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()

def gen_lat(seedname="wannier90"):
    '''
    main function to covert w90's hamiltonian to pybinding's format
    '''
    # read-in stuff
    lat_vec, Rlatt, hopps, deg, num_wann, num_kpts = read_tb(Filename=seedname+"_tb.dat")
    wan_centers = read_center(Filename=seedname+"_centres.xyz")

    #print(f"Converting fromat: \t\t\t\t",flush=True)

    # generate lat object
    lat = pb.Lattice(a1 = lat_vec[0],
                     a2 = lat_vec[1],
                     a3 = lat_vec[2])

    # putting in all sites and their on-site energies.
    for i in progressbar(range(len(Rlatt)), "Converting on-site energyies: ", 20):
        if all(Rlatt[i]==[0, 0, 0]):
            for m in range(num_wann):
                # icount1+=1
                lat.add_one_sublattice(str(m), wan_centers[m], onsite_energy=np.real(hopps[i,m,m]))

    # putting in all hopping elements.
    # NOTE: pybinding reports error when adding hermitian conjugate of existing hoppings.
    # we just do brute force error handling on this since it's faster that using if
    # to determine which hoppings to add. (like in pythtb's interfce.)
    # note that this means we assume Wannier Hamiltonian is Hermitian.
    for i in progressbar(range(len(Rlatt)), "Converting hopping energyies: ", 20):
        for m in range(num_wann):
            for n in range(num_wann):
                try:
                    lat.add_one_hopping(Rlatt[i],
                                        str(m),
                                        str(n),
                                        hopps[i,m,n])
                except:
                    continue


    #print("done.",flush=True)

    return lat
