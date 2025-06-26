# class MyError(Exception):
#     pass
#
# try:
#     raise MyError("Something custom went wrong!")
# except MyError as e:
#     print("Caught error:", e)
# class NegativeNumberError(Exception):
#     def __init__(self, number):
#         message = f"Invalid input: {number} is negative. Only positive numbers are allowed."
#         super().__init__(message)

# def check_positive(number):
#     if number < 0:
#         raise NegativeNumberError(number)
#     return number
#
# try:
#     check_positive(-10)
# except NegativeNumberError as e:
#     print("Custom exception caught:", e)

# class AgeTooLowError(Exception):
#     def __init__(self, age):
#         super().__init__(f"Age {age} is too low. Must be at least 18.")
#
# def check_age(age):
#     if age < 18:
#         raise AgeTooLowError(age)
#
# try:
#     check_age(16)
# except AgeTooLowError as e:
#     print("Validation failed:", e)

# class InvalidNameError(Exception):
#     def __init__(self, name):
#         super().__init__(f"Invalid name: '{name}'. Name must be at least 3 characters and contain only letters.")
#
#
# class InvalidScoreError(Exception):
#     def __init__(self, score):
#         super().__init__(f"Invalid score: {score}. Score must be between 0-100.")
#
#
# def validate_student(name, score):
#     # Validate name
#     if len(name) < 3 or not name.isalpha():
#         raise InvalidNameError(name)
#
#     # Validate score
#     if not (0 <= score <= 100):
#         raise InvalidScoreError(score)
#
#     return f"Valid student: {name} ({score}/100)"
#
#
# # Test cases
# test_cases = [
#     ("Amit", 85),  # Valid
#     ("Li", 90),  # Invalid name
#     ("Priya", 105),  # Invalid score
#     ("An2jali", 75)  # Invalid name (contains digit)
# ]
#
# for name, score in test_cases:
#     try:
#         print(validate_student(name, score))
#     except (InvalidNameError, InvalidScoreError) as e:
#         print(f"Validation failed: {e}")

# import re
#
# class InvalidEmailError(Exception):
#     def __init__(self, email):
#         super().__init__(f"Invalid email format: '{email}'")
#
# def check_email(email):
#     # Simple regex for demonstration (not exhaustive)
#     pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
#     if not re.match(pattern, email):
#         raise InvalidEmailError(email)
#     return True
#
# # Example usage
# try:
#     check_email("student@sanjivani.edu")
#     print("Email is valid.")
#     check_email("not-an-email")
# except InvalidEmailError as e:
#     print(e)
#
# class FailedException(Exception):
#     def __init__(self,marks):
#         message = f"You have failed exam {marks}"
#         super().__init__(message)
#
# try:
#     marks = 34
#     if(marks<75):
#         raise FailedException(marks)
# except FailedException as e:
#     print(e)





