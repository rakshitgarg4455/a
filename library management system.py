import pickle
import time
import os
import getpass

#=========================PUSH=========================#
def push():
    os.system("cls")
    b = 0
    c = 0

    while(True):
        try:
            bookno = int(input("Enter Book Number:"))
        except(ValueError):
            print("Enter a valid integer\a")
            time.sleep(1)
            os.system("cls")
            continue
        with open("library records.dat", "rb") as f:
            while(True):
                try:
                    a = list(pickle.load(f))
                    if(bookno == a[0]):
                        print("Enter a unique value\a")
                        time.sleep(1)
                        os.system("cls")
                        break
                except(EOFError):
                    b = 1
                    break
        if(b == 1):
            break

    while(True):
        try:
            bookname = input("Enter Book Name:")
        except(ValueError):
            print("Enter a valid string\a")
            time.sleep(1)
            os.system("cls")
            continue
        with open("library records.dat", "rb") as f:
            f.seek(0)
            while(True):
                try:
                    a = list(pickle.load(f))
                    if(bookname == a[1]):
                        print("Enter a unique value\a")
                        time.sleep(1)
                        os.system("cls")
                        break
                except(EOFError):
                    c = 1
                    break
        if(c == 1):
            break

    while(True):
        try:
            pages = int(input("Enter the number of pages in the book:"))
            break
        except(ValueError):
            print("Enter a valid Integer")
            time.sleep(1)
            os.system("cls")

    while(True):
        try:
            copies = int(input("Enter the number of copies available:"))
            break
        except(ValueError):
            print("Enter a valid Integer\a")
            time.sleep(1)
            os.system("cls")

    while(True):
        try:
            genre = input("Enter the genre of the book:")
            break
        except(ValueError):
            print("Enter a valid string\a")
            time.sleep(1)
            os.system("cls")

    l = [bookno, bookname, pages, copies, genre]
    with open("library records.dat", "ab") as f:
        pickle.dump(l, f)
#=========================PUSH=========================#

#=========================DISPLAY=========================#
def dispall():
    os.system("cls")
    print("Format-> [Book number, name of book, book length, number of copies, genre]")
    with open("library records.dat", "rb") as f:
        count = 1
        while(True):
            try:
                print(count, ".", pickle.load(f))
                count += 1
            except(EOFError):
                if(count == 1):
                    print("Records are empty")
                    time.sleep(1)
                break
    os.system("pause")

def dispsortlen():
    os.system("cls")
    list1 = []
    list2 = []
    list3 = []
    with open("library records.dat", "rb") as f:
        b = 0
        while(True):
            try:
                a = list(pickle.load(f))
                list1.append(a)
            except(EOFError):
                break

        if(len(list1) == 0):
            print("Records are empty")
            b = 1

        if(b != 1):
            for i in list1:
                list2.append(i[2])
            list2.sort()
            for i in range(len(list1)):
                for i2 in range(len(list1)):
                    if(list2[i] == list1[i2][2]):
                        list3.append(list1[i2])
            while(True):
                try:
                    c = int(input("1. Ascending order\n2. Descending Order"))
                    break
                except(ValueError):
                    print("Enter a valid integer\a")
                    time.sleep(1)
                    os.system("cls")
            if(c == 1):
                for i in list3:
                    print(i)
            elif(c == 2):
                list3.reverse()
                print("Format-> [Book number, name of book, book length, number of copies, genre]")
                for i in list3:
                    print(i)
    os.system("pause")

def dispsortcopies():
    os.system("cls")
    list1 = []
    list2 = []
    list3 = []
    with open("library records.dat", "rb") as f:
        b = 0
        while(True):
            try:
                a = list(pickle.load(f))
                list1.append(a)
            except(EOFError):
                break

        if(len(list1) == 0):
            print("Records are empty")
            b = 1

        if(b != 1):
            for i in list1:
                list2.append(i[3])
            list2.sort()
            for i in range(len(list1)):
                for i2 in range(len(list1)):
                    if(list2[i] == list1[i2][3]):
                        list3.append(list1[i2])
            while(True):
                try:
                    c = int(input("1. Ascending order\n2. Descending Order"))
                    break
                except(ValueError):
                    print("Enter a valid integer\a")
                    time.sleep(1)
                    os.system("cls")
            if(c == 1):
                for i in list3:
                    print(i)
            elif(c == 2):
                list3.reverse()
                print("Format-> [Book number, name of book, book length, number of copies, genre]")
                for i in list3:
                    print(i)
    os.system("pause")

