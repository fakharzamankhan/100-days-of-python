class QuizBrain:

    def __init__(self,q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        inputted_answer=input(f"Q. {self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(inputted_answer,current_question.answer)


    def still_has_question(self):
        #method 1
        return self.question_number < len(self.questions_list)
        #method 2
        # if self.question_number < len(self.questions_list):
        #     return True
        # else:
        #     return False

    def check_answer(self,u_answer,c_answer):
        if u_answer.lower() == c_answer.lower():
            print("You are Right! ")
            self.score += 1
        else:
            print("Wrong Answer! ")
        print(f"Correct Answer was: {c_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")



