counter = 0
while True:   # counter < 5
    u_input = input("Type something:")
    counter += 1
    if u_input == 'exit' or counter >= 5:
        break

    else:
        print(u_input)
