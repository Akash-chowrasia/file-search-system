import os
#from .ColorPython import Color
def searching(search):
    l=os.listdir()
    temp=[]
    if search in l:
        return True
    for i in l:
        if os.path.isdir(i) == True:
            temp.append(i)
    if len(temp)==0:
        return False
    origindir=os.getcwd()
    for i in temp:
        os.chdir(i)
        t=searching(search)
        if t==True:
            return t
        os.chdir(origindir)
    else:
        return False

def searchfile(search):
    temp1=[]
    #os.chdir(os.path.join(os.environ['HOME']))
    list=os.listdir()
    if search in list:
        return True
    for i in list:
        if os.path.isdir(i) == True:
            temp1.append(i)
    if len(temp1)==0:
        return False
    originaldir=os.getcwd()
    for i in temp1:
        os.chdir(i)
        result=searching(search)
        if result == True:
            return True
        os.chdir(originaldir)
    else:
        return False

def main():
    file_to_search = input("Enter File Name To Search: ")
    result = searchfile(file_to_search)
    if result == True:
        print("File found at : ",os.getcwd())
    else:
        print("File Not Found")

if __name__ == '__main__':
    main()
