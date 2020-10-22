girls = int(input("Girls coming to the party: "))
boys = int(input("Boys coming to the party: "))

if girls == boys and girls + boys >= 20:
    print("The party is excellent!")
elif girls != boys and girls + boys > 20:
    print("Quite cool party!")
elif girls > 0 and girls + boys < 20:
    print("Average party...")
elif girls == 0 and boys > 0:
    print("Sausage party")
