import itertools
import random
from random import randint


def display_file(record_count):
    record_number = 1
    while record_number <= int(record_count):
        with open("ExactechCertificate" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
            output_file.write("Record Number:" + str(record_number))
            output_file.write('\n')
        header1(record_count)
        details_list = [detail1, detail2, detail3]
        for x in range(randint(1, 3)):
            random.choice(details_list)(record_count)
        footer1(record_count)
        record_number += 1

def header1(record_count):
    header1 = []

    with open('ExactechCertificate.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 0, 13):
            header1.append(each_line)

    with open("ExactechCertificate" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(header1)


def detail1(record_count):
    detail1 = []

    with open('ExactechCertificate.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 13, 26):
            detail1.append(each_line)

    with open("ExactechCertificate" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail1)


def detail2(record_count):
    detail2 = []

    with open('ExactechCertificate.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 27, 38):
            detail2.append(each_line)

    with open("ExactechCertificate" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail2)


def detail3(record_count):
    detail3 = []

    with open('ExactechCertificate.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 39, 45):
            detail3.append(each_line)

    with open("ExactechCertificate" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail3)


def footer1(record_count):
    footer1 = []

    with open('ExactechCertificate.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 45, 46):
            footer1.append(each_line)

    with open("ExactechCertificate" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(footer1)
