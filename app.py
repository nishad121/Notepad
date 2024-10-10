# quiz.py

# Define the questions and answers
QUESTIONS = {
    "What is the capital of France?": ["Paris", "London", "Berlin", "Madrid"],
    "Which planet is known as the Red Planet?": ["Earth", "Mars", "Venus", "Mercury"],
    "Who painted the Mona Lisa?": ["Leonardo da Vinci", "Michelangelo", "Rembrandt", "Vincent van Gogh"]
}

# Function to conduct the quiz
def quiz():
    score = 0
    total_questions = len(QUESTIONS)
    
    for question, alternatives in QUESTIONS.items():
        print(f"\nQuestion: {question}")
        
        for i, alternative in enumerate(alternatives):
            print(f"{i + 1}. {alternative}")
        
        answer = input("\nEnter your choice (1-4): ")
        
        if answer.isdigit() and 1 <= int(answer) <= 4:
            if alternatives[0] == alternatives[int(answer) - 1]:
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect. The correct answer was {alternatives[0]}.")
        else:
            print("Invalid input. Please enter a number between 1 and 4.")
    
    print(f"\nQuiz finished! Your final score is {score}/{total_questions}")

# Main program loop for retaking the quiz
def main():
    while True:
        quiz()
        play_again = input("\nWould you like to retake the quiz? (yes/no): ").lower()
        if play_again != "yes":
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()
