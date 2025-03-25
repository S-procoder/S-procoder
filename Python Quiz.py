# Simple Python Quiz

def ask_question(question, options, correct_answer):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    try:
        answer = int(input("Your answer (1-4): "))
        if options[answer - 1] == correct_answer:
            return True
        else:
            return False
    except (ValueError, IndexError):
        print("Invalid input. Please select an option between 1 and 4.")
        return False

def main():
    print("Welcome to the Python Quiz!")
    score = 0
    
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Berlin", "Madrid", "Paris", "Rome"],
            "correct_answer": "Paris"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Earth", "Mars", "Jupiter", "Venus"],
            "correct_answer": "Mars"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["Atlantic", "Indian", "Arctic", "Pacific"],
            "correct_answer": "Pacific"
        },
        {
            "question": "Who wrote the play 'Romeo and Juliet'?",
            "options": ["Charles Dickens", "Mark Twain", "William Shakespeare", "Jane Austen"],
            "correct_answer": "William Shakespeare"
        }
    ]
    
    for q in questions:
        if ask_question(q['question'], q['options'], q['correct_answer']):
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect!\n")
    
    print(f"You finished the quiz! Your score is {score}/{len(questions)}.")

if __name__ == "__main__":
    main()
