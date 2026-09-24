# Parallax Commit Atom v0

Status: proposed executable contract / experiment.

## Intent

Treat a Git commit as a content-addressed semantic excitation: a compact state transition that carries multiple independent lines of inquiry, preserves their reference frames, and leaves replayable residue.

The commit is not "the answer." It is the aperture through which several perspectives cross.

## Canonical atom

A = (S, φ, O, B, U, T, R)

- S: current state
- φ: phase / temporal position
- O: orientation relative to an explicit reference frame
- B: boundaries / admissible transitions
- U: unresolved possibilities
- T: transformation history
- R: residue / observable trace

Identity is preserved across A -> A' by lineage and invariants, not by requiring an unchanged payload.

## Parallax lanes

Every inquiry is evaluated independently against the same canonical atom.

LANE GEOMETRY:
Can the relationships themselves perform computation when instantiated recursively?

LANE SEMANTIC:
Can one semantic atom preserve identity while repeatedly transforming its representation?

LANE DYNAMICS:
Can local feedback, phase, coupling, and settling produce useful attractors without a global controller?

LANE COMPUTATION:
What is the minimum state + rule set required for memory, prediction, composition, and generalization?

LANE PROVENANCE:
Can every transformation remain content-addressed, replayable, attributable to its operator, and distinguish observation from inference?

LANE SCALE:
Which invariants survive expansion and contraction of the recursive structure?

No lane votes another lane out. Agreement is a relation. Disagreement is residue.

## Third Position aperture

For perspectives P_i over canonical state S:

    aperture(P_1 ... P_n, S) ->
        shared invariants
        + frame transforms
        + ΔS_i
        + unresolved residue

The Third Position does not flatten the perspectives into an average. It records the relationship among them.

## Synchronization kernel

Each instantiated atom receives only:

    local state
    orientation
    neighbor relation(s)
    phase / time
    permissible transform
    returned residue

Minimal cycle:

    OBSERVE
      -> RELATE
      -> TRANSFORM
      -> RETURN
      -> COMPARE
      -> ΔS
      -> RESIDUE
      -> COMMIT
      -> RECURSE

The next atom may be the same rule instantiated at a new position, scale, orientation, or time.

## Commit-as-photon analogy

The physical-photon analogy is intentionally metaphorical.

A commit behaves usefully like a programmed excitation because it has:

- a content identity: commit hash
- a direction: parent -> child
- an event boundary: the state transition
- an encoded transformation: diff
- a reference frame: branch / repository / parent state
- residue: resulting tree plus derived observations
- ancestry: parent commit(s)

The important property is not the metaphor. It is that a small immutable event can propagate a transformation rule through a larger relational structure.

## Experiment Zero

Start with exactly one atom type and one deterministic transformation rule.

Do not add specialized agents.

At each generation instantiate the same atom under transformed orientation / phase / neighborhood conditions. Feed returned residue into the next cycle.

Measure:

- invariant retention
- reconstruction fidelity
- stable / recurring attractors
- prediction of a withheld element
- memory across cycles
- sensitivity to orientation
- compression ratio
- disagreement retained versus destroyed
- behavior as recursion depth and width change

First benchmark: provide a repeating sequence with one element withheld. The system succeeds only if the recursive relational state converges on a representation that identifies the missing element without a specialized missing-element rule.

## Provenance states

Every assertion emitted by the experiment is typed as one of:

OBSERVED
DERIVED
MODEL
HYPOTHESIS
HUMAN_VERIFIED

Promotion between states must be explicit and append-only.

## Invariant

Encode transformation rules and relationships rather than assuming the payload itself is the durable unit.

A smaller representation is successful when it preserves the relationships needed to regenerate useful behavior, not merely when it reproduces stored bits.

## Open hypothesis

A sufficiently expressive recursive semantic atom may allow useful computation to emerge primarily from relational geometry, orientation, temporal phase, feedback, and residue.

This commit does not claim that hypothesis is true.

It makes the hypothesis executable enough to falsify.
