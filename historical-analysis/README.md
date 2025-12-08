# Historical Analysis: Colonial Resource Extraction & Afro-Diaspora Communities

## Overview

This directory contains structured datasets documenting:
1. **Colonial Resource Extraction**: Historical analysis of colonial entities, their extracted resources, operating regions, and modern corporate successors
2. **Afro-Diaspora Communities**: Documentation of Afro-diaspora communities worldwide, their origins, locations, and cultural significance

## Purpose

These datasets serve to:
- Document the historical continuity between colonial extraction and modern corporate structures
- Preserve knowledge of Afro-diaspora communities and their cultural heritage
- Provide structured data for educational, research, and awareness purposes
- Enable analysis of historical patterns and their contemporary implications

## Directory Structure

```
historical-analysis/
├── data/
│   ├── colonial_entities.json          # Colonial resource extraction data
│   └── afro_diaspora_communities.json  # Afro-diaspora community data
├── schemas/
│   ├── colonial_entity_schema.json     # JSON schema for colonial entities
│   └── afro_diaspora_schema.json       # JSON schema for diaspora communities
└── README.md                            # This file
```

## Data Files

### Colonial Entities (`colonial_entities.json`)

Documents 49 colonial entities and their modern successors, including:
- **Trading Companies**: Royal African Company, Dutch West India Company, East India Company
- **Mining Operations**: De Beers, Rio Tinto, Anglo American, Glencore
- **Oil & Gas**: BP, Shell, ExxonMobil, TotalEnergies, Chevron
- **Financial Institutions**: Barclays Bank, Standard Chartered, Rothschild & Sons
- **Agriculture & Manufacturing**: Unilever, Nestlé, Cargill, Heineken

**Data Fields**:
- `name`: Colonial entity or company name
- `resources`: Primary resources extracted (gold, oil, slaves, diamonds, etc.)
- `operating_regions`: Geographic regions of colonial operation
- `modern_successor`: Current corporate entity or institutional legacy
- `category`: Classification (trading_company, mining, oil_gas, finance, agriculture, manufacturing, other)

### Afro-Diaspora Communities (`afro_diaspora_communities.json`)

Documents 13 distinct Afro-diaspora communities globally, including:
- **Americas**: Afro-Brazilian, Afro-Cuban, Afro-Colombian, Afro-Mexican, Afro-Puerto Rican, Afro-Dominican
- **North America**: Afro-Indigenous (USA - Gullah/Geechee, Black Seminoles)
- **Asia**: Afro-Chinese, Afro-Filipino, Afro-Indian (Siddi)
- **Middle East**: Afro-Palestinian, Afro-Iraqi, Afro-Iranian

**Data Fields**:
- `group_name`: Name of the Afro-diaspora community
- `symbol`: Flag or emoji representation
- `origin`: Historical migration route and context
- `present_location`: Current geographic locations
- `notable_features`: Cultural contributions, notable individuals, traditions

## Data Sources & Methodology

### Colonial Entities
The colonial entities data is compiled from:
- Historical records of colonial trading companies and their charters
- Academic research on resource extraction in colonial Africa, Asia, and the Americas
- Corporate histories and mergers & acquisitions records
- Modern corporate successor relationships

### Afro-Diaspora Communities
The diaspora communities data is compiled from:
- Historical migration records and slave trade documentation
- Academic research on Afro-diaspora populations
- Cultural anthropology studies
- Community self-documentation and oral histories

## Usage

### Validation

JSON schemas are provided to validate the data structure:

```bash
# Validate colonial entities data
jsonschema -i data/colonial_entities.json schemas/colonial_entity_schema.json

# Validate diaspora communities data
jsonschema -i data/afro_diaspora_communities.json schemas/afro_diaspora_schema.json
```

### Loading Data

```javascript
// JavaScript/Node.js
const colonialEntities = require('./data/colonial_entities.json');
const diasporaCommunities = require('./data/afro_diaspora_communities.json');

// Python
import json
with open('data/colonial_entities.json') as f:
    colonial_entities = json.load(f)
with open('data/afro_diaspora_communities.json') as f:
    diaspora_communities = json.load(f)
```

## Key Insights

### Colonial Resource Extraction Patterns

1. **Continuity of Corporate Control**: Many modern multinational corporations have direct lineage to colonial-era entities
   - BP ← Anglo-Persian Oil Company
   - Shell ← Royal Dutch Shell (colonial operations)
   - De Beers ← De Beers Consolidated Mines
   - Unilever ← Lever Brothers (palm oil extraction)

2. **Resource Categories**:
   - **Extractive Resources**: Oil (15 entities), Gold (10), Diamonds (4), Copper/Cobalt (5)
   - **Agricultural**: Palm oil, Cocoa, Coffee, Cotton, Rubber
   - **Human Trafficking**: Multiple entities engaged in slave trade alongside resource extraction

3. **Geographic Concentration**:
   - West Africa: Primary region for slave trade and early colonial extraction
   - Southern Africa: Focus on precious minerals and metals
   - Congo: Concentrated exploitation of rubber, ivory, copper, and cobalt
   - Nigeria: Significant oil extraction operations

4. **Sector Evolution**:
   - Trading Companies → Modern financial institutions and conglomerates
   - Colonial mining → Contemporary multinational mining corporations
   - Oil companies maintained direct lineage with name changes

### Afro-Diaspora Distribution

1. **Geographic Spread**: Communities documented across 4 continents
   - Americas (7 communities)
   - Asia (3 communities)
   - Middle East (3 communities)

2. **Cultural Resilience**: All communities maintain distinct cultural practices, languages, or traditions despite displacement

3. **Migration Routes**:
   - Atlantic Slave Trade → Americas and Caribbean
   - Trans-Saharan and Indian Ocean Trade → Middle East and Asia
   - Galleon Trade → Philippines
   - Modern Diaspora → China

## Important Notes

### Historical Context
- This data documents historical injustices including slavery, colonial exploitation, and forced labor
- The information is presented for educational and awareness purposes
- Modern successor companies may have varying degrees of connection to historical practices

### Data Accuracy
- Data compiled from multiple historical and academic sources
- Corporate succession relationships may be complex with multiple mergers and acquisitions
- Community names and locations reflect common usage but may not capture all self-identifications

### Ongoing Research
This is a living dataset that may be updated as:
- New historical research emerges
- Additional communities are documented
- Corporate structures change or new connections are identified

## Contributing

To suggest additions or corrections:
1. Ensure data is historically accurate with verifiable sources
2. Follow the existing JSON schema structure
3. Provide source citations for new information
4. Maintain respectful and educational tone

## License

This dataset is compiled for educational purposes. Historical facts and data compilations are not subject to copyright, though specific creative expressions may be.

## Acknowledgments

This work builds upon:
- Historical research by scholars of colonialism and the African diaspora
- Community historians and cultural preservation efforts
- Public historical records and corporate archives

---

**Last Updated**: December 2025
**Dataset Version**: 1.0
