global med_database, med_list, med_date
med_list = []
med_database = {'oral_drug': [], 'injectable': [],
                'vaccines': [], 'antiseptics': []}
med_date = {}  # These are global lists used as the database.

# The first menu


def menu_one():
    choice = int(input('''----------------- Medical ERP by Siddharth--------------------
        Select your option or press 0 to exit
        1. Enter Medicines in the database.
        2. Search for the category if the medicines.
        3. Check if the medicines are present in list of medicines.
        4. Show all the medicines with the given expiry date
        Your option : '''))
    return choice

# The second menu for inserting data


def menu_2():
    category = int(input('''----------------- Medical ERP by Siddharth--------------------
        Select your option or press 0 to exit
        Enter your category:
        1. Oral Drugs
        2. Injectable
        3. Vaccine
        4. Antiseptics
        5. Medicine List
        6. Expiry dates of the medicine    
        Your option : '''))
    return category

# The third menu to input medicines as a list


def menu_3():
    med_name = str(input('''----------------- Medical ERP by Siddharth--------------------
        Select your option or press 0 to exit
        Enter your Medicines seperated by a comma: '''))
    if med_name == '0':
        exit()

    return list(med_name.split(","))

# The fourth menu to insert date


def menu_4():
    med_date = str(input('''----------------- Medical ERP by Siddharth--------------------
        Select your option or press 0 to exit
        Enter your expiry date in the format DD/MM/YYYY: '''))
    return list(med_date.split(","))

# The fifth menu to input individual medicine


def menu_5():
    med_name = str(input('''----------------- Medical ERP by Siddharth--------------------
        Select your option or press 0 to exit
        Enter The Medicine Name: '''))
    if med_name == '0':
        exit()
    return med_name

# The driver function to parse the inputs in the main list


def driver():
    user_input = menu_one()
    if user_input == 0:
        exit()
    if user_input == 1:
        database_create()
    if user_input == 2:
        Med_Cat(menu_5())
    if user_input == 3:
        name_list = menu_3()
        med_count(name_list)
    if user_input == 4:
        usr_date = menu_4()
        chk_exp(usr_date)

# The function to insert all thr values in option 1


def database_create():
    category = menu_2()
    if category == 1:
        value = menu_3()
        med_database.update(oral_drug=value)
        print("Database updated with values : ", med_database)
    if category == 2:
        value = menu_3()
        med_database.update(injectable=value)
        print("Database updated with values : ", med_database)
    if category == 3:
        value = menu_3()
        med_database.update(vaccines=value)
        print("Database updated with values : ", med_database)
    if category == 4:
        value = menu_3()
        med_database.update(antiseptics=value)
        print("Database updated with values : ", med_database)
    if category == 5:
        value = menu_3()
        med_list.append(value)
        print("Database updated with values : ", med_list)
    if category == 6:
        value = menu_3()
        date = menu_4()
        global med_date
        med_date = dict(zip(value, date))
        print("Database updated with values : ", med_date)

# The function to search for category name


def Med_Cat(med_name):
    if len(med_database) != 0:

        for i in med_database:
            for j in med_database[i]:
                if med_name == j:
                    print(j, " is in category", i)

    else:
        print("The database is empty")

# Checks is the medicines entered is present in the medicine list


def med_count(name_list):
    med_list1 = med_list[0]
    l = []
    if len(med_list) != 0:
        for i in med_list1:
            for j in name_list:
                if i == j:
                    l.append(j)
                    name_list.remove(j)
        print("The medicines found were : ", l)
        print("The medicines not found were :", name_list)
    else:
        print("The medicine list is empty")

# Returns the medicines with entered date


def chk_exp(usr_date):
    if len(med_date) != 0:
        for key, value in med_date.items():
            if value == usr_date[0]:
                print("The medicines expiring at this date are", key)
    else:
        print("The medicine list is empty")


# Driver code
while True:
    try:
        driver()
    except:
        exit()


'''
Test Data: 
----------------------------------------------------------------------------------------------------------------------------
Oral Drugs : Penicillin,Cephalosporins,Macrolides,Tetracycline,Sulfonamidesm,Quinolones                            
Injectables: Acetylcysteine,Acyclovir,Alteplase,Amiodarone,Acetadote,Zovirax  
Vaccines: MMR,varicella,pertussis,Recombivax HB,Heplisav-B,Pediarix
Antiseptics : Chlorhexidine,Povidone-Iodine,Chloroxylenol,Isopropyl Alcohol,Hexachlorophene,Benzalkonium Chloride
Medicine list: Vicodin,Norco,Xodol,Combiflam,Brufen,Amoxil
-----------------------------------------------------------------------------------------------------------------------------
Medicine names : Acetylcysteine,Cephalosporins,Amiodarone,Chloroxylenol,Xodol,Acyclovir
Medicine List: Neurontin,Prinivil,Zestril,Lipitor,Vicodin,Brufen
Expiry dates [Database]: 01/09/2020,24/09/2020,21/10/2020,05/11/2020,06/11/2020
Expiry dates [Test]: 27/08/2020,11/09/2020,28/09/2020,13/11/2020,23/12/2020
-----------------------------------------------------------------------------------------------------------------------------
'''
