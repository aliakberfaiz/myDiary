#Diary version 2.0
print "Hello Ali"
#first read then write
from datetime import datetime
date,time=str(datetime.now()).split(' ')
data=raw_input("What do you want to add \n")
#open for 'w'riting
f=open('diary.txt','a')
#write a txt in file
f.write('\t'+date+'\t'+time+'\n')
f.write(data+'\n')
#close the file
f.close()
