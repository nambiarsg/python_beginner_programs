mylist = [1,2,3,4,5,6,7,8,9,10]
#print all the values in the list
for y in mylist:
    print(y, end=',')
	
#modify some of the values in the list

mylist[2:5] = [20,21,22]

print('modified list')

for y in mylist:
    print(y)
