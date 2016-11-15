import itertools
import random
from random import randint


def display_file(record_count):
    record_number = 1
    while record_number <= int(record_count):
        header_list = [header1, header2, header3, header4]
        random.choice(header_list)(record_count)
        with open("AlentInvoice" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
            output_file.write("Record Number:" + str(record_number))
            output_file.write('\n')
        second_header_list = [header5, header6, header7, header8]
        random.choice(second_header_list)(record_count)
        details_list = [detail1, detail2, detail3, detail4, detail5, detail6, detail7, detail8]
        for x in range(randint(1, 8)):
            random.choice(details_list)(record_count)
        footer_list = [footer1, footer2, footer3, footer4]
        random.choice(footer_list)(record_count)
        record_number += 1


def header1(record_count):
    header1 = []

    with open('AlentInvoice.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 0, 7):
            header1.append(each_line)

    with open("AlentInvoice" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
            output_file.writelines(header1)


def header2(record_count):
    header2 = []

    with open('AlentInvoice.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 46, 53):
            header2.append(each_line)

    with open("AlentInvoice" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
            output_file.writelines(header2)


def header3(record_count):
    header3 = []

    with open('AlentInvoice.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 93, 100):
            header3.append(each_line)

    with open("AlentInvoice" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
            output_file.writelines(header3)


def header4(record_count):
    header4 = []

    with open('AlentInvoice.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 149, 156):
            header4.append(each_line)

    with open("AlentInvoice" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
            output_file.writelines(header4)


def header5(record_count):
    header5 = []

    with open('AlentInvoice.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 7, 22):
            header5.append(each_line)

    with open("AlentInvoice" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
            output_file.writelines(header5)


def header6(record_count):
    header6 = []

    with open('AlentInvoice.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 53, 67):
            header6.append(each_line)

    with open("AlentInvoice" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
            output_file.writelines(header6)


def header7(record_count):
    header7 = []

    with open('AlentInvoice.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 100, 115):
            header7.append(each_line)

    with open("AlentInvoice" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
            output_file.writelines(header7)


def header8(record_count):
    header8 = []

    with open('AlentInvoice.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 156, 171):
            header8.append(each_line)

    with open("AlentInvoice" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
            output_file.writelines(header8)


def detail1(record_count):
    detail1 = []

    with open('AlentInvoice.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 22, 26):
            detail1.append(each_line)

    with open("AlentInvoice" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
            output_file.writelines(detail1)


def detail2(record_count):
    detail2 = []

    with open('AlentInvoice.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 26, 42):
            detail2.append(each_line)

    with open("AlentInvoice" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
            output_file.writelines(detail2)


def detail3(record_count):
    detail3 = []

    with open('AlentInvoice.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 67, 73):
            detail3.append(each_line)

    with open("AlentInvoice" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
            output_file.writelines(detail3)


def detail4(record_count):
    detail4 = []

    with open('AlentInvoice.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 73, 89):
            detail4.append(each_line)

    with open("AlentInvoice" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
            output_file.writelines(detail4)


def detail5(record_count):
    detail5 = []

    with open('AlentInvoice.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 115, 131):
            detail5.append(each_line)

    with open("AlentInvoice" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
            output_file.writelines(detail5)


def detail6(record_count):
    detail6 = []

    with open('AlentInvoice.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 131, 145):
            detail6.append(each_line)

    with open("AlentInvoice" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
            output_file.writelines(detail6)


def detail7(record_count):
    detail7 = []

    with open('AlentInvoice.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 171, 177):
            detail7.append(each_line)

    with open("AlentInvoice" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
            output_file.writelines(detail7)


def detail8(record_count):
    detail8 = []

    with open('AlentInvoice.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 177, 196):
            detail8.append(each_line)

    with open("AlentInvoice" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
            output_file.writelines(detail8)


def footer1(record_count):
    footer1 = []

    with open('AlentInvoice.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 42, 46):
            footer1.append(each_line)

    with open("AlentInvoice" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
            output_file.writelines(footer1)


def footer2(record_count):
    footer2 = []

    with open('AlentInvoice.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 89, 93):
            footer2.append(each_line)

    with open("AlentInvoice" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
            output_file.writelines(footer2)


def footer3(record_count):
    footer3 = []

    with open('AlentInvoice.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 145, 149):
            footer3.append(each_line)

    with open("AlentInvoice" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
            output_file.writelines(footer3)


def footer4(record_count):
    footer4 = []

    with open('AlentInvoice.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 196, 200):
            footer4.append(each_line)

    with open("AlentInvoice" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
            output_file.writelines(footer4)