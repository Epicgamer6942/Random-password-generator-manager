import pickle
def addpass(pwd,domain,acc = "None"):
    domain = "http(s)://" + domain
    if acc == "None":
        with open("Unassigned password.dat","ab") as f1:
            sno = int(input("Enter sno:"))
            master = [sno,{
                acc:[pwd,domain]
            }]
            pickle.dump(master,f1)
    else:
        with open("Assigned.dat","ab") as f2:
            sno = int(input("Enter sno:"))
            master = [sno,{
                acc:[pwd,domain]
            }]
            pickle.dump(master,f2)


def displaypass(assignment = "Unassigned"):
    if assignment == "Unassigned":
        f1=open("Unassigned password.dat","rb")
        try:
            while True:
                rec=pickle.load(f1)
                print(rec)
        except EOFError:
            f1.close()
    else:
        try:
            f1=open("Assigned.dat","rb")
            while True:
                rec=pickle.load(f1)
                print(rec)
        except EOFError:
            f1.close()

def removepass(args = "all",assignment = "Unassigned"):
    if assignment == "Unassigned":
        if args == "all" :
            with open("Unassigned password.dat", "wb") as f1:
                print("Successfully deleted all data")
        else:
            l1 = []
            try:
                with open("Unassigned Passwords.dat", "rb") as f1:
                    
                    while True:
                        a = pickle.load(f1)
                        l1.append(a)
            except EOFError:
                f1.close()
                with open("Unassigned password.dat", "wb") as f2:
                    for i in l1:
                        pickle.dump(i,f2)
    else:
        if args == "all" :
            with open("Assigned.dat", "wb") as f1:
                print("Successfully deleted all data")
        else:
            l1 = []
            try:
                with open("Assigned.dat", "rb") as f1:
                     while True:
                        a = pickle.load(f1)
                        l1.append(a)
                        
            except EOFError:
                l1.pop()
                f1.close()
                with open("Assigned.dat", "wb") as f2:
                    for i in l1:
                        pickle.dump(i,f2)





    
