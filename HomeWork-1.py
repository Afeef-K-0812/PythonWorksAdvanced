# 1. Reverse the lines in a file

#f=open('text.txt','w')
#l=['red\n','blue\n','green\n','yellow\n','black\n']
#f.writelines(l)
#f.close()

#f=open('text.txt','r')
#s=f.readlines()
#rev=s[::-1]

#f=open('text.txt','w')
#f.writelines(rev)
#f.close()


# 2. A file totalstudents.txt contains the names of all students in a class, and a file passedstudents.txt contains the names of students who passed the exam.
  # Write a Python program to:
  # Read the names from both files.
  # Find the students who did not pass.
  # Write their names to a new file named failed_students.txt, one name per line.

#f=open('totalstudents.txt','w')
#l=['Arun\n','Amal\n','Anu\n','Rahul\n','Varsha\n','Veena\n']
#n=f.writelines(l)
#f.close()

#f=open('passedstudents.txt','w')
#l=['Arun\n','Anu\n','Rahul\n','Varsha\n']
#n=f.writelines(l)
#f.close()

#f=open('totalstudents.txt','r')
#s=f.readlines()
#print('total students',s)

#a=open('passedstudents.txt','r')
#p=a.readlines()
#print('passed students',p)

#b=open('failedstudents.txt','w')
#c=[]
#for i in s:
#    if i not in p:
#        c.append(i)
#b.writelines(c)
#print('failed students',c)


# 3. Two files, swiggy.txt and zomato.txt, contain the names of food items ordered from each platform.
  # Write a Python program to read words from swiggy.txt and zomato.txt, combine them, and count how many times each word appears. Store the result in a dictionary and print it

#s=open('swiggy.txt','w')
#l=['biriyani\n','shawarma\n','fried rice\n','noodles\n']
#s.writelines(l)
#s.close()

#z=open('zomato.txt','w')
#l=['fried rice\n','burger\n','shawarma\n']
#z.writelines(l)
#z.close()

#s=open('swiggy.txt','r')
#q=s.readlines()
#print(q)

#z=open('zomato.txt','r')
#w=z.readlines()
#print(w)

#f=q+w
#print(f)

#d={i:f.count(i) for i in f}
#print(d)


# 4. A file marks.txt contains the names and marks of students as shown below:
  # Anu 80
  # Rahul 65
  # Meera 90
  # Arun 70
  # Write a Python program to read the file and write the names of students who scored more than 75 marks into a file named names.txt.

#f=open('marks.txt','r')
#m=f.readlines()
#print(m)

#n=open('names.txt','w')

#for i in m:
#    l=i.split()
#    if int(l[1])>75:
#        n.write(l[0]+'\n')
