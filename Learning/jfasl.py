import os, shutil

current = "C:\\Foderking\\SMLoadr-win-x64_v1.9.5\\DOWNLOADS\\Timbaland"
os.chdir("C:\\Users\\Foderking\\Downloads\\Timbo")

for i in os.listdir():
    if len(os.listdir(i)) == 1:
        folder = os.listdir(i)[0]
        new = os.path.join(os.path.abspath(i), folder)
        # print(os.path.abspath(folder))
        moved = shutil.move(new,current)
        # print(f'{moved} moved')