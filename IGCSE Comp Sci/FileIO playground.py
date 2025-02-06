import csv

# with open("my_file.txt", "w") as file:
#     while True:
#         line = input("Enter a line (or type 'exit' to stop): ")
#         if line.lower() == "exit":
#             break
#         file.write(line + "\n")

# with open("shakespeare.txt", "r") as shakespeare:
#     hamlet = 0
#     goat = 0
#     for line in shakespeare:
#         if "Hamlet" in line:
#             hamlet += 1
#             with open("HAMLET.txt", "a") as hamlet_file:
#                 hamlet_file.write(str(line) + "\n")
#         elif "Goat" in line:
#             goat += 1
#     print(f"Hamlet: {hamlet}, Goat: {goat}")

# with open("ramen-ratings.csv", "r"):
#     countries = set()
#     with open("ramen-ratings.csv", "r") as file:
#         reader = csv.reader(file)
#         next(reader)
#         for row in reader:
#             countries.add(row[4])
#     country_count = len(countries)
#     print("Countries:", country_count)

# with open("ramen-ratings.csv", "r") as file:
#     reader = csv.reader(file)
#     next(reader)
#     ratings = {"Japan": [], "South Korea": [], "Hong Kong": [], "Taiwan": [], "China": []}
#     for row in reader:
#         country = row[4]
#         try:
#             rating = float(row[5])
#             if country in ratings:
#                 ratings[country].append(rating)
#         except ValueError:
#             continue
#     average_ratings = {country: sum(ratings[country]) / len(ratings[country]) for country in ratings}
#     best_country = max(average_ratings, key=average_ratings.get)
#     print(f"The country with the best average ramen rating is {best_country} with an average rating of {average_ratings[best_country]:.2f}")

# with open("ramen-ratings.csv", "r") as file:
#     reader = csv.reader(file)
#     next(reader)
#     zero_star_reviews = {}
#     for row in reader:
#         country = row[4]
#         try:
#             rating = float(row[5])
#             if rating == 0.0:
#                 if country in zero_star_reviews:
#                     zero_star_reviews[country] += 1
#                 else:
#                     zero_star_reviews[country] = 1
#         except ValueError:
#             continue
#     most_zero_star_country = max(zero_star_reviews, key=zero_star_reviews.get)
#     print(f"The country with the most 0 star reviews is {most_zero_star_country} with {zero_star_reviews[most_zero_star_country]} reviews")