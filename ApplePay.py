import itertools
import random
from random import randint


def display_file(record_count):
    header1(record_count)
    record_number = 1
    first_loop = 0
    while record_number <= int(record_count):
        with open("ApplePay" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            if first_loop != 0:
                output_file.write("  </APPLE-PAY-RECORDNUMBER>")
                output_file.write('\n')
            output_file.write("  <APPLE-PAY-RECORDNUMBER RECORDNUMBER=" + '"' + str(record_number) + '"' + ">")
            output_file.write('\n')
            first_loop += 1
        details_list = [detail1, detail2, detail3, detail4, detail5, detail6, detail7, detail8, detail9, detail10]
        for x in range(randint(1, 10)):
            random.choice(details_list)(record_count)
        record_number += 1
    footer1(record_count)


def header1(record_count):
    header1 = []

    with open('ApplePay.xml', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 0, 2):
            header1.append(each_line)

    with open("ApplePay" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            output_file.writelines(header1)


def detail1(record_count):
    detail1 = []

    with open('ApplePay.xml', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 2, 16):
            detail1.append(each_line)

    with open("ApplePay" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            output_file.writelines(detail1)


def detail2(record_count):
    detail2 = []

    with open('ApplePay.xml', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 16, 30):
            detail2.append(each_line)

    with open("ApplePay" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            output_file.writelines(detail2)


def detail3(record_count):
    detail3 = []

    with open('ApplePay.xml', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 30, 44):
            detail3.append(each_line)

    with open("ApplePay" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            output_file.writelines(detail3)


def detail4(record_count):
    detail4 = []

    with open('ApplePay.xml', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 44, 58):
            detail4.append(each_line)

    with open("ApplePay" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            output_file.writelines(detail4)


def detail5(record_count):
    detail5 = []

    with open('ApplePay.xml', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 58, 72):
            detail5.append(each_line)

    with open("ApplePay" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            output_file.writelines(detail5)


def detail6(record_count):
    detail6 = []

    with open('ApplePay.xml', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 72, 86):
            detail6.append(each_line)

    with open("ApplePay" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            output_file.writelines(detail6)


def detail7(record_count):
    detail7 = []

    with open('ApplePay.xml', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 86, 100):
            detail7.append(each_line)

    with open("ApplePay" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            output_file.writelines(detail7)


def detail8(record_count):
    detail8 = []

    with open('ApplePay.xml', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 100, 114):
            detail8.append(each_line)

    with open("ApplePay" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            output_file.writelines(detail8)


def detail9(record_count):
    detail9 = []

    with open('ApplePay.xml', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 114, 128):
            detail9.append(each_line)

    with open("ApplePay" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            output_file.writelines(detail9)


def detail10(record_count):
    detail10 = []

    with open('ApplePay.xml', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 128, 142):
            detail10.append(each_line)

    with open("ApplePay" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            output_file.writelines(detail10)


def footer1(record_count):
    footer1 = []

    with open('ApplePay.xml', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 142, 143):
            footer1.append(each_line)

    with open("ApplePay" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            output_file.writelines("  </APPLE-PAY-RECORDNUMBER>")
            output_file.writelines('\n')
            output_file.writelines(footer1)
            output_file.writelines('\n')