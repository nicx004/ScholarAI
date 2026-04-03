#!/usr/bin/env python3
"""Download all scholarships from Supabase to restore JSON file"""

import os
import sys
import json
from pathlib import Path

# Add backend path
sys.path.insert(0, str(Path(__file__).parent / "backend"))

from services.supabase_service import supabase

print("=" * 70)
print("📥 DOWNLOADING SCHOLARSHIPS FROM SUPABASE")
print("=" * 70)

try:
    # Get all scholarships from Supabase, ordered by ID
    result = supabase.table('scholarships').select('*').order('id').execute()
    
    if result.data:
        scholarships = []
        for record in result.data:
            # Reconstruct the scholarship object
            scholarship = {
                "id": record['id'],
                "raw_data": record.get('raw_json', {}).get('raw_data', {}),
                "structured_criteria": {
                    "scholarship_name": record['scholarship_name'],
                    "min_gpa": record['min_gpa'],
                    "max_gpa": record['max_gpa'],
                    "eligible_majors": record['eligible_majors'] or [],
                    "deadline": record['deadline'],
                    "amount": float(record['amount']) if record['amount'] else None,
                    "location": record['location'],
                    "eligible_years": record['eligible_years'] or [],
                    "ethnicity": record['ethnicity'],
                    "gender": record['gender'],
                    "citizenship": record['citizenship'],
                    "age_limit": record['age_limit'],
                    "membership_required": record['membership_required'],
                    "min_income": record['min_income'],
                    "max_income": record['max_income'],
                    "restrictions": record['restrictions'],
                    "link": record['link']
                }
            }
            scholarships.append(scholarship)
        
        # Save to JSON
        with open('scholarships_structured.json', 'w', encoding='utf-8') as f:
            json.dump(scholarships, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Downloaded {len(scholarships)} scholarships from Supabase")
        print(f"   IDs: {scholarships[0]['id']} to {scholarships[-1]['id']}")
        print(f"   Saved to: scholarships_structured.json")
        
    else:
        print("⚠️ No scholarships found in Supabase")
        
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()

print("=" * 70)
