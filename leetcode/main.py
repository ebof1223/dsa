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

def get_random_problem(category, var_name):
    """Get a random problem from a specific category."""
    problems = load_problems(category, var_name)
    if problems:
        return random.choice(problems)
    else:
        return "No problems available for this category."

def update_csv(category, problem, is_revisit=False):
    """Update the CSV file with the new problem or revisit information."""
    if not os.path.exists(CSV_FILE):
        print(f"Error: {CSV_FILE} does not exist. Please create it first.")
        return

    today = date.today().isoformat()
    
    # Read the entire CSV file
    rows = []
    with open(CSV_FILE, mode='r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)

    if is_revisit:
        # Find the row with the problem and update it
        for row in rows:
            if row[2] == problem:
                row.append(today)
                need_more_revisits = input("Do you need to revisit this problem again? (1: Yes, 2: No): ")
                if need_more_revisits == "2":
                    row.append("(D)")
                break
    else:
        # Add a new row for a new problem
        revisit = input("Does this problem need to be revisited? (1: Yes, 2: No): ")
        revisit = "Yes" if revisit == "1" else "No"
        rows.append([today, category, problem, revisit])

    # Write the updated data back to the CSV file
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    
    print(f"Progress updated in {CSV_FILE}")

def display_problem(category, problem, is_revisit=False):
    """Display a problem and update the CSV file."""
    print(f"\nProblem from {category.replace('-', ' ').title()}:")
    print(problem)
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
            if row[3] == "Yes" and "(D)" not in row:  # Check if it needs revisiting and isn't done
                revisit_problems.append((row[1], row[2]))  # (category, problem)

    if not revisit_problems:
        print("No problems to revisit.")
        return None, None

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
                problem = get_random_problem(category, var_name)
                display_problem(category, problem)
            elif 1 <= choice <= len(categories):
                category, var_name = categories[choice - 1]
                problem = get_random_problem(category, var_name)
                display_problem(category, problem)
            else:
                print("Invalid choice. Please try again.")
                input("Press Enter to continue...")
        except ValueError:
            print("Invalid input. Please enter a number.")
            input("Press Enter to continue...")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            input("Press Enter to continue...")

def main():
    if not os.path.exists(CSV_FILE):
        print(f"Warning: {CSV_FILE} does not exist. Please create it with the headers: Date,Concept,Problem,Needs Revisit")
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
            category, problem = get_revisit_problem()
            if category and problem:
                display_problem(category, problem, is_revisit=True)
            else:
                input("Press Enter to return to the main menu...")
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
