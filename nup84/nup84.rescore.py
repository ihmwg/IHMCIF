"""
  Script to rescore one of the final Nup84 models (from an RMF file).
  Use by copying into the scripts subdirectory of the nup84 GitHub
  repository. It simply does the same setup as the regular
  nup84.isd.modeling.py script, but rather than then doing a sampling
  run, it reads in the RMF file and calculates the score.
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
import tempfile
import shutil

# The RMF file to rescore
input_rmf = '../outputs/3-xray.after_cluster_on_hub.cluster1.top5.pdb.rmf.score/31.0.rmf3'

# The corresponding stat file
stat_file = os.path.join(os.path.dirname(input_rmf), 'stat.filtered.out')
# The RMF file is assumed to be the top-scoring model from the cluster,
# i.e. the first line in the stat file
stat = eval(open(stat_file).readline())
# Get optimized nuisance values for crosslink restraints
optimized_sigma_dss = stat['ISDCrossLinkMS_Sigma_1_DSS']
optimized_sigma_edc = stat['ISDCrossLinkMS_Sigma_1_EDC']


class TempDir(object):
    def __init__(self):
        self.tmpdir = tempfile.mkdtemp()
    def __del__(self):
        shutil.rmtree(self.tmpdir, ignore_errors=True)

def remove_densities(in_file, out_file):
    m = IMP.Model()

    rh = RMF.open_rmf_file_read_only(in_file)
    h = IMP.rmf.create_hierarchies(rh, m)
    for component in h[0].get_children():
        for rep in component.get_children():
            if rep.get_name() == 'Densities':
                IMP.atom.destroy(rep)

    rh = RMF.create_rmf_file(out_file)
    IMP.rmf.add_hierarchies(rh, h)
    IMP.rmf.save_frame(rh)


tmpdir = TempDir()
cleaned_rmf = os.path.join(tmpdir.tmpdir, "clean.rmf")
remove_densities(in_file=input_rmf, out_file=cleaned_rmf)

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

beadsize=20

n84_fastafile  ='../data/protein_fasta.Nup84.txt'
n85_fastafile  ='../data/protein_fasta.Nup85.txt'
n120_fastafile ='../data/protein_fasta.Nup120.txt'
n133_fastafile ='../data/protein_fasta.Nup133.txt'
n145c_fastafile='../data/protein_fasta.Nup145c.txt'
seh1_fastafile ='../data/protein_fasta.Seh1.txt'
sec13_fastafile='../data/protein_fasta.Sec13.txt'

#n84n_pdbfile   ='../data/ScNup84N_7-488.pdb'
#n84c_pdbfile   ='../data/ScNup84C_506-726.pdb'
#n85_pdbfile    ='../data/ScNup85_44-744.pdb'
#n120_pdbfile   ='../data/ScNup120_1-1037.pdb'
#n133n_pdbfile  ='../data/ScNup133N_56-480.pdb'
#n133c_pdbfile  ='../data/ScNup133C_490_1157.pdb'
#n145c_pdbfile  ='../data/ScNup145C_126-553.pdb'
#seh1_pdbfile   ='../data/ScSeh1_1-346.pdb'
#sec13_pdbfile  ='../data/ScSec13_2-296.pdb'

# After removal of disordered regions in PDB files.
n84_pdbfile   ='../data/ScNup84_7-488_506-726_new.pdb'
n85_pdbfile    ='../data/ScNup85_44-744_new.pdb'
n120_pdbfile   ='../data/ScNup120_1-1037_new.pdb'
n133n_pdbfile  ='../data/ScNup133N_56-480_new.pdb'
n133c_pdbfile  ='../data/ScNup133C_490_1157_new.pdb'
n145c_pdbfile  ='../data/ScNup145C_126-553_new.pdb'
seh1_pdbfile   ='../data/ScSeh1_1-346_new.pdb'
sec13_pdbfile  ='../data/ScSec13_2-296_new.pdb'

#-----------------
simo.create_component("Nup84",color=0.0)
simo.add_component_sequence("Nup84", n84_fastafile)

Nup84=simo.autobuild_model("Nup84", n84_pdbfile,"A", resrange=(1,726), resolutions=[1,10], missingbeadsize=beadsize)

simo.show_component_table("Nup84")
simo.setup_component_geometry("Nup84")
#-----------------

simo.create_component("Nup85",color=0.1)
simo.add_component_sequence("Nup85", n85_fastafile)

Nup85_1=simo.autobuild_model("Nup85", n85_pdbfile,"B", resrange=(1,529), resolutions=[1,10], missingbeadsize=beadsize)
Nup85_2=simo.autobuild_model("Nup85", n85_pdbfile,"B", resrange=(530,744), resolutions=[1,10], missingbeadsize=beadsize)

simo.show_component_table("Nup85")
simo.setup_component_geometry("Nup85")

#-----------------
simo.create_component("Nup120",color=0.2)
simo.add_component_sequence("Nup120", n120_fastafile)
Nup120_1=simo.autobuild_model("Nup120", n120_pdbfile,"C", resrange=(1,710), resolutions=[1,10], missingbeadsize=beadsize)
Nup120_2=simo.autobuild_model("Nup120", n120_pdbfile,"C", resrange=(711,1037), resolutions=[1,10], missingbeadsize=beadsize)

simo.show_component_table("Nup120")
simo.setup_component_geometry("Nup120")

#-----------------
simo.create_component("Nup133",color=0.3)
simo.add_component_sequence("Nup133", n133_fastafile)

Nup133_1=simo.autobuild_model("Nup133",n133n_pdbfile,"D", resrange=(1,480),resolutions=[1,10],missingbeadsize=beadsize)
Nup133_2=simo.autobuild_model("Nup133",n133c_pdbfile,"D", resrange=(481,1157),resolutions=[1,10],missingbeadsize=beadsize)

simo.show_component_table("Nup133")
simo.setup_component_geometry("Nup133")
#-----------------

simo.create_component("Nup145c",color=0.4)
simo.add_component_sequence("Nup145c", n145c_fastafile)

Nup145c=simo.autobuild_model("Nup145c",n145c_pdbfile,"E", resrange=(1,712),resolutions=[1,10],missingbeadsize=beadsize)

simo.show_component_table("Nup145c")
simo.setup_component_geometry("Nup145c")

#-----------------
simo.create_component("Seh1",color=0.5)
simo.add_component_sequence("Seh1", seh1_fastafile)
Seh1=simo.autobuild_model("Seh1",seh1_pdbfile,"F", resrange=(1,349),resolutions=[1,10],missingbeadsize=beadsize)

simo.show_component_table("Seh1")
simo.setup_component_geometry("Seh1")
#-----------------
simo.create_component("Sec13",color=0.6)
simo.add_component_sequence("Sec13", sec13_fastafile)
Sec13=simo.autobuild_model("Sec13",sec13_pdbfile,"G", resrange=(1,297),resolutions=[1,10],missingbeadsize=beadsize)

simo.show_component_table("Sec13")
simo.setup_component_geometry("Sec13")

#-----------------

simo.setup_component_sequence_connectivity("Nup84", resolution=1.0, scale=4.0)
simo.setup_component_sequence_connectivity("Nup85", resolution=1.0, scale=4.0)
simo.setup_component_sequence_connectivity("Nup120", resolution=1.0, scale=4.0)
simo.setup_component_sequence_connectivity("Nup133", resolution=1.0, scale=4.0)
simo.setup_component_sequence_connectivity("Nup145c", resolution=1.0, scale=4.0)
simo.setup_component_sequence_connectivity("Seh1", resolution=1.0, scale=4.0)
simo.setup_component_sequence_connectivity("Sec13", resolution=1.0, scale=4.0)

# Read in RMF file from previous modeling run
for c in simo.get_component_names():
    simo.set_coordinates_from_rmf(c, cleaned_rmf, 0)

Nup84_all   = Nup84
Nup85_all   = Nup85_1+Nup85_2
Nup120_all  = Nup120_1+Nup120_2
Nup133_all  = Nup133_1+Nup133_2
Nup145c_all = Nup145c
Seh1_all    = Seh1
Sec13_all   = Sec13

Nup84_complex=Nup84_all+Nup85_all+Nup120_all+Nup133_all+Nup145c_all+Seh1_all+Sec13_all

simo.set_rigid_body_from_hierarchies(Nup84)
simo.set_rigid_body_from_hierarchies(Nup85_1)
simo.set_rigid_body_from_hierarchies(Nup85_2)
simo.set_rigid_body_from_hierarchies(Nup120_1)
simo.set_rigid_body_from_hierarchies(Nup120_2)
simo.set_rigid_body_from_hierarchies(Nup133_1)
simo.set_rigid_body_from_hierarchies(Nup133_2)
simo.set_rigid_body_from_hierarchies(Nup145c)
simo.set_rigid_body_from_hierarchies(Seh1)
simo.set_rigid_body_from_hierarchies(Sec13)

simo.set_super_rigid_body_from_hierarchies(Sec13+Nup85_all+Seh1+Nup145c)
simo.set_super_rigid_body_from_hierarchies(Nup84_all)
simo.set_super_rigid_body_from_hierarchies(Nup85_all)
simo.set_super_rigid_body_from_hierarchies(Nup120_all)
simo.set_super_rigid_body_from_hierarchies(Nup133_all)
simo.set_super_rigid_body_from_hierarchies(Nup145c_all)
simo.set_super_rigid_body_from_hierarchies(Seh1_all)
simo.set_super_rigid_body_from_hierarchies(Sec13_all)

simo.set_super_rigid_body_from_hierarchies(Nup84_complex)

simo.set_floppy_bodies()

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

# Set nuisance values (from stat file)
for key in xl1.sigma_dictionary:
    sigma=xl1.sigma_dictionary[key][0]
    sigma.set_scale(optimized_sigma_dss)

for key in xl2.sigma_dictionary:
    sigma=xl2.sigma_dictionary[key][0]
    sigma.set_scale(optimized_sigma_edc)

# Evaluate the score
print(IMP.pmi.tools.get_restraint_set(m).evaluate(False))
