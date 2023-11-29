phonebook = {}
n = int(input())

for _ in range(n):
    input_value = input()
    parts = input_value.split()
    phonebook[parts[0]] = parts[1]
for _ in range(n):
    j = input()

    if j in phonebook:
        print(f"{j}={phonebook[j]}")
    else:
        print("Not found")
