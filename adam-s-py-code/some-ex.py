who = input("What type of person do you want to put in the story? ")
what = input("What do you want to fart on the person? ")
age = input("what is the persons age? ")
print ("one time an", who, "was walking somewhere and a big {} farted on them".format(what))
print ("and this is what happened do them")
if int(age) > 80 and int(age) <125:
    print("Wow too old, they couldn't handle the fart and they died!")
elif int(age) <= 80 and int(age) > 2:
    print("This person is okay, not too old or young")
elif int(age) < 2:
    print("too young they died from the fart!")
else:
    print("That person is too old to be real, come on now!")

