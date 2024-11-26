
# Overview

The [IHMCIF dictionary](dist/mmcif_ihm.dic) provides the data representation required for archiving 
integrative/hybrid structural models in [PDB-IHM](https://pdb-ihm.org).

This dictionary is an extension of the [PDBx/mmCIF](http://mmcif.wwpdb.org) dictionary
and provides the additional defintions required to handle integrative / hybrid models.  

The IHMCIF dictionary provides a mechanism to capture the following information regarding
integrative / hybrid models: 

  - Defintions of multi-scale, multi-state, ordered, ensembles

  - Definition of models with heterogenous composition

  - Descriptions of the starting structural models of individual molecular components obtained 
    from experimental and computational techniques such as
      - X-ray diffraction
      - NMR spectroscopy 
      - Electron microscopy
      - Computational models
      - Intergrative models

  - Definitions of the spatial restraints derived from a variety of experimental data such as
      - 2D and 3D electron microscopy (2DEM and 3DEM)
      - Chemical crosslinking mass spectrometry (CX-MS)
      - Small angle scattering (SAS)
      - Forster resonance energy transfer (FRET)
      - Electron paramagnetic resonance spectroscopy (EPR)
      - Hydrogen-deuterium exchange mass spectrometry (HDX-MS)
      - Atomic force microscopy (AFM)
      - Distrance restraints from coevolution data
      - Generic distance restraints obtained from biophysical and proteomics methods

  - Referencing associated data from external resources

  - Definitions of the ambiguities/uncertainties associated with the experimental data and
    preliminary validation metrics. 

  - Description of the modeling workflow

The IHMCIF dictionary currently has over 30 new data categories and 300 new data items.

*For more details regarding the dictionary, see the 
[IHMCIF dictionary documentation](dictionary_documentation/documentation.md) 
and the [mmCIF resources website](https://mmcif.wwpdb.org/dictionaries/mmcif_ihm.dic/Index/).*

Cite the IHMCIF dictionary:  
*Vallat B, Webb BM, Westbrook JD, Goddard TD, Hanke CA, Graziadei A, Peisach E, Zalevsky A, Sagendorf J, 
Tangmunarunkit H, Voinea S, Sekharan M, Yu J, Bonvin AAMJJ, DiMaio F, Hummer G, Meiler J, Tajkhorshid E, 
Ferrin TE, Lawson CL, Leitner A, Rappsilber J, Seidel CAM, Jeffries CM, Burley SK, Hoch JC, Kurisu G, 
Morris K, Patwardhan A, Velankar S, Schwede T, Trewhella J, Kesselman C, Berman HM, Sali A. 
IHMCIF: An Extension of the PDBx/mmCIF Data Standard for Integrative Structure Determination Methods. 
J Mol Biol. 2024, 168546. doi: [10.1016/j.jmb.2024.168546](https://doi.org/10.1016/j.jmb.2024.168546).*

*For tips on structuring integrative modeling studies to be amenable to
deposition, see [this page](dictionary_documentation/modeling-tips.md).*

Browse the [wiki page](https://github.com/ihmwg/IHMCIF/wiki) for archived information regarding
[weekly meetings](https://github.com/ihmwg/IHMCIF/wiki/Meetings) and descriptions of 
[integrative modeling examples](https://github.com/ihmwg/IHMCIF/wiki/Use-cases).

# Organization of the repository

[README.md](README.md) - this file

[IHMCIF extension](dist/mmcif_ihm_ext.dic) - IHM dictionary extension

[IHMCIF complete](dist/mmcif_ihm.dic) - IHM dictionary extension merged with the parent PDBx/mmCIF dictionary

[dictionary_documentation](dictionary_documentation) - directory with detailed documentation 
regarding the data categories defined in the [IHMCIF dictionary](dist/mmcif_ihm.dic) along with examples.  

[examples](examples) - directory with examples of integrative models compliant with the IHM dictionary

[deposition](deposition) - directory tracks support for generating IHM dictionary compliant data files by 
modeling software such as [IMP](https://integrativemodeling.org). 

## Discussion

 - Discussion on the file formats is conducted via email - please subscribe to
   [the mailing list](https://salilab.org/mailman/listinfo/ihm-repval).

 - To get an email every time this GitHub repository is updated, please
   subscribe to the [IHM-mmCIF-commits mailing list](https://salilab.org/mailman/listinfo/ihm-mmcif-commits).

## Deposition of models to [PDB-IHM](https://pdb-ihm.org)

Models can be deposited to [PDB-IHM](https://pdb-ihm.org) in a semi-automated fashion, 
via the [deposition and data harvesting system](https://data.pdb-ihm.org).
The system accepts mmCIF files compliant with the [PDBx/mmCIF](https://mmcif.wwpdb.org/) 
and [IHMCIF](dist/mmcif_ihm.dic) dictionaries. Compliant files can be generated using 
the [python-ihm](https://github.com/ihmwg/python-ihm) software library. 
Modeling software such as [IMP](https://github.com/salilab/imp) have interal support for IHMCIF. 
See [the deposition directory](deposition) for more information.

## Visualization of integrative models

There is currently basic support for visualization of IHM mmCIF models
in daily builds of [UCSF ChimeraX](https://www.cgl.ucsf.edu/chimerax/) 
and in [Molstar](https://molstar.org/).
