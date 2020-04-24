import math

def bisection(function, a, b):
      start=a
      end=b
      if function(a)==0:
          return a
      elif function(b)==0:
          return b
      elif(function(a)*function(b)>0):
          print("could not find root")
          return 

      else:
          mid=start+(end-start)/2
          while(abs(start-mid)>10**-7):
             if function(mid)==0:
                  return mid
             elif function(mid)*function(start)<0:
                  end=mid
             else:
                  start=mid
             mid=start+(end-start)/2
          return mid

def f(x):
     return math.pow(x,3)-2*x-5



main():
    print(bisection(f,1,1000))




if __name__=="__main__":
    main()

