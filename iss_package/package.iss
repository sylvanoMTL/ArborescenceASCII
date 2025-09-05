[Setup]
AppName=ArborescenceASCII
AppVersion=0.1
DefaultDirName={pf}\ArborescenceASCII
DefaultGroupName=ArborescenceASCII
OutputBaseFilename=ArborescenceASCII_Installer
Compression=lzma
SolidCompression=yes


[Files]
; Copy everything from Nuitka dist folder into the program folder
Source: "C:\PythonProgrammingSylvain\ArborescenceASCII\ArborescenceASCII.dist\*"; \
    DestDir: "{app}"; \
    Flags: recursesubdirs createallsubdirs ignoreversion

; Copy the TOML config file into {app}\utils
Source: "C:\PythonProgrammingSylvain\ArborescenceASCII\user_data\file_details.toml"; \
    DestDir: "{app}\user_data"; Flags: ignoreversion

; Copy about.html into {app}\utils
Source: "C:\PythonProgrammingSylvain\ArborescenceASCII\utils\about.html"; \
    DestDir: "{app}\utils"; Flags: ignoreversion

; Copy icon.ico into {app}\graphics
Source: "C:\PythonProgrammingSylvain\ArborescenceASCII\graphics\icon.ico"; \
    DestDir: "{app}\graphics"; Flags: ignoreversion


    
[Icons]
; Start Menu shortcut
Name: "{group}\ArborescenceASCII"; Filename: "{app}\ArborescenceASCII.exe"
; Optional desktop shortcut
Name: "{commondesktop}\ArborescenceASCII"; Filename: "{app}\ArborescenceASCII.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Create a &desktop icon"; GroupDescription: "Additional icons:"





