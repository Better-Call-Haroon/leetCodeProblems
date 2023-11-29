phonebook = {}
print("How many numbers do you want to save in a phonebook")
n = int(input())

for _ in range(n):
    input_value = input()
    parts = input_value.split()
    phonebook[parts[0]] = parts[1]

print("Whose phone number do you want?")
j = input()

if j in phonebook:
    print(phonebook[j])
else:
    print("Record not found")
