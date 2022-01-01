question_promts = [
    "What color are apples?\n(a) Red/Green\n (b) purple\n\n",
    "What i like?\n(a) money\n (b) codeing\n\n",
    "Which city is pretty?\n(a) lahore\n (b) karachi\n\n",
]

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

questions = [
    Question(question_promts[0], "b"), 
    Question(question_promts[1], "a"), 
    Question(question_promts[2], "a")
]

def run_test(questions):
    score = 0
    for Question in questions:
        answer = input(Question.prompt)
        if answer == Question.answer:
            score +=1

        print(f"you got {score} / {len(questions)}")

run_test(questions)