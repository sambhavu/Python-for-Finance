fib <- function(n) { 
  
  
  stopifnot(n>0) 
  if(n == 1){ 
    0
  } else if (n==2) { 
    1
  } 

  else{ 
    fib(n -1 ) + fib(n -2 ) 
    
  } 
  

}
