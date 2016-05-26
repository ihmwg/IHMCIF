import IMP.pmi.representation
import IMP.pmi.tools
from IMP.pmi.tools import OrderedDict
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
        elif isinstance(obj, float):
            return "%.3f" % obj
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

class StartingModelCoordDumper(Dumper):
    def __init__(self, simo):
        super(StartingModelCoordDumper, self).__init__(simo)
        self.model_hier = OrderedDict()

    def add_model(self, name, hier):
        self.model_hier[name] = hier

    def dump(self, writer):
        ordinal = 1
        with writer.loop("_ihm_starting_model_coord",
                     ["starting_model_id", "group_PDB", "id", "type_symbol",
                      "atom_id", "comp_id", "entity_id", "seq_id", "Cartn_x",
                      "Cartn_y", "Cartn_z", "B_iso_or_equiv",
                      "ordinal_id"]) as l:
            for model_name, hier in self.model_hier.items():
                for a in IMP.atom.get_leaves(hier):
                    coord = IMP.core.XYZ(a).get_coordinates()
                    atom = IMP.atom.Atom(a)
                    element = atom.get_element()
                    element = IMP.atom.get_element_table().get_name(element)
                    atom_name = atom.get_atom_type().get_string()
                    group_pdb = 'ATOM'
                    if atom_name.startswith('HET:'):
                        group_pdb = 'HETATM'
                        del atom_name[:4]
                    res = IMP.atom.get_residue(atom)
                    res_name = res.get_residue_type().get_string()
                    chain = IMP.atom.get_chain(res)
                    l.write(starting_model_id=model_name, group_PDB=group_pdb,
                            id=atom.get_input_index(), type_symbol=element,
                            atom_id=atom_name, comp_id=res_name,
                            entity_id=self.simo._entity_id[model_name],
                            seq_id=res.get_index(), Cartn_x=coord[0],
                            Cartn_y=coord[1], Cartn_z=coord[2],
                            B_iso_or_equiv=atom.get_temperature_factor(),
                            ordinal_id=ordinal)
                    ordinal += 1


class Representation(IMP.pmi.representation.Representation):
    def __init__(self, m, fh, *args, **kwargs):
        self._cif_writer = CifWriter(fh)
        self._entity_id = {}
        self.starting_model_coord_dump = StartingModelCoordDumper(self)
        super(Representation, self).__init__(m, *args, **kwargs)

    def create_component(self, name, *args, **kwargs):
        self._entity_id[name] = len(self._entity_id) + 1
        super(Representation, self).create_component(name, *args, **kwargs)

    def flush(self):
        for dumper in SoftwareDumper, EntityDumper:
            dumper(self).dump(self._cif_writer)
        for dumper in (self.starting_model_coord_dump,):
            dumper.dump(self._cif_writer)

    def add_component_pdb(self, name, pdbname, chain, resolutions,
                          resrange=None, *args, **kwargs):
        sel = IMP.atom.NonWaterNonHydrogenPDBSelector() & IMP.atom.ChainPDBSelector(chain)
        ph = IMP.atom.read_pdb(pdbname, self.m, sel)
        self.starting_model_coord_dump.add_model(name, ph)
        return super(Representation, self).add_component_pdb(name, pdbname,
                                     chain, resolutions, resrange=resrange,
                                     *args, **kwargs)
