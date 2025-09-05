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
    user_data_dir = project_root / "user_data"
    utils_dir = project_root / "utils"
    about_html = utils_dir / "about.html"
    file_details_toml = user_data_dir / "file_details.toml"
    
    # Nuitka command
    cmd = [
        sys.executable, "-m", "nuitka",
        str(main_script),
        "--standalone",
        "--enable-plugin=pyside6",
        #"--windows-disable-console", # for Windows
        # Include entire utils directory - this is the key change
        f"--include-data-dir={utils_dir}=utils",
        f"--include-data-dir={user_data_dir}=user_data",
        #include icon
        "--windows-icon-from-ico=graphics/icon.ico",
        
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
        print(f"📦 Output: {project_root}/ArborescenceASCII.dist")
        
        # Check if utils directory was copied correctly
        dist_utils = project_root / "ArborescenceASCII.dist" / "utils"
        if dist_utils.exists():
            print(f"✅ Utils directory found at: {dist_utils}")
        else:
            print("⚠️  Utils directory not found in expected location")
                # Check if utils directory was copied correctly
        dist_user_data = project_root / "ArborescenceASCII.dist" / "user_data"
        if dist_user_data.exists():
            print(f"✅ Utils directory found at: {dist_user_data}")
        else:
            print("⚠️  Utils directory not found in expected location")
    else:
        print("❌ Compilation failed!")
    
    return result.returncode == 0

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)