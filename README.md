This code is a simple program that checks the strength of a password and evaluates its strength using a few different criteria. The application allows the user to enter a password and then displays how many lowercase letters, uppercase letters, numbers, spaces, and special characters the password contains. Based on the number of each of these types, a score is given to the password. Based on this score, the user is then presented with an opinion for password strength. Also, the app allows the user to enter or exit to check the strength of a new password.

In fact, this program contains two main functions:

1. `check_password_strength()`: This function takes the password input from the user, counts the number of each type of character (lowercase letters, uppercase letters, numbers, spaces and special characters), calculates the points for each type, and Based on the total score, it gives the user an opinion on the strength of the password.

2. `check_pwd()`: This function asks the user if they want to check a new password, and then based on the user's input, asks them if they want to continue.

When the program runs (`__name__ == '__main__'`), the user is greeted and then allowed to check their password. The program then continues in a loop until the user wants to check another password or exit.

You can run this program and check the score and description by entering different passwords!
