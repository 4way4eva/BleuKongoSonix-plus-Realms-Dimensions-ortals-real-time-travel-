# ENFT System - EV0L Enhanced NFTs

## Overview

The ENFT (EV0L Enhanced NFT) system is the ownership and collectibles framework for the EVOLVERSE ecosystem. This system manages digital and hybrid real-to-meta assets across the Galaxy Grub division and beyond.

## Project Information

- **Project**: EVOLVERSE - Simuldion
- **Division**: EVOL GalacyGrub
- **Market Reach**: Interplanetary Intercultural Real To-Meta Hybrid
- **Core Currency**: EGoin
- **Ownership Model**: ENFT
- **Current Valuation**: $1,487 Trillion USD
- **Growth Trajectory**: Annual Skyward

## Core ENFT Policies

All ENFT artifacts must comply with three foundational policies:

1. **kids_first**: Family-friendly and appropriate for all ages
2. **sabbath_safe**: Respects rest, spiritual practices, and healthy boundaries
3. **no_dark_patterns**: No manipulative design or predatory mechanics

These policies ensure the EVOLVERSE maintains its ethical standards and inclusive community values.

## Directory Structure

```
enft/
├── artifacts/          # ENFT artifact definitions (JSON files)
├── bundles/           # Bundle configurations
├── brokers/           # Trading and exchange systems
├── data/              # Data and analytics
├── schemas/           # JSON schemas for validation
├── enft-config.yml    # Configuration file
├── validate.py        # Validation script
└── README.md          # This file
```

## ENFT Artifacts

### ENFT-0001: BLEU FLAME Commemorative Plate

**Tagline**: "A Dish So Smart, It Remembers You."

The inaugural ENFT artifact - a commemorative plate featuring SmartCeramic technology with memory ink that reacts to temperature and maintains ECuln balance.

#### Tiers

1. **Public Edition** - 8,333 editions
   - Global drop available to the public
   - Bundled with first VerseMeal (Gam LT)

2. **Elite Founder's Plates** - 38 editions
   - Exclusive founder's edition
   - Minted only once

3. **True Edition** - 1-of-1
   - God Tier ultimate collector's piece
   - Singular edition

#### Material Specifications

- **Primary Material**: SmartCeramic
- **Special Properties**:
  - Memory ink technology
  - Temperature reactivity
  - ECuln balance maintenance
  - Owner recognition capability

#### Design Elements

- Glowing glyphs
- Blue flame etch pattern
- Interactive temperature-reactive surface
- ENFT signature underneath

## Validation

### Prerequisites

Install the required Python dependencies:

```bash
pip install jsonschema
```

### Running Validation

To validate all ENFT artifacts against their schemas:

```bash
python3 enft/validate.py
```

The validation script will:
- Check all artifacts in the `artifacts/` directory
- Validate against the JSON schema
- Verify core policy compliance
- Report any errors or warnings

### Validation Requirements

All artifacts must:
- Follow the ENFT-XXXX naming convention
- Comply with all three core policies (kids_first, sabbath_safe, no_dark_patterns)
- Include required fields: name, description, type, tiers, material, design
- Have at least one tier defined
- Pass JSON schema validation

## Creating New ENFT Artifacts

1. Copy the template from `schemas/enft-artifact.schema.json`
2. Create a new JSON file in `artifacts/` with format `ENFT-XXXX.json`
3. Fill in all required fields
4. Ensure all three core policies are set to `true`
5. Run validation: `python3 enft/validate.py`

## Schema

The ENFT artifact schema (`schemas/enft-artifact.schema.json`) defines:

- **Required fields**: enft_id, name, description, type, tiers, material, design, policies, metadata
- **Tier types**: Public, Elite, God_Tier
- **Artifact types**: commemorative_plate, wearable, tool, property, currency, experience
- **Policy requirements**: All three core policies must be true

## Investment

**"Invest in the Verse That Feeds the Universe."**

The ENFT system represents a new paradigm in digital ownership, combining:
- Real-world utility (SmartCeramic technology)
- Meta-world presence (digital collectibles)
- Interplanetary scalability
- Ethical design principles

## Support

For questions about the ENFT system, artifact creation, or validation issues, please refer to the EVOLVERSE documentation or contact the Galaxy Grub division.

---

*EVOLVERSE - Where the Physical Meets the Meta*
