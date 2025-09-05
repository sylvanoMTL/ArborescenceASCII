import os
import sys

def get_resource_path(*path_parts):
    """Return absolute path to resource, works with Nuitka --standalone."""
    if getattr(sys, 'frozen', False):
        # Nuitka standalone: resources go into <exename>.dist/
        exe_dir = os.path.dirname(sys.executable)
        dist_dir = os.path.join(exe_dir, os.path.splitext(os.path.basename(sys.executable))[0] + ".dist")
        return os.path.join(dist_dir, *path_parts)
    else:
        # Normal Python run: relative to project root
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_dir, *path_parts)


def main():
    print(get_resource_path("utils", "file_details.toml"))

if __name__ == "__main__":
   main()