"""
code description 
this function takes integer age as argument and print is old or will be old 
"""
def ageMachine(age):
        if age > 50:
            print("Du bist alt geworden!")
        else:
            print("Aha")

"""
this function accepts two integer as argument and add them 
"""
def addTwoNumber(first_number:int , second_number:int)->int:
    return first_number+second_number


result = addTwoNumber(5,6)
print(f"it is result:{result}")




print("wie alt bist du?")
#input function return is always a string
age_from_user = input()

ageMachine(age_from_user)