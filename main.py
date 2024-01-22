"""
School Online - Console Application
"""

database = {
    "students": [""],
    "clazzes": [""],
    "subjects": [""]
}

id = 0
table = {}

def main():
    print("--Aplikace ŠKOLA ONLINE--")
    print('\n',"Vytvořit Studenta: 1",'\n',"Upravit Studenta: 2",'\n',"Odstranit Studenta: 3")
    print('\n',"Vytvořit Třídu: 4",'\n',"Upravit Třídu: 5",'\n',"Odstranit Třídu: 6")
    print('\n',"Vytvořit Předmět: 7",'\n',"Upravit Předmět: 8",'\n',"Odstranit Předmět: 9")
    print('\n',"Vytvořit Tabulku: 10",'\n',"Vyhledat Tabulku: 11",'\n',"Odstranit Tabulku: 12")
    print('\n',"Dát známku pro studenta v tabulce: 13")
    print("ex = Odejít z funkce zpět")
    print("end = Ukončí program")
    
    while True:
        choice = input("Zadej číslo: ")
        if choice == "1":
            create_student()
        elif choice == "2" and database["students"] != [""]:
            edit_student()
        elif choice == "3" and database["students"] != [""]:
            delete_student()
        elif choice == "4":
            create_clazz()
        elif choice == "5" and database["clazzes"] != [""]:
            edit_clazz()
        elif choice == "6" and database["clazzes"] != [""]:
            delete_clazz()
        elif choice == "7":
            create_subject()
        elif choice == "8" and database["subjects"] != [""]:
            edit_subject()
        elif choice == "9" and database["subjects"] != [""]:
            delete_subject()
        elif choice == "10" and database["students"] != [""] and database["clazzes"] != [""] and database["subjects"] != [""]:
            create_table()
        elif choice == "11" and table != {}:
            find_table()
        elif choice == "12" and table != {}:
            delete_table()
        elif choice == "13" and table != {}:
            give_grade()
        elif choice == "end":
            exit()
        else:
            print("Špatný výběr (nebo daný prvek, který chcete upravit/odstranit neexistuje)")

def create_student():
    while True:
        new_student = input("Zadej jméno nového studenta: ")
        if new_student == "ex":
            main()
        elif new_student in database["students"]:
            print(f"Student {new_student} již existuje.")
        else:
            database["students"].append(new_student)
            print(f"Nový student {new_student} byl vytvořen.")
            main()
            break
        
def create_clazz():
    while True:
        new_clazz = input("Zadejte třídu (např. 3.A): ").upper()
        if new_clazz == "ex":
            main()
        elif len(new_clazz) == 3 and new_clazz[0].isdigit() and new_clazz[1] == '.' and new_clazz[2].isalpha() and new_clazz not in database["clazzes"]:
            database["clazzes"].append(new_clazz)
            print(f"Třída {new_clazz} byla vytvořena.")
            main()
            break
        else:
            print("Špatný formát (Nebo třída byla již vytvořena)")
            
def create_subject():
    while True:
        new_subject = input("Zadejte předmět (např. DBA nebo CJ): ").upper()
        if new_subject == "ex":
            main()
        elif len(new_subject) <= 3 and new_subject.isalpha() and new_subject not in database["subjects"]:
            database["subjects"].append(new_subject)
            print(f"Předmět {new_subject} byl vytvořen.")
            main()
            break
        else:
            print("Špatný formát (Nebo předmět byl již vytvořen)")
    
def edit_student():
    while True:
        existing_student = input("Zadejete jméno studenta, kterého chcete upravit: ")
        if existing_student == "ex":
            main()
        elif existing_student in database["students"]:
            for i, existing_student in enumerate(database["students"]):
                if database["students"][i] == existing_student:
                    database["students"][i] = input("Zadejete jméno nově upraveného studenta: ")
                    main()
            break
        else:
            print("Student neexistuje")

def edit_clazz():
    while True:
        existing_clazz = input("Zadejete třídu, kterou chcete upravit: ").upper()
        if existing_clazz == "ex":
            main()
        elif existing_clazz in database["clazzes"]:
            for i, existing_clazz in enumerate(database["clazzes"]):
                if database["clazzes"][i] == existing_clazz:
                    while True:
                        database["clazzes"][i] = input("Zadejete nově upravenou třídu: ").upper()
                        if len(database["clazzes"][i]) == 3 and database["clazzes"][i][0].isdigit() and database["clazzes"][i][1] == '.' and database["clazzes"][i][2].isalpha():
                            main()
                            return
                        else:
                            print("Špatný formát")
                break
        else:
            print("Třída neexistuje")
            
