import os
import zipfile
import shutil

user = os.getlogin()
file = "VSCode-darwin-universal.zip"
destination = f"/Users/{user}/Applications"
chemin_zip = f"/Users/{user}/Applications/{file}"

if not os.path.exists(destination):
    os.makedirs(destination)
    print(f"Le répertoire {destination} a été créé avec succès.")
else:
    print(f"Le répertoire {destination} existe déjà.")

os.system(f"curl https://vscode.download.prss.microsoft.com/dbazure/download/stable/af28b32d7e553898b2a91af498b1fb666fdebe0c/VSCode-darwin-universal.zip --output VSCode-darwin-universal.zip")

shutil.move(file, destination)

os.system(f"unzip {chemin_zip}")

os.system(f"mv /Users/{user}/Visual\ Studio\ Code.app /Users/{user}/Applications")

# Correction de la commande curl pour télécharger get-pip.py et installation de pip
os.system("curl https://bootstrap.pypa.io/pip/2.7/get-pip.py -o get-pip.py && python get-pip.py --user")

os.system(f"rm /Users/{user}/Applications/{file}")
os.system(f"rm /Users/{user}/get-pip.py")
