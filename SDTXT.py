f=open('diary.txt')
while True:
    line=f.readline()
    if len(line)==0:
        break
    print(line)
#close the file
f.close
input("\n\n\npress any key to exit")
