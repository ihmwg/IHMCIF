IMP support for mmCIF categories
================================

IMP currently outputs models in its own format (RMF) but should be able to
natively support at least part of the mmCIF IHM dictionary. For each category
in this dictionary, IMP support is listed as "automatic", i.e. with some work
at our end, IMP should be able to fully populate this category; "manual", i.e.
this category would need to be filled in manually, at least for the near future;
or "partial", i.e. some data items can be filled in by IMP but others would
need to be manually supplied.


`IHM_STARTING_MODEL_DETAILS`: partial. IMP doesn't know or care where its
input structures originate. But we may be able to parse PDB headers to
populate some of these data items (e.g. Modeller-generated models have a
Modeller-specific EXPDTA PDB header).

`IHM_MODEL_REPRESENTATION`: automatic. IMP knows the model representation.

`IHM_STRUCT_ASSEMBLY`: automatic. IMP knows the model representation.

`IHM_MODELING_EXPERIMENT`: automatic. All modeling from one Python script
can be captured. This assumes some organization at our end (i.e. not splitting
the protocol into a handful of one-off scripts).

`IHM_MULTI_STATE_MODELING`: partial. IMP knows the number of states modeled
but doesn't care what they are - this would need to be supplied by the user.

`IHM_TIME_ORDERED_ENSEMBLE`: partial. Would need to be handled as for
`IHM_MULTI_STATE_MODELING`.

`IHM_MODELING_POST_PROCESS`: partial. Filtering can certainly be supported;
clustering information would need to be filled in by hand for the Nup84 at
least (although recent PMI has much better analysis support and may be able
to handle this automatically in future).

`IHM_ENSEMBLE_INFO`: partial. As for `IHM_MODELING_POST_PROCESS`.

`IHM_MODEL_LIST`: manual. Deciding how many models to deposit probably can't
be automated.

`IHM_DATASET_LIST`: partial. IMP knows the input datasets, but the user
would probably need to supply any DOIs or other references.

`IHM_DATASET_RELATED_DB_REFERENCE`, `IHM_DATASET_OTHER`: manual. See
`IHM_DATASET_LIST`.

`IHM_CROSS_LINK_LIST`: automatic. IMP can generate this directly from the
crosslink files it takes as input.

`IHM_CROSS_LINK_RESTRAINT`: automatic. This information can be extracted
from IMP stat files.

`IHM_CROSS_LINK_RESULT`: manual. As above, we should be able to automate this
in future with improvements to our clustering protocols.

`IHM_2DEM_CLASS_AVERAGE_RESTRAINT`: automatic. This can be extracted from the
IMP restraint and input image.

`IHM_2DEM_CLASS_AVERAGE_FITTING`: automatic. Rescoring the model is necessary
to extract the transformation, but this can be scripted.

`IHM_3DEM_RESTRAINT`: automatic. All information can be extracted from the
IMP restraint.

`IHM_STARTING_MODEL_COORD`: automatic. IMP knows the starting coordinates.

`IHM_SPHERE_OBJ_SITE`: automatic. This can be extracted from existing RMF files.

`IHM_GAUSSIAN_OBJ_SITE`: automatic. Stored in RMF files.

`IHM_GAUSSIAN_OBJ_ENSEMBLE`: manual. Localization densities would currently
have to be manually supplied. Future clustering improvements would automate
this.


