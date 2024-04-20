my_list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

for i in my_list:
    if i % 2 == 0:
        print(i)

for  i in my_list:
    if i % 5 == 0 and i > 0:
        print(i)

sum = 0
for i in my_list:
    sum = sum + i 
print(sum)

sum = 0 
for i in my_list:
    if i % 2 == 0:
        sum = sum + i
print(sum)

new_list = []
for i in my_list:
    if i % 2 == 1:
        print(i)
        
new_list = []
for i in my_list:
    if i % 3 == 0 and i == 0 and i > 0:
        new_list.append(i)
        print(new_list)
