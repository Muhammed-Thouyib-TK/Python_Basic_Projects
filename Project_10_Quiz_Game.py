Question_bank = [
    {'qns':'Which is the Truncation Division Operator ?','ans':'c'},
    {'qns':'Which of the following ML Algorithm Is Particularly useful for Identifying the most important features in a dataset ?','ans':'c'},
    {'qns':'The Correlation learning rule is a modified version of which learning Algorithm ?','ans':'a'},
    {'qns':'Which of the Following is not a Python Keyword ?','ans':'b'}
    ]
Answer_Bank = [['A. /','B. %','C. //','D. |'],
               ['A. Decision Trees','B. SVM','C. Random Forest','D. Linear Regression'],
               ['A. Hebbian Learning','B. Perceptron Learning','C. Delta Learning','D. LMS Learning'],
               ['A. assert','B. eval','C. nonlocal','D. pass']]


Score = 0
Total = 0

def intro_section(): # intro section
    print(f"{'='*50} \nWelcome to My Quiz Game \n{'='*50}")

def match_make(): # match make
    for key in range(len(Question_bank)):
        print(Question_bank[key]['qns'])
        for i in Answer_Bank[key]:
            print(i) 
        choice = input("Enter Your Choice : ").lower()
        global Total
        Total += 1
        checker(choice,key)

def checker(choice,key): # checker
        if choice == Question_bank[key]['ans']:
            global Score
            Score += 1
            print(f"Your Score {Score}/{Total}")
        else:
            print(f"Incorrect Answer \nCorrect Answer Is {Question_bank[key]['ans']}")
            print(f"Your Score {Score}/{Total}")
        print(f'\n{'-'*50} \n')


def main():
    intro_section()
    match_make()
    print(f"You Have Given {Score} Correct Answers \nYour Score Is {(Score/Total)*100}")
main()
    