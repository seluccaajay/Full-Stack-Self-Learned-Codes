import os
source=r'C:\Users\sakrk\OneDrive\Desktop\Folder A'
destination=r'C:\Users\sakrk\OneDrive\Desktop\Folder B'
files=os.listdir(source)
for f in files:
    print(f)
    file=open(source+'\\'+f,'rb')
    var1=file.read()+
    file.close()
    Newfile=open(destination+'\\'+f,'wb')
    Newfile.write(var1)
    Newfile.close()