#number of values you want in your hashmap
x=int(input())
#taking input 
phoneBook={}
for i in range(0,x):
    name=input('enter the name')
    phoneno=int(input('enter the phone number'))
    phoneBook[name]=phoneno
y=input('enter the name you want to search')
if y in phoneBook:
    print(phoneBook[y])
else:
    print('not found')

