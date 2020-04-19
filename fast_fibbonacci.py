import sys 

def fibonacci(n: int): 
     if n < 0: 
         raise ValueError("Negative numbers are not supported")
     return _fib(n)[0]


def _fib(n: int): 
      
     if n==0:
         return (0,1)
    
     else:
         a, b=_fib(n//2)
         c=a*(b*2-a)
         d=a*a+b*b
         if(n%2==0):
            return(c,d)
         else:
            return(d,c+d) 




if __name__=="__main": 
     args=sys.argv[1:]
     if len(args)!=1:
         print("Not enough parameters")
         exit(1)
     try:
         n=int(args[0])
     except ValueError:
         print("could not convert parameters")
         exit(1)
     print("F(%d) = %d"% (n,fibonnaci(n)))
