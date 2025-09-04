import os
import sys
import subprocess
from pathlib import Path

def main():
    print("🔨 Compiling ArborescenceASCII with Nuitka...")
    
    # Set up paths
    compile_dir = Path(__file__).parent
    project_root = compile_dir.parent
    main_script = project_root / "src" / "ArborescenceASCII.py"
    
    # Check if main script exists
    if not main_script.exists():
        print(f"❌ Main script not found: {main_script}")
        return False
    
    # Nuitka command
    cmd = [
        sys.executable, "-m", "nuitka",
        str(main_script),
        "--standalone",
        "--enable-plugin=pyside6",
        "--disable-console",
        
        # Include data files
        f"--include-data-files={project_root}/utils/about.html=utils/about.html",
        f"--include-data-files={project_root}/utils/file_details.toml=utils/file_details.toml",
        
        # Output settings
        "--output-dir=dist",
        "--output-filename=ArborescenceASCII"
    ]
    
    print("📄 Command:")
    print(" ".join(cmd))
    print()
    
    # Run compilation
    print("🚀 Starting compilation...")
    result = subprocess.run(cmd, cwd=project_root)
    
    if result.returncode == 0:
        print("✅ Compilation successful!")
        print(f"📦 Output: {project_root}/dist/")
    else:
        print("❌ Compilation failed!")
    
    return result.returncode == 0

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)