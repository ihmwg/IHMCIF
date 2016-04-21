import IMP.pmi.representation
import IMP.pmi.tools
import sys
import os
import operator

class _LineWriter(object):
    def __init__(self, writer, line_len=80):
        self.writer = writer
        self.line_len = line_len
        self.column = 0
    def write(self, val):
        val = self.writer._repr(val)
        if self.column > 0:
            if self.column + len(val) + 1 > self.line_len:
                self.writer.fh.write("\n")
                self.column = 0
            else:
                self.writer.fh.write(" ")
                self.column += 1
        self.writer.fh.write(val)
        self.column += len(val)


class CifCategoryWriter(object):
    def __init__(self, writer, category):
        self.writer = writer
        self.category = category
    def write(self, **kwargs):
        self.writer._write(self.category, kwargs)
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        pass


class CifLoopWriter(object):
    def __init__(self, writer, category, keys):
        self.writer = writer
        self.category = category
        self.keys = keys
    def write(self, **kwargs):
        l = _LineWriter(self.writer)
        for k in self.keys:
            l.write(kwargs.get(k, self.writer.omitted))
        self.writer.fh.write("\n")
    def __enter__(self):
        f = self.writer.fh
        f.write("#\nloop_\n")
        for k in self.keys:
            f.write("%s.%s\n" % (self.category, k))
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        self.writer.fh.write("#\n")


class CifWriter(object):
    omitted = '.'
    unknown = '?'

    def __init__(self, fh):
        self.fh = fh
    def category(self, category):
        return CifCategoryWriter(self, category)
    def loop(self, category, keys):
        return CifLoopWriter(self, category, keys)
    def _write(self, category, kwargs):
        for key in kwargs:
            self.fh.write("%s.%s %s\n" % (category, key,
                                          self._repr(kwargs[key])))
    def _repr(self, obj):
        if isinstance(obj, str) and '"' not in obj \
           and "'" not in obj and " " not in obj:
            return obj
        else:
            return repr(obj)


class Dumper(object):
    """Base class for helpers to dump output to mmCIF"""
    def __init__(self, simo):
        self.simo = simo


class SoftwareDumper(Dumper):
    def dump(self, writer):
        with writer.loop("_software",
                         ["pdbx_ordinal", "name", "classification", "version",
                          "type", "location"]) as l:
            l.write(pdbx_ordinal=1, name="Integrative Modeling Platform (IMP)",
                    version=IMP.__version__, type="program",
                    classification="integrative model building",
                    location='https://integrativemodeling.org')
            l.write(pdbx_ordinal=2, name="IMP PMI module",
                    version=IMP.pmi.__version__, type="program",
                    classification="integrative model building",
                    location='https://integrativemodeling.org')


class EntityDumper(Dumper):
    def dump(self, writer):
        all_entities = [x for x in sorted(self.simo._entity_id.items(),
                                          key=operator.itemgetter(1))]
        with writer.loop("_entity",
                         ["id", "type", "src_method", "pdbx_description",
                          "formula_weight", "pdbx_number_of_molecules",
                          "details"]) as l:
            for name, entity_id in all_entities:
                l.write(id=entity_id, type='polymer', src_method='man',
                        pdbx_description=name, formula_weight=writer.unknown,
                        pdbx_number_of_molecules=1, details=writer.unknown)


class Representation(IMP.pmi.representation.Representation):
    def __init__(self, m, fh, *args, **kwargs):
        self._cif_writer = CifWriter(fh)
        self._entity_id = {}
        super(Representation, self).__init__(m, *args, **kwargs)

    def create_component(self, name, *args, **kwargs):
        self._entity_id[name] = len(self._entity_id) + 1
        super(Representation, self).create_component(name, *args, **kwargs)

    def flush(self):
        for dumper in SoftwareDumper, EntityDumper:
            dumper(self).dump(self._cif_writer)
