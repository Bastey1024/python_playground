class QuizBrain:
  def __init__(self,q_list):
    self.question_number=0
    self.score=0
    self.question_list= q_list
    
    

  def still_has_questions(self):
    return len(self.question_list) > self.question_number

  def check_answer(self,user_answer,correct_answer):
    if user_answer.lower() == correct_answer.lower():
      print("Right!")
      self.score+=1
          
    else:
      print("False!")
    print(f"The correct answer: {correct_answer}")
    print(f"Your current Score is : {self.score}/{self.question_number}")

   

     
  def next_question(self):
    
    current_question=self.question_list[self.question_number]
    self.question_number+=1
    user_answer=input(f"Q.{self.question_number} : {current_question.text}(True / False)")
    
    if self.still_has_questions():
      self.check_answer(user_answer,current_question.answer)
    else:
      print("You completet the Quiz!")
      print(f"Your final Score is : {self.score}/{self.question_number}")


    