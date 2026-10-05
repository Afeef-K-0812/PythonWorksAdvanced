# 1. Write

#f=open('k.txt','w')
#f.write('hello')


#s=['python\n','java\n','php\n']
#f.writelines(s)


# 2. Read

#f=open('k.txt','r')
#content=f.read()
#print(content)

#f=open('k.txt','r')
#content=f.readlines()
#print(content)


# Write a program to read a text file and display the number of lines in a file

#f=open('k.txt','r')
#content=f.readlines()
#print(len(content))


# Write a program to display the number of words in a file

#f=open('k.txt','r')
#w=f.read()
#print(len(w.split()))


# Write a program to update the second line in a file

#f=open('k.txt','r')
#w=f.readlines()
#w[1]='z\n'

#f.close()

#f=open('k.txt','w')
#f.writelines(w)

#f.close()


# Write a program to display the last 5 lines in a file

# f=open('k.txt','r')
# a=f.readlines()
# print(a[-5:])


# Program to search a particular word in a file

#f=open('k.txt','r')
#b=f.read()
#n=input('Enter word ')
#if n in b:
#  print(' word found')
#else:
#  print('word not found')


# Find the number of letters,digits,and spaces in a file

#f=open('k.txt','r')
#a=f.read()
#lcount=0
#scount=0
#dcount=0
#for i in a:
#    if(i.isalpha()):
#        lcount+=1
#    elif(i.isdigit()):
#        dcount+=1
#    elif(i.isspace()):
#        scount+=1
#    else:
#        pass
#print('number of letters',lcount)
#print('number of digits',dcount)
#print('number of space',scount)


# 3. Append

#f=open('k.txt','a')
#f.write('python')


#s=open('p1.txt','r')
#q=s.read()

#f=open('k1.txt','a')
#d=f.write(q)


#f=open('k1.txt','a+')
#q=f.write('python')
#s=f.read()
#print(s)


#f=open('k1.txt','a+')

#print('current position',f.tell())
#f.write('python')
#print('current position',f.tell())

