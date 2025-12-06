#!/usr/bin/env python3
"""
ENFT Artifact Validator

Validates ENFT artifacts against their JSON schemas.
"""

import json
import sys
from pathlib import Path

def load_json(filepath):
    """Load and parse a JSON file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def validate_artifact(artifact_file):
    """Validate an artifact file has required fields."""
    try:
        artifact = load_json(artifact_file)
        
        # Check schema field
        if 'schema' not in artifact:
            print(f"❌ {artifact_file.name}: Missing 'schema' field")
            return False
        
        schema_type = artifact['schema']
        
        # Validate based on schema type
        if schema_type == 'EV0L/ENFT.v1':
            required = ['artifact_id', 'title', 'creator', 'provenance', 'issuance', 'policy']
        elif schema_type == 'EV0L/ENFT_BUNDLE.v1':
            required = ['bundle_id', 'artifacts']
        elif schema_type == 'EV0L/BROKER_PLACEMENT.v1':
            required = ['artifact_id', 'density_score', 'bills_issued', 'metavault', 'declared_by', 'declaration']
        else:
            print(f"⚠️  {artifact_file.name}: Unknown schema type '{schema_type}' - skipping validation")
            print(f"    Known schemas: EV0L/ENFT.v1, EV0L/ENFT_BUNDLE.v1, EV0L/BROKER_PLACEMENT.v1")
            return True  # Don't fail on unknown schemas, but warn clearly
        
        # Check required fields
        missing = [field for field in required if field not in artifact]
        if missing:
            print(f"❌ {artifact_file.name}: Missing required fields: {', '.join(missing)}")
            return False
        
        # Additional validation for ENFT artifacts
        if schema_type == 'EV0L/ENFT.v1':
            policy = artifact.get('policy', {})
            if not all([policy.get('kids_first'), policy.get('sabbath_safe'), policy.get('no_dark_patterns')]):
                print(f"⚠️  {artifact_file.name}: Policy requirements not all set to true")
        
        print(f"✅ {artifact_file.name}: Valid {schema_type}")
        return True
        
    except json.JSONDecodeError as e:
        print(f"❌ {artifact_file.name}: Invalid JSON - {e}")
        return False
    except Exception as e:
        print(f"❌ {artifact_file.name}: Validation error - {e}")
        return False

def main():
    """Main validation function."""
    enft_dir = Path(__file__).parent
    
    print("🔍 ENFT Artifact Validation")
    print("=" * 50)
    
    all_valid = True
    
    # Validate artifacts
    print("\n📦 Artifacts:")
    artifacts_dir = enft_dir / 'artifacts'
    if artifacts_dir.exists():
        for artifact_file in sorted(artifacts_dir.glob('*.json')):
            if not validate_artifact(artifact_file):
                all_valid = False
    
    # Validate bundles
    print("\n📚 Bundles:")
    bundles_dir = enft_dir / 'bundles'
    if bundles_dir.exists():
        for bundle_file in sorted(bundles_dir.glob('*.json')):
            if not validate_artifact(bundle_file):
                all_valid = False
    
    # Validate broker placements
    print("\n🏦 Broker Placements:")
    brokers_dir = enft_dir / 'brokers'
    if brokers_dir.exists():
        for broker_file in sorted(brokers_dir.glob('*.json')):
            if not validate_artifact(broker_file):
                all_valid = False
    
    print("\n" + "=" * 50)
    if all_valid:
        print("✅ All artifacts validated successfully!")
        return 0
    else:
        print("❌ Validation failed for one or more artifacts")
        return 1

if __name__ == '__main__':
    sys.exit(main())
