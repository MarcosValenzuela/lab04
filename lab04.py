 """
 main
    question = "What is the capital of California? "
    answer = "Sacramento"
    ask(question, answer)

 ask
    tries = 0
    loop three times
        increment tries
        ask user input
        check user input is equal to answer
            if so, print "Correct" then exit loop
    if not correct
        print to the user  "You have used up you all your guesses."
        print the correct answer "The answer is 'Sacramento'"

main
"""