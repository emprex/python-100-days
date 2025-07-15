questions = [
    {"question": "What is the capital of France?", "answer": "paris"},
    {"question": "What is 2 + 2?", "answer": "4"},
    {"question": "What color do you get by mixing red and blue?", "answer": "purple"}
]

score = 0

for q in questions:
    user_answer = input(q["question"] + " ").strip().casefold()
    if user_answer == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Incorrect. The correct answer was: {q['answer'].capitalize()}\n")

print(f"You scored {score} out of {len(questions)}.")
if score == len(questions):
    print("Excellent! You got all questions right!")
elif score >= len(questions) // 2:
    print("Good job! Keep practicing.")
else:
    print("Don't worry, try again to improve your score!")