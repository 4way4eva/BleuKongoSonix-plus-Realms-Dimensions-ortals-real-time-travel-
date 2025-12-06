# EV0L Enhanced NFT (ENFT) System

## Overview

The EV0L ENFT system is a sovereign artifact tracking and issuance framework designed to preserve historical records, educational materials, and cultural heritage through blockchain-inspired provenance tracking.

**Banner:** "No Trust — Kids First. Sabbath-safe continuity. Sovereign authorship attested."

## Core Principles

- **Kids First**: All content and systems prioritize child safety and appropriate educational content
- **Sabbath-safe Continuity**: Respects cultural and religious practices with appropriate safeguards
- **No Dark Patterns**: Transparent, ethical design with no manipulative elements
- **Sovereign Authorship**: Clear attribution and provenance for all artifacts

## Directory Structure

```
enft/
├── artifacts/          # Individual ENFT artifacts
│   ├── ENFT-0001.json  # Overscale Law Scroll — Seven-to-Six Anomaly
│   ├── ENFT-0002.json  # Routes Ledger — Silk Road Archive
│   └── ENFT-0003.json  # Global Extraction Dossier — Congo Free State
├── bundles/            # Collections of related artifacts
│   └── BNDL-0012.json  # Historical Archives Bundle
├── brokers/            # Broker placement and distribution records
│   └── ENFT-0003-placement.json
├── data/               # Source data referenced by artifacts
│   ├── routes.csv
│   └── Global_Extraction_Dossier.csv
├── schemas/            # JSON Schema definitions
│   ├── ENFT.v1.schema.json
│   ├── ENFT_BUNDLE.v1.schema.json
│   └── BROKER_PLACEMENT.v1.schema.json
└── enft-config.yml     # System configuration
```

## Artifact Types

### ENFT Artifacts (EV0L/ENFT.v1)

Individual artifacts representing:
- **Educational scrolls and legal documents** (ENFT-0001: Overscale Law Scroll)
- **Historical trade route archives** (ENFT-0002: Routes Ledger)
- **Colonial extraction documentation** (ENFT-0003: Global Extraction Dossier)

Each artifact includes:
- Unique artifact ID
- Title and creator attribution
- School and realm tags for categorization
- Provenance information (signatures, SHA256, timestamp)
- Issuance details (bill codes, denominations, market routes)
- Policy compliance markers

### ENFT Bundles (EV0L/ENFT_BUNDLE.v1)

Collections of related artifacts grouped by:
- Theme (e.g., historical archives)
- Institution (e.g., Historian Middle School)
- Time period or realm

### Broker Placements (EV0L/BROKER_PLACEMENT.v1)

Distribution and placement records including:
- Density scores
- Bill issuance tracking
- MetaVault assignments
- Route configurations

## Bill Codes

The system uses color-coded bill types for different artifact categories:

- **ROYAL_BLEU**: Primary sovereignty and legal documents
- **ARCHIVE_BLEU**: Historical archives and educational materials
- **TRANSPARENCY_BLEU**: Public records and accountability documents
- **SKYY_BLEU**: Secondary issuance for complementary materials
- **ROSE_BLEU**: Special commemorative issuances

## Roles and Assurance

### Active Roles

- **Dean of School**: Educational oversight and curriculum approval
- **Treasurer of Treasury**: Financial and issuance authority
- **Keeper of Codex**: Archive maintenance and provenance verification

### Assurance Requirements

- **Commit Signing**: REQUIRED for all repository changes
- **Provenance**: All artifacts must include ScrollSig, SHA256, and ENFT_Anchor
- **Tribunal on Tamper**: Active monitoring and response to unauthorized modifications

## Artifact Examples

### ENFT-0001: Overscale Law Scroll

A foundational legal document from Madam C.J. Walker University addressing the "Seven-to-Six Anomaly" with specific glyphs, sequences, and sovereign law principles.

**Key Features:**
- Anomaly marker: 🦅💨🫁🧘‍♂️😔eighty/6Þ^Y
- Sequence: [2, 3, 4, 5, 6, -7]
- Issuance: ROYAL_BLEU and SKYY_BLEU bills
- Denominations: 10, 50, 77

### ENFT-0002: Routes Ledger — Silk Road Archive

Historical trade route documentation focusing on the China-Kaifeng Jewish community connections along the Silk Road.

**Source Data:** `routes.csv#row:China-Kaifeng-Jews`

### ENFT-0003: Global Extraction Dossier

Documentation of colonial extraction activities, specifically the Belgian Congo Free State period (1885-1908).

**Source Data:** `Global_Extraction_Dossier.csv#Belgian-Congo-Free-State`

## Schema Validation

All artifacts can be validated against their respective JSON schemas located in `enft/schemas/`:

- `ENFT.v1.schema.json` - Individual artifact schema
- `ENFT_BUNDLE.v1.schema.json` - Bundle schema
- `BROKER_PLACEMENT.v1.schema.json` - Broker placement schema

## Usage

To add a new artifact:

1. Create a JSON file in `enft/artifacts/` following the ENFT.v1 schema
2. Ensure all required fields are present (artifact_id, title, creator, provenance, issuance, policy)
3. Reference any source data files in `enft/data/`
4. Add to a bundle if appropriate
5. Create broker placement record if needed

## Compliance

All artifacts must comply with the three core policy requirements:
- ✅ `kids_first: true`
- ✅ `sabbath_safe: true`
- ✅ `no_dark_patterns: true`

## License and Attribution

This ENFT system maintains proper attribution through:
- Creator fields in each artifact
- School and realm tags for institutional affiliation
- Signed provenance with timestamps
- SHA256 hashes for integrity verification

---

**Declaration**: "This codex inheritance is Treasury."  
**Declared by**: Dr. Sosa (Dean & Treasurer)
