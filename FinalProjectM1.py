import statistics

admins = {'Python':'Pass123@', 'users':'Pass1234@'}

studentDict = {'Jeff':[78,98,99],
               'Alex':[89,65,85],
               'Sam':[89,78,77]}

def enterGrades():
    nameToEnter = input('Student name: ')
    gradesToEnter = input('Entering grades: ')

    if nameToEnter in studentDict:
        print('Student name is valid!!')
        studentDict[nameToEnter].append(float(gradesToEnter))
    else:
        print('Invalid student name')
    print(studentDict)

def removeStudent():
    nameToRemove = input('What student to remove?')

    if nameToRemove in studentDict:
        print('Student is removed')
        del studentDict[nameToRemove]
    else:
        print('Invalid name of the student')
    print(studentDict)


def studentAvg():
    for eachStudent in studentDict:
        gradeList = studentDict[eachStudent]
        avgGrades = statistics.mean(gradeList)

        print(eachStudent,'Here is average:', avgGrades)

def main():
    print("""
          Welcome to Grade Central

          [1] - Enter Grades
          [2] - Remove Student
          [3] - Student Average Grades
          [4] - Exit

          """)
    action = input('What would you like to do today?(Enter the number)')

    if action == '1':
        enterGrades()
    elif action == '2':
        removeStudent()
    elif action == '3':
        studentAvg()
    elif action == '4':
        exit()
    else:
        print('Invalid entry:')

login = input('Username: ')
Passw = input('Password: ')

if login in admins:
    if admins[login] == Passw:
        print('Welcome',login)
        while True:
            main()
    else:
        print('Invalid Password')
else:
    print('Invalid login, try again')
    
       
      
    



