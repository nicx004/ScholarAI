"""
Organize LLM Scholarship Tracker into proper folder structure
Run this before pushing to GitHub!
"""

import os
import shutil
from pathlib import Path

def create_folder_structure():
    """Create all necessary folders"""
    folders = [
        'backend',
        'backend/models',
        'backend/routes',
        'backend/services',
        'backend/utils',
        'scripts',
        'tests',
        'data',
        'docs'
    ]
    
    for folder in folders:
        Path(folder).mkdir(parents=True, exist_ok=True)
        print(f"✅ Created: {folder}/")
        
        # Create __init__.py for Python packages
        if 'backend' in folder:
            init_file = Path(folder) / '__init__.py'
            if not init_file.exists():
                init_file.write_text('"""Package initialization"""\n')
                print(f"   Added: {init_file}")

def move_files():
    """Move files to appropriate folders"""
    file_moves = {
        # Backend files
        'app.py': 'backend/app.py',
        'config.py': 'backend/config.py',
        
        # Routes
        'backend/routes/eligibility_routes.py': 'backend/routes/eligibility_routes.py',
        'backend/routes/scholarship_routes.py': 'backend/routes/scholarship_routes.py',
        'backend/routes/user_routes.py': 'backend/routes/user_routes.py',
        
        # Services
        'backend/services/megallm_service.py': 'backend/services/megallm_service.py',
        'backend/services/supabase_service.py': 'backend/services/supabase_service.py',
        
        # Utils
        'backend/utils/pdf_parser.py': 'backend/utils/pdf_parser.py',
        
        # Scripts
        'batch_processor.py': 'scripts/batch_processor.py',
        'sync_to_supabase.py': 'scripts/sync_to_supabase.py',
        'process_first_90.py': 'scripts/process_first_90.py',
        'resume_processing.py': 'scripts/resume_processing.py',
        'check_progress.py': 'scripts/check_progress.py',
        
        # Tests
        'test_models.py': 'tests/test_models.py',
        
        # Data
        'scholarships_structured.json': 'data/scholarships_structured.json',
        'extraction_structure.py': 'scripts/extraction_structure.py',
        'extraction_processor.py': 'scripts/extraction_processor.py',
    }
    
    moved_count = 0
    for source, destination in file_moves.items():
        if os.path.exists(source):
            # Create parent directory if needed
            Path(destination).parent.mkdir(parents=True, exist_ok=True)
            
            # Move file (skip if already in place)
            if source != destination:
                try:
                    shutil.move(source, destination)
                    print(f"📦 Moved: {source} → {destination}")
                    moved_count += 1
                except Exception as e:
                    print(f"⚠️  Skip: {source} ({e})")
    
    print(f"\n✅ Moved {moved_count} files")

def create_readme_in_folders():
    """Create README.md in each major folder"""
    readmes = {
        'backend/README.md': '# Backend\n\nFlask application with API endpoints and business logic.',
        'backend/models/README.md': '# Models\n\nPydantic models for data validation.',
        'backend/routes/README.md': '# Routes\n\nAPI route handlers (Flask blueprints).',
        'backend/services/README.md': '# Services\n\nBusiness logic and external service integrations.',
        'scripts/README.md': '# Scripts\n\nData processing and utility scripts.',
        'tests/README.md': '# Tests\n\nUnit and integration tests.',
        'data/README.md': '# Data\n\nJSON files and datasets.',
        'docs/README.md': '# Documentation\n\nProject documentation and guides.'
    }
    
    for filepath, content in readmes.items():
        path = Path(filepath)
        if not path.exists():
            path.write_text(content)
            print(f"📝 Created: {filepath}")

def show_structure():
    """Display the new folder structure"""
    print("\n" + "="*50)
    print("📂 NEW FOLDER STRUCTURE")
    print("="*50)
    
    for root, dirs, files in os.walk('.'):
        # Skip hidden and cache folders
        if any(skip in root for skip in ['.git', '__pycache__', 'venv', 'node_modules']):
            continue
            
        level = root.replace('.', '').count(os.sep)
        indent = ' ' * 2 * level
        print(f"{indent}📁 {os.path.basename(root)}/")
        
        subindent = ' ' * 2 * (level + 1)
        for file in sorted(files)[:5]:  # Show first 5 files
            print(f"{subindent}📄 {file}")
        if len(files) > 5:
            print(f"{subindent}   ... and {len(files)-5} more files")

if __name__ == '__main__':
    print("🚀 Starting repository organization...\n")
    
    # Step 1: Create folders
    print("Step 1: Creating folder structure...")
    create_folder_structure()
    
    # Step 2: Move files
    print("\nStep 2: Moving files to folders...")
    move_files()
    
    # Step 3: Create README files
    print("\nStep 3: Creating README files...")
    create_readme_in_folders()
    
    # Step 4: Show result
    show_structure()
    
    print("\n" + "="*50)
    print("✅ ORGANIZATION COMPLETE!")
    print("="*50)
    print("\nNext steps:")
    print("1. Review the changes")
    print("2. Run: git add .")
    print("3. Run: git commit -m 'Organize project structure'")
    print("4. Run: git push origin main")
