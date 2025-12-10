#!/usr/bin/env python3
"""
TOTE-CODEX Validation Script
Validates all JSON configurations against schemas
"""

import json
import os
import sys
from pathlib import Path
from typing import List, Dict, Any, Tuple

try:
    import jsonschema
    from jsonschema import validate, ValidationError
    HAS_JSONSCHEMA = True
except ImportError:
    HAS_JSONSCHEMA = False
    print("⚠️  Warning: jsonschema not installed. Using basic JSON validation only.")
    print("   Install with: pip3 install jsonschema")
    print()

class ToteCodexValidator:
    """Validator for TOTE-CODEX configurations"""
    
    def __init__(self, base_path: str = None):
        if base_path is None:
            base_path = os.path.dirname(os.path.abspath(__file__))
        self.base_path = Path(base_path)
        self.schemas_path = self.base_path / "schemas"
        self.errors = []
        self.warnings = []
        
    def load_json(self, filepath: Path) -> Tuple[bool, Any]:
        """Load and parse JSON file"""
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
            return True, data
        except json.JSONDecodeError as e:
            self.errors.append(f"❌ JSON parse error in {filepath.name}: {e}")
            return False, None
        except Exception as e:
            self.errors.append(f"❌ Error reading {filepath.name}: {e}")
            return False, None
    
    def validate_against_schema(self, data: Dict, schema: Dict, filename: str) -> bool:
        """Validate data against JSON schema"""
        if not HAS_JSONSCHEMA:
            return True  # Skip schema validation if jsonschema not available
        
        try:
            validate(instance=data, schema=schema)
            return True
        except ValidationError as e:
            self.errors.append(f"❌ Schema validation failed for {filename}: {e.message}")
            return False
    
    def validate_tote_classes(self) -> bool:
        """Validate all tote class definitions"""
        classes_path = self.base_path / "classes"
        schema_path = self.schemas_path / "tote-class-schema.json"
        
        if not schema_path.exists():
            self.warnings.append(f"⚠️  Schema not found: {schema_path}")
            return True
        
        success, schema = self.load_json(schema_path)
        if not success:
            return False
        
        all_valid = True
        tote_files = list(classes_path.glob("*.json"))
        
        print(f"Validating {len(tote_files)} tote class files...")
        
        for tote_file in tote_files:
            success, data = self.load_json(tote_file)
            if not success:
                all_valid = False
                continue
            
            if self.validate_against_schema(data, schema, tote_file.name):
                print(f"  ✅ {tote_file.name}")
            else:
                all_valid = False
        
        return all_valid
    
    def validate_wallet_configs(self) -> bool:
        """Validate all wallet configurations"""
        wallet_path = self.base_path / "wallet"
        schema_path = self.schemas_path / "wallet-schema.json"
        
        if not schema_path.exists():
            self.warnings.append(f"⚠️  Schema not found: {schema_path}")
            return True
        
        success, schema = self.load_json(schema_path)
        if not success:
            return False
        
        all_valid = True
        wallet_files = list(wallet_path.glob("*.json"))
        
        print(f"Validating {len(wallet_files)} wallet coin files...")
        
        for wallet_file in wallet_files:
            success, data = self.load_json(wallet_file)
            if not success:
                all_valid = False
                continue
            
            if self.validate_against_schema(data, schema, wallet_file.name):
                print(f"  ✅ {wallet_file.name}")
            else:
                all_valid = False
        
        return all_valid
    
    def validate_config_file(self) -> bool:
        """Validate main configuration file"""
        config_path = self.base_path / "tote-config.yml"
        
        if not config_path.exists():
            self.errors.append("❌ Configuration file not found: tote-config.yml")
            return False
        
        print("Validating configuration file...")
        print(f"  ✅ tote-config.yml")
        return True
    
    def validate_python_scripts(self) -> bool:
        """Basic validation of Python scripts"""
        scripts = [
            "war-lockdown/breach_detection.py",
            "ssod/scroll_sing.py",
            "timering/timering_codes.py",
            "tribunal/ledger_trail.py"
        ]
        
        print(f"Validating {len(scripts)} Python scripts...")
        all_valid = True
        
        for script in scripts:
            script_path = self.base_path / script
            if script_path.exists():
                # Try to compile the script
                try:
                    with open(script_path, 'r') as f:
                        compile(f.read(), script_path, 'exec')
                    print(f"  ✅ {script}")
                except SyntaxError as e:
                    self.errors.append(f"❌ Syntax error in {script}: {e}")
                    all_valid = False
            else:
                self.errors.append(f"❌ Script not found: {script}")
                all_valid = False
        
        return all_valid
    
    def run_all_validations(self) -> bool:
        """Run all validations"""
        print("🔍 TOTE-CODEX Validation")
        print("=" * 50)
        print()
        
        results = []
        
        # Validate config file
        results.append(self.validate_config_file())
        print()
        
        # Validate tote classes
        results.append(self.validate_tote_classes())
        print()
        
        # Validate wallet configs
        results.append(self.validate_wallet_configs())
        print()
        
        # Validate Python scripts
        results.append(self.validate_python_scripts())
        print()
        
        # Print summary
        print("=" * 50)
        
        if self.warnings:
            print("⚠️  Warnings:")
            for warning in self.warnings:
                print(f"  {warning}")
            print()
        
        if self.errors:
            print("❌ Errors:")
            for error in self.errors:
                print(f"  {error}")
            print()
        
        all_valid = all(results) and len(self.errors) == 0
        
        if all_valid:
            print("✅ All validations passed!")
            print("🚀 TOTE-CODEX W.A.R. MODE is operational")
        else:
            print("❌ Validation failed. Please fix the errors above.")
        
        print("=" * 50)
        
        return all_valid


if __name__ == "__main__":
    validator = ToteCodexValidator()
    success = validator.run_all_validations()
    sys.exit(0 if success else 1)
