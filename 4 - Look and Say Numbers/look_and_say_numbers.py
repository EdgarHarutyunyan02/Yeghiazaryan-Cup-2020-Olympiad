def say(text):
    text = str(text)+' '
    new_text = ''
    count = 1
    letter = text[0]
    for i in range(1, len(text)):
        if (text[i] == letter):
            count += 1
        else:
            new_text += f'{count}{letter}'
            letter = text[i]
            count = 1

    return new_text


k = int(input())

start = '1'
for i in range(k-1):
    start = say(start)
print(start)
