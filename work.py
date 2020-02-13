import os,glob
os.chdir("D:/Users/ashwnaya/Downloads")
for file in glob.glob("*.jpg"):
    print(file)