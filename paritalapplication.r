library(purrr)

mult_three_n <- function(x, y, z) { 
  x*y*z
  
  
} 


mult_by_15 <- partial(mult_three_n, x = 3, y = 5)

mult_by_15(z=4) 

