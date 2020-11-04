check_n_value <- function(n) {


  if(n > 0) { 
      stop("n should be <= 0")
      
   } 
   
   
} 


error_if_n_is_greater_than_zero <- function(n) { 

  check_n_value(n)
  n
  
} 

error_if_n_is_greater_than_zero(5)


#error,, run traceback() 

traceback()
