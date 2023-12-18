import string
import getpass


def check_password_strength():
   password = getpass.getpass('پسورد خودتو وارد کن: ')
   strength = 0
   remarks = ''
   lower_count = upper_count = num_count = wspace_count = special_count = 0

   for char in list(password):
       if char in string.ascii_lowercase:
           lower_count += 1
       elif char in string.ascii_uppercase:
           upper_count += 1
       elif char in string.digits:
           num_count += 1
       elif char == ' ':
           wspace_count += 1
       else:
           special_count += 1

   if lower_count >= 1:
       strength += 1
   if upper_count >= 1:
       strength += 1
   if num_count >= 1:
       strength += 1
   if wspace_count >= 1:
       strength += 1
   if special_count >= 1:
       strength += 1

   if strength == 1:
       remarks = ('این خیلی بده!'
           ' سریع پسوردتو عوض کن')
   elif strength == 2:
       remarks = ('این پسورد ضعیفه!'
           ' باید پسورد قوی تری انتخاب کنی')
   elif strength == 3:
       remarks = 'پسوردت خوبه. اما خیلی قوی نیست'
   elif strength == 4:
       remarks = ('حدس پسوردت سخته'
           ' ولی میتونی سخت ترش هم بکنی')
   elif strength == 5:
       remarks = ('این خوبه باریکلاااااا!!!!!'
           ' هکر هیچ غلطی نمیتونهه بکنه :)')

   print('Your password has:-')
   print(f'{lower_count} lowercase letters')
   print(f'{upper_count} uppercase letters')
   print(f'{num_count} digits')
   print(f'{wspace_count} whitespaces')
   print(f'{special_count} special characters')
   print(f'Password Score: {strength / 5}')
   print(f'Remarks: {remarks}')


def check_pwd(another_pw=False):
   valid = False
   if another_pw:
       choice = input(
           'Do you want to check another password\'s strength (y/n) : ')
   else:
       choice = input(
           'Do you want to check your password\'s strength (y/n) : ')

   while not valid:
       if choice.lower() == 'y':
           return True
       elif choice.lower() == 'n':
           print('Exiting...')
           return False
       else:
           print('Invalid input...please try again. \n')


if __name__ == '__main__':
   print('== Welcome to Password Strength Checker fllow madgod.dev==')
   check_pw = check_pwd()
   while check_pw:
       check_password_strength()
       check_pw = check_pwd(True)