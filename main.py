import generator
import binaryutils as bu
while True:
    print("Hello welcome to the program, Choose one of the following programs from the list")
    print("1.Add a new password","\n2.Display existing lists of passwords","\n3.Delete a password",
          "\n4.Quit the program")
    x = int(input("Enter choice: "))
    if x == 1:
        maxlen = int(input("Enter length of password:"))
        domain = input("Enter domain name:")
        acc = input("Enter account name:")
        pwd = generator.passgen(maxlen)
        if acc != "None":
            bu.addpass(pwd,domain,acc)
        else:
            bu.addpass(pwd,domain)
    elif x == 2:
        assign = input("Type assigned if passwords are stored")
        if assign == "Unassigned":
            bu.displaypass()
        else:
            bu.displaypass("Assigned")
    elif x == 3:
        args = input("Type \'all\' to delete all records:")
        assignment = input("Type assigned if passwords are stored")
        if assignment != "Unassigned":
            bu.removepass(args,assignment)
        else:
            bu.removepass(args)
    elif x == 4:
        print("All unassigned passwords are listed below")
        bu.displaypass()
        print("All assigned passwords are listed below")
        bu.displaypass("Assigned")
        break
    