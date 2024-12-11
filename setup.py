import os
import shutil

def setup_project():
    # Create directory structure
    directories = [
        'assets/icons',
        'scripts',
        'ui',
        'utils',
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        # Create __init__.py files
        if directory not in ['assets/icons']:
            with open(f"{directory}/__init__.py", 'w') as f:
                pass

    # Create placeholder icon if it doesn't exist
    if not os.path.exists('assets/icons/agenda_icon.ico'):
        print("Warning: agenda_icon.ico not found in assets/icons/")

    print("Project structure created successfully!")

if __name__ == "__main__":
    setup_project() 