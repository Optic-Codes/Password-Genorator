import random

chars = 'abcdefghijklmnopqurstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZlmnopqurstuvwxyzABCDEFGHIJK1234567890!@$%^&*(_-+=>?/`~'

def invalid_option():
    new_choice = input('invalid option, enter 1 to genorate a new password or 2 to exit.')
    if new_choice == '2':
        quit()
    elif new_choice == '1': 
        pass
    else:
        invalid_option()

while 1:
    menue_choice = input('Menue: Continue(1)   Quit(2)')
    if menue_choice == '2':
            quit()
    elif menue_choice == '1':
            pass
    else:
            invalid_option()
    while menue_choice == '1':
        try:
            password_length = int(input('Password Length:'))
            password_count = int(input('Password Count:'))
            for x in range(0,password_count):
                password = ''
                for x in range(0, password_length):
                    password_char = random.choice(chars)
                    password = password + password_char
                print('password:', password)
                menue_choice = None
                break
        
        except:
            print('There was an error. Please try again and make sure that the password length and count where numbers.')
