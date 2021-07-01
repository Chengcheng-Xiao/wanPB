# wanPB

Converting [Wannier90's](http://www.wannier.org) Hamiltonian to [pybinding](https://docs.pybinding.site/en/stable/) compatible format.

## Prerequisites:
- python3.6+
- pybinding
- numpy

## Usage

Input files:

- `seedname_centres.xyz`
- `seedname_tb.dat`

Command-line interface:
```
w90_pb --seedname "wannier90"
```

Output file:

- `seedname.pbz` (check out [this](https://docs.pybinding.site/en/stable/api.html#results) page of how to read this file.)
