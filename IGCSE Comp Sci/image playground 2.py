# from PIL import Image, ImageDraw
# height = 100
# width = 100
# initial_color = (255,255,255)


# pic = Image.new('RGB', (height, width), initial_color) # params are color mode, size (height, width), color (r, g, b)


# # pic.putpixel((0,0), (0,0,0)) # params are coordinates, color NOTE: needs double brackets


# # Challenge 1
# # def rectangle(image, x1, y1, x2, y2):
# #     for x in range(x1, x2):
# #         image.putpixel((x, y1), (0,0,0))
# #         image.putpixel((x, y2), (0,0,0))
# #     for y in range(y1, y2):
# #         image.putpixel((x1, y), (0,0,0))
# #         image.putpixel((x2, y), (0,0,0))
# # rectangle(pic, 10, 10, 90, 90)


# # Challenge 2
# # def line (image, x1, y1, x2, y2):
# #     if x1 == x2:
# #         for y in range(y1, y2):
# #             image.putpixel((x1, y), (0,0,0))
# #     else:
# #         for x in range(x1, x2):
# #             y = int(((y2-y1)/(x2-x1)) * (x - x1) + y1)
# #             image.putpixel((x, y), (0,0,0))
# # line(pic, 10, 10, 90, 90)



# # Challenge 3
# # def triangle(image, x1, y1, x2, y2, x3, y3):
# #     draw = ImageDraw.Draw(image)
# #     draw.line([(x1, y1), (x2, y2)], fill=(0, 0, 0))
# #     draw.line([(x2, y2), (x3, y3)], fill=(0, 0, 0))
# #     draw.line([(x3, y3), (x1, y1)], fill=(0, 0, 0))
# # triangle(pic, 10, 10, 90, 90, 50, 10)


# # # Challenge 4
# # def circle(image, x, y, radius):
# #     draw = ImageDraw.Draw(image)
# #     draw.ellipse((x-radius, y-radius, x+radius, y+radius), (0, 0, 0))
# # circle(pic, 50, 50, 40)


# # Challenge 5
# # def gradient(image, left_color, right_color):
# #     for x in range(100):
# #         r = int(((right_color[0] - left_color[0]) / 100) * x + left_color[0])
# #         g = int(((right_color[1] - left_color[1]) / 100) * x + left_color[1])
# #         b = int(((right_color[2] - left_color[2]) / 100) * x + left_color[2])
# #         for y in range(100):
# #             image.putpixel((x, y), (r, g, b))
# # # gradient(pic, (255, 0, 0), (0, 0, 255))


# # pic.save("my_pic.png")