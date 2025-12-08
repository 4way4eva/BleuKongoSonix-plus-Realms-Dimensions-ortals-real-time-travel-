#!/usr/bin/env python3
"""
ENFT Artifact Validation Script
Validates all ENFT artifacts against their schemas and policies
"""

import json
import sys
import os
from pathlib import Path
from typing import Dict, List, Tuple

try:
    import jsonschema
    from jsonschema import validate, ValidationError
except ImportError:
    print("Error: jsonschema module not installed")
    print("Install with: pip install jsonschema")
    sys.exit(1)


def load_json_file(filepath: Path) -> Dict:
    """Load and parse a JSON file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in {filepath}: {e}")
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath}")


def validate_artifact(artifact_path: Path, schema_path: Path) -> Tuple[bool, List[str]]:
    """
    Validate an ENFT artifact against the schema
    Returns: (is_valid, list_of_errors)
    """
    errors = []
    
    try:
        artifact = load_json_file(artifact_path)
        schema = load_json_file(schema_path)
        
        # Validate against JSON schema
        try:
            validate(instance=artifact, schema=schema)
        except ValidationError as e:
            errors.append(f"Schema validation error: {e.message}")
            return False, errors
        
        # Validate core policies
        policies = artifact.get('policies', {})
        required_policies = ['kids_first', 'sabbath_safe', 'no_dark_patterns']
        
        for policy in required_policies:
            if policy not in policies:
                errors.append(f"Missing required policy: {policy}")
            elif policies[policy] is not True:
                errors.append(f"Policy {policy} must be true, got {policies[policy]}")
        
        if errors:
            return False, errors
        
        # Additional validations
        if 'tiers' in artifact and len(artifact['tiers']) == 0:
            errors.append("At least one tier must be defined")
        
        # Validate ENFT ID format
        enft_id = artifact.get('enft_id', '')
        if not enft_id.startswith('ENFT-'):
            errors.append(f"Invalid ENFT ID format: {enft_id}")
        
        if errors:
            return False, errors
        
        return True, []
        
    except Exception as e:
        errors.append(f"Validation error: {str(e)}")
        return False, errors


def main():
    """Main validation function"""
    # Get script directory
    script_dir = Path(__file__).parent.absolute()
    artifacts_dir = script_dir / 'artifacts'
    schema_path = script_dir / 'schemas' / 'enft-artifact.schema.json'
    
    print("=" * 60)
    print("ENFT Artifact Validation")
    print("=" * 60)
    print()
    
    # Check if schema exists
    if not schema_path.exists():
        print(f"❌ Schema file not found: {schema_path}")
        sys.exit(1)
    
    print(f"✓ Schema loaded: {schema_path.name}")
    print()
    
    # Check if artifacts directory exists
    if not artifacts_dir.exists():
        print(f"❌ Artifacts directory not found: {artifacts_dir}")
        sys.exit(1)
    
    # Find all artifact JSON files
    artifact_files = list(artifacts_dir.glob('ENFT-*.json'))
    
    if not artifact_files:
        print(f"⚠️  No artifacts found in {artifacts_dir}")
        sys.exit(0)
    
    print(f"Found {len(artifact_files)} artifact(s) to validate")
    print()
    
    # Validate each artifact
    all_valid = True
    results = []
    
    for artifact_path in sorted(artifact_files):
        print(f"Validating: {artifact_path.name}")
        is_valid, errors = validate_artifact(artifact_path, schema_path)
        
        if is_valid:
            print(f"  ✓ Valid")
            results.append((artifact_path.name, True, []))
        else:
            print(f"  ❌ Invalid")
            for error in errors:
                print(f"    - {error}")
            results.append((artifact_path.name, False, errors))
            all_valid = False
        print()
    
    # Summary
    print("=" * 60)
    print("Validation Summary")
    print("=" * 60)
    
    valid_count = sum(1 for _, is_valid, _ in results if is_valid)
    invalid_count = len(results) - valid_count
    
    print(f"Total artifacts: {len(results)}")
    print(f"Valid: {valid_count}")
    print(f"Invalid: {invalid_count}")
    print()
    
    if all_valid:
        print("✓ All artifacts passed validation!")
        sys.exit(0)
    else:
        print("❌ Some artifacts failed validation")
        sys.exit(1)


if __name__ == '__main__':
    main()
