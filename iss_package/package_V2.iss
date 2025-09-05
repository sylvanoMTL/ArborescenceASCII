[Setup]
AppName=ArborescenceASCII
AppVersion=0.1
AppPublisher=Sylvain Boyer
AppPublisherURL=https://www.the-frog.fr
DefaultDirName={autopf}\ArborescenceASCII
DefaultGroupName=ArborescenceASCII
OutputBaseFilename=ArborescenceASCII_Installer
Compression=lzma
SolidCompression=yes
SetupIconFile=graphics\icon.ico
UninstallDisplayIcon={app}\ArborescenceASCII.exe
UninstallDisplayName=ArborescenceASCII
ArchitecturesAllowed=x64
ArchitecturesInstallIn64BitMode=x64
PrivilegesRequired=lowest
DisableProgramGroupPage=yes

[Files]
; Copy everything from Nuitka dist folder into the program folder
Source: "ArborescenceASCII.dist\*"; DestDir: "{app}"; Flags: recursesubdirs createallsubdirs ignoreversion

; Copy configuration and resource files to the app directory (same level as exe)
Source: "file_details.toml"; DestDir: "{app}"; Flags: ignoreversion
Source: "about.html"; DestDir: "{app}"; Flags: ignoreversion

; Copy icon file for reference (optional, since it's embedded in exe)
Source: "graphics\icon.ico"; DestDir: "{app}\graphics"; Flags: ignoreversion

[Icons]
; Start Menu shortcut with icon
Name: "{group}\ArborescenceASCII"; Filename: "{app}\ArborescenceASCII.exe"; IconFilename: "{app}\ArborescenceASCII.exe"; IconIndex: 0

; Desktop shortcut with icon
Name: "{commondesktop}\ArborescenceASCII"; Filename: "{app}\ArborescenceASCII.exe"; IconFilename: "{app}\ArborescenceASCII.exe"; IconIndex: 0; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Create a &desktop icon"; GroupDescription: "Additional icons:"; Flags: unchecked

[Run]
; Optional: Launch the application after installation
Filename: "{app}\ArborescenceASCII.exe"; Description: "Launch ArborescenceASCII"; Flags: nowait postinstall skipifsilent

[UninstallDelete]
; Clean up any files created by the application
Type: files; Name: "{app}\*.log"
Type: files; Name: "{app}\*.tmp"