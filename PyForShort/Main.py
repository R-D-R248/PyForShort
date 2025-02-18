import os

def CreateShortcut(*, name, path, target):
    path = path.replace("/", "\\")
    target = target.replace("/", "\\")
    
    if os.path.exists(path):
        if path[-1] == "\\":
            shortcut = path + name + ".lnk"
        else:
            shortcut = path + "\\" + name + ".lnk"
        
        os.system(f"powershell $s=(New-Object -COM WScript.Shell).CreateShortcut('{shortcut}');$s.TargetPath='{target}';$s.Save()")
    else:
        raise FileNotFoundError(f"Error: The location '{path}' is not valid.")
