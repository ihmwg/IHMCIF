IMP includes provisional support to automatically generate mmCIF files
that encapsulate a modeling protocol when using PMI.

To use, replace the `modules/pmi` directory in your IMP checkout with the
current head of the `mmcif` branch of the
[PMI repository](https://github.com/salilab/pmi), e.g.

    cd imp/modules
    rm -rf pmi
    git clone -b mmcif https://github.com/salilab/pmi.git

then build IMP from source as per usual.

Next, in your PMI script, replace the `IMP.pmi.representation.Representation`
object with `IMP.pmi.mmcif.Representation`. This behaves like
the regular `Representation` object except that it takes a `fh` argument
(which should be an mmCIF file open in write mode) and provides a `flush` method
which dumps the current state of the system to that file.

