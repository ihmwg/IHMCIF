# Overview

## Goal

We want to be able to deposit hybrid or integrative models into [PDB-dev](https://pdb-dev.rcsb.rutgers.edu/).
These are models that are not necessarily atomic (e.g. parts or all of the
system may be coarse grained) and are derived by integrating information
from multiple sources. Examples include

 - Modeling of the [Nup84 subcomplex](https://salilab.org/nup84)
   of the Nuclear Pore Complex (Sali Lab), by combining comparative models
   with crosslinking and EM class averages, representing subunits as beads
   (1, 10, or 20 residues per bead).
 - ATG1-complex (Hummer Lab): Tetramer of tetramers
   (Atg17-Atg31-Atg29-Atg1-Atg13), 4448 residues. Missing residues and
   loops modeled as flexible linkers (3 rigid domains, 52 linkers).
   EROS refined coarse-grained simulations (COMPLEXES, 1AA =1bead) using
   SAXS data. Ensemble of ~100 dynamic structures.

More examples can be found in the [Google doc](https://docs.google.com/document/d/1tuHzE6N8ENy-8NxeV8CFv9W1BDoJkRoc9VRwoK0Ic5E/edit?usp=sharing).

Existing PDB format is not sufficient since it assumes atomic structures,
and only supports a small number of input experimental data sources (e.g.
X-ray crystallography, NMR).

## mmCIF

We propose extending the existing mmCIF format to store this information
since

 - mmCIF is designed to be extensible
 - PDB is already moving traditional atomic structures to mmCIF format
 - several libraries for handling mmCIF files are already available
 - there is reasonable support from viewers (e.g. [UCSF Chimera](https://www.cgl.ucsf.edu/chimera/))
 - alternative formats for coarse-grained structures
   (e.g. [RMF](https://integrativemodeling.org/rmf/)) don't store all the
   information we're interested in, and aren't widely supported outside
   of UCSF ([IMP](https://integrativemodeling.org/),
   [Chimera](https://www.cgl.ucsf.edu/chimera/))

We plan to support integrative/hybrid models by means of an mmCIF extension
dictionary, [ihm-extension.dic](ihm-extension.dic). Since this merely extends the existing mmCIF
specification, "traditional" data (such as atomic coordinates) can be stored
just as in regular mmCIF files.

A [number of examples](examples/) of using the dictionary are provided.
[One such example](examples/nup84/nup84.cif) contains the structures derived by the Sali lab
for the Nup84 complex, above.

## Deposition

Ultimately, models will be deposited into [PDB-dev](https://pdb-dev.rcsb.rutgers.edu/).
In order for this to work in a semi-automated fashion, integrative/hybrid
modeling packages need to support the mmCIF file format and the IHM extension.
See [the deposition directory](deposition) for the current status of
software support.

## Extension dictionary

*For more details, see the [extension dictionary documentation](dictionary_documentation/documentation.md).*

The extension dictionary aims to cover:

 - Input data (e.g. crosslinks, EM map, EM class average, subunit structures)
   - For example, crosslinks ("residue I in protein A is linked to residue J
     in protein B") directly from the experiment are stored in the
     `_ihm_cross_link_list` mmCIF category.
   - PDB IDs or homology/comparative models are listed in the
     `_ihm_starting_model_details` category and their coordinates in
     `_ihm_starting_model_coord`.
 - Our interpretation of the data (e.g. ambiguity, segmentation)
   - For example, with the crosslink above there may be multiple copies of
     proteins A or B, while residues I or J may not exist or may be
     represented at a lower resolution. The modeling interpretation of these
     crosslinks is described in the `_ihm_cross_link_restraint` category.
   - Our model may correspond to only a subset of the experimental data
     (e.g. an EM map may be of a complex and we're only modeling a subcomplex)
     or vice versa (e.g. we're modeling a complex and we have EM class
     averages for subcomplexes created by domain deletion).
   - Note that we do *not* store raw restraints in the file, since we consider
     these to be implementation details. At least for IMP, the software, and
     our approaches to solve modeling problems, are constantly changing, so
     it would be futile to try to capture every last parameter (particularly
     since ideally models are refined and rebuilt with newer or different
     software as new experimental information becomes available). For
     "perfect" reproduction of the inputs we link to the archive holding
     the raw modeling inputs (Python scripts in IMP's case).
 - Multi-scale models; e.g. parts of the system may be represented atomically
   or with 1 residue beads if input structures are available; other parts may
   represented with 20 residue beads (e.g. disordered regions or regions with
   sequence but no known structure). Parts of the system may be
   represented at multiple such resolutions simultaneously. See the
   `_ihm_model_representation` mmCIF category.
 - Multi-state models; multiple states (e.g. open and closed) may exist
   simultaneously such that some or all of the collected experimental
   information (e.g. crosslinks) reflects more than one state, and cannot
   be satisfied by a single model. The mmCIF file contains all states modeled,
   with links to the sets of experiments consistent with each
   state (if known). See the `_multi_state_modeling` category.
 - Time-ordered models; multiple models may be deposited that represent
   a trajectory, reaction cycle/pathway, or other time-ordered relationship.
   The mmCIF file stores a simple directed graph of these models (as a set
   of edges). See the `_ihm_time_ordered_ensemble` category.
 - Output representation (cluster representatives)
   - Coarse-grained coordinates (spherical or 3D Gaussian beads); see the
     `_ihm_sphere_obj_site` and `_ihm_gaussian_obj_site` categories. The
     format can easily be extended to add other representations.
   - Atomic coordinates can use existing PDB-style fields (atom_site).
   - Non-Cartesian values (e.g. Bayesian parameters or nuisances)
 - Ensemble info (number & size of clusters); see `_ihm_cluster_info`.
 - Other metadata (e.g. publications, software versions used) using standard
   mmCIF categories (e.g. `_citation`, `_citation_author`, `_software`).
 - Basic validation (how well do the models fit the data, are they minima,
   violations of crosslinks etc.)
   - For example, crosslink satisfaction in the final models is stored in
     the `_ihm_cross_link_result` category.

Where possible, we link to existing databases (e.g. EMDB, EMPIAR, PRIDE) rather
than trying to duplicate the data in the mmCIF. For example, an EM map is
simply represented with an EMDB ID. For data not currently available in a
repository, we use a DOI (see the `_ihm_dataset_other` category).
For example, there is currently no repository for
EM class averages (EMDB stores maps; EMPIAR stores micrographs that were used
to generate a map). Those used by the Sali lab in the Nup84 study were uploaded
to GitHub and then archived at zenodo.org, which assigns a permanent DOI,
in this case [10.5281/zenodo.46266](http://dx.doi.org/10.5281/zenodo.46266).
In other cases the data may be available in the supplementary information of
a publication, in which case the publisher-assigned DOI can be used.
