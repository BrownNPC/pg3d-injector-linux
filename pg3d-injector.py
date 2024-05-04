import subprocess
import os

import ssl

# Disable SSL certificate verification globally
ssl._create_default_https_context = ssl._create_unverified_context


#  pyinstaller fix?
env = dict(os.environ)  # make a copy of the environment
lp_key = 'LD_LIBRARY_PATH'  # for GNU/Linux and *BSD.
lp_orig = env.get(lp_key + '_ORIG')
if lp_orig is not None:
    print('using original')
    env[lp_key] = lp_orig  # restore the original, unmodified value
else:
    # This happens when LD_LIBRARY_PATH was not set.
    # Remove the env var as a last resort:
    env.pop(lp_key, None)



import protontricks as pt
import sys
from util import run_command
import dldll

# os.environ['WINEDEBUG'] = '-'

# Find Steam path and Steam library paths

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