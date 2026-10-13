[Setup]
AppName=ResumeBuilder
AppVersion=1.0.0
AppPublisher=ResumeBuilder
DefaultDirName={autopf}\ResumeBuilder
DefaultGroupName=ResumeBuilder
OutputDir=installer
OutputBaseFilename=ResumeBuilder_Setup
SetupIconFile=logo.ico
Compression=lzma2
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=admin
UninstallDisplayName=ResumeBuilder
CreateUninstallRegKey=yes
ChangesEnvironment=no

[Files]
Source: "dist\ResumeBuilder.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\ResumeBuilder"; Filename: "{app}\ResumeBuilder.exe"
Name: "{commondesktop}\ResumeBuilder"; Filename: "{app}\ResumeBuilder.exe"

[Run]
Filename: "{app}\ResumeBuilder.exe"; Description: "启动 ResumeBuilder"; Flags: nowait postinstall skipifsilent
