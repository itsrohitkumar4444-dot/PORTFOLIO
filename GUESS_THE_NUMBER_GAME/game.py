import random 
upper_limit = int(input("enter the upper limit:"))#taking upper limit from user
lower_limit = int(input("enter the lower limit:"))#taking lower limit from user
number = random.randint(lower_limit, upper_limit)#generating random number in givem range by using randint function as it includes both the limits
print("you have only 5 chances to guess the number")#informing user about number of chances
for i in range(1,6):#for is used for easier approach, use of while loop is also possiblle
    guess = int(input("Enter your Guess :"))#taking the guessed number fro user 
    if guess == number: #if the guess is correct
        print("Congratulations you guessed the number")
        break #break statement for coming out of the for loop
    else:
        print("wrong guess")#if the guess is wrong
        print(f"you have {5-i} chances left")#informing user about remaining chances
        if guess < number:#if guessed number is less than the actual number
            print("your guess is low")
        else:#if guessed number is greater than the actual number
            print("your guess is high")
print(f"You were unable to guess the number which is {number}")#printing the actual number after all chances are over