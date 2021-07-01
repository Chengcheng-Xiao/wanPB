import numpy as np
from wanPB.w90_parser import *
import pybinding as pb
import matplotlib.pyplot as plt
pb.pltutils.use_style()

def gen_lat(seedname="wannier90"):
    '''
    main function to covert w90's hamiltonian to pybinding's format
    '''
    # read-in stuff
    lat_vec, Rlatt, hopps, deg, num_wann, num_kpts = read_tb(Filename=seedname+"_tb.dat")
    wan_centers = read_center(Filename=seedname+"_centres.xyz")

    print(f"Converting... \t\t\t\t", end='',flush=True)

    # generate lat object
    lat = pb.Lattice(a1 = lat_vec[0],
                     a2 = lat_vec[1],
                     a3 = lat_vec[2])

    # icount1=0
    for i in range(len(Rlatt)):
        if all(Rlatt[i]==[0, 0, 0]):
            for m in range(num_wann):
                # icount1+=1
                lat.add_one_sublattice(str(m), wan_centers[m], onsite_energy=np.real(hopps[i,m,m]))

    # icount = 0
    for i in range(len(Rlatt)):
        for m in range(num_wann):
            for n in range(num_wann):
                try:
                    lat.add_one_hopping(Rlatt[i],
                                        str(m),
                                        str(n),
                                        hopps[i,m,n])
                    # icount+=1
                except:
                    continue

    print("done.",flush=True)

    return lat
