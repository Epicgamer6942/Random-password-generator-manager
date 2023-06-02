import pickle
import pprint
import generator
def addpass(pwd,domain,acc = "None"):
    domain = "http(s)://" + domain
    if acc == "None":
        with open("Unassigned password.dat","ab") as f1:
            sno = int(input("Enter sno:"))
            master = [domain,acc,pwd]
            pickle.dump(master,f1)
    else:
        with open("Assigned.dat","ab") as f2:
            sno = int(input("Enter sno:"))
            master = [domain,acc,pwd]
            pickle.dump(master,f2)


def displaypass(assignment = "Unassigned"):
    if assignment == "Unassigned":
        f1=open("Unassigned password.dat","rb")
        try:
            while True:
                rec=pickle.load(f1)
                pprint(rec)
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
def searchpass(assignment = "Unassigned"):
    dom = input("Enter domain name:")
    domainFull = "http(s)://" + dom
    global l1
    l1 = []
    if assignment == "Unassigned":
        try:
            with open("Unassigned password.dat","rb") as f1:
                while True:
                    a = pickle.load(f1)
                    if a[0] == domainFull:
                        l1.append(a)
        except EOFError:
            print("All the passwords in that domain have been displayed below:")
            for i in l1:
                print(i)
            f1.close()
        return l1   
    else:
        try:
            with open("Assigned.dat","rb") as f1:
                while True:
                    a = pickle.load(f1)
                    if a[0] == domainFull:
                        l1.append(a)
        except EOFError:
            print("All the passwords in that domain have been displayed below:")
            for i in l1:
                print(i)
            f1.close()
        return l1         

def editpass(assignment = 'Unassigned'):
    #format = [domain,acc,pwd]
    assignment = input("Enter assignment:")
    searchpass(assignment)
    pwd = input("Type the password you want to change:")
    maxlen = int(input("Enter new length of password:"))
    newPass = generator.passgen(maxlen)
    temp_lst = []
    if assignment.title() == "Unassigned":
        try:
            with open("Unassigned password.dat","rb") as f1:
                while True:
                    a = pickle.load(f1)
                    temp_lst.append(a)
                    for i in range(len(temp_lst)):
                        if temp_lst[i][-1] == pwd:
                            temp_lst[i][-1] = newPass
        except EOFError:
            f1.close()
            with open("Unassigned password.dat", "wb") as f2:
                for i in temp_lst:
                    pickle.dump(i,f2)
    else :
        try:
            with open("Assigned.dat","rb") as f1:
                while True:
                    a = pickle.load(f1)
                    temp_lst.append(a)
                    for i in range(len(temp_lst)):
                        if temp_lst[i][-1] == pwd:
                            temp_lst[i][-1] = newPass
        except EOFError:
            f1.close()
            with open("assigned.dat", "wb") as f2:
                for i in temp_lst:
                    pickle.dump(i,f2)

        









    
