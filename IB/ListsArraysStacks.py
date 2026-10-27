# Reverse Sentence
stack = []
index = 0

def push(sentence):
    global index
    for word in sentence.split():
        stack.append(word)
    index += 1

def pop():
    global index
    index -= 1
    if index == 0:
        return "Stack is empty. No sentence to pop."
    reversed_sentence = []
    while stack[index]:
        reversed_sentence.append(stack.pop())
    return ' '.join(reversed_sentence)

while True:
    print("\nMenu:")
    print("1. Push sentence onto stack")
    print("2. Pop and reverse sentence from stack")
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        sentence = input("Enter a sentence: ")
        push(sentence)
        print("Sentence pushed onto stack.")
    elif choice == '2':
        reversed_sentence = pop()
        if reversed_sentence == "Stack is empty. No sentence to pop.":
            print(reversed_sentence)
        else:
            print("Reversed sentence:", reversed_sentence)
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")