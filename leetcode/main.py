import random
import importlib
import csv
from datetime import date
import os

# List of all category files with their corresponding variable names
categories = [
    ("arrays-hashing", "array_and_hashing_problems"),
    ("two-pointer", "two_pointer_problems"),
    ("stack", "stack_problems"),
    ("binary-search", "binary_search_problems"),
    ("sliding-window", "sliding_window_problems"),
    ("linked-lists", "linked_list_problems"),
    # ("trees", "trees_problems"),
    # ("tries", "trie_problems"),
    # ("heap-priority-que", "heap_priority_queue_problems"),
    # ("backtracking", "backtracking_problems"),
    # ("graphs", "graph_problems"),
    # ("advanced-graphs", "advanced_graph_problems"),
    # ("one-d-dp", "one_d_dp_problems"),
    # ("two-d-dp", "two_d_dp_problems"),
    # ("greedy", "greedy_problems"),
    # ("intervals", "interval_problems"),
    # ("math-geometry", "math_and_geometry_problems"),
    # ("bit-manipulation", "bit_manipulation_problems")
]
CSV_FILE = 'leetcode_progress.csv'

def load_problems(category, var_name):
    """Load problems from a category file."""
    try:
        module = importlib.import_module(category)
        problem_list = getattr(module, var_name)
        if not problem_list:
            print(f"Warning: Problem list for {category} is empty.")
        return problem_list
    except ImportError:
        print(f"Error: Could not import module {category}.")
        return []
    except AttributeError:
        print(f"Error: Could not find variable {var_name} in module {category}.")
        return []

def get_problem_by_difficulty(category, var_name):
    """Get a problem from a specific category based on difficulty progression."""
    problems = load_problems(category, var_name)
    if not problems:
        return "No problems available for this category."

    attempted_problems = set()
    with open(CSV_FILE, mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            if row[1] == category:
                attempted_problems.add(row[3])  # row[3] is the problem name

    available_problems = [p for p in problems if p[1] not in attempted_problems]

    if not available_problems:
        return "All problems in this category have been attempted."

    easy_problems = [p for p in available_problems if p[0] == 1]
    medium_problems = [p for p in available_problems if p[0] == 2]
    hard_problems = [p for p in available_problems if p[0] == 3]

    if easy_problems:
        return random.choice(easy_problems)
    elif medium_problems:
        return random.choice(medium_problems)
    elif hard_problems:
        return random.choice(hard_problems)
    else:
        return "No new problems available in this category."

def update_csv(category, problem, is_revisit=False):
    """Update the CSV file with the new problem or revisit information."""
    if not os.path.exists(CSV_FILE):
        print(f"Error: {CSV_FILE} does not exist. Please create it first.")
        return

    today = date.today().isoformat()
    difficulty = 'Easy' if problem[0] == 1 else 'Medium' if problem[0] == 2 else 'Hard'
    
    rows = []
    with open(CSV_FILE, mode='r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)

    if is_revisit:
        for row in rows:
            if row[3] == problem[1]:  # row[3] is now the problem name
                row.append(today)
                need_more_revisits = input("Do you need to revisit this problem again? (1: Yes, 2: No): ")
                if need_more_revisits == "2":
                    row.append("(D)")
                break
    else:
        revisit = input("Does this problem need to be revisited? (1: Yes, 2: No): ")
        revisit = "Yes" if revisit == "1" else "No"
        rows.append([today, category, difficulty, problem[1], revisit])

    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    
    print(f"Progress updated in {CSV_FILE}")

def display_problem(category, problem, is_revisit=False):
    """Display a problem and update the CSV file."""
    print(f"\nProblem from {category.replace('-', ' ').title()}:")
    print(f"Difficulty: {problem[0]}")
    print(problem[1])  # problem[1] is the problem name
    update_csv(category, problem, is_revisit)
    input("\nPress Enter to return to the menu...")

def get_revisit_problem():
    """Get a random problem that needs revisiting from the CSV file."""
    if not os.path.exists(CSV_FILE):
        print(f"Error: {CSV_FILE} does not exist.")
        return None, None

    revisit_problems = []
    with open(CSV_FILE, mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            if row[4] == "Yes" and "(D)" not in row:  # row[4] is now the "Needs Revisit" column
                revisit_problems.append((row[1], row[2], row[3]))  # (category, difficulty, problem)

    if not revisit_problems:
        print("No problems to revisit.")
        return None, None, None

    return random.choice(revisit_problems)

def grind_menu():
    """Display the grind menu with all categories."""
    while True:
        print("\nLeetCode Problem Selector")
        print("-------------------------")
        print("Categories:")
        for i, (category, _) in enumerate(categories, 1):
            print(f"{i}. {category.replace('-', ' ').title()}")
        print(f"{len(categories) + 1}. Random Category")
        print("0. Back to Main Menu")

        choice = input("\nEnter your choice (0-19): ")

        if choice == "0":
            return

        try:
            choice = int(choice)
            if choice == len(categories) + 1:
                category, var_name = random.choice(categories)
            elif 1 <= choice <= len(categories):
                category, var_name = categories[choice - 1]
            else:
                print("Invalid choice. Please try again.")
                input("Press Enter to continue...")
                continue

            problem = get_problem_by_difficulty(category, var_name)
            if isinstance(problem, str):
                print(problem)
                input("Press Enter to continue...")
            else:
                display_problem(category, problem)
        except ValueError:
            print("Invalid input. Please enter a number.")
            input("Press Enter to continue...")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            input("Press Enter to continue...")

def main():
    if not os.path.exists(CSV_FILE):
        print(f"Warning: {CSV_FILE} does not exist. Please create it with the headers: Date,Category,Difficulty,Problem,Needs Revisit")
        input("Press Enter to continue...")

    while True:
        print("\nLeetCode Practice App")
        print("---------------------")
        print("1. Grind (New Problems)")
        print("2. Revisit")
        print("0. Exit")

        choice = input("\nEnter your choice (0-2): ")

        if choice == "0":
            print("Thank you for using the LeetCode Practice App. Goodbye!")
            break
        elif choice == "1":
            grind_menu()
        elif choice == "2":
            category, difficulty, problem = get_revisit_problem()
            if category and difficulty and problem:
                display_problem(category, (difficulty, problem), is_revisit=True)
            else:
                input("Press Enter to return to the main menu...")
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
