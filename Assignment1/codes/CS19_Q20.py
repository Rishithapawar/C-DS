import random

count = 0
for i in range(25):
    array =  random.sample(range(1, 26), 25)
    #print(array)
    #print("\n")
    n = random.randint(0,24) 
    #print(n)
    if array[n] == min(array) or array[0]==max(array):
        count = count+1
#print(count)
print(count/25)
