import numpy as np
import pybinding as pb
pb.pltutils.use_style()
import matplotlib.pyplot as plt

# read-in lattice
lat = pb.load("wannier90.pbz")

# construct model
model = pb.Model(lat, pb.translational_symmetry())

# use lapack solver
solver = pb.solver.lapack(model)

# get me recripocal vectors
rvec = np.array(lat.reciprocal_vectors())

# construct high symmetry points.
Gamma   = np.sum([0,0,0]*rvec,axis=0)
K1      = np.sum([0,0.5,0]*rvec,axis=0)
M       = np.sum([1/3.,1/3.,0]*rvec,axis=0)

# calculate bands
bands = solver.calc_bands(Gamma, K1, M, Gamma,  step=0.01)
bands.plot(point_labels=[r'$\Gamma$', 'K', 'M', r'$\Gamma$'])

# plot bands
plt.savefig("InSe_band.png",dpi=500)
