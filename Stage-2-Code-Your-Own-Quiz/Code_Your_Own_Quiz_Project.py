# Easy quiz - Itsy-Bitsy Spider
easy_quiz ="The itsy-bitsy _1____ climbed up the water _2___. \
Down came the _3__ and washed the spider out.Out came the _4__ and dried up \
all the rain. And the itsy-bitsy spider climbed up the spout again"


# A list of blank numbers to be passed into the start_quiz function
parts_of_lyrics_easy  = ["_1____", "_2___", "_3__", "_4__"]

# Correct answers for easy quiz
correct_answers_easy = ["spider", "spout", "rain", "sun"]


# Medium quiz - Let it go
medium_quiz ="Don't let them in, don't let them see. Be the good _1__ you always\
have to be. Conceal,don't feel, don't let them know. Well now they know. \
Let it go, let it go. Can't hold it back _2_____.Let it go, let it go. \
Turn away and slam the door. I don't _3__ what they're going to say. \
Let the _4___ rage on.The cold never bothered me _5____"


parts_of_lyrics_medium = ["_1__", "_2_____", "_3__", "_4___", "_5____"]

correct_answers_medium = ["girl", "anymore", "care", "storm", "anyway"]


# Hard quiz - Hello by Adele
hard_quiz = "Hello, it's _1. I was _2_______ if after all these years you'd \
like to meet. To go over everything. They say that time's supposed to heal ya.\
But I ain't done much _3_____. Hello, can you _4__ me. I'm in _5________ dreamin\
g about who we used to be. When we were _6_____ and free. I've forgotten how it\
felt before the world fell at our feet"

parts_of_lyrics_hard = ["_1", "_2_______", "_3_____", "_4__", "_5________", "_6_____"]

correct_answers_hard = ["me", "wondering", "healing", "hear", "California", "younger"]


# Level-choosing function: Ask user to choose quiz level
def choose_level():
	level = input("Which level would you like to try? (easy/ medium/ hard) ")
	while level not in ["easy", "medium", "hard"]:#not in() is great here
		level = input("Please input easy/ medium/ hard. Which level? ")
	if level == "easy":
		start_quiz(easy_quiz, parts_of_lyrics_easy, correct_answers_easy)
	elif level == "medium":
		start_quiz(medium_quiz, parts_of_lyrics_medium, correct_answers_medium)
	else:
		start_quiz(hard_quiz, parts_of_lyrics_hard, correct_answers_hard)

# Game_play function: ask first question and check if it is correct or not
def start_quiz(quiz, blanks, answers):
    """
    1.blanks = parts_of_lyrics, show the quiz to the player\
    2.then count blanks by len()\
    3.count how many quiz left by range(1,5) (means [1,2,3,4,5])\
    4.input() means show player the question
    """
    print (quiz)
    num_blanks = len(blanks)
    for quiz_num in range(0, num_blanks):
        user_input = input("What's " + blanks[quiz_num] + "? ") #show player the quiz number
        #if the answer incorrect
        while answer_incorrect(user_input, answers[quiz_num]):
            user_input = input("oohoh.. incorrect. Try again. What's " + blanks[quiz_num] + "? ")
            quiz = quiz.replace(blanks[quiz_num], answers[quiz_num]) #if answer correct show him next number
            print (quiz)
		#num_blanks - 1 since Python is 0 based
        if quiz_num == num_blanks - 1:
                print ("Congratulations! You finished the quiz.")

# Compare answer function: convert user_input and correct_answer to lower case and compare if it is incorrect
def answer_incorrect(user_input, correct_answer):
	user_input = user_input.lower()
	""" .lower()is change Upper case to lower case, like A to a"""
	correct_answer = correct_answer.lower()
	return user_input != correct_answer


# Main operating area
def main():
	choose_level()
	
main()

#Summary
#In this project I use the functions includ:
#def()
#while()
#not in()
#if() elif() else()
#for()in()
#input()
#len()
#.lower()
#range()
