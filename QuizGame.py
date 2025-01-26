
def takeString(tex):
    while True:
        st = input(tex)
        if st.strip() == "":
            print("This section can not be empty")
        elif " " in st.strip():
            print("Can not contain any space")
        else:
            return st

def studentSignup():
    studentFile = open('Students.txt', 'r')
    roll = studentFile.readlines()[-1].split(",")[0]
    studentFile.close()
    roll = int(roll) + 1
    name = takeString("Enter name : ")
    while True:
        while True:
            password = input("Create password : ")
            if len(password) < 8:
                print("Password is too short")
            else :
                break
        password_ = input("Type password again : ")
        if password == password_:
            break
        else:
            print("Password did not matched")
    studentInfo = str(roll) + " " + name + " " + password + "\n"
    studentFile = open("Students.txt", "a")
    studentFile.write(studentInfo)
    studentFile.close()
    print("Sign-up successful")
    print("Your roll number is", roll)


def teacherSignup():
    teacherFile = open('Teachers.txt', 'r')
    code = teacherFile.readlines()[-1].split()[0]
    teacherFile.close()
    code = int(code) + 1
    name = takeString("Enter name : ")
    while True:
        password = input("Create password : ")
        if len(password) < 8:
            print("Password is too short")
        else :
            break
        password_ = input("Type password again : ")
        if password == password_:
            break
        else:
            print("Password did not matched")
    teacherInfo = str(code) + " " + name + " " + password + "\n"
    teacherFile = open("Teachers.txt", "a")
    teacherFile.write(teacherInfo)
    teacherFile.close()
    print("Sign-up successful")
    print("Your code number is", code)

def studentLogin():
    rollInput = takeString("Enter roll :")
    studentFile = open('Students.txt', 'r')
    flag = 0
    while True:
        StudentInfo = studentFile.readline().split()
        if rollInput.strip() == StudentInfo[0].strip():
            flag = 1
            break
        elif StudentInfo[0] == "":
            break
    if flag == 0:
        Print("Roll number not Found")
        return
    else:
        roll = StudentInfo[0]
        name = StudentInfo[1]
        password = StudentInfo[2]
    password_ = input("Enter Password : ")
    if password.strip() == password_.strip():
        print("Welcome", name)
        print()
        studentPage(roll)
    else:
        print("Wrong Password")
        print()
        return

def teacherLogin():
    codeInput = takeString("Enter code : ")
    teacherFile = open('Teachers.txt', 'r')
    flag = 0
    while True:
        teacherInfo = teacherFile.readline().split()
        print(teacherInfo)
        if teacherInfo == []:
            break
        elif codeInput.strip() == teacherInfo[0].strip():
            flag = 1
            break
    if flag == 0:
        print("Code number not Found")
        return
    else:
        code = teacherInfo[0]
        name = teacherInfo[1]
        password = teacherInfo[2]
    password_ = input("Enter Password : ")
    print()
    if password.strip() == password_.strip():
        print("Welcome", name)
        teachersPage(code)
    else:
        print("Wrong Password")
        print()
        return

def teachersPage(code):
    while True:
        print("1. View your tests")
        print("2. Add test")
        print("3. Logout")
        num = int(input("Select an option : "))
        print()
        if num == 1:
            testFile = open('tests.txt', 'r')
            while True:
                testInfo = testFile.readline().split()
                if testInfo == []:
                    break
                elif code.strip() == testInfo[1].strip():
                    print(testInfo)
                    #todo format
            testFile.close()
            print()
        elif num == 2:
            testFile = open('tests.txt', 'r')
            testno = testFile.readlines()[-1].split()[0]
            testFile.close()
            testno = int(testno) + 1
            testName = input("Enter the name of your test : ")
            questionTxt = input("Enter the question txt file : ")
            #todo .txt check
            passMark = input("Enter pass mark : ")
            print()
            testInfo = str(testno) + " " + code + " " + testName + " " + questionTxt + " " + passMark + "\n"
            testFile = open("tests.txt", "a")
            testFile.write(testInfo)
            testFile.close()
        elif num == 3:
            print("Loged out successfully")
            return
        else:
            print("Invalid selection")

def studentPage(roll):
    while True:
        print("1. Take a test")
        print("2. Logout")
        num = int(input("Select an option : "))
        print()
        if num == 1:
            testFile = open('tests.txt', 'r')
            while True:
                testInfo = testFile.readline().split()
                if testInfo == []:
                    break
                else:
                    print(testInfo)
                    # todo format
            testFile.close()
            testNum = int(input("Select a test : "))
            print()
            testFile = open('tests.txt', 'r')
            for i in range(testNum - 1):
                testInfo = testFile.readline()
            testInfo = testFile.readline().split()
            Qtxt = testInfo[3]
            passMark = testInfo[4]
            takeTest(Qtxt, passMark)
            input("Press Enter to continue ")
        elif num == 2:
            print("Loged out successfully")
            return
        else:
            print("Invalid selection")

def takeTest(Qtxt, passMark):
    class Que:
        def __init__(self, Q):
            self.Q = Q
            self.Op1 = Qfile.readline()
            self.Op2 = Qfile.readline()
            self.Op3 = Qfile.readline()
            self.Op4 = Qfile.readline()
            self.Ca = Qfile.readline()

        def printQ(self):
            print(self.Q)
            print(self.Op1)
            print(self.Op2)
            print(self.Op3)
            print(self.Op4)

    Qfile = open(Qtxt, "r")
    Qlist = []
    score = 0

    while 1:
        Q = Qfile.readline()
        if Q == "end":
            break
        else:
            Qlist.append(Que(Q))

    for i in Qlist:
        i.printQ()
        userInput = (input("Enter correct option : ")).lower()
        userInput = userInput.strip()
        ca = i.Ca.strip()
        if userInput == ca:

            print("Your answer is correct")
            score += 1
        else:
            print("Your answer is wrong")
            print("The correct answer is", i.Ca)
    if score >= int(passMark):
        print("Congratulations, you have successfully passed the test!")
    else:
        print("Sorry, you did not pass the test this time. Better luck next time.")
    print("Your total score is", score)

def frontPage():
    print("-----Quiz Game-----")
    print("Are you a ")
    print("1. Student")
    print("2. Teacher")
    print("3. Close program")
    while True:
        num = int(input("Select an option : "))
        if num == 3:
            return
        elif num < 1 or num > 2:
            print("Invalid selection")
        else:
            break
    print()
    print("1. Login")
    print("2. Signup")
    while True:
        num2 = int(input("Select an option : "))
        if num2 < 1 or num2 > 2:
            print("Invalid selection")
        else:
            break
    print()
    if num == 1 and num2 == 1:
        studentLogin()
    elif num == 1 and num2 == 2:
        studentSignup()
    elif num == 2 and num2 == 1:
        teacherLogin()
    elif num == 2 and num2 == 2:
        teacherSignup()

frontPage()