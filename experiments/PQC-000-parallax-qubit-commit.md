# Parallax Qubit Commit — PQC/0

Status: proposed executable contract.

## Intent

Treat a Git commit as a classical, immutable carrier for a bounded multi-perspective inquiry. The "qubit" name is an analogy to preserving unresolved alternatives and their relationships; this is not quantum computation and does not claim physical superposition.

## Invariant

Encode transformation rules, not merely payload.

A commit MUST preserve:
- source state,
- orientation/reference frame,
- independent inquiry lanes,
- agreements and disagreements,
- transformation path,
- delta-state (ΔS),
- residue,
- provenance,
- unresolved alternatives.

No lane may silently overwrite another lane.

## Atom

```
Q = {
  id,
  parent,
  source_state,
  orientation,
  lanes[],
  interference,
  invariant,
  delta_s,
  residue,
  provenance,
  next_frontier[]
}
```

Each lane is a projection of the same source state:

```
lane_i = observe(source_state, frame_i, provenance)
```

The parallax operator does not vote. It compares projections and records:

```
interference = {
  stable_invariants,
  constructive_overlap,
  contradiction,
  unresolved,
  novel_relations
}
```

The Third Position is the relation among projections, not an additional winning projection.

## Commit semantics

Git gives the atom content-addressed residue. Parent commits provide causal ancestry. A tree provides the bounded state emitted by the inquiry.

Conceptually:

```
parent_state
   |
   +-- lane/source
   +-- lane/structure
   +-- lane/semantic
   +-- lane/causal
   +-- lane/adversarial
   +-- lane/temporal
   +-- lane/implementation
   +-- lane/observer
          |
          v
     interference
          |
          v
     invariant + ΔS + residue
          |
          v
       COMMIT Q
          |
          +--> next recursive frontier
```

## Eight-lane bootstrap

The initial octo-parallax sampler uses eight orientations:

1. Source — what is directly present?
2. Structure — what relationships/topology exist?
3. Semantic — what meanings survive representation changes?
4. Causal — what transformations could explain the state transition?
5. Adversarial — what interpretation fails under counterexample?
6. Temporal — what changes across ancestry/history?
7. Implementation — what can be executed or tested?
8. Observer — how did frame/orientation affect the other seven readings?

Eight is a bootstrap configuration, not a metaphysical constant.

## Collapse rule

The system does not force binary collapse. It settles only what is supported.

```
settled = intersection(lanes, evidence, invariant)
residue = alternatives - settled
```

Residue remains addressable and may become the next inquiry frontier.

## Recursive rule

```
Q[n+1] = Parallax(
    source = Q[n].residue + Q[n].next_frontier,
    parent = Q[n],
    invariant = preserve(Q[n].invariant)
)
```

Recursion MUST be bounded by depth, evidence budget, visited-state hashes, or explicit stopping criteria.

## Git representation

A PQC commit should emit:

```
parallax/<run-id>/
  atom.json
  lanes/
    source.json
    structure.json
    semantic.json
    causal.json
    adversarial.json
    temporal.json
    implementation.json
    observer.json
  interference.json
  residue.json
  provenance.json
```

The commit hash then addresses the complete classical state of that inquiry.

## Testable hypothesis

A chain of PQC commits can function as a memory/computation substrate where capability emerges from recursive transformations and relations among small semantic atoms rather than from continuously enlarging each atom.

This is an open hypothesis. The first benchmark should test whether repeated PQC transitions can infer a missing element in a simple sequence while preserving competing hypotheses and reconstructable provenance.
