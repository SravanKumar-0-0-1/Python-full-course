#Quiz-game: This is simple quiz game for the practice of lists,tuples, set and if loop and for loop
# this game check your answers scored based on the answerrs and shows the real answers and yours in the final.

questions=["1.what  is the most trending language in 2024:"
           ,"2.which ai is used in google:"
           ,"3.which state is fruit bowl of india:"
           ,"4.what is the fastest animal:"
           ,"5.what is the extension for python file:"]
options=[["A.Python","B.Java","C.C","D.C++"],
         ["A.Alexa","B.GeminiAI","C.chatgpt","D.deepsearch"],
         ["A.Goa","B.Mumbai","C.Kerala","D.Telangana"],
         ["A.ostrich","B.Horse","C.Tiger","D.Cheeth"],
         ["A..java","B..py","C..xl","D..cpp"]]
answers=["A","B","C","D","B"]
guesses=[]
question_num=0
score=0

for question in questions:
    print("-----------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess=input("Enter your answer(A,B,C,D): ").upper()
    guesses.append(guess)
    if guess==answers[question_num]:
        print("Correct")
        score+=1
    else:
        print("Incorrect")
        print(f"The correct answers is{answers[question_num]}")
    question_num+=1

print("-----------------------------")
print("answers:",end="")
for answer in answers:
    print(answer,end=" ")
print()
print("guesses:",end="")
for guess in guesses:
    print(guess,end=" ")
print()
score=int(score/len(questions)*100)
print(f"Your score is: {score}")