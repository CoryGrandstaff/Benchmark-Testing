import itertools
import random
from random import randint


def display_file(record_count):
    header1(record_count)
    record_number = 1
    while record_number <= int(record_count):
        with open("WKVariableText" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
            output_file.write("^Record Number" + '\n' + str(record_number))
            output_file.write('\n')
        details_list = [detail1, detail2, detail3]
        for x in range(randint(1, 3)):
            random.choice(details_list)(record_count)
        record_number += 1


def header1(record_count):
    header1 = []

    with open('WKVariableText.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 0, 1):
            header1.append(each_line)

    with open("WKVariableText" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
            output_file.writelines(header1)


def detail1(record_count):
    detail1 = []

    with open('WKVariableText.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 1, 32):
            detail1.append(each_line)

    with open("WKVariableText" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
            output_file.writelines(detail1)


def detail2(record_count):
    detail2 = []

    with open('WKVariableText.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 32, 63):
            detail2.append(each_line)

    with open("WKVariableText" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
            output_file.writelines(detail2)


def detail3(record_count):
    detail3 = []

    with open('WKVariableText.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 63, 94):
            detail3.append(each_line)

    with open("WKVariableText" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
            output_file.writelines(detail3)
            output_file.writelines('\n')
