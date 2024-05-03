import subprocess
import protontricks as pt
import sys
from util import run_command
from dldll import check_and_download

# os.environ['WINEDEBUG'] = '-'

# Find Steam path and Steam library paths

check_and_download("stanuwu", "PixelGunCheatInternal", "./")
def inject_dll():
    path = pt.find_steam_path()[-1]
    libs_path = pt.get_steam_lib_paths(path)

    # Get Steam apps
    apps = pt.get_steam_apps(steam_path=path, steam_lib_paths=libs_path, steam_root=path)

    # find pg3d 
    for app in apps: 
        if app.appid == 2524890:
            pg3d=app

    # Find Proton directory
    proton_app = pt.find_steam_compat_tool_app(path, appid=2524890, steam_apps=apps)


    process=pt.run_command(winetricks_path='',use_bwrap=False, proton_app=proton_app, steam_app=pg3d,  command='wine Injector.exe -i ./PixelGunCheat.dll -n "Pixel Gun 3D.exe"', use_steam_runtime=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    # output, error = process.communicate()
    # process.wait()
    if process ==0:
        return True
    else:
        # shutdown program
        sys.exit(1)


inject_dll()