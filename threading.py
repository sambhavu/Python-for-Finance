import threading



def add(num1, num2):
    sum =  num1 + num2
    print(sum)

def main():
    adder = threading.Thread(target = add(2,3))
    adder.start()



main()
