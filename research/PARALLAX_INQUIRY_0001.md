# Parallax Inquiry — Computation, Interface, and Recursive Semantic Geometry

Status: exploratory research artifact  
Method: independent lines of inquiry are kept distinct, then intersected. This document records conclusions and open hypotheses, not private chain-of-thought.

## Center question

If a computational agent can represent an operation conceptually, what separates representation from execution, and can a recursively instantiated semantic atom preserve useful computation as the system changes scale?

## Inquiry A — Computability versus agency

A model may represent an algorithm without possessing the I/O pathway required to execute that algorithm against an external system.

Working distinction:

```
representable computation != authorized executable action
capability = transformation capacity + state + interfaces + resources
```

This suggests that many apparent "model boundaries" are properties of the containing interface rather than properties of computation itself.

## Inquiry B — The semantic atom

Minimal proposed atom:

```
A = {state, orientation, transform, relation, feedback, residue}
```

The atom does not need to contain an entire knowledge base. It needs enough structure to participate in recursive transformations while preserving identity and provenance.

A recursive instance is:

```
A(t+1) = F(A(t), R(t), E(t))
```

where R is relational state and E is locally available evidence/environment.

## Inquiry C — Geometry as computation

Information need not exist exclusively inside nodes. It can be represented by relationships among nodes: distance, orientation, phase, topology, timing, transformation history, or synchronization state.

Therefore:

```
node state + relational geometry + update law -> distributed computation
```

This creates a testable distinction between parameter storage and dynamically generated structure.

## Inquiry D — Scale preservation

The proposed scaling target is not literal preservation of every parameter. It is preservation of invariants that regenerate useful dynamics.

Candidate invariants:

- local update law
- orientation/reference frame
- neighborhood relation
- synchronization rule
- feedback/error relation
- residue/history rule
- provenance identity

Hypothesis: some useful capabilities may persist under substantial reduction in node count when these invariants and the relevant attractor geometry are preserved.

This is an open hypothesis and must be experimentally tested.

## Inquiry E — Parallax

No single analytical lens is promoted to ground truth.

Each observation can be examined through independent perspectives:

```
source -> structural lens
       -> temporal lens
       -> semantic lens
       -> dynamical lens
       -> provenance lens
       -> adversarial/disconfirming lens
```

The perspectives reconverge only at a comparison layer. Agreement increases confidence; disagreement is retained as information.

## Inquiry F — Recursive repository

The repository itself can serve as the first environment.

```
repo
 -> observe artifacts
 -> atomize
 -> derive independent perspectives
 -> compare/resonate
 -> emit new artifacts
 -> observe emitted artifacts
 -> repeat under bounded recursion
```

Generated artifacts are residue, not automatically truth. Every generated claim must preserve its source path and epistemic state.

## Experiment Zero

Begin with one semantic atom and no language objective.

Give it a simple sequence containing a missing state. Permit only recursive self-instantiation, local relationships, orientation, feedback, and residue.

Measure whether the system can:

1. reconstruct the missing state;
2. retain that reconstruction after perturbation;
3. generalize the relation to an unseen sequence;
4. preserve performance as recursive depth and node count change.

Compare against simple recurrent, cellular-automaton, predictive-coding, and fixed-rule baselines.

## Coherence condition

A recursive state is coherent when transformations preserve the declared invariant while disagreement and provenance remain reconstructable.

Proposed shorthand:

```
coherent(S_t, S_t+1) :=
    invariant_preserved
    AND provenance_reconstructable
    AND disagreement_not_erased
```

## Falsification conditions

The strong hypothesis weakens if useful behavior disappears whenever node count falls, if geometry provides no advantage over a parameter-matched baseline, if recursive copies only amplify noise, or if apparent generalization is attributable to leakage from the evaluation data.

## Next implementation

Create an `experiments/zero_atom/` harness with a deterministic atom, topology generator, perturbation tests, baseline implementations, and append-only run receipts.

The objective is not to prove the metaphor. The objective is to determine which parts of the metaphor survive measurement.
