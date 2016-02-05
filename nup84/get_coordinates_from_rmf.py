#!/usr/bin/python

from __future__ import print_function
import sys
import IMP.rmf
import RMF

def add_center(h, geometric_center):
    """Add the contribution from a hierarchy to the geometric center.
       For compatibility with PMI's PDB output, only use the 1 residue
       per bead representation in this calculation."""
    name = h.get_name()
    if name == 'Densities' or name.endswith('Res:10'):
        return 0
    num_leaves = 0
    for child in h.get_children():
        num_leaves += add_center(child, geometric_center)
    if IMP.core.XYZ.get_is_setup(h):
        geometric_center += IMP.core.XYZ(h).get_coordinates()
        num_leaves += 1
    return num_leaves

def get_geometric_center(h):
    """Find the geometric center of the given hierarchy."""
    geometric_center = IMP.algebra.Vector3D(0,0,0)
    num_leaves = add_center(h, geometric_center)
    return geometric_center / num_leaves

def print_func(out, indent):
    print(" " * indent + out)

def print_fragment(c, center, indent):
    """Display an IMP.atom.Fragment (typically a PMI bead)"""
    frag = IMP.atom.Fragment(c)
    resind = frag.get_residue_indexes()
    sphere = IMP.core.XYZR(c)
    coord = sphere.get_coordinates() - center
    print_func("Residues %d through %d, mass %.2f, coord %.3f %.3f %.3f radius %.3f" % (resind[0], resind[-1], IMP.atom.Mass(c).get_mass(), coord[0], coord[1], coord[2], sphere.get_radius()), indent)

def print_residue(c, center, indent):
    """Display an IMP.atom.Residue"""
    res = IMP.atom.Residue(c)
    sphere = IMP.core.XYZR(c)
    coord = sphere.get_coordinates() - center
    print_func("Residue %d name %s mass %.2f, coord %.3f %.3f %.3f radius %.3f" % (res.get_index(), res.get_residue_type(), IMP.atom.Mass(c).get_mass(), coord[0], coord[1], coord[2], sphere.get_radius()), indent)

def print_component(c, center, indent=0):
    name = c.get_name()
    if name == 'Densities':
        return
    if IMP.atom.Fragment.get_is_setup(c):
        print_fragment(c, center, indent)
    elif IMP.atom.Residue.get_is_setup(c):
        print_residue(c, center, indent)
    elif not name.endswith('_pdb'):
        desc = name
        if name.endswith('_Res:1'):
            desc += " (1 residue per bead representation)"
        elif name.endswith('_Res:10'):
            desc += " (10 residues per bead representation)"
        print_func(desc, indent)
    for child in c.get_children():
        print_component(child, center, indent + 2)

if len(sys.argv) != 2:
    print("Usage: %s rmf_file" % sys.argv[0], file=sys.stderr)
    sys.exit(1)

m = IMP.Model()
f = RMF.open_rmf_file_read_only(sys.argv[1])
h = IMP.rmf.create_hierarchies(f, m)
# Update rigid body coordinates
m.update()

# Find geometric center (so we can center everything at the origin; for
# compatibility with PMI's PDB output).
center = get_geometric_center(h[0])

for subunit in h[0].get_children():
    print_component(subunit, center)
