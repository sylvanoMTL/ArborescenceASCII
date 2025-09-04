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
    
    # Check if required data files exist
    utils_dir = project_root / "utils"
    about_html = utils_dir / "about.html"
    file_details_toml = utils_dir / "file_details.toml"
    
    if not about_html.exists():
        print(f"⚠️  Warning: about.html not found at {about_html}")
    if not file_details_toml.exists():
        print(f"⚠️  Warning: file_details.toml not found at {file_details_toml}")
    
    # Nuitka command
    cmd = [
        sys.executable, "-m", "nuitka",
        str(main_script),
        "--standalone",
        "--enable-plugin=pyside6",
        "--disable-console",
        
        # Include data files only if they exist
        f"--include-data-files={about_html}=utils/about.html",
        f"--include-data-files={file_details_toml}=utils/file_details.toml",
        
        # Include entire utils directory to be safe
        f"--include-data-dir={utils_dir}=utils",
        
        # Output settings
        "--output-dir=dist",
        "--output-filename=ArborescenceASCII",
        
        # Performance optimizations
        "--enable-plugin=anti-bloat",
        "--disable-plugin=tk-inter"
    ]
    
    print("📄 Command:")
    print(" ".join(cmd))
    print()
    
    # Show project structure
    print("📁 Project structure:")
    print(f"   Source: {main_script}")
    print(f"   Utils: {utils_dir}")
    print(f"   Output: {project_root}/dist/")
    print()
    
    # Run compilation
    print("🚀 Starting compilation...")
    result = subprocess.run(cmd, cwd=project_root)
    
    if result.returncode == 0:
        print("✅ Compilation successful!")
        print(f"📦 Output: {project_root}/dist/")
        
        # Check if executable was created
        dist_dir = project_root / "dist"
        exe_files = list(dist_dir.glob("**/ArborescenceASCII*"))
        if exe_files:
            print(f"🎯 Executable: {exe_files[0]}")
    else:
        print("❌ Compilation failed!")
        print("💡 Common fixes:")
        print("   - Ensure Nuitka is installed: pip install nuitka")
        print("   - Check that PySide6 is installed: pip install pyside6")
        print("   - Verify all imports in your Python files")
    
    return result.returncode == 0

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)