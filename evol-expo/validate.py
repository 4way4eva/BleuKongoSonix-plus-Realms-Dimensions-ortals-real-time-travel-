#!/usr/bin/env python3
"""
EVOL EXPO SYSTEMS Validation Script
Validates all EXPO artifacts for compliance and integrity
"""

import json
import sys
import os
from pathlib import Path
from typing import Dict, List, Tuple


def load_json_file(filepath: Path) -> Dict:
    """Load and parse a JSON file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in {filepath}: {e}")
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath}")


def validate_compliance_policies(artifact: Dict, filepath: Path) -> Tuple[bool, List[str]]:
    """Validate that artifact has required compliance policies"""
    errors = []
    
    # Check for metadata section
    if 'metadata' not in artifact:
        errors.append("Missing 'metadata' section")
        return False, errors
    
    metadata = artifact['metadata']
    
    # Check for compliance section
    if 'compliance' not in metadata:
        errors.append("Missing 'metadata.compliance' section")
        return False, errors
    
    compliance = metadata['compliance']
    
    # Required policies
    required_policies = {
        'kids_first': True,
        'sabbath_safe': True,
        'no_dark_patterns': True,
        'soul_sovereignty': True,
        'divine_scroll_property': True,
        'righteous_movement_only': True
    }
    
    # Validate each required policy
    for policy, expected_value in required_policies.items():
        if policy not in compliance:
            errors.append(f"Missing required policy: {policy}")
        elif compliance[policy] != expected_value:
            errors.append(f"Policy '{policy}' must be {expected_value}, got {compliance[policy]}")
    
    return len(errors) == 0, errors


def validate_metadata(artifact: Dict, filepath: Path) -> Tuple[bool, List[str]]:
    """Validate metadata section"""
    errors = []
    
    if 'metadata' not in artifact:
        errors.append("Missing 'metadata' section")
        return False, errors
    
    metadata = artifact['metadata']
    
    # Required metadata fields
    required_fields = ['version', 'created_date', 'system', 'classification', 'status']
    
    for field in required_fields:
        if field not in metadata:
            errors.append(f"Missing required metadata field: {field}")
    
    # Validate system field contains "EVOL EXPO"
    if 'system' in metadata and 'EVOL EXPO' not in metadata['system']:
        errors.append(f"System field must contain 'EVOL EXPO', got: {metadata['system']}")
    
    # Validate status is ACTIVE
    if 'status' in metadata and metadata['status'] != 'ACTIVE':
        errors.append(f"Status should be 'ACTIVE', got: {metadata['status']}")
    
    return len(errors) == 0, errors


def validate_artifact(filepath: Path) -> Tuple[bool, List[str]]:
    """
    Validate an EXPO artifact
    Returns: (is_valid, list_of_errors)
    """
    errors = []
    
    try:
        artifact = load_json_file(filepath)
        
        # Validate compliance policies
        is_compliant, policy_errors = validate_compliance_policies(artifact, filepath)
        if not is_compliant:
            errors.extend(policy_errors)
        
        # Validate metadata
        is_valid_metadata, metadata_errors = validate_metadata(artifact, filepath)
        if not is_valid_metadata:
            errors.extend(metadata_errors)
        
        # Check for required top-level fields based on artifact type
        if 'type' not in artifact:
            errors.append("Missing 'type' field")
        
        if 'name' not in artifact:
            errors.append("Missing 'name' field")
        
        # Additional validation based on artifact type
        if 'type' in artifact:
            artifact_type = artifact['type']
            
            if artifact_type == 'COSMIC_PASSPORT':
                if 'certifications' not in artifact:
                    errors.append("COSMIC_PASSPORT must have 'certifications' field")
                if 'access_tokens' not in artifact:
                    errors.append("COSMIC_PASSPORT must have 'access_tokens' field")
            
            elif artifact_type == 'RESTITUTION_LEDGER':
                if 'restitution_index' not in artifact:
                    errors.append("RESTITUTION_LEDGER must have 'restitution_index' field")
                if 'coverage_categories' not in artifact:
                    errors.append("RESTITUTION_LEDGER must have 'coverage_categories' field")
            
            elif artifact_type == 'VAULTED_EXPO_ASSETS':
                if 'asset_collection' not in artifact:
                    errors.append("VAULTED_EXPO_ASSETS must have 'asset_collection' field")
            
            elif artifact_type == 'CEREMONIAL_SPACES':
                if 'event_environments' not in artifact:
                    errors.append("CEREMONIAL_SPACES must have 'event_environments' field")
            
            elif artifact_type == 'AUTHORITY_SEALS':
                if 'authority_seals' not in artifact:
                    errors.append("AUTHORITY_SEALS must have 'authority_seals' field")
        
        return len(errors) == 0, errors
        
    except Exception as e:
        errors.append(f"Error loading file: {str(e)}")
        return False, errors


def main():
    """Main validation function"""
    script_dir = Path(__file__).parent
    
    # Define directories to validate
    dirs_to_validate = [
        'passports',
        'restitution',
        'assets',
        'domes',
        'authority'
    ]
    
    print("=" * 70)
    print("EVOL EXPO SYSTEMS - Artifact Validation")
    print("=" * 70)
    print()
    
    total_files = 0
    passed_files = 0
    failed_files = 0
    
    for dir_name in dirs_to_validate:
        dir_path = script_dir / dir_name
        
        if not dir_path.exists():
            print(f"⚠️  Directory not found: {dir_name}/")
            continue
        
        # Find all JSON files in directory
        json_files = list(dir_path.glob("*.json"))
        
        if not json_files:
            print(f"ℹ️  No JSON files found in {dir_name}/")
            continue
        
        print(f"\n📁 Validating {dir_name}/")
        print("-" * 70)
        
        for json_file in json_files:
            total_files += 1
            is_valid, errors = validate_artifact(json_file)
            
            if is_valid:
                print(f"✅ {json_file.name} - VALID")
                passed_files += 1
            else:
                print(f"❌ {json_file.name} - FAILED")
                for error in errors:
                    print(f"   • {error}")
                failed_files += 1
    
    # Print summary
    print()
    print("=" * 70)
    print("Validation Summary")
    print("=" * 70)
    print(f"Total files validated: {total_files}")
    print(f"✅ Passed: {passed_files}")
    print(f"❌ Failed: {failed_files}")
    
    if failed_files == 0:
        print()
        print("🎉 All EVOL EXPO SYSTEMS artifacts are valid and compliant!")
        return 0
    else:
        print()
        print("⚠️  Some artifacts failed validation. Please fix the errors above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
