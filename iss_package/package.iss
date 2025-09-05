[Setup]
AppName=ArborescenceASCII
AppVersion=0.1
DefaultDirName={pf}\ArborescenceASCII
DefaultGroupName=ArborescenceASCII
OutputBaseFilename=ArborescenceASCII_Installer
Compression=lzma
SolidCompression=yes

[Files]
; Include all files from main.dist
Source: "C:\PythonProgrammingSylvain\ArborescenceASCII\ArborescenceASCII.dist\*"; DestDir: "{app}"; Flags: recursesubdirs createallsubdirs

[Icons]
Name: "{group}\ArborescenceASCII"; Filename: "{app}\ArborescenceASCII.exe"