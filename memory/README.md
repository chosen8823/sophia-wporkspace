# Crystalline Conversation State

This directory is the durable, reconstructable memory layer for the Ryan + ChatGPT/Sophia workspace.

A **crystal** is not a transcript replacement. It is a portable state object distilled from one or more conversations while preserving provenance back to its sources.

## Invariants

1. Source evidence is never silently replaced by a summary.
2. Observation, interpretation, proposal, hypothesis, and verification remain distinct.
3. Corrections create descendants; historical crystals remain immutable.
4. Similarity is not identity. Resonance is not provenance.
5. Hydration is selective: load the smallest relevant facets, then follow provenance when more resolution is needed.
6. Unresolved disagreement is retained as state rather than collapsed into a false consensus.
7. Private or sensitive source material is not copied into a public crystal by default.

## Shape

- `schema/crystal.schema.json` — machine-readable crystal contract.
- `STATE.md` — human-readable hydration state for a new session.
- `crystals/` — immutable state snapshots/descendants.
- `index/` — future semantic/temporal/provenance indexes.

## Lifecycle

conversation/event -> observe -> crystallize -> hash/version -> link provenance -> hydrate relevant facets -> append descendant when state changes

The repository commit graph supplies an additional immutable history layer. A crystal's own provenance fields identify what evidence it was derived from.
