number_of_glasses = int(input())

while number_of_glasses > 1:
    my_attempt = ((number_of_glasses) % 3 + 2) % 3
    if (my_attempt == 0):
        my_attempt = 1

    number_of_glasses -= my_attempt
    print(my_attempt)
    if number_of_glasses <= 1:
        break
    jury_attempt = int(input())
    number_of_glasses -= jury_attempt
