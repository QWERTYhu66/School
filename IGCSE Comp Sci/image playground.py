# from PIL import Image, ImageDraw

# width, height = 760, 400
# stripe_height = height // 13
# union_width = width * 2 // 5
# union_height = stripe_height * 7

# flag = Image.new("RGB", (width, height), "white")
# draw = ImageDraw.Draw(flag)

# for i in range(0, 13, 2):
#     draw.rectangle([0, i * stripe_height, width, (i + 1) * stripe_height], fill=(179, 25, 66))

# draw.rectangle([0, i * stripe_height, width, (14) * stripe_height], fill=(179, 25, 66))

# draw.rectangle([0, 0, union_width, union_height], fill=(0, 0, 139))

# star_rows = 9
# star_cols = 11
# star_diameter = union_width // 20
# star_radius = star_diameter // 2
# star_spacing_x = union_width // 11
# star_spacing_y = union_height // 9.5

# for row in range(star_rows):
#     for col in range(star_cols):
#         if (row % 2 == 0 and col % 2 == 0) or (row % 2 == 1 and col % 2 == 1):
#             center_x = col * star_spacing_x + star_spacing_x // 2
#             center_y = row * star_spacing_y + star_spacing_y // 2
#             draw.ellipse(
#                 [
#                     center_x - star_radius,
#                     center_y - star_radius,
#                     center_x + star_radius,
#                     center_y + star_radius,
#                 ],
#                 fill="white",
#             )

# path = "image.png"
# flag.save(path)
# path