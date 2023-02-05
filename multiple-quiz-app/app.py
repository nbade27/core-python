from Question import Question
questions_prompts = [
    "What color are Apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n",
]

questions = [
    Question(questions_prompts[0],"a"),
    Question(questions_prompts[1],"c"),
    Question(questions_prompts[2],"b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
           score = score+1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")


run_test(questions)
