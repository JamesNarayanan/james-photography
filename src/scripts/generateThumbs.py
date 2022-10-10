import os
from PIL import Image


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


wd = os.path.dirname(os.path.realpath(__file__))
path = wd + "/../assets/fullsize/"
files = os.listdir(path)
files = [f for f in files if f.endswith(".jpeg")]

print(f"Deleting old thumbnails...", end="\r")
for file in os.listdir(path + "../thumbs/"):
    if file.endswith(".jpeg"):
        os.remove(path + "../thumbs/" + file)
print(f"Deleting old thumbnails... {bcolors.OKGREEN}Done{bcolors.ENDC}")

print(
    f"Generating thumbnails for {bcolors.OKCYAN}{len(files)}{bcolors.ENDC} files...")

for i, file in enumerate(files):
    img = Image.open(path + file)
    img.thumbnail((512, 512))
    img.save(path + "../thumbs/" + file)

    checks = "✓" * (i + 1)
    dots = "." * (len(files) - i - 1)
    print(
        f"Thumbnails Generated: {bcolors.OKGREEN}{checks}{bcolors.FAIL}{dots}{bcolors.ENDC}", end="\r")

print(f"\n{bcolors.OKGREEN}Done!{bcolors.ENDC}")
