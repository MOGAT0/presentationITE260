import time
def txt(string):
    b = list(string)
    for word in b:
        print(word, end="", flush=True)
        time.sleep(0.05)
txt("Hello there!\nWelcome to our python Project\n")
txt("\nIn this project we have two programs a user can use")
txt("\nThis include Addition game and Quiz game\n")
txt("\nIn order to use any of this program just type\n1  for Addition game\n2  for Quiz game and\n0 to Quit\n")

def main():
    txt('\nWhat program you would like to use? ')
    Q1 = input()

    if Q1 >= '3':
        txt("\nThe number you have entered is not on the list\nPlease try again\n")
        main()

    if Q1 == '1':
        txt("\nWELCOME TO OUR ADDITION GAME\n")
        txt("Let's get started!\n")
        while True:
            from random import randint
            score = 0
            for i in range(5):
                f1 = randint(0, 100)
                f2 = randint(0, 100)
                rd = f1 + f2
                print(f1, "+", f2, "=")
                ans = float(input())
                if ans == rd:
                    score+=1
                else:
                    score+=0
            print("You got", score, "out of ", i + 1)

            brk2 = input("Would you like to continue?(Y/N): ")
            if brk2.upper() == 'N':
                main()
    
    if Q1 == '2':
        txt("\nWELCOME TO OUR QUIZ GAME")
        txt("\nLet's get started!\n")
        txt("\n(Note* Wrong Spelling Wrong!)")
        while True:
            score = 0
            cnt = 0
            ques1 = input("\nWhat stands for CPU?\n")
            if ques1.lower() == 'central processing unit':
                print("Correct!")
                score += 1
                cnt += 1
            else:
                print("Incorrect!")
                cnt += 1
            
            ques2 = input("\nWhat stands for PSU?\n")
            if ques2.lower() == 'power supply unit':
                print('Correct!')
                score += 1
                cnt += 1
            else:
                print("Incorrect")
                cnt += 1
            
            ques3 = input("\nWhat stands for RAM?\n")
            if ques3.lower() == 'random access memory':
                print("Correct!")
                score += 1
                cnt += 1
            else:
                print("Incorrect!")
                cnt += 1
            
            ques4 = input("\nIt is a battery that updates time and date of a computer even if it's turned off\n")
            if ques4.lower() == 'cmos battery' or ques4.lower() == 'cmos':
                print("Correct!")
                score += 1
                cnt += 1
            else:
                print("Incorrect!")
                cnt += 1
            
            ques5 = input("\nIt inputs information into the computer\n")
            if ques5.lower() == 'keyboard':
                print("Correct!")
                score += 1
                cnt += 1
            else:
                print("Incorrect!")
                cnt += 1

            txt("You got " + str(score) + " out of " + str(cnt) + "\n")

            brk3 = input("Would you like to continue?(Y/N): ")
            if brk3.upper() == 'N':
                main()
                
    if Q1 == '0':
        txt("Thank you for using our program!\n")
        quit()
            
main()