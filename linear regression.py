import requests 
import numpy as np 

def collect_dataset(): 
    
     response=requests.get() 
     lines = response.text.splitlines() 
     data =[]
     for item in lines: 
          item = item.split(",")  
          data.append(item) 

      data.pop(0)
      dataset=np.matrix(data)
      return dataset 

def run_steep_gradient_decent(data_x, data_y, len_data, alpha, theta): 
     n=len_data 
     prod=np.dot(theta,data_x.transpose())
     prod-=data_y.transpose()
     sum_grad=np.dot(prod,data_x) 
     theta = theta-(alpha/n)*sum_grad 
     return theta 

def sum_of_square_error(data_x,data_y,len_data,theta): 
     prod=np.dot(theta,data_x.transpose())
     prod-=data_y.transpose() 
     sum_elem=np.sum(np.square(prod))
     error=sum_elem/(2*len_data) 
     return error 

