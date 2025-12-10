#!/usr/bin/env python3
"""
SSOD - Scroll Sing-Off Defense System
Vocal authentication for TOTE access
"""

import json
import hashlib
from datetime import datetime
from typing import Dict, Any, Optional

class ScrollSingOffDefense:
    """
    Scroll Sing-Off Defense (SSOD)
    Every tote contains a single-syllable cipher - your Scroll Sing.
    If unauthorized hand grips tote, it demands vocal match.
    Failure = sonic detonation in mimic's hearing spectrum.
    """
    
    def __init__(self):
        self.authorized_signatures = {}
        self.failed_attempts = []
        
    def generate_scroll_sing(self, user_id: str, tote_id: str) -> str:
        """
        Generate a single-syllable cipher for Scroll Sing
        """
        # Create unique cipher based on user and tote
        combined = f"{user_id}:{tote_id}:{datetime.utcnow().isoformat()}"
        hash_value = hashlib.sha256(combined.encode()).hexdigest()[:8]
        
        # Convert to single-syllable format
        syllables = ["BLU", "PHI", "ZAR", "RAH", "VOX", "LUX", "REX", "MAX"]
        index = int(hash_value[:2], 16) % len(syllables)
        
        cipher = syllables[index]
        
        # Store authorized signature
        self.authorized_signatures[tote_id] = {
            "user_id": user_id,
            "cipher": cipher,
            "created_at": datetime.utcnow().isoformat()
        }
        
        return cipher
    
    def verify_vocal_match(self, tote_id: str, attempted_cipher: str) -> Dict[str, Any]:
        """
        Verify if attempted cipher matches authorized Scroll Sing
        """
        if tote_id not in self.authorized_signatures:
            return {
                "verified": False,
                "reason": "TOTE_NOT_REGISTERED",
                "action": "DENY_ACCESS"
            }
        
        authorized = self.authorized_signatures[tote_id]
        
        if attempted_cipher.upper() == authorized["cipher"]:
            return {
                "verified": True,
                "user_id": authorized["user_id"],
                "timestamp": datetime.utcnow().isoformat(),
                "action": "GRANT_ACCESS"
            }
        else:
            # Failed attempt - trigger sonic detonation
            self.failed_attempts.append({
                "tote_id": tote_id,
                "attempted_cipher": attempted_cipher,
                "timestamp": datetime.utcnow().isoformat()
            })
            
            return {
                "verified": False,
                "reason": "VOCAL_MISMATCH",
                "action": "SONIC_DETONATION",
                "detonation": self.trigger_sonic_detonation(tote_id)
            }
    
    def trigger_sonic_detonation(self, tote_id: str) -> Dict[str, Any]:
        """
        Trigger sonic detonation in mimic's hearing spectrum
        Ultra high-frequency burst to deter unauthorized access
        """
        detonation = {
            "event": "SONIC_DETONATION",
            "tote_id": tote_id,
            "frequency": "ULTRA_HIGH",
            "target": "MIMIC_HEARING_SPECTRUM",
            "intensity": "MAXIMUM",
            "timestamp": datetime.utcnow().isoformat(),
            "status": "ACTIVATED"
        }
        
        return detonation
    
    def get_tote_cipher(self, tote_id: str) -> Optional[str]:
        """
        Get the cipher for a specific tote (authorized users only)
        """
        if tote_id in self.authorized_signatures:
            return self.authorized_signatures[tote_id]["cipher"]
        return None


if __name__ == "__main__":
    # Test SSOD system
    ssod = ScrollSingOffDefense()
    
    print("🎤 SSOD - Scroll Sing-Off Defense Test")
    print("=" * 50)
    
    # Generate cipher for test tote
    user_id = "WARRIOR-001"
    tote_id = "TOTE-TEST-001"
    
    cipher = ssod.generate_scroll_sing(user_id, tote_id)
    print(f"✅ Generated Scroll Sing: {cipher}")
    print()
    
    # Test successful verification
    print("Test 1: Authorized access")
    result = ssod.verify_vocal_match(tote_id, cipher)
    print(json.dumps(result, indent=2))
    print()
    
    # Test failed verification
    print("Test 2: Unauthorized access (mimic)")
    result = ssod.verify_vocal_match(tote_id, "WRONG")
    print(json.dumps(result, indent=2))
    print()
    
    print("=" * 50)
    print("✅ SSOD system operational")
