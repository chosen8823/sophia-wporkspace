# Architecture

The system treats every discoverable item as an artifact atom with immutable content identity.

A run has five logical stages:

**Observe**: enumerate artifacts and retain source identity.

**Resolve**: extract references and candidate relationships without treating them as facts.

**Oscillate**: apply independent analytical lenses. Lenses are allowed to disagree.

**Resonate**: compare representations and surface recurring motifs, structures, and candidate relationships.

**Recurse**: selected relationships become a bounded next frontier.

Future adapters may ingest GitHub metadata, archived web pages, public creator profiles, SpiderFoot-style observations, and crawler output. All adapters emit the same evidence envelope.

The graph distinguishes OBSERVED, DERIVED, MODEL, HYPOTHESIS, and HUMAN-VERIFIED states. No downstream stage may silently promote one state into another.
