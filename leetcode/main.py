import random
import importlib

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
def load_problems(category, var_name):
    """Load problems from a category file."""
    module = importlib.import_module(category)
    return getattr(module, var_name)

def get_random_problem(category, var_name):
    """Get a random problem from a specific category."""
    problems = load_problems(category, var_name)
    return random.choice(problems)

def display_problem(category, problem):
    """Display a problem and wait for user input before returning."""
    print(f"\nRandom problem from {category.replace('-', ' ').title()}:")
    print(problem)
    input("\nPress Enter to return to the menu...")

def main():
    while True:
        print("\nLeetCode Problem Selector")
        print("-------------------------")
        print("Categories:")
        for i, (category, _) in enumerate(categories, 1):
            print(f"{i}. {category.replace('-', ' ').title()}")
        print(f"{len(categories) + 1}. Random Category")
        print("0. Exit")

        choice = input("\nEnter your choice (0-19): ")

        if choice == "0":
            print("Thank you for using the LeetCode Problem Selector. Goodbye!")
            break

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

if __name__ == "__main__":
    main()
