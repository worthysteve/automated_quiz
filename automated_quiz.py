import random
import json
import math

def load_questions():
    """
    Load questions from a local JSON file named 'questions.json'.

    Returns:
        list: A list of question dictionaries extracted from the JSON file.
    """
    with open("questions.json", "r") as f:
        questions = json.load(f)['questions']   
    return questions

def get_random_question(questions, used_questions):
    """
    Select a random question that has not yet been used.

    Args:
        questions (list): All available questions.
        used_questions (list): List of previously used questions.

    Returns:
        dict or None: A randomly selected question or None if all have been used.
    """
    remaining_questions = [q for q in questions if q not in used_questions]
    if len(remaining_questions) == 0:
        return None  # No more questions to ask
    return random.choice(remaining_questions)

def ask_question(question, points):
    """
    Display a question, prompt for user input, evaluate the response, and return result.

    Args:
        question (dict): The question to be asked.
        points (int): The number of points the question is worth.

    Returns:
        tuple: (result, question)
            - result (bool or str): True if correct, False if incorrect, 'exit' if user quits.
            - question (dict or None): The question object if answered, otherwise None.
    """
    print("\n" + question['question'])

    answer_options_dict = question['options'][0]  
    options_keys = {key.strip("."): key for key in answer_options_dict.keys()}  # Normalize keys

    # Display all options
    for key, original_key in options_keys.items():
        print(f"{original_key} {answer_options_dict[original_key]}")

    try:
        user_input = input("Select the correct option (A, B, C, or D) or type 'exit' or 'q' to quit: ").strip().upper()

        if user_input in ['EXIT', 'Q']:
            return 'exit', None

        if user_input not in options_keys:
            print("Invalid choice, defaulting to wrong answer.")
            return False, None

        # Extract correct answer
        correct_answer_key = list(question['answer'][0].keys())[0]
        correct_answer_value = question['answer'][0][correct_answer_key]

        if options_keys[user_input] == correct_answer_key:
            print(f"Your answer was '{correct_answer_key} {correct_answer_value}'! It is correct.")
            print(f"You got {points} point(s) for this question.")
            return True, question
        else:
            print(f"Your answer was '{options_keys[user_input]} {answer_options_dict[options_keys[user_input]]}'. Wrong answer.")
            print(f"The correct answer was '{correct_answer_key} {correct_answer_value}'.")
            print(f"You lost {points} point(s) for this question.")
            return False, question

    except Exception as e:
        print(f"Error: {e}")
        return False, None

def calculate_max_score(total_questions):
    """
    Calculate the maximum score possible using the batch-based scoring system.

    Args:
        total_questions (int): Total number of questions in the quiz.

    Returns:
        int: The highest achievable score.
    """
    max_score = 0
    batch = 1
    remaining_questions = total_questions

    while remaining_questions > 0:
        questions_in_batch = min(10, remaining_questions)  # Max 10 questions per batch
        max_score += batch * questions_in_batch  # Batch score = batch number × questions in batch
        remaining_questions -= 10
        batch += 1

    return max_score

def main():
    """
    Main function to control the flow of the quiz game.
    """
    print()
    print("Welcome to 'HOW SMART ARE YOU' quiz")
    print("Let's test your IQ and see how smart you are")

    questions = load_questions()
    total_questions = len(questions)
    max_possible_score = calculate_max_score(total_questions)  # Compute max possible score

    used_questions = []  
    score = 0  # Initialize the score
    wrong_answers = 0  # Counter for wrong answers
    question_counter = 0  # Tracks total questions asked

    while True:
        question = get_random_question(questions, used_questions)
        if not question:
            print("All questions have been used. Ending the quiz.")
            break

        batch_points = (question_counter // 10) + 1  # Points increase every 10 questions
        correct, question = ask_question(question, batch_points)

        if correct == 'exit':
            print(f"Thanks for playing! Your final score is: {score} out of {max_possible_score}.")
            break

        if correct:
            score += batch_points
            used_questions.append(question)
        else:
            wrong_answers += 1
            if wrong_answers == 10:
                print("\nYou've reached 10 wrong answers! Quiz over.")
                break

        question_counter += 1
        print(f"Your current total score is: {score} out of {max_possible_score}.\n")

    print(f"Your final score is: {score} out of {max_possible_score}.\n")

if __name__ == "__main__":
    main()
