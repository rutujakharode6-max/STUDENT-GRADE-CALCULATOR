import datetime

def calculate_grade(average):
    """Returns a letter grade based on the average mark using if/elif/else statements."""
    if 90 <= average <= 100:
        return 'A'
    elif 80 <= average < 90:
        return 'B'
    elif 70 <= average < 80:
        return 'C'
    elif 60 <= average < 70:
        return 'D'
    elif 0 <= average < 60:
        return 'F'
    else:
        return 'Invalid'

def get_grade_comment(letter_grade):
    """Returns personalized motivational comments for each grade level."""
    if letter_grade == 'A':
        return "Outstanding achievement! Keep aiming high."
    elif letter_grade == 'B':
        return "Great effort! You're doing very well."
    elif letter_grade == 'C':
        return "Good job, but there's room for improvement."
    elif letter_grade == 'D':
        return "You passed, but let's work harder next time."
    elif letter_grade == 'F':
        return "Don't give up! Seek some extra help and try again."
    else:
        return "No comment."

# ANSI escape codes for colors
class Colors:
    RESET = '\033[0m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    MAGENTA = '\033[95m'
    RED = '\033[91m'
    CYAN = '\033[96m'

def get_color_for_grade(grade):
    """Returns the ANSI escape code for the specific grade."""
    if grade == 'A': return Colors.GREEN
    elif grade == 'B': return Colors.CYAN
    elif grade == 'C': return Colors.YELLOW
    elif grade == 'D': return Colors.MAGENTA
    elif grade == 'F': return Colors.RED
    return Colors.RESET

def display_results_table(comprehensive_results):
    """Displays results in a formatted table using f-strings and color coding."""
    print("\n" + "="*105)
    print(f"{'Student Name':<15} | {'Subject 1':>9} | {'Subject 2':>9} | {'Subject 3':>9} | {'Average':>7} | {'Grade':^5} | {'Comments':<35}")
    print("-" * 105)
    for res in comprehensive_results:
        m1, m2, m3 = res['marks']
        color = get_color_for_grade(res['grade'])
        reset = Colors.RESET
        
        grade_str = f"{color}{res['grade']:^5}{reset}"
        
        print(f"{res['name']:<15} | {m1:>9.1f} | {m2:>9.1f} | {m3:>9.1f} | {res['average']:>7.2f} | {grade_str} | {res['comment']:<35}")
    print("=" * 105)

def display_statistics(class_average, highest_average, lowest_average, grade_counts, total_students):
    """Prints class statistics in a visually appealing boxed format."""
    print("\n" + "+" + "-"*35 + "+")
    print(f"|{'CLASS STATISTICS':^35}|")
    print("+" + "-"*35 + "+")
    print(f"| Total Students : {total_students:>16} |")
    print(f"| Class Average  : {class_average:>16.2f} |")
    print(f"| Highest Average: {highest_average:>16.2f} |")
    print(f"| Lowest Average : {lowest_average:>16.2f} |")
    print("+" + "-"*35 + "+")
    print(f"|{'GRADE DISTRIBUTION':^35}|")
    print("+" + "-"*35 + "+")
    for g in ['A', 'B', 'C', 'D', 'F']:
        color = get_color_for_grade(g)
        reset = Colors.RESET
        print(f"| Grade {color}{g}{reset}        : {grade_counts[g]:>16} |")
    print("+" + "-"*35 + "+")
def search_student(comprehensive_results):
    """Searches for a student by name (case-insensitive, partial match)."""
    query = input("\nEnter student name to search: ").strip().lower()
    found_students = []
    # Use loops to find partial name matches
    for res in comprehensive_results:
        if query in res['name'].lower():
            found_students.append(res)
            
    if found_students:
        display_results_table(found_students)
    else:
        print("\n[!] Student not found.")

def save_to_file(comprehensive_results, class_average, highest_average, lowest_average, grade_counts):
    """Exports results to a .txt file with a timestamped filename."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"student_report_{timestamp}.txt"
    try:
        with open(filename, 'w') as f:
            f.write("="*105 + "\n")
            f.write(f"{'Student Name':<15} | {'Subject 1':>9} | {'Subject 2':>9} | {'Subject 3':>9} | {'Average':>7} | {'Grade':^5} | {'Comments':<35}\n")
            f.write("-" * 105 + "\n")
            for res in comprehensive_results:
                m1, m2, m3 = res['marks']
                f.write(f"{res['name']:<15} | {m1:>9.1f} | {m2:>9.1f} | {m3:>9.1f} | {res['average']:>7.2f} | {res['grade']:^5} | {res['comment']:<35}\n")
            f.write("=" * 105 + "\n\n")
            
            f.write("+" + "-"*35 + "+\n")
            f.write(f"|{'CLASS STATISTICS':^35}|\n")
            f.write("+" + "-"*35 + "+\n")
            f.write(f"| Total Students : {len(comprehensive_results):>16} |\n")
            f.write(f"| Class Average  : {class_average:>16.2f} |\n")
            f.write(f"| Highest Average: {highest_average:>16.2f} |\n")
            f.write(f"| Lowest Average : {lowest_average:>16.2f} |\n")
            f.write("+" + "-"*35 + "+\n")
            f.write(f"|{'GRADE DISTRIBUTION':^35}|\n")
            f.write("+" + "-"*35 + "+\n")
            for g in ['A', 'B', 'C', 'D', 'F']:
                f.write(f"| Grade {g}        : {grade_counts[g]:>16} |\n")
            f.write("+" + "-"*35 + "+\n")
        print(f"\n[+] Successfully saved report to {filename}")
    except Exception as e:
        print(f"\n[!] Error saving to file: {e}")

def main_menu(comprehensive_results, class_average, highest_average, lowest_average, grade_counts):
    """Displays the interactive menu system using a while loop."""
    while True:
        print("\n" + "="*30)
        print(f"{'MAIN MENU':^30}")
        print("="*30)
        print("1) View All Results")
        print("2) Search Student")
        print("3) Save to File")
        print("4) View Statistics")
        print("5) Exit")
        print("="*30)
        
        try:
            choice = input("Enter your choice (1-5): ").strip()
            if choice == '1':
                display_results_table(comprehensive_results)
            elif choice == '2':
                search_student(comprehensive_results)
            elif choice == '3':
                save_to_file(comprehensive_results, class_average, highest_average, lowest_average, grade_counts)
            elif choice == '4':
                display_statistics(class_average, highest_average, lowest_average, grade_counts, len(comprehensive_results))
            elif choice == '5':
                print("\nExiting application. Goodbye!")
                break
            else:
                print("\n[!] Invalid choice. Please enter a number between 1 and 5.")
        except KeyboardInterrupt:
            print("\n\n[!] Program interrupted by user (Ctrl+C). Returning to menu...")
            continue
        except Exception as e:
            print(f"\n[!] An unexpected error occurred: {e}")

def main():
    # Ask how many students to process (1-50) using a while loop with try-except validation
    while True:
        try:
            num_students = int(input("How many students would you like to process (1-50)? "))
            if 1 <= num_students <= 50:
                break
            else:
                print("Please enter a number specifically between 1 and 50.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    # Initialize empty lists for student names, subject marks, and final grades
    student_names = []
    subject_marks = []
    final_grades = []

    # Process each student using a for loop iterating through the number of students
    for i in range(num_students):
        print(f"\n--- Student {i+1} ---")
        
        # Validate student name is a non-empty string
        while True:
            name = input("Enter student name: ").strip()
            if name:
                student_names.append(name)
                break
            else:
                print("Validation Error: Name cannot be empty. Please enter a valid string.")
        
        # Use a nested while loop to collect exactly 3 subject marks
        marks = []
        for subject in range(1, 4):
            while True:
                try:
                    mark_input = input(f"Enter mark for subject {subject} (0-100): ")
                    mark = float(mark_input)
                    if 0 <= mark <= 100:
                        marks.append(mark)
                        break
                    else:
                        print("Validation Error: Mark out of range! It must be between 0 and 100.")
                except ValueError:
                    print("ValueError caught: Invalid input. You must enter a numeric value.")
        
        # Store the three marks as sublists in a master marks list
        subject_marks.append(marks)
        
    # Process the collected data
    comprehensive_results = []
    
    # Iterate through the marks list using for loops to calculate each student's average
    for i in range(len(subject_marks)):
        name = student_names[i]
        marks = subject_marks[i]
        
        # Calculate average and round to 2 decimal places
        average = round(sum(marks) / len(marks), 2)
        
        # Call the grading functions
        grade = calculate_grade(average)
        comment = get_grade_comment(grade)
        
        # Store results in a comprehensive results list containing dictionaries
        comprehensive_results.append({
            'name': name,
            'marks': marks,
            'average': average,
            'grade': grade,
            'comment': comment
        })
        final_grades.append(grade)

    # Calculate class statistics using built-in Python functions and list comprehensions
    if comprehensive_results:
        all_averages = [res['average'] for res in comprehensive_results]
        class_average = round(sum(all_averages) / len(all_averages), 2)
        highest_average = max(all_averages)
        lowest_average = min(all_averages)
        
        # Count of each grade (A, B, C, D, F)
        grade_counts = {
            'A': final_grades.count('A'),
            'B': final_grades.count('B'),
            'C': final_grades.count('C'),
            'D': final_grades.count('D'),
            'F': final_grades.count('F')
        }
        
        # Launch the interactive menu
        main_menu(comprehensive_results, class_average, highest_average, lowest_average, grade_counts)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[!] Program interrupted by user (Ctrl+C). Exiting gracefully.")
