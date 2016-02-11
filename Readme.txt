File: nup-strawman/Readme.txt
Date: 21-Sep-2014  

Readme.txt               This file

nup84-strawman-1.cif     Example PDBx data file based on data from your GitHub
                         site nup84-master/data/*   (PDB templates *_new.pdb).

imp-extension.dic        PDBx/mmCIF extension dictionary for the NUP IMP project


Summary

The example file contains a draft of how a "future" hybrid-capable PDB might
represent an IMP structure model. 

The information describing accession, title, authorship citation, software,
molecular description (e.g. polymer sequence details) are populated using
the existing PDBx/mmCIF data categories.

New data categories have been created to describe template selection,
model representation/architecture, cross-linking restraints, template
model coordinates, pseudo atom positions, 2DEM and 3DEM restraints, 
clustering information, modeling experiment details, structural 
assemblies, experimental datasets used.  

The template and model representation should reflect the details in the
table Supplemental Figure S3. The fasta sequences, cross-linking, and
template coordinate data from your repository have been incorporated.
Only the template model coordinates identified as *_new.pdb were used
in the example as I assume that others where not simultaneously used
by the modeling tasks. 

A new separate category is provided for the 'bead' coordinates.
Each bead position includes a back reference to its sequence seqment
modeling details.   In this draft I have included a residue range
and radius with each coordinate position.  If the bead represents a
single residue then beginning and ending residues are the same.
If the bead represents a larger piece of sequence then this is indicated.
I have not yet been able to produce a real coordinate output for the bead
model so I assume that bead radius is variable.  There may be other details
that you would like to include for each bead object and these could be
easily added.  

In the example I inserted a dummy set of pseudo positions for a single
copy of each polymer as an illustration (coordinates and radii all = 1.0).

This version does not include a representations of the mapping of images
of EM class averages as I did not completely appreciate detais of
covariance data in these data files.  I could  these with a bit of
tutorial on this subject.  

Similarly this version does not include any description validation
results/constraint violations. If there are some critical data quality
diagnostics that you feel should be included then these could be 
added to the dictionary as well.  
