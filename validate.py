#!/usr/bin/env python3
"""
TOTE-CODEX W.A.R. MODE Validation Script

This script validates all JSON files in the TOTE-CODEX system
to ensure they comply with JSON syntax and core policies.
"""

import json
import sys
import os
from pathlib import Path

def validate_json_file(filepath):
    """Validate a single JSON file."""
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
        print(f"✅ VALID: {filepath}")
        return True, data
    except json.JSONDecodeError as e:
        print(f"❌ INVALID JSON: {filepath}")
        print(f"   Error: {e}")
        return False, None
    except Exception as e:
        print(f"❌ ERROR: {filepath}")
        print(f"   Error: {e}")
        return False, None

def check_compliance(data, filepath):
    """Check if data complies with core policies."""
    if 'metadata' in data:
        metadata = data['metadata']
        if 'compliance' in metadata:
            compliance = metadata['compliance']
            
            required_policies = {
                'kids_first': True,
                'sabbath_safe': True,
                'no_dark_patterns': True
            }
            
            for policy, expected_value in required_policies.items():
                if policy not in compliance:
                    print(f"⚠️  WARNING: {filepath} missing policy '{policy}'")
                    return False
                elif compliance[policy] != expected_value:
                    print(f"⚠️  WARNING: {filepath} policy '{policy}' = {compliance[policy]}, expected {expected_value}")
                    return False
            
            print(f"✅ COMPLIANT: {filepath}")
            return True
        else:
            print(f"⚠️  WARNING: {filepath} missing 'compliance' in metadata")
            return False
    else:
        print(f"ℹ️  INFO: {filepath} has no metadata (may not require compliance)")
        return True

def main():
    """Main validation function."""
    print("=" * 60)
    print("TOTE-CODEX W.A.R. MODE - JSON Validation")
    print("=" * 60)
    print()
    
    # Get the base directory
    base_dir = Path(__file__).parent
    
    # Files to validate
    json_files = [
        base_dir / 'tote-codex/classes/weapon-tote-classes.json',
        base_dir / 'tote-codex/war/war-system.json',
        base_dir / 'tote-codex/war/scroll-sing-defense.json',
        base_dir / 'tote-codex/war/timering-codes.json',
        base_dir / 'tote-codex/ledger/tribunal-ledger.json',
        base_dir / 'tote-codex/wallet/bleu-wallet-integration.json',
    ]
    
    total_files = len(json_files)
    valid_files = 0
    compliant_files = 0
    
    print(f"Validating {total_files} JSON files...\n")
    
    for filepath in json_files:
        if not filepath.exists():
            print(f"❌ FILE NOT FOUND: {filepath}")
            continue
            
        is_valid, data = validate_json_file(filepath)
        if is_valid:
            valid_files += 1
            if check_compliance(data, filepath):
                compliant_files += 1
        print()
    
    print("=" * 60)
    print("VALIDATION SUMMARY")
    print("=" * 60)
    print(f"Total files:      {total_files}")
    print(f"Valid JSON:       {valid_files}/{total_files}")
    print(f"Policy compliant: {compliant_files}/{total_files}")
    print()
    
    if valid_files == total_files and compliant_files == total_files:
        print("✅ ALL SYSTEMS GO - TOTE-CODEX W.A.R. MODE READY")
        return 0
    elif valid_files == total_files:
        print("⚠️  All files are valid JSON, but some may not be policy compliant")
        return 1
    else:
        print("❌ Some files have JSON syntax errors")
        return 1

if __name__ == "__main__":
    sys.exit(main())
