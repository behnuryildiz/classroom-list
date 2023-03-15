import time

classroom = ["Behnur Yildiz", "Ozcan Yildiz"]
print("CURRENT CLASSROOM LIST: \t")
for i, student in enumerate (classroom, start=1):  # to start the list from 1 instead of 0
    print (f"{i}- {student}")
    
while True:
    new_student = "Add a new student"
    more_students = "Add several students at once"
    delete_student = "Delete a student"
    show_list = "Show the classroom list"
    learn_number = "Learn the class number of a student"
    delete_more = "Delete several students from the list"


    option = input(f"\nWHICH OPTION DO YOU WANT TO USE? GIVE THE WORTH IN NUMBER:\nOPTIONS: \n 1) {new_student} \n 2) {more_students} \n 3) {delete_student} \n 4) {show_list} \n 5) {learn_number}\n 6) {delete_more} \n to exit: 0 \n-- ")
  
    option = int(option)

    print(f"\nYou chose the option {option}\n")
    if type(option) != int:
        print ("YOU SHOULD GIVE A VALID WORTH IN NUMBER")
        time.sleep (2)
    if int(option) not in range (0,7):
        print("NOT IN RANGE OF THESE OPTIONS")
        time.sleep (2)


    if option == 1:
        new_student = str(input("WHAT ARE THE FIRST AND LASTNAME OF THE NEW STUDENT ?: \n "))
        if new_student not in classroom: 
            if len(new_student) != 0:
                classroom.append(new_student)
                print (f"THE NEW STUDENT {new_student} SUCCESSFULLY ADDED!")
            else:
                print("SOMETHING WENT WRONG! TRY WITH A VALID NAME AGAIN!")
        else:
            print (f"THAT STUDENT NAMED {new_student} ALREADY EXISTS IN THE CLASSROOM LIST!")
        for i, student in enumerate (classroom, 1):
            print(f"{i}- {student}")
        time.sleep (2)

    elif option == 2:
        more_students = input("WRITE THE NEW STUDENTS' NAMES SEPERATED WITH COMMA: ")
        new_students = more_students.split(',')
        duplicates = []
        for student in new_students:
            if student.strip() not in classroom:
                classroom.append (student.strip())
            else:
                duplicates.append(student.strip())
        if duplicates:
            print(f"THE FOLLOWING STUDENT(S) EXIST(S) IN THE LIST: {', ' .join(duplicates)}") 
        for i, student in enumerate (classroom, 1):
            print(f"{i}- {student}")
        time.sleep (2)

    elif option == 3:
        delete_student = input("WHICH STUDENT DO YOU WANT TO REMOVE FROM THE CLASSROOM LIST? : \n")
        if delete_student in classroom:
            classroom.remove(delete_student)
            print (f"THE STUDENT {delete_student} SUCCESSFULLY DELETED!")
            print ("THE NEW CLASSROOM LIST LOOKS LIKE: \n")
        else:
            print(f"THE STUDENT NAMED {delete_student} NOT IN THE CLASSROOM LIST AT ALL. ENSURE IF THE NAMES ARE WRITTEN CORRECTLY.")
        for i, student in enumerate (classroom, 1):
            print(f"{i}- {student}")
        time.sleep (2)

    elif option == 4:
        print("THE ACTUAL CLASSROOM LIST:")
        for i, student in enumerate(classroom, 1):
            print (f"{i}- {student}")
        time.sleep (2)

    elif option == 5:
        student_name = input("WHICH STUDENT'S NUMBER DO YOU WANT TO LEARN? \n")
        for i, student in enumerate(classroom, start=1):  #to start the list from 1 instead of 0
            if student == student_name:
                print (f"{student} HAS THE SCHOOL NUMBER {i}")   
        time.sleep(2)

    elif option == 6:
        delete_students = input("WHICH STUDENT(S) DO YOU WANT TO DELETE FROM THE CLASSROOM LIST? : \n")
        to_delete = delete_students.split(',')
        couldnt_find=[]
        for delete in to_delete:
            if delete.strip() in classroom:           
                classroom.remove(delete.strip())
            else:
                couldnt_find.append (delete.strip())
        if couldnt_find:
            print(f"THE NAME(S) COULDN'T BE FIND: {', ' .join(couldnt_find)}")

        for i, student in enumerate(classroom, 1):
            print (f"{i}- {student}")
        time.sleep(3)


    elif option == 0:
        print ("...EXITED...")
        break
