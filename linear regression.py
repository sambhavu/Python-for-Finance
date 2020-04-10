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
def run_linear_regression(data_x,data_y): 
     iterations = 100000
     alpha= 0.0001550
     no_featuers=data_x.shape[1]
     len_data=data_x.shape[0]-1
     theta=np.zeros((1,no_features))

     for i in range(0,iterations): 
           theta=run_steep_gradient_decent(data_x,data_y,len_data, alpha, theta) 
           error=sum_of_squares_error(data_x,data_y,len_data,theta) 

     return theta 

main(): 
    data=collect_dataset()
    len_data=data.shape[0]
    
    data_x=np.c_[np.ones(len_data),data[:,:-1]].astype(float) 
    data_y=data[:,-1].astype(float)

    theta=run_linear_regression(data_x,data_y)
    len_result=theta.shape[1]
    print("resultant feature vector: ")
    for i in range(0,len_result): 
           print("%.5f" % (theta[0,i]))

if __name__=="__main__":
     main() 


