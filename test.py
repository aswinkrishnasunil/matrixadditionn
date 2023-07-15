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







def matrixmul():
    """
    logic :: (p, q, n) p: rows of first matrix 
    q: coloumns of second matrix
    (p = q)

    matrix1 = p x n
    matrix2=  n x q
    result =  p x q

    """
    p =int(input("enter the number of rows in matrix one:: "))
    q= int(input("enter the number of columns in matrix two:: "))
    n= int(input("enter the coloumns of matrix1/rows of matrix2:: "))

    if p == q:
        print("enter elements for matrix one:: ")
    
        matrix1=[[int(input())for i in range (n)]for j in range (p)]

        print("matrix one is here ::  ")

        for i in range(p):
            for j in range(n):
                print(format(matrix1[i][j],"<3"),end="")

            print()

        print("enter elements for matrix two:: ")
    
        matrix2=[[int(input())for i in range (q)]for j in range (n)]

        print("matrix two is here ::  ")

        for i in range(n):
            for j in range(q):
                print(format(matrix2[i][j],"<3"),end="")

            print()
        result=[[0 for i in range(q)]for j in range(p)]



        print ("result:: ")

        for i in range(p):
            for j in range (q):
                for k in range (n):
                    result[i][j] = result[i][j] + matrix1[i][k] * matrix2[k][j]

        for i in range(p):
            for j in range(q):
                print(format(result[i][j],"<5"),end="")
            print()

                 


    else:
        print("error")
        print("REMINDER::row of matrix one should equal to coloumns of matrix two")
    



matrixmul()
