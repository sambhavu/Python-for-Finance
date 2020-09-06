import random 

class Point: 

    def __init__ (self, x: float, y: float) -> None: 
        self.x = x 
        self.y = y
        
        
    def is_in_unit_circle(self) -> bool: 
        return(self.x ** 2 + self.y**2) <= 1
        
        
    def random_unit_square(cls): 
         return cls(x=random.random(), y = random.random()) 
         
         
         
def estimate_pi(number_of_simulations: int) -> float: 
    if number_of_simulations < 1: 
        raise ValueError("At least one simulation is necessary to estimate PI. ") 
        
        
    number_in_unit_circle = 0
    for simulation_index in range(number_of_simulations): 
        random_point = Point.random_unit_square() 
        
        if random_point.is_in_unit_circle(): 
            
            number_in_unit_circle += 1
            
            
    return 4 * number_in_unit_circle / number_of_simulations 
    
    
if __name__ == "__main__": 
    from math import pi 
    
    prompt = "Please enter the desired number of monte carlo simulations: " 
    my_pi = estimate_pi(int(input(prompt).strip())) 
    print("An esitmate of PI is {my_pi} with an error of {abs(my_pi - pi)}" ) 
    
    
    
