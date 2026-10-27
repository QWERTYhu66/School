# Age Verifier
# while True:
#     age = input("Please enter your age: ")
#     try:
#         x = int(age)
#         if x > 120:
#             print("Please enter a valid age.")
#             continue
#         print(f"You are {x} years old.")
#         break
#     except ValueError:
#         print("Please enter a valid number.")

# List Average Calculator
# numbers = []
# while True:
#     num = input("Enter a number (or type 'done' to finish): ")
#     if num.lower() == 'done':
#         if not numbers:
#             print("No numbers were entered.")
#         else:
#             break
#     try:
#         x = int(num)
#         numbers.append(x)
#     except ValueError:
#         print("Please enter a valid number.")

# average = int(sum(numbers) / len(numbers))
# print(f"The average of the numbers is: {average}")

# def average(numbers):
#     if not numbers:
#         return 0

#     return sum(numbers) / len(numbers)

# nums = []

# while True:
#     try:
#         n = float(input("Enter number (-1 to quit): "))
#         if n == -1:
#             break
#         nums.append(n)

#     except ValueError:
#         print("Invalid input. Please enter a number.")

#     except KeyboardInterrupt:
#         print("\nProgram cancelled.")
#         break

# print("The average is:", average(nums))