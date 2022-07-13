class QuizBrain:

    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        correct_answer = current_question.answer
        user_answer = input(f"Q.{self.question_number+1} {current_question.text} (True/False): ")
        self.check_answer(user_answer, correct_answer)
        self.question_number += 1

    def check_answer(self, user_answer, correct_answer):
        # print(self.question_number)
        # current_question = self.question_list[self.question_number]
        # correct_answer = current_question.answer  # next_question() 안에 있으므로 반복됨
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"you got it right!  score so far : {self.score}")
        else:
            print("That's wrong")

    def still_has_questions(self):
        return self.question_number < len(self.question_list)