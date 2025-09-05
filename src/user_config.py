from pathlib import Path
import shutil
import sys
from appdirs import user_data_dir
from getResourcePath import get_resource_path

APP_NAME = "ArborescenceASCII"
APP_AUTHOR = "MecaFrog"

def get_user_toml():
    """Return path to user-editable TOML in %APPDATA%. Copies default if missing."""
    
    # 1 Determine user folder in %APPDATA%
    user_dir = Path(user_data_dir(APP_NAME, APP_AUTHOR,roaming=True))
    user_dir.mkdir(parents=True, exist_ok=True)  # Creates folder if missing
    
    toml_file = user_dir / "file_details.toml"

    # 2 If the file doesn't exist yet, copy the default template
    if not toml_file.exists():
        # Determine where the default template lives
        if getattr(sys, "frozen", False):
            exe_dir = Path(sys.executable).parent
            default_file = exe_dir / "user_data" / "file_details.toml"
        else:
            default_file = Path(get_resource_path("user_data", "file_details.toml"))

        # Copy default TOML to %APPDATA%
        if default_file.exists():
            shutil.copy(default_file, toml_file)
        else:
            toml_file.write_text("")  # fallback: empty file

    # 3 Return path to the user-editable TOML in %APPDATA%
    return toml_file
