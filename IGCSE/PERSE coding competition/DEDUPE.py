de = input()
current_char = de[0]
output_string = ""

for char in de:
    if current_char != char:
        output_string += current_char
        current_char = char

output_string += de[-1]

print(output_string)