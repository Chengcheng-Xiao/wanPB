set style data dots
set nokey
set xrange [0: 2.25337]
set yrange [ -9.55801 :  1.05019]
set arrow from  0.88417,  -9.55801 to  0.88417,   1.05019 nohead
set arrow from  1.66393,  -9.55801 to  1.66393,   1.05019 nohead
set xtics ("G"  0.00000,"Y"  0.88417,"M"  1.66393,"G"  2.25337)
 plot "wannier90_band.dat"