def dispsortalpha():
    os.system("cls")
    list1 = []
    list2 = []
    list3 = []
    with open("library records.dat", "rb") as f:
        b = 0
        while(True):
            try:
                a = list(pickle.load(f))
                list1.append(a)
            except(EOFError):
                break

        if(len(list1) == 0):
            print("Records are empty")
            b = 1

        if(b != 1):
            for i in list1:
                list2.append(i[1])
            list2.sort()
            for i in range(len(list1)):
                for i2 in range(len(list1)):
                    if(list2[i] == list1[i2][1]):
                        list3.append(list1[i2])
            while(True):
                try:
                    c = int(input("1. Ascending order\n2. Descending Order"))
                    break
                except(ValueError):
                    print("Enter a valid integer\a")
                    time.sleep(1)
                    os.system("cls")
            if(c == 1):
                for i in list3:
                    print(i)
            elif(c == 2):
                list3.reverse()
                print("Format-> [Book number, name of book, book length, number of copies, genre]")
                for i in list3:
                    print(i)
    os.system("pause")


def display():
    os.system("cls")
    while(True):
        try:
            a = int(input("1. All\n2. Sorted by book length\n3. Sorted by number of copies\n4. Sorted by alphabetic order\n"))
        except(ValueError):
            print("Enter a valid integer\a")
            time.sleep(1)
            os.system("cls")
            continue
        if(a == 1):
            dispall()
            break
        elif(a == 2):
            dispsortlen()
            break
        elif(a == 3):
            dispsortcopies()
            break
        elif(a == 4):
            dispsortalpha()
            break
        else:
            print("Enter a valid value(1-4)\a")
#=========================DISPLAY=========================#

#=========================SEARCH=========================#
def searchname():
    os.system("cls")
    b = []
    while(True):
        try:
            a = input("Enter the book name:")
            break
        except(ValueError):
            print("Enter a valid string\a")
            time.sleep(1)
            os.system("cls")
    with open("library records.dat", "rb") as f:
        while(True):
            try:
                b = list(pickle.load(f))
                if(a == b[1]):
                    break
            except(EOFError):
                b = []
                break
    if(b == []):
        print("No books with this name found")
    else:
        print("Format-> [Book number, name of book, book length, number of copies, genre]")
        print(b)
    os.system("pause")

def searchbookno():
    os.system("cls")
    b = []
    while(True):
        try:
            a = int(input("Enter the book number:"))
            break
        except(ValueError):
            print("Enter a valid integer\a")
            time.sleep(1)
            os.system("cls")
    with open("library records.dat", "rb") as f:
        while(True):
            try:
                b = list(pickle.load(f))
                if(a == b[0]):
                    break
            except(EOFError):
                b = []
                break
    if(b == []):
        print("No books with this number found")
    else:
        print("Format-> [Book number, name of book, book length, number of copies, genre]")
        print(b)
    os.system("pause")

def searchbooklen():
    os.system("cls")
    c = []
    while(True):
        try:
            a = int(input("Search books with length-\n1. less than a certain value\n2. greater than a certain value\n"))
            if(a == 1):
                os.system("cls")
                while(True):
                    try:
                        b = int(input("Enter upper limit book length:"))
                        break
                    except(ValueError):
                        print("Enter a valid integer\a")
                        time.sleep(1)
                        os.system("cls")
                with open("library records.dat", "rb") as f:
                    while(True):
                        try:
                            d = list(pickle.load(f))
                            if(d[2] <= b):
                                c.append(d)
                        except(EOFError):
                            break
                if(len(c) == 0):
                    print("No book with such length found")
                    time.sleep(1)
                else:
                    print("Format-> [Book number, name of book, book length, number of copies, genre]")
                    for i in c:
                        print(i)
            elif(a == 2):
                os.system("cls")
                while(True):
                    try:
                        b = int(input("Enter lower limit book length:"))
                        break
                    except(ValueError):
                        print("Enter a valid integer\a")
                        time.sleep(1)
                        os.system("cls")
                with open("library records.dat", "rb") as f:
                    while(True):
                        try:
                            d = list(pickle.load(f))
                            if(d[2] >= b):
                                c.append(d)
                        except(EOFError):
                            break
                if(len(c) == 0):
                    print("No book with such length found")
                else:
                    print("Format-> [Book number, name of book, book length, number of copies, genre]")
                    for i in c:
                        print(i)
            else:
                print("Enter a valid choice(1, 2)\a")
            break
        except(ValueError):
            print("Enter a valid integer\a")
            time.sleep(1)
            os.system("cls")
    os.system("pause")

