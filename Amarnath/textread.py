import numpy as np

networking='C:\\Users\\vamsi\\OneDrive\\Desktop\\python\\Python\\amarnath\\networking.txt'
def count(networking):

    count=0
    with open(networking, 'r') as file:
        for line in file:
            count+=1
    return(count)
def count1(networking,line):
    count=0
    with open(networking, 'r') as file:
        for curr,lines  in enumerate(file,start=1):
            if curr == line:
                return lines
    return None
           

   


line=count(networking)

print(line)
bas=np.random.randint(1,line)

print(bas)

var=count1(networking,bas)
print(var)

