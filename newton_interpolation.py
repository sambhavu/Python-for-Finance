import math 

def ucal(u,p)
    temp=u
    for i in range (1,p): 
          temp = temp*(u-i) 

    return temp




def main():
    
   n=int(input("Enter number of values: ") 
   y=[]
   for i in range(n): 
        y.append([]) 
   for i in range(n): 
        for j in range (n): 
              y[i].append(j)
              y[i][j]=0


   print("Enter values in list")
   x=list(map(int, input().split()))
   print("Enter Values of parameters")
   for i in range(n):
        y[i][0]=float(input())
   
   value=input(int("Enter value to interpolate")
   u=(value-x[0])/(x[1]-x[0])



   for i in range(1,n): 
        for j in range(n-1):
             y[j][i]=y[j+1][i-1]-y[j][i-1]


    sum=y[0][0]
    for i in range(1,n): 
         summ+= ucalc(u,i) * y[0][i] /math.factorial(i)




    print(f"Value at {value} is {summ}")


if __name__== "_main__":
     main() 
