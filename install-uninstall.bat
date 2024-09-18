@echo off
if not exist "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\womi-nuke" (
    mkdir "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\womi-nuke"
    copy "%~dp0womi-nuker.exe" "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\womi-nuke"
    powershell "$s=(New-Object -COM WScript.Shell).CreateShortcut('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\womi-nuker.lnk');$s.TargetPath='C:\ProgramData\Microsoft\Windows\Start Menu\Programs\womi-nuke\womi-nuker.exe';$s.Save()"
    start "" "%~dp0info-in.exe"
) else (
    if exist "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\womi-nuker.lnk" (
        del "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\womi-nuker.lnk"
    )
    rmdir /s /q "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\womi-nuke"
    start "" "%~dp0info-unin.exe"
)