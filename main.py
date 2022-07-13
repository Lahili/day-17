from data import question_data
from question_model import Question
from quizbrain import QuizBrain

question_bank = []
for index in range(len(question_data)):
    question_bank.append(Question(question_data[index]["text"], question_data[index]["answer"]))

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("\n")
print("You've completed the quiz")
print(f"Your final score was {quiz_brain.score}/{len(question_data)}")
# question_bank2 = []
# for data in question_data:
#     print(data)
#     data_text = data["text"]
#     data_answer = data["answer"]
#     question = Question(data_text, data_answer)
#     question_bank2.append(question)