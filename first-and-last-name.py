n = input("Write your name: ").strip()
name = n.split()
if len(name) > 1:
    print("Your first name is: {}".format(name[0]))
    print("And your last name is: {}".format(name[-1]))

elif len(name) == 1:
    print("Your name is: {}".format(name[0]))