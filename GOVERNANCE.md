# Governance

## Purpose

This file defines repository governance for H.U.G.S. It is separate from healthcare authority classes A0 through A4.

A0 through A4 are reserved for healthcare-system authority only. Repository governance uses GOV and AMEND identifiers.

## GOV-01: Doctrinal authority

Spark remains the continuity bridge and final human authority over H.U.G.S. canon.

## GOV-02: Amendment proposal rights

Amendments may be proposed by maintainers, reviewers, researchers, clinicians, patient advocates, auditors, or institutions. Proposal rights do not create authority to silently modify doctrine.

## GOV-03: Review procedure

Every substantive amendment should identify the affected doctrine, control, schema, example, or governance file; describe the reason for change; identify affected interoperability assumptions; and preserve prior versions through versioned evolution.

## GOV-04: Dispute and escalation path

Disputed amendments should be escalated to a recorded review note. If consensus cannot be reached, the repository should preserve competing variants without silently merging them.

## GOV-05: Versioning

Patch versions may correct typographical, formatting, or mechanical errors. Minor versions may add controls, schemas, examples, or explanatory materials without changing core doctrine. Major versions may change doctrine or compliance architecture.

## GOV-06: Adoption thresholds

External adoption may reference a specific H.U.G.S. version only if the adopting entity identifies the version, scope, deviations, and noncompliant extensions.

## GOV-07: Emergency correction procedure

Emergency corrections may be issued for schema errors, broken references, integrity failures, misleading examples, or urgent safety concerns. They must be marked as emergency corrections and later reconciled into the normal version history.

## GOV-08: Deprecation procedure

Deprecated files must remain accessible or clearly referenced. Deprecation should not erase prior canon.

## GOV-09: Interoperability approval procedure

No external SPARK-NITT doctrine, equation, control system, ethics kernel, receipt mechanism, or repository is imported into H.U.G.S. unless interoperability is explicit, documented, versioned, and non-silent.