def edit_subject():
    while True:
        existing_subject = input("Zadejete název předmětu, který chcete upravit: ").upper()
        if existing_subject == "ex":
            main()
        elif existing_subject in database["subjects"]:
            for i, existing_subject in enumerate(database["subjects"]):
                if database["subjects"][i] == existing_subject:
                    database["subjects"][i] = input("Zadejete název nově upraveného předmětu: ").upper()
                    main()
            break
        else:
            print("Předmět neexistuje")
            
def delete_student():
    while True:
        student_to_delete = input("Zadejete jméno studenta, kterého odstranit: ")
        if student_to_delete == "ex":
            main()
        elif student_to_delete in database["students"]:
            for i, student_to_delete in enumerate(database["students"]):
                if database["students"][i] == student_to_delete:
                    database["students"].remove(student_to_delete)
                    main()
            break
        else:
            print("Student neexistuje")

def delete_clazz():
    while True:
        clazz_to_delete = input("Zadejete třídu, kterou chcete odstranit: ").upper()
        if clazz_to_delete == "ex":
            main()
        elif clazz_to_delete in database["clazzes"]:
            for i, clazz_to_delete in enumerate(database["clazzes"]):
                if database["clazzes"][i] == clazz_to_delete:
                    database["clazzes"].remove(clazz_to_delete)
                    main()
            break
        else:
            print("Třída neexistuje")
            
def delete_subject():
    while True:
        subject_to_delete = input("Zadejete předmět, který chcete odstranit: ").upper()
        if subject_to_delete == "ex":
            main()
        elif subject_to_delete in database["subjects"]:
            for i, subject_to_delete in enumerate(database["subjects"]):
                if database["subjects"][i] == subject_to_delete:
                    database["subjects"].remove(subject_to_delete)
                    main()
            break
        else:
            print("Předmět neexistuje")

def create_table():
    global id
    id += 1
    table[id] = []
    while True:
        add_student = input("Zadejete studenta: ")
        if add_student == "ex":
            main()
        elif add_student in database["students"] and not any(add_student in table_data for table_data in table.values()):
            table[id].append(add_student)
            break
        else:
            print("Student neexistuje nebo byl již vytvořen")
    while True:
        add_clazz = input("Zadejete třídu: ").upper()
        if add_clazz == "ex":
            main()
        elif add_clazz in database["clazzes"]:
            table[id].append(add_clazz)
            break
        else:
            print("Třída neexistuje")
    while True:
        add_subject = input("Zadejete předmět: ").upper()
        if add_subject == "ex":
            main()
        elif add_subject in database["subjects"]:
            table[id].append(add_subject)
            print(table[id])
            main()
            break
        else:
            print("Předmět neexistuje")
    
def find_table():
    while True:
        student_in_table = input("Zadejte jméno studenta z tabulky: ")
        if student_in_table == "ex":
            main()
        else:
            found = False

            for table_id, table_data in table.items():
                if student_in_table in table_data:
                    print(f"Tabulka: {table[table_id]}")
                    found = True
                    main()
                    break

            if not found:
                print(f"Student {student_in_table} nenalezen v žádné tabulce.")
            
def delete_table():
    while True:
        student_in_table = input("Zadejte jméno studenta z tabulky, kterou chcete odstranit: ")
        if student_in_table == "ex":
            main()
        else:
            found = False

            for table_id, table_data in table.items():
                if student_in_table in table_data:
                    del table[table_id]
                    found = True
                    main()
                    break

            if not found:
                print(f"Student {student_in_table} nenalezen v žádné tabulce.")
            
def give_grade():
    while True:
        student_in_table = input("Zadejte jméno studenta z tabulky, kterému chcete dát známku: ")
        if student_in_table == "ex":
            main()
        else:
            found = False
            for table_id, table_data in table.items():
                if student_in_table in table_data:
                    print(f"Tabulka: {table[table_id]}")
                    found = True
                    while True:
                        grade = input("Zadejte závěrečnou známku (1-5): ")
                        if grade == "ex":
                            main()
                        if grade.isdigit() and 1 <= int(grade) <= 5:
                            table[table_id].append(grade)
                            print(table[table_id])
                            main()
                            break
                        else:
                            print("Špatný formát")

            if not found:
                print(f"Student {student_in_table} nenalezen v žádné tabulce.")
            
main()