#!/usr/bin/python3
# imports from all the other files in project
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# makes a blank list for all the questions
question_bank = []

# for each question in question_model.py
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    # Takes created variables above and inputs the question and answer into a question bank
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Makes the object 'quiz' and inserts the question bank into the class
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")