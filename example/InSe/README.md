# InSe

1. Wannierzation:
```
wannier90.x wannier90
```

2. Converting Hamiltonian to pybinding compatible format:
```
wanpb.x --seedname "wannier90"
```

3. Plot bands calculated by Wannier90:
```
gnuplot -presist wannier90_band.gnu
```

4. Plot bands calculated by pybinding (saved as `InSe_band.png`):
```
plot_band.py
```
