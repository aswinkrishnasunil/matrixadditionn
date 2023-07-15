class A():
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("hello")




    def print (self):

        print("u got it",self.a,self.b)



def matrixadd():

    r=int(input("enter the row number:: "))
    c=int(input("enter the coloumn number:: "))
    
    print("enter the elements for matrix 1:: ")
    matrix1 = [[int(input()) for i in range(c)]for j in range(r)]
    print("matrix 1:: ")
    for i in range(r):
        for j in range(c):
            print(format(matrix1[i][j],"<3"),end="")
        print()

    print("enter the elements for matrix 2 :: ")
    matrix2 = [[int(input()) for i in range(c)]for j in range(r)]
    print("matrix 1 & 2 :: ")
    for i in range(r):
        for j in range(c):
            print(matrix1[i][j]," ",matrix2[i][j],end="  ")
        print()
    
    result=[[0 for i in range(c)]for j in range(r)]
    for i in range (r):
        for j in range (c):
            result[i][j]= matrix1[i][j] + matrix2[i][j]
    print("result")        

    for i in range (r):
        for j in range (c):
            print(format(result[i][j],"<3"),end="")
        print()   
matrixadd()
