@echo off

echo Sprawdzam istnienie folderu: C:\ProgramData\Microsoft\Windows\Start Menu\Programs\womi-nuke
if not exist "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\womi-nuke" (
    echo Folder nie istnieje. Tworzę folder...
    mkdir "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\womi-nuke"
    echo Kopiowanie plików do: C:\ProgramData\Microsoft\Windows\Start Menu\Programs\womi-nuke
    copy "%~dp0favicon.ico" "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\womi-nuke"
    copy "%~dp0womi-nuker.exe" "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\womi-nuke"
    echo Tworzenie skrótu do: C:\ProgramData\Microsoft\Windows\Start Menu\Programs\womi-nuker.exe
    powershell "$s=(New-Object -COM WScript.Shell).CreateShortcut('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\womi-nuker.lnk');$s.TargetPath='C:\ProgramData\Microsoft\Windows\Start Menu\Programs\womi-nuke\womi-nuker.exe';$s.Save()"
    echo Uruchamianie info-in.exe
    start "" "%~dp0info-in.exe"
) else (
    echo Folder istnieje. Usuwam folder i skrót...
    if exist "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\womi-nuker.lnk" (
        echo Usuwanie skrótu: C:\ProgramData\Microsoft\Windows\Start Menu\Programs\womi-nuker.lnk
        del "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\womi-nuker.lnk"
    )
    echo Usuwanie folderu: C:\ProgramData\Microsoft\Windows\Start Menu\Programs\womi-nuke
    rmdir /s /q "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\womi-nuke"
    echo Uruchamianie info-unin.exe
    start "" "%~dp0info-unin.exe"
)
exit