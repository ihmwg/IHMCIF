"""
  Script to rescore one of the final Nup84 models (from an RMF file).
  Use by copying into the scripts subdirectory of the nup84 GitHub
  repository. It simply does the same setup as the regular
  nup84.isd.modeling.py script, but rather than then doing a sampling
  run, it reads in the RMF file and calculates the score.

  Note that this is a work in progress - in particular, the output score
  seems way too large for a relaxed model. Ben to investigate.
"""

from __future__ import print_function
import IMP
import IMP.core
import IMP.algebra
import IMP.atom
import IMP.container
import RMF
import IMP.rmf

import IMP.pmi.restraints.crosslinking
import IMP.pmi.restraints.stereochemistry
import IMP.pmi.restraints.em
import IMP.pmi.restraints.em2d
import IMP.pmi.restraints.basic
import IMP.pmi.restraints.proteomics
import IMP.pmi.representation
import IMP.pmi.tools
import IMP.pmi.samplers
import IMP.pmi.output
import IMP.pmi.macros

import os
import sys

rbmaxtrans = 2.00
fbmaxtrans = 2.00
rbmaxrot=0.04
nrmffiles=1000
nframes=100
nsteps=100
outputobjects = []
sampleobjects = []

m = IMP.Model()
simo = IMP.pmi.representation.Representation(m,upperharmonic=True,disorderedlength=False)

exec(open("nup84.topology.py").read())

simo.set_rigid_bodies_max_rot(rbmaxrot)
simo.set_floppy_bodies_max_trans(fbmaxtrans)
simo.set_rigid_bodies_max_trans(rbmaxtrans)
simo.set_floppy_bodies()
simo.setup_bonds()

prot = simo.prot
outputobjects.append(simo)
sampleobjects.append(simo)


ev = IMP.pmi.restraints.stereochemistry.ExcludedVolumeSphere(simo,resolution=10)
ev.add_to_model()
outputobjects.append(ev)

eb = IMP.pmi.restraints.basic.ExternalBarrier(simo,radius=300)
eb.add_to_model()
outputobjects.append(eb)

columnmap={}
columnmap["Protein1"]=0
columnmap["Protein2"]=2
columnmap["Residue1"]=1
columnmap["Residue2"]=3
columnmap["IDScore"]=4
columnmap["XLUniqueID"]=5

ids_map=IMP.pmi.tools.map()
ids_map.set_map_element(1.0,1.0)

xl1 = IMP.pmi.restraints.crosslinking.ISDCrossLinkMS(simo,
                                   '../data/yeast_Nup84_DSS.new.dat',
                                   length=21.0,
                                   slope=0.01,
                                   columnmapping=columnmap,
                                   ids_map=ids_map,resolution=1.0,
                                   filelabel="DSS",
                                   label="DSS")
xl1.add_to_model()
sampleobjects.append(xl1)
outputobjects.append(xl1)
xl1.set_psi_is_sampled(False)
psi=xl1.get_psi(1.0)[0]
psi.set_scale(0.05)


xl2 = IMP.pmi.restraints.crosslinking.ISDCrossLinkMS(simo,
                                   '../data/EDC_XL_122013.new.dat',
                                   length=16.0,
                                   slope=0.01,
                                   columnmapping=columnmap,
                                   ids_map=ids_map,resolution=1.0,
                                   filelabel="EDC",
                                   label="EDC")
xl2.add_to_model()
sampleobjects.append(xl2)
outputobjects.append(xl2)
xl2.set_psi_is_sampled(False)
psi=xl2.get_psi(1.0)[0]
psi.set_scale(0.05)

# 2DEM restraints
images = ['../data/nup84_kinked_from_class2.pgm']

em2d = IMP.pmi.restraints.em2d.ElectronMicroscopy2D(simo,
                                                    images,
                                                    resolution=1.0,
                                                    pixel_size = 5.91,
                                                    image_resolution = 30.0,
                                                    projection_number = 400)
em2d.add_to_model()
em2d.set_weight(500)
outputobjects.append(em2d)

# Read in RMF file (use ../outputs/remove-densities.py script to generate
# a compatible RMF)
rh = RMF.open_rmf_file_read_only('../outputs/3-xray.after_cluster_on_hub.cluster1.top5.pdb.rmf.score/out.rmf3')
IMP.rmf.link_hierarchies(rh, [simo.prot])
IMP.rmf.load_frame(rh, RMF.FrameID(0))

# Set nuisance values (from stat file)
for key in xl1.sigma_dictionary:
    sigma=xl1.sigma_dictionary[key][0]
    sigma.set_scale(10.0020377979)

for key in xl2.sigma_dictionary:
    sigma=xl2.sigma_dictionary[key][0]
    sigma.set_scale(7.15769480855)

# Evaluate the score (note: does not seem right)
print(IMP.pmi.tools.get_restraint_set(m).evaluate(False))
