# Resonance OSINT Lab

A local-first, evidence-first recursive repository and public-source analysis lab.

The first target is this repository itself. The crawler walks repository artifacts, extracts references and concepts, records provenance, and emits multiple analysis perspectives without collapsing disagreement.

## Invariants

- Observation is not attribution.
- Similarity is not identity.
- Derived claims retain links to source evidence.
- Every analysis pass is append-only and reproducible.
- Recursion is bounded by explicit depth, budget, and visited-state rules.
- Secrets and credentials are never copied into generated findings.

## First loop

```
repository -> inventory -> artifact atoms -> references -> perspectives
     ^                                             |
     |---------------- recursive frontier --------|
```

Run:

```bash
python -m resonance_osint crawl .
```

Generated output goes under `resonance/` as JSONL so later graph, embedding, signing, and visualization layers can consume the same event stream.
