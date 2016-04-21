This provides initial support for IMP/PMI to output files in mmCIF format.

To use, link this directory to `lib/IMP/pmi/mmcif_output/` under your
IMP build directory.

Next, in your PMI script, replace the `IMP.pmi.representation.Representation`
object with `IMP.pmi.mmcif_output.Representation`. This behaves like
the regular `Representation` object except that it takes a `fh` argument
(which should an mmCIF file open in write mode) and provides a `flush` method
which dumps the current state of the system to that file. 
