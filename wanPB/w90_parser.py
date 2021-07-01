import numpy as np
import os

def read_tb(Filename="wannier90_tb.dat"):
    '''
    Parser for Seedname_tb.dat file.
    '''
    if os.path.exists(Filename) == False:
        print(f"ERROR: {Filename} not found." )
        exit()

    print(f"Reading: {Filename}... \t\t", end='', flush=True)
    # read in all data
    with open(Filename, 'r') as f:
        data = f.readlines()

    # lattice vectors
    lat_vec = np.array([data[1].strip().split(),
                        data[2].strip().split(),
                        data[3].strip().split()], dtype=float)

    # basic data
    num_wann = int(data[4])
    num_kpts = int(data[5])

    # get degeneracy data
    nrpt_lines = int(np.ceil(num_kpts / 15.0))
    istart = 6 + nrpt_lines
    deg=[]
    for i in range(6,istart):
        deg.append(np.array([int(j) for j in data[i].split()]))
    deg=np.concatenate(deg,0)

    # get hoppings
    # some initialization
    icount=0
    Rlatt = []
    hopps = []
    r_hop= np.zeros([num_wann,num_wann], dtype=complex)

    for i in range(istart,istart+(num_wann**2+2)*num_kpts):
        line=data[i].split()
        if len(line) > 3:
            # Let's use 0 based index
            m = int(line[0]) - 1
            n = int(line[1]) - 1
            r_hop[m,n] = complex(round(float(line[2]),6),round(float(line[3]),6))
        else:
            R = np.array([float(x) for x in line[0:3]])
        icount+=1
        if(icount % (num_wann**2 + 2) == 0):
            Rlatt.append(R)
            hopps.append(r_hop)
            # reinitialize r_hop
            r_hop= np.zeros([num_wann,num_wann], dtype=complex)

    Rlatt=np.asarray(Rlatt, dtype=int)
    hopps=np.asarray(hopps)
    deg = np.reshape(deg,[num_kpts,1,1])
    hopps=hopps/deg

    print("done.",flush=True)

    return lat_vec, Rlatt, hopps, deg, num_wann, num_kpts

# lat_vec, Rlatt, hopps, deg, num_wann, num_kpts = read_tb(Filename='wannier90_tb.dat')

def read_center(Filename="wannier90_centres.xyz"):
    '''
    Parser for seedname_centers.xyz
    '''
    if os.path.exists(Filename) == False:
        print(f"ERROR: {Filename} not found." )
        exit()

    print(f"Reading: {Filename}... \t", end='', flush=True)

    with open("wannier90_centres.xyz", 'r') as f:
        data = f.readlines()

    wan_centers = []
    for i in range(2,len(data)):
        if data[i].split()[0] == 'X':
            wan_centers.append(data[i].split()[1:])

    wan_centers = np.asarray(wan_centers,dtype=float)

    print("done.",flush=True)
    return wan_centers
