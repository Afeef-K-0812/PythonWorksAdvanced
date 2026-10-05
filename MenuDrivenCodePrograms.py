# Menu Driven Code

def file_read():
    file_name=input('Enter File Name ')
    f=open(file_name,'r')
    content=f.read()
    print(content)

def file_write():
    file_name=input('Enter File Name ')
    content=input('Enter the content to write ')
    f=open(file_name,'w')
    f.write(content)

def file_append():
    file_name=input('Enter File Name ')
    content=input('Enter the content to append ')
    f=open(file_name,'a')
    f.write(content)

def file_search():
    file_name=input('Enter File Name ')
    word=input('Enter the word to search ')
    f=open(file_name,'r')
    s=f.read()
    if word in s:
        print('Word Found')
    else:
        print('Word Not Found')

def file_remove():
    file_name=input('Enter File Name To Remove ')
    import os
    os.remove(file_name)
    print('File',file_name,'Removed')

while(1):
    print('Menu Driven File Operations')
    print('1. File Read')
    print('2. File Write')
    print('3. File append')
    print('4. File Search')
    print('5. File Remove')
    print('6. Exit')

    ch=int(input('Enter Your Choice '))

    if ch==1:
        file_read()

    elif ch==2:
        file_write()

    elif ch==3:
        file_append()

    elif ch==4:
        file_search()

    elif ch==5:
        file_remove()

    else:
        exit()