def searchcopies():
    os.system("cls")
    c = []
    while(True):
        try:
            a = int(input("Search books with number of copies available-\n1. less than a certain value\n2. greater than a certain value\n"))
            if(a == 1):
                os.system("cls")
                while(True):
                    try:
                        b = int(input("Enter upper limit number of copies available:"))
                        break
                    except(ValueError):
                        print("Enter a valid integer\a")
                        time.sleep(1)
                        os.system("cls")
                with open("library records.dat", "rb") as f:
                    while(True):
                        try:
                            d = list(pickle.load(f))
                            if(d[3] <= b):
                                c.append(d)
                        except(EOFError):
                            break
                if(len(c) == 0):
                    print("No book with such availability found")
                else:
                    print("Format-> [Book number, name of book, book length, number of copies, genre]")
                    for i in c:
                        print(i)
            elif(a == 2):
                os.system("cls")
                while(True):
                    try:
                        b = int(input("Enter lower limit number of copies available:"))
                        break
                    except(ValueError):
                        print("Enter a valid integer\a")
                        time.sleep(1)
                        os.system("cls")
                with open("library records.dat", "rb") as f:
                    while(True):
                        try:
                            d = list(pickle.load(f))
                            if(d[3] >= b):
                                c.append(d)
                        except(EOFError):
                            break
                if(len(c) == 0):
                    print("No book with such availability found")
                else:
                    print("Format-> [Book number, name of book, book length, number of copies, genre]")
                    for i in c:
                        print(i)
            else:
                print("Enter a valid choice(1, 2)\a")
            break
        except(ValueError):
            print("Enter a valid integer\a")
            time.sleep(1)
            os.system("cls")
    os.system("pause")

def searchgenre():
    os.system("cls")
    b = []
    while(True):
        try:
            a = input("Enter genre:")
            break
        except(ValueError):
            print("Enter a valid string\a")
            time.sleep(1)
            os.system("cls")
    with open("library records.dat", "rb") as f:
        while(True):
            try:
                c = pickle.load(f)
                if(a in c[4]):
                    b.append(c)
            except(EOFError):
                break
    if(len(b) == 0):
        print("No book with such genre found")
    else:
        print("Format-> [Book number, name of book, book length, number of copies, genre]")
        for i in b:
            print(i)
    os.system("pause")

def search():
    os.system("cls")
    while(True):
        try:
            a = int(input("1. Name\n2. Book number\n3. Number of pages\n4. Number of copies\n5. Genre\n"))
        except(ValueError):
            print("Enter a valid integer\a")
            time.sleep(1)
            os.system("cls")
            continue
        if(a == 1):
            searchname()
            break
        elif(a == 2):
            searchbookno()
            break
        elif(a == 3):
            searchbooklen()
            break
        elif(a == 4):
            searchcopies()
            break
        elif(a == 5):
            searchgenre()
            break
        else:
            print("Enter a valid choice(1-5)\a")
#=========================SEARCH=========================#

#=========================POP=========================#
def popbyno():
    os.system("cls")
    c = []
    d = []
    while(True):
        try:
            a = int(input("Enter the book number:"))
            break
        except(ValueError):
            print("Enter a valid integer")
            time.sleep(1)
            os.system("cls")
    with open("library records.dat", "rb") as f:
        while(True):
            try:
                b = list(pickle.load(f))
                if(b[0] == a):
                    d = b
                else:
                    c.append(b)
            except(EOFError):
                break
    if(d == []):
        print("No record of a book with this name found")
        return d
    with open("library records.dat", "wb") as f:
        for i in c:
            pickle.dump(i, f)
    return d
    

def popbyname():
    os.system("cls")
    c = []
    d = []
    while(True):
        try:
            a = input("Enter the book name:")
            break
        except(ValueError):
            print("Enter a valid string")
            time.sleep(1)
            os.system("cls")
    with open("library records.dat", "rb") as f:
        while(True):
            try:
                b = list(pickle.load(f))
                if(b[1] == a):
                    d = b
                else:
                    c.append(b)
            except(EOFError):
                break
    if(d == []):
        print("No record of a book with this name found")
        return d
    with open("library records.dat", "wb") as f:
        for i in c:
            pickle.dump(i, f)
    return d
    
def pop():
    os.system("cls")
    while(True):
        try:
            a = int(input("Search record to be deleted by-\n1. Book number\n2. Book name\n"))
            if(a == 1):
                popbyno()
                break
            elif(a == 2):
                popbyname()
                break
            else:
                print("Enter a valid choice (1, 2)\a")
        except(ValueError):
            print("Enter a valid integer\a")
            time.sleep(1)
            os.system("cls")
