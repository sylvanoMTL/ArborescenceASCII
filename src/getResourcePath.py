import os, sys


def get_resource_path(*path_parts):
    """Return absolute path to resource, works with Nuitka + Inno installer."""
    exe_dir = os.path.dirname(sys.executable)
    full_path = os.path.join(exe_dir, *path_parts)
    if os.path.exists(full_path):
        print(f"Frozen/Installed executable run, Using exe_dir path: {full_path}")
        return full_path

    # fallback: normal python run
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    fallback_path = os.path.join(base_dir, *path_parts)
    print(f"Normal python run, Using fallback path: {fallback_path}")
    return fallback_path


# Usage
if __name__ == "__main__":
    # print(get_resource_path("user_data", "file_details.toml"))
    print(get_resource_path())