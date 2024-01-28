
my_clippings = open("resources/My Clippings.txt", "r")
for line in my_clippings:
    try:
        # last character of every line is \n. So we take the second last character.
        last_char = line[-2]
    except IndexError:
        # Empty line
        continue
    if last_char == ")":
        print(line)