#=========================POP=========================#

def alterno(c):
    os.system("cls")
    b = 0
    while(True):
        try:
            bookno = int(input("Enter new value:"))
        except(ValueError):
            print("Enter a valid integer\a")
            time.sleep(1)
            os.system("cls")
            continue
        with open("library records.dat", "rb") as f:
            while(True):
                try:
                    a = list(pickle.load(f))
                    if(bookno == a[0]):
                        print("Enter a unique value\a")
                        time.sleep(1)
                        os.system("cls")
                        break
                except(EOFError):
                    b = 1
                    break
        if(b == 1):
            break
    c[0] = bookno
    with open("library records.dat", "ab") as f:
        pickle.dump(c, f)


def altername(c):
    os.system("cls")
    b = 0
    while(True):
        try:
            bookno = input("Enter new value:")
        except(ValueError):
            print("Enter a valid string\a")
            time.sleep(1)
            os.system("cls")
            continue
        with open("library records.dat", "rb") as f:
            while(True):
                try:
                    a = list(pickle.load(f))
                    if(bookno == a[1]):
                        print("Enter a unique value\a")
                        time.sleep(1)
                        os.system("cls")
                        break
                except(EOFError):
                    b = 1
                    break
        if(b == 1):
            break
    c[1] = bookno
    with open("library records.dat", "ab") as f:
        pickle.dump(c, f)

def alter():
    os.system("cls")
    while(True):
        try:
            a = int(input("Element to be used to search for the record to be altered:\n1. Book number\n2. Book name\n"))
            if(a == 1):
                b = popbyno()
                break
            elif(a == 2):
                b = popbyname()
                break
            else:
                print("Enter a valid choice (1, 2)\a")
        except(ValueError):
            print("Enter a valid integer\a")
            time.sleep(1)
            os.system("cls")
    if(b == []):
        return 0
    os.system("cls")
    while(True):
        try:
            c = int(input("Element to be changed:\n1. Book number\n2. Book name\n3. Book length\n4. Available number of copies\n5. Genre\n"))
            if(c == 1):
                alterno(b)
            elif(c == 2):
                altername(b)
            elif(c == 3):
                os.system("cls")
                while(True):
                    try:
                        d = int(input("Enter new value:"))
                        break
                    except(ValueError):
                        print("Enter a valid integer\a")
                        time.sleep(1)
                        os.system("cls")
                b[2] = d
                with open("library records.dat", "ab") as f:
                    pickle.dump(b, f)
            elif(c == 4):
                os.system("cls")
                while(True):
                    try:
                        d = int(input("Enter new value:"))
                        break
                    except(ValueError):
                        print("Enter a valid integer\a")
                        time.sleep(1)
                        os.system("cls")
                b[3] = d
                with open("library records.dat", "ab") as f:
                    pickle.dump(b, f)
            elif(c == 5):
                os.system("cls")
                while(True):
                    try:
                        d = input("Enter new value:")
                        break
                    except(ValueError):
                        print("Enter a valid string\a")
                        time.sleep(1)
                        os.system("cls")
                b[4] = d
                with open("library records.dat", "ab") as f:
                    pickle.dump(b, f)
            break
        except(ValueError):
            print("Enter a valid integer\a")
            time.sleep(1)
            os.system("cls")

if(getpass.getpass("Enter password:") == "password"):
    print('''                                                       
|     o |                                                                  |      
|     . |---. ,---. ,---. ,---. ,   .    ,---. ,---. ,---. ,---. ,---. ,---| ,---.
|     | |   | |     ,---| |     |   |    |     |---' |     |   | |     |   | `---.
`---' ` `---' `     `---^ `     `---|    `     `---' `---' `---' `     `---' `---'
                                `---'                                             
    ''')
    x = 1
    try:
        with open("library records.dat", "rb") as f:
            pickle.load(f)
    except(FileNotFoundError):
        x = 0
    if(x == 0):
        with open("library records.dat", "wb") as f:
            time.sleep(1)
            os.system("cls")

    while(True):
        try:
            print("1. Push")
            print("2. Pop")
            print("3. Sorted Display")
            print("4. Search")
            print("5. Alter")
            a = int(input("What action to perform:"))
            if(a == 1):
                push()
            elif(a == 2):
                pop()
            elif(a == 3):
                display()
            elif(a == 4):
                search()
            elif(a == 5):
                alter()
            else:
                print("Enter a valid choice(1-5)\a")
                time.sleep(1)
            os.system("cls")
        except(ValueError):
            print("Enter a valid integer\a")
            time.sleep(1)
            os.system("cls")
