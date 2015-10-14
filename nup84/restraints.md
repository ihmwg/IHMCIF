Restraints used in the Nup84 modeling
=====================================

All IMP restraints are C++ or Python subclasses of the Restraint base class.
All Restraints have a user-defined name.

RestraintSet class: a pseudo-restraint that acts as a container of other
Restraints.

Each Nup84 component has a RestraintSet called "sortedsegments". This contains
a set of PairRestraints, each of which connects one of the low resolution beads
to the next bead (by sequence).

PairRestraint class: inputs: particle 1, particle 2, and a PairScore to score
the interaction. In the Nup84 case we use a PairScore subclass called
SphereDistancePairScore which scores the distance between the surfaces of the
two beads. (Another commonly used class is DistancePairScore which scores the
distance between the centers.)

SphereDistancePairScore class: inputs: a UnaryFunction that converts the
distance into a score. For Nup84 we use Harmonic or HarmonicUpperBound, both
of which take as inputs a mean distance and a force constant.

Each Nup84 component also has a RestraintSet called "unmodeledregions". This is
currently empty, since we model everything at some resolution.

The next restraint is excluded volume, which is a PairsRestraint.

PairsRestraint class: inputs: a set of pairs of particles to act on
(in IMP we store these in a Container class) and the PairScore to apply to each
pair. For Nup84 we use a ClosePairContainer and a
HarmonicUpperBound(SphereDistancePairScore).

ClosePairContainer class: contains all pairs of particles that are nearby in
space (i.e. a nonbonded list). inputs: distance cutoff, slack (controls how
frequently the list is rebuilt during the simulation), a ClosePairFinder to
populate the list, and a Container of all particles to operate on. For Nup84,
we use a RigidClosePairsFinder which handles rigid bodies, and a Container
that is a simple list of all 10-residue-per-bead particles.

Nup84 "barrier" restraint: a SingletonsRestraint that applies a function to
each particle. Performs similarly to PairsRestraint. In this case we use it
to prevent every particle in the simulation from drifting more than 300A from
the origin (probably an implementation detail).

Next come the crosslinks. For each input dataset a number of RestraintSets
are created to score them in a Bayesian fashion. For Nup84 there are two
such datasets, data/yeast_Nup84_DSS.new.dat and data/EDC_XL_122013.new.dat.

RestraintSet "prior_linear" is a list of PairRestraints, one per crosslink.
Each is simply a PairRestraint that applies a DistancePairScore to the two
particles with a Linear UnaryFunction (this adds a small linear contribution
to the crosslink for long range).

RestraintSet "data" contains a LogWrapper Restraint, which simply converts all
of its child Restraint scores into log space. Those child restraints are
each CrossLinkMSRestraint objects, each of which takes as input a crosslink
length and an inner slope, plus one or more contributions from particle pairs.
Both the particle coordinates and the associated Bayesian 'nuisance'
parameters (sigma and psi) are optimized when we build models.

RestraintSets "prior_psi", "prior_sigmas" and "prior_length" contain simple
Restraints that make sure the nuisance parameters don't go outside their
defined range.

Finally, the EM2D restraint scores particles against one or more EM class
averages using a PCAFitRestraint. In the Nup84 case we score all atomic
resolution particles against the single class average in
data/nup84_kinked_from_class2.pgm.

PCAFitRestraint class: inputs: images file name, particles to fit against,
pixel size, image resolution, number of projections, weight.

To summarize, the restraints used for Nup84 are:

 - For each Nup84 component
   - RestraintSet "sortedsegments"
     - PairRestraint(bead1, bead2,
                     SphereDistancePairScore(HarmonicUpperBound(
                                                  distance, force_constant)))
     - [for each pair of beads in sequence]
   - RestraintSet "unmodeledregions" (empty)
 - PairsRestraint "excluded_volume" (ClosePairContainer(distance_cutoff, slack,
                           RigidClosePairsFinder(), all_10_residue_particles))
 - SingletonsRestraint "barrier" (DistanceToSingletonScore(
                        HarmonicUpperBound(radius, force_constant), center),
                        all_particles)
 - For each crosslinking dataset
   - RestraintSet "prior_data"
     - LogWrapper
       - CrossLinkMSRestraint(length, inner_slope, set of (p1, p2, sigma1,
                                                           sigma2, psi))
       - [for each crosslink]
   - RestraintSet "prior_linear"
     - PairRestraint(p1, p2, DistancePairScore(Linear(intercept, slope)))
     - [for each crosslink]
   - RestraintSet "prior_length"
   - RestraintSet "prior_sigmas"
     - UniformPrior(min_nuisance, max_nuisance)
   - RestraintSet "prior_psi"
     - UniformPrior(min_nuisance, max_nuisance)
     - JeffreysRestraint()
 - PCAFitRestraint(images, all_atomic_particles, pixel_size, image_resolution,
                   number_of_projections, weight)
