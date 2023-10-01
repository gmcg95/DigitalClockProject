import time


# function that obtains current hour in a specific format (h/m/s) and adding 0 as first index, if the number is < 10
def get_current_time():
    current_time = time.localtime()
    hour = str(current_time.tm_hour).zfill(2)   # string casting and zfill(2) adds a 0 before if number <10/hour
    minute = str(current_time.tm_min).zfill(2)  # string casting and zfill(2) adds a 0 before if number <10/minute
    second = str(current_time.tm_sec).zfill(2)  # string casting and zfill(2) adds a 0 before if number <10/second
    return f'{hour}:{minute}:{second}'


# this list in list define the screening for every number and separator; it's a list with a list for each number(0-9)
digits = [
    [
        ' __ ',
        '|  |',
        '|__|',
        '    ',
    ],  # 0
    [
        '    ',
        '   |',
        '   |',
        '    ',
    ],  # 1
    [
        ' __ ',
        ' __|',
        '|__ ',
        '    ',
    ],  # 2
    [
        ' __ ',
        ' __|',
        ' __|',
        '    ',
    ],  # 3
    [
        '    ',
        '|__|',
        '   |',
        '    ',
    ],  # 4
    [
        ' __ ',
        '|__ ',
        ' __|',
        '    ',
    ],  # 5
    [
        ' __ ',
        '|__ ',
        '|__|',
        '    ',
    ],  # 6
    [
        ' __ ',
        '   |',
        '   |',
        '    ',
    ],  # 7
    [
        ' __ ',
        '|__|',
        '|__|',
        '    ',
    ],  # 8
    [
        ' __ ',
        '|__|',
        ' __|',
        '    ',
    ],  # 9
    [
        '   ',
        ' o ',
        ' o ',
        '   ',
    ],  # Separator ':'
]


# function for the output of current hour in the form of a digital clock
def display_hour():
    current_time = get_current_time()
    for i in range(4):
        line = ''
        for char in current_time:
            if char == ':':
                line += digits[10][i]  # Separator ':'
            else:
                digit = int(char)
                line += digits[digit][i]
        print(line)


try:
    while True:
        display_hour()
        time.sleep(1)  # second actualisation
except KeyboardInterrupt:
    pass  # except // pass is used for the sake of the try except syntax, mainly for the try condition
