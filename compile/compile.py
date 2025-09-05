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
    
    # Check data files
    utils_dir = project_root / "utils"
    about_html = utils_dir / "about.html"
    file_details_toml = utils_dir / "file_details.toml"
    
    # Nuitka command
    cmd = [
        sys.executable, "-m", "nuitka",
        str(main_script),
        "--standalone",
        "--enable-plugin=pyside6",
        
        # Include entire utils directory - this is the key change
        f"--include-data-dir={utils_dir}=utils",
        
        # Output settings
        # "--output-dir=dist",
        "--output-filename=ArborescenceASCII",
        
        # Performance optimizations
        "--enable-plugin=anti-bloat",
        "--disable-plugin=tk-inter"
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
        
        # Check if utils directory was copied correctly
        dist_utils = project_root / "dist" / "ArborescenceASCII.dist" / "utils"
        if dist_utils.exists():
            print(f"✅ Utils directory found at: {dist_utils}")
        else:
            print("⚠️  Utils directory not found in expected location")
            
    else:
        print("❌ Compilation failed!")
    
    return result.returncode == 0

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)