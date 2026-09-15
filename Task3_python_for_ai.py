# Week 1 - Task 3
# Python for AI: Variables, Data Types, User Input, Operators
# AI Example Used: Predicting Pass/Fail based on marks 
#Temperature conversion for a weather AI
#Age eligibility checker



print("===== PART 1: Variables and Data Types =====")

# Variables holding different data types
student_name = "Rahul"          # string
student_marks = 78.5            # float
attempts = 2                    # integer
is_passed = True                # boolean

print("Name:", student_name, "| Type:", type(student_name))
print("Marks:", student_marks, "| Type:", type(student_marks))
print("Attempts:", attempts, "| Type:", type(attempts))
print("Passed (default):", is_passed, "| Type:", type(is_passed))

print("\n===== PART 2: Taking User Input =====")

# User input is always taken as a string, so we convert (typecast) it
name = input("Enter student name: ")
marks = float(input("Enter marks obtained (out of 100): "))

print("\n===== PART 3: Operators =====")

# Arithmetic operator - convert marks to percentage (already out of 100 here)
percentage = marks  # already a percentage in this example
print("Percentage:", percentage)

# Comparison operators - used to make the pass/fail decision
pass_mark = 40
is_pass = marks >= pass_mark
print("Is Pass (marks >= 40)?", is_pass)

# Logical operator - simple AI-style rule: distinction needs marks > 75 AND no backlog
has_backlog = False
is_distinction = (marks > 75) and (not has_backlog)

print("\n===== PART 4: Mini AI-style Decision (Pass/Fail Predictor) =====")

# This behaves like a very simple "Rule-Based AI" that predicts a result
if marks >= 90:
    result = "Excellent - Distinction"
elif marks >= 75:
    result = "Very Good - First Class"
elif marks >= pass_mark:
    result = "Pass"
else:
    result = "Fail"

print(f"Student: {name}")
print(f"Marks: {marks}")
print(f"Prediction: {result}")

# ---------------------------------------------------------
# BONUS EXAMPLE: Temperature Converter for a "Weather AI"
# ---------------------------------------------------------
print("\n===== BONUS: Temperature Converter (Weather AI) =====")
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} C is equal to {fahrenheit} F")

if fahrenheit > 95:
    advice = "It's very hot, stay hydrated!"
elif fahrenheit < 50:
    advice = "It's cold, wear something warm!"
else:
    advice = "The weather is pleasant."
print("AI Suggestion:", advice)
