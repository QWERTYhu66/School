# Bad:
# def doStuff():
#     total = 0
#     count = 0
#     while True:
#         try:
#             num = input("Enter a number (or type STOP): ")
#             if num == "STOP":
#                 if count > 0:
#                     if total > 0:
#                         if total < 1000000:
#                             print("Total is: " + str(total))
#                         else:
#                             print("Way too big!")
#                     else:
#                         if total == 0:
#                             print("Zero?")
#                         else:
#                             print("Negative?")
#                 else:
#                     print("No numbers?")
#                 break
#             else:
#                 x = int(num)
#                 if x > 0:
#                     total = total + x
#                     count = count + 1
#                 else:
#                     if x == 0:
#                         print("Why zero?")
#                     else:
#                         if x < 0:
#                             total = total + x
#                             count = count + 1
#                         else:
#                             print("???")
#         except:
#             print("That's not even a number?? try again...")
#             continue

# doStuff()

# Good:
# def doStuff():
#     total = count = 0
#     while True:
#         try:
#             num = input("Enter a number (or type STOP): ")
#             if num == "STOP":
#                 if count == 0:
#                     print("No numbers?")
#                 elif total > 0:
#                     print("Total is:", total) if total < 1000000 else print("Way too big!")
#                 elif total == 0:
#                     print("Zero?")
#                 else:
#                     print("Negative?")
#                 break
#             x = int(num)
#             if x == 0:
#                 print("Why zero?")
#             else:
#                 total += x
#                 count += 1
#         except:
#             print("That's not even a number?? try again...")
# doStuff()