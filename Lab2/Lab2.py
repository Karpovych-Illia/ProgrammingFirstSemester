
"""
Лаба 2 Створити консольну міні програму.
Користувач повинен побачити перелік всіх виставлених оцінок якщо правлиьно введе логін та пароль від своєї імітованої обліковки.
Також повинен побачити кількість оцінок від 5 до 12 задовільно та від 1 до 4 незадовільно.
Оцінки це список для кожного існуючого користувача новий мінімум 4 користувача.
"""


database = [
    {
    "name": "Nazar",
    "password": "123123",
    "grades": [1,2,2,4,2,1,10,2]
    },
    {
        "name": "Vasya",
        "password": "000000",
        "grades": [9,10,10,9,12,7,10,9]
    },
    {
        "name": "Petya",
        "password": "123456",
        "grades": [3,6,7,8,9,10,12]
    },
    {
        "name": "Kolya",
        "password": "654321",
        "grades": [11, 9, 12, 10, 9, 12, 4]
    }
]

login_name = input("Enter your name: ")
login_password = input("Enter your password: ")

found = False

for user in database:
    if user["name"] == login_name and user["password"] == login_password:
        found = True
        print("You logged in successfully!")
        print("Your grades:")
        good_grades = 0
        bad_grades = 0
        for grade in user["grades"]:
            print(grade)
            if 5 <= grade <= 12:
                good_grades += 1
            elif 1 <= grade <= 4:
                bad_grades += 1
        print("Good grades:" , good_grades)
        print("Bad grades:" , bad_grades)
        break

if found == False:
    print("Uncorrect login or password!")

