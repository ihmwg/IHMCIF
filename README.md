
# Overview

The [IHM dictionary](ihm-extension.dic) provides the data representation required for archiving 
integrative/hybrid structural models in [PDB-dev](https://pdb-dev.wwpdb.org).

This dictionary is an extension of the [PDBx/mmCIF](http://mmcif.wwpdb.org) dictionary
and provides the additional defintions required to handle integrative / hybrid models.  

The IHM dictionary provides a mechanism to capture the following information regarding
integrative / hybrid models: 

  - Defintions of multi-scale, multi-state, and ordered ensembles

  - Descriptions of the starting structural models of individual molecular components obtained 
    from experimental and computational techniques such as
      - X-ray diffraction
      - NMR spectroscopy 
      - Computational models

  - Definitions of the spatial restraints derived from a variety of experimental data such as
      - 2D and 3D electron microscopy
      - Chemical crosslinking mass spectrometry 
      - Small angle scattering
      - Generic distance restraints obtained from biophysical and proteomics methods

  - Referencing associated data from external resources

  - Definitions of the ambiguities/uncertainties associated with the experimental data and
    preliminary validation metrics. 

  - Description of the modeling workflow

The I/H methods dictionary currently has over 30 new data categories and 300 new data items.

*For more details regarding the dictionary, see the 
[extension dictionary documentation](dictionary_documentation/documentation.md).*

*For tips on structuring integrative modeling studies to be amenable to
deposition, see [this page](dictionary_documentation/modeling-tips.md).

Browse the [wiki page](https://github.com/ihmwg/IHM-dictionary/wiki) for information regarding
[weekly meetings](https://github.com/ihmwg/IHM-dictionary/wiki/Meetings) and descriptions of 
[integrative modeling examples](https://github.com/ihmwg/IHM-dictionary/wiki/Use-cases).

# Organization of the repository

[README.md](README.md) - this file

[ihm-extension.dic](ihm-extension.dic) - IHM dictionary extension

[dictionary_documentation](dictionary_documentation) - directory with detailed documentation 
regarding the data categories defined in the [IHM dictionary](ihm-extension.dic) along with examples.  

mmcif_ihm_v0.xxx.sdb - The serialized dictionary for use with the 
[RCSB mmCIF dictionary suite](https://sw-tools.rcsb.org/apps/MMCIF-DICT-SUITE/index.html). 
This tool can be used to check whether a data file is compliant with the latest dictionary. 

[examples](examples) - directory with examples of integrative models compliant with the IHM dictionary

[deposition](deposition) - directory tracks support for generating IHM dictionary compliant data files by 
modeling software such as [IMP](https://integrativemodeling.org). 

## Discussion

 - Discussion on the file formats is conducted via email - please subscribe to
   [the mailing list](https://salilab.org/mailman/listinfo/ihm-repval).

 - We also [meet weekly via Skype](https://github.com/ihmwg/IHM-dictionary/wiki/Meetings) to discuss issues. All are
   welcome to join some or all meetings.

 - To get an email every time this GitHub repository is updated, please
   subscribe to the [IHM-mmCIF-commits mailing list](https://salilab.org/mailman/listinfo/ihm-mmcif-commits).

## Deposition of models to [PDB-dev](https://pdb-dev.wwpdb.org)

In order to deposit models to [PDB-dev](https://pdb-dev.wwpdb.org) in a semi-automated fashion, 
integrative/hybrid modeling packages need to support the mmCIF file format and the IHM extension.
See [the deposition directory](deposition) for the current status of software support.

## Visualization of integrative models

There is currently basic support for visualization of IHM mmCIF models
in daily builds of [UCSF ChimeraX](https://www.cgl.ucsf.edu/chimerax/).
