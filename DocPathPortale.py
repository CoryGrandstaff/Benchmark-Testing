import itertools
import random
from random import randint


def display_file(record_count):
    record_number = 1
    while record_number <= int(record_count):
        with open("DocPathPortale" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
            output_file.write("Record Number:" + str(record_number))
            output_file.write('\n')
        header1(record_count)
        details_list = [detail1, detail2, detail3, detail4, detail5, detail6, detail7, detail8, detail9, detail10,
                    detail11, detail12, detail13, detail14, detail15, detail16, detail17, detail18, detail19]
        for x in range(randint(1, 19)):
            random.choice(details_list)(record_count)
        footer1(record_count)
        record_number += 1

def header1(record_count):
    header1 = []

    with open('DocPathPortale.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 0, 8):
            header1.append(each_line)

    with open("DocPathPortale" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
            output_file.writelines(header1)


def detail1(record_count):
    detail1 = []

    with open('DocPathPortale.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 8, 11):
            detail1.append(each_line)

    with open("DocPathPortale" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
            output_file.writelines(detail1)


def detail2(record_count):
    detail2 = []

    with open('DocPathPortale.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 11, 14):
            detail2.append(each_line)

    with open("DocPathPortale" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
            output_file.writelines(detail2)


def detail3(record_count):
    detail3 = []

    with open('DocPathPortale.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 14, 17):
            detail3.append(each_line)

    with open("DocPathPortale" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
            output_file.writelines(detail3)


def detail4(record_count):
    detail4 = []

    with open('DocPathPortale.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 17, 20):
            detail4.append(each_line)

    with open("DocPathPortale" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
            output_file.writelines(detail4)


def detail5(record_count):
    detail5 = []

    with open('DocPathPortale.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 20, 23):
            detail5.append(each_line)

    with open("DocPathPortale" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
            output_file.writelines(detail5)


def detail6(record_count):
    detail6 = []

    with open('DocPathPortale.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 23, 26):
            detail6.append(each_line)

    with open("DocPathPortale" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
            output_file.writelines(detail6)


def detail7(record_count):
    detail7 = []

    with open('DocPathPortale.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 26, 29):
            detail7.append(each_line)

    with open("DocPathPortale" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
            output_file.writelines(detail7)


def detail8(record_count):
    detail8 = []

    with open('DocPathPortale.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 29, 32):
            detail8.append(each_line)

    with open("DocPathPortale" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
            output_file.writelines(detail8)


def detail9(record_count):
    detail9 = []

    with open('DocPathPortale.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 32, 35):
            detail9.append(each_line)

    with open("DocPathPortale" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
            output_file.writelines(detail9)


def detail10(record_count):
    detail10 = []

    with open('DocPathPortale.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 35, 38):
            detail10.append(each_line)

    with open("DocPathPortale" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
            output_file.writelines(detail10)


def detail11(record_count):
    detail11 = []

    with open('DocPathPortale.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 38, 41):
            detail11.append(each_line)

    with open("DocPathPortale" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
            output_file.writelines(detail11)


def detail12(record_count):
    detail12 = []

    with open('DocPathPortale.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 41, 44):
            detail12.append(each_line)

    with open("DocPathPortale" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
            output_file.writelines(detail12)


def detail13(record_count):
    detail13 = []

    with open('DocPathPortale.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 44, 47):
            detail13.append(each_line)

    with open("DocPathPortale" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
            output_file.writelines(detail13)


def detail14(record_count):
    detail14 = []

    with open('DocPathPortale.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 47, 50):
            detail14.append(each_line)

    with open("DocPathPortale" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
            output_file.writelines(detail14)


def detail15(record_count):
    detail15 = []

    with open('DocPathPortale.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 50, 53):
            detail15.append(each_line)

    with open("DocPathPortale" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
            output_file.writelines(detail15)


def detail16(record_count):
    detail16 = []

    with open('DocPathPortale.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 53, 56):
            detail16.append(each_line)

    with open("DocPathPortale" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
            output_file.writelines(detail16)


def detail17(record_count):
    detail17 = []

    with open('DocPathPortale.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 56, 59):
            detail17.append(each_line)

    with open("DocPathPortale" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
            output_file.writelines(detail17)


def detail18(record_count):
    detail18 = []

    with open('DocPathPortale.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 59, 62):
            detail18.append(each_line)

    with open("DocPathPortale" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
            output_file.writelines(detail18)


def detail19(record_count):
    detail19 = []

    with open('DocPathPortale.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 62, 65):
            detail19.append(each_line)

    with open("DocPathPortale" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
            output_file.writelines(detail19)


def footer1(record_count):
    footer1 = []

    with open('DocPathPortale.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 65, 70):
            footer1.append(each_line)

    with open("DocPathPortale" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
            output_file.writelines(footer1)
            output_file.writelines('\n')