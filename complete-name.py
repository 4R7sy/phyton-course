name = input("Write your complete name: ").strip()
print(name.upper())
print(name.lower())
print(len(name) - name.count(" "))
firstName = name.split()
print(firstName[0])