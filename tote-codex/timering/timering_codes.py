#!/usr/bin/env python3
"""
TimeRing Code System
Time-bound access codes for TOTE security
"""

import json
import random
import string
from datetime import datetime, timedelta
from typing import Dict, Any, Optional

class TimeRingCodeSystem:
    """
    TimeRing Code System
    Each tote issues a TimeRing Code at moment of deployment
    Code binds to 1 moment only in EV0LClock
    Access outside time ring = Codex Purge + Vault Return
    """
    
    def __init__(self):
        self.active_codes = {}
        self.expired_codes = []
        
    def generate_timering_code(self, tote_id: str, tote_class: str, 
                               window_minutes: int = 60) -> Dict[str, Any]:
        """
        Generate a TimeRing Code
        Format: THY-{id}B-{cipher}
        Example: THY-51B-ΣΦ7
        """
        # Generate components
        id_part = ''.join(random.choices(string.digits + string.ascii_uppercase, k=2))
        
        # Greek cipher options
        greek_chars = ['Σ', 'Φ', 'Ω', 'Δ', 'Θ', 'Λ', 'Ξ', 'Π']
        cipher = ''.join(random.choices(greek_chars + list(string.digits), k=3))
        
        # Create code
        code = f"THY-{id_part}B-{cipher}"
        
        # Define access window
        now = datetime.utcnow()
        window_start = now
        window_end = now + timedelta(minutes=window_minutes)
        
        code_data = {
            "code_id": f"TR-{int(datetime.utcnow().timestamp())}",
            "timering_code": code,
            "evol_timestamp": now.isoformat(),
            "tote_id": tote_id,
            "tote_class": tote_class,
            "user_signature": f"SIG-{random.randint(10000, 99999)}",
            "active": True,
            "access_window": {
                "start": window_start.isoformat(),
                "end": window_end.isoformat()
            },
            "purge_on_violation": True,
            "vault_return_enabled": True
        }
        
        self.active_codes[code] = code_data
        return code_data
    
    def verify_timering_code(self, code: str, access_time: Optional[datetime] = None) -> Dict[str, Any]:
        """
        Verify TimeRing Code against current time
        """
        if access_time is None:
            access_time = datetime.utcnow()
        
        if code not in self.active_codes:
            return {
                "verified": False,
                "reason": "CODE_NOT_FOUND",
                "action": "DENY_ACCESS"
            }
        
        code_data = self.active_codes[code]
        
        if not code_data["active"]:
            return {
                "verified": False,
                "reason": "CODE_DEACTIVATED",
                "action": "DENY_ACCESS"
            }
        
        # Check time window
        window_start = datetime.fromisoformat(code_data["access_window"]["start"])
        window_end = datetime.fromisoformat(code_data["access_window"]["end"])
        
        if window_start <= access_time <= window_end:
            return {
                "verified": True,
                "code_id": code_data["code_id"],
                "tote_id": code_data["tote_id"],
                "tote_class": code_data["tote_class"],
                "timestamp": access_time.isoformat(),
                "action": "GRANT_ACCESS"
            }
        else:
            # Outside time window - trigger purge
            violation = self.handle_time_violation(code, access_time)
            return {
                "verified": False,
                "reason": "OUTSIDE_TIME_RING",
                "action": "CODEX_PURGE_VAULT_RETURN",
                "violation": violation
            }
    
    def handle_time_violation(self, code: str, access_time: datetime) -> Dict[str, Any]:
        """
        Handle access outside TimeRing window
        Triggers: Codex Purge + Vault Return
        """
        code_data = self.active_codes[code]
        
        violation = {
            "event": "TIME_RING_VIOLATION",
            "timering_code": code,
            "tote_id": code_data["tote_id"],
            "attempted_access": access_time.isoformat(),
            "window_start": code_data["access_window"]["start"],
            "window_end": code_data["access_window"]["end"],
            "actions": []
        }
        
        # Codex Purge
        if code_data["purge_on_violation"]:
            violation["actions"].append({
                "type": "CODEX_PURGE",
                "status": "EXECUTED",
                "timestamp": datetime.utcnow().isoformat()
            })
        
        # Vault Return
        if code_data["vault_return_enabled"]:
            violation["actions"].append({
                "type": "VAULT_RETURN",
                "status": "INITIATED",
                "timestamp": datetime.utcnow().isoformat()
            })
        
        # Deactivate code
        code_data["active"] = False
        self.expired_codes.append(code_data)
        
        return violation
    
    def deactivate_code(self, code: str) -> bool:
        """
        Manually deactivate a TimeRing Code
        """
        if code in self.active_codes:
            self.active_codes[code]["active"] = False
            return True
        return False


if __name__ == "__main__":
    # Test TimeRing system
    tr = TimeRingCodeSystem()
    
    print("⏰ TimeRing Code System Test")
    print("=" * 50)
    
    # Generate code
    tote_id = "TOTE-TEST-001"
    tote_class = "ROYAL-TOTE"
    
    code_data = tr.generate_timering_code(tote_id, tote_class, window_minutes=60)
    print("✅ Generated TimeRing Code:")
    print(json.dumps(code_data, indent=2))
    print()
    
    # Test valid access
    print("Test 1: Access within time window")
    result = tr.verify_timering_code(code_data["timering_code"])
    print(json.dumps(result, indent=2))
    print()
    
    # Test invalid access (simulate future time)
    print("Test 2: Access outside time window")
    future_time = datetime.utcnow() + timedelta(hours=2)
    result = tr.verify_timering_code(code_data["timering_code"], future_time)
    print(json.dumps(result, indent=2))
    print()
    
    print("=" * 50)
    print("✅ TimeRing system operational")
