from data import question_data
from quiz_brain import QuizBrain
from question_model import Question

question_bank =[]




for i in range(0,len(question_data)):
  question=Question(question_data[i]["question"],question_data[i]["correct_answer"])
  question_bank.append(question)



quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
  quiz.next_question()


