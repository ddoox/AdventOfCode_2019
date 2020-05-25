input_min = 153517
input_max = 630395

meet_criteria = 0

for number in range(input_min, input_max + 1):
    criteria = True
    has_double = False
    first_char = True
    char_previous = "9"
    double_number = "9"

    number = str(number)

    for char in number:
        if first_char:
            char_previous = char
            first_char = False
        else:
            if char == char_previous:
                if number.count(char) == 2:
                    has_double = True
        if char < char_previous:
            criteria = False
            break

        char_previous = char

    if criteria and has_double:
        meet_criteria += 1

print(meet_criteria)
