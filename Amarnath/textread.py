networking='C:\\Users\\hp\\Desktop\\python\\Python\\Amarnath\\networking.txt'
def count(networking):
    count=0
    with open(networking, 'r') as file:
        for line in file:
            count+=1
    return(count)
line=count(networking)
print(line)