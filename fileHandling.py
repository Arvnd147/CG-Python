# open(filename,mode)
# methods/mode: "r", "a", "w", "x": read, append, write, create
#"t" -> text mode, "b" -> binary mode(images)

#open a file
# return file object
f = open("fileHandling\demoFile.txt")

#read file
#print(f.read())
#print(open("fileHandling\demoFile.txt").read())
#print(f.readline())
print(f.read(5))

#write a file
f1 = open("fileHandling\demoFile2.txt","a")
f1.write("Now the file has some content")
f.close()

f1 = open("fileHandling\demoFile2.txt","r")
print(f1.read())

f2 = open("myfile.txt","x")

#remove file
import os
os.remove("demoFile.txt")

if os.path.exists("demoFile.txt"):
    os.remove("demoFile.txt")
else:
    print("The file does not exist")
    
#remove folder
os.rmdir("myfolder")
#we can remove only empty folders
