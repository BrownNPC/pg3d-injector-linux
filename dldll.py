import urllib.request
import json
import os

def download_latest_release(repo_owner, repo_name, save_dir, filename='PixelGunCheat.dll'):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest"
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read())
        version = data['tag_name']
        download_url = data['assets'][0]['browser_download_url']  
        file_name = filename
        urllib.request.urlretrieve(download_url, file_name)
        return version

def check_and_download(repo_owner, repo_name, save_dir):
    version_file = os.path.join(save_dir, f"{repo_name}_version.txt")
    if os.path.exists(version_file):
        with open(version_file, 'r') as f:
            saved_version = f.read().strip()
    else:
        saved_version = None

    latest_version = download_latest_release(repo_owner, repo_name, save_dir)

    if saved_version != latest_version:
        with open(version_file, 'w') as f:
            f.write(latest_version)
        print(f"New version available: {latest_version}, downloading...")
        download_latest_release(repo_owner, repo_name, save_dir)
    else:
        print("You have the latest version.")


# Replace these variables with your repository owner, repository name, and the path where you want to save the downloaded file
repo_owner = "BKUC-Development"
repo_name = "BKUC"
save_dir = "./"


check_and_download(repo_owner, repo_name, save_dir)
# check_and_download('nefarius', 'Injector', './')
def download_injector():
    if os.path.exists('Injector.exe'):
        return True
    url = 'https://github.com/BrownNPC/pg3d-injector-linux/raw/1/Injector.exe'

    urllib.request.urlretrieve(url, 'Injector.exe')

download_injector()