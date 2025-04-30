f=open("mahesh.txt",'r')
data=f.read()


line=data.splitlines()
words=data.split()
spaces=data.count(" ")
charc=len(data)-spaces
print('Line number::',len(line))
print('Word number::',len(words))
print('spaces::', spaces)
print('characters::', charc)
f.close()
# Compare this snippet from file01.py:
# f=open("file.txt",'r')