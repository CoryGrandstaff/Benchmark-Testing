import itertools
import random
from random import randint


def display_file(record_count):
    header1(record_count)
    record_number = 1
    first_loop = 0
    while record_number <= int(record_count):
        with open("bankstatement" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            if first_loop != 0:
                output_file.write("</RECORDNUMBER>")
                output_file.write('\n')
            output_file.write("<RECORDNUMBER RECORDNUMBER=" + '"' + str(record_number) + '"' + ">")
            output_file.write('\n')
            first_loop += 1
        header2(record_count)
        details_list = [detail1, detail2, detail3, detail4, detail5, detail6, detail7, detail8, detail9, detail10,
                        detail11, detail12, detail13, detail14, detail15, detail16, detail17, detail18, detail19,
                        detail20, detail21, detail22, detail23, detail24, detail25, detail26, detail27, detail28,
                        detail29, detail30, detail31, detail32, detail33, detail34, detail35]
        for x in range(randint(1, 35)):
            random.choice(details_list)(record_count)
        record_number += 1
        total1(record_count)
    footer1(record_count)


def header1(record_count):
    header1 = []

    with open('bankstatement.xml', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 0, 2):
            header1.append(each_line)

    with open("bankstatement" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            output_file.writelines(header1)

def header2(record_count):
    header2 = []

    with open('bankstatement.xml', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 2, 26):
            header2.append(each_line)

    with open("bankstatement" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            output_file.writelines(header2)

def detail1(record_count):
    detail1 = []

    with open('bankstatement.xml', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 26, 34):
            detail1.append(each_line)

    with open("bankstatement" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            output_file.writelines(detail1)


def detail2(record_count):
    detail2 = []

    with open('bankstatement.xml', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 34, 42):
            detail2.append(each_line)

    with open("bankstatement" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            output_file.writelines(detail2)


def detail3(record_count):
    detail3 = []

    with open('bankstatement.xml', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 42, 50):
            detail3.append(each_line)

    with open("bankstatement" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            output_file.writelines(detail3)


def detail4(record_count):
    detail4 = []

    with open('bankstatement.xml', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 50, 58):
            detail4.append(each_line)

    with open("bankstatement" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            output_file.writelines(detail4)


def detail5(record_count):
    detail5 = []

    with open('bankstatement.xml', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 58, 66):
            detail5.append(each_line)

    with open("bankstatement" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            output_file.writelines(detail5)


def detail6(record_count):
    detail6 = []

    with open('bankstatement.xml', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 66, 74):
            detail6.append(each_line)

    with open("bankstatement" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            output_file.writelines(detail6)


def detail7(record_count):
    detail7 = []

    with open('bankstatement.xml', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 74, 82):
            detail7.append(each_line)

    with open("bankstatement" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            output_file.writelines(detail7)


def detail8(record_count):
    detail8 = []

    with open('bankstatement.xml', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 82, 90):
            detail8.append(each_line)

    with open("bankstatement" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            output_file.writelines(detail8)


def detail9(record_count):
    detail9 = []

    with open('bankstatement.xml', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 90, 98):
            detail9.append(each_line)

    with open("bankstatement" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            output_file.writelines(detail9)


def detail10(record_count):
    detail10 = []

    with open('bankstatement.xml', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 98, 106):
            detail10.append(each_line)

    with open("bankstatement" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            output_file.writelines(detail10)


def detail11(record_count):
    detail11 = []

    with open('bankstatement.xml', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 106, 114):
            detail11.append(each_line)

    with open("bankstatement" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            output_file.writelines(detail11)


def detail12(record_count):
    detail12 = []

    with open('bankstatement.xml', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 114, 122):
            detail12.append(each_line)

    with open("bankstatement" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            output_file.writelines(detail12)


def detail13(record_count):
    detail13 = []

    with open('bankstatement.xml', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 122, 130):
            detail13.append(each_line)

    with open("bankstatement" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            output_file.writelines(detail13)


def detail14(record_count):
    detail14 = []

    with open('bankstatement.xml', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 130, 138):
            detail14.append(each_line)

    with open("bankstatement" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            output_file.writelines(detail14)


def detail15(record_count):
    detail15 = []

    with open('bankstatement.xml', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 138, 146):
            detail15.append(each_line)

    with open("bankstatement" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            output_file.writelines(detail15)


def detail16(record_count):
    detail16 = []

    with open('bankstatement.xml', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 146, 154):
            detail16.append(each_line)

    with open("bankstatement" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            output_file.writelines(detail16)


def detail17(record_count):
    detail17 = []

    with open('bankstatement.xml', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 154, 162):
            detail17.append(each_line)

    with open("bankstatement" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            output_file.writelines(detail17)


def detail18(record_count):
    detail18 = []

    with open('bankstatement.xml', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 162, 170):
            detail18.append(each_line)

    with open("bankstatement" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            output_file.writelines(detail18)


def detail19(record_count):
    detail19 = []

    with open('bankstatement.xml', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 170, 178):
            detail19.append(each_line)

    with open("bankstatement" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            output_file.writelines(detail19)


def detail20(record_count):
    detail20 = []

    with open('bankstatement.xml', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 178, 186):
            detail20.append(each_line)

    with open("bankstatement" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            output_file.writelines(detail20)


def detail21(record_count):
    detail21 = []

    with open('bankstatement.xml', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 186, 194):
            detail21.append(each_line)

    with open("bankstatement" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            output_file.writelines(detail21)


def detail22(record_count):
    detail22 = []

    with open('bankstatement.xml', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 194, 202):
            detail22.append(each_line)

    with open("bankstatement" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            output_file.writelines(detail22)


def detail23(record_count):
    detail23 = []

    with open('bankstatement.xml', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 202, 210):
            detail23.append(each_line)

    with open("bankstatement" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            output_file.writelines(detail23)


def detail24(record_count):
    detail24 = []

    with open('bankstatement.xml', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 210, 218):
            detail24.append(each_line)

    with open("bankstatement" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            output_file.writelines(detail24)


def detail25(record_count):
    detail25 = []

    with open('bankstatement.xml', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 218, 226):
            detail25.append(each_line)

    with open("bankstatement" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            output_file.writelines(detail25)


def detail26(record_count):
    detail26 = []

    with open('bankstatement.xml', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 226, 234):
            detail26.append(each_line)

    with open("bankstatement" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            output_file.writelines(detail26)


def detail27(record_count):
    detail27 = []

    with open('bankstatement.xml', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 234, 242):
            detail27.append(each_line)

    with open("bankstatement" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            output_file.writelines(detail27)


def detail28(record_count):
    detail28 = []

    with open('bankstatement.xml', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 242, 250):
            detail28.append(each_line)

    with open("bankstatement" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            output_file.writelines(detail28)


def detail29(record_count):
    detail29 = []

    with open('bankstatement.xml', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 250, 258):
            detail29.append(each_line)

    with open("bankstatement" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            output_file.writelines(detail29)


def detail30(record_count):
    detail30 = []

    with open('bankstatement.xml', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 258, 266):
            detail30.append(each_line)

    with open("bankstatement" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            output_file.writelines(detail30)


def detail31(record_count):
    detail31 = []

    with open('bankstatement.xml', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 266, 274):
            detail31.append(each_line)

    with open("bankstatement" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            output_file.writelines(detail31)


def detail32(record_count):
    detail32 = []

    with open('bankstatement.xml', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 274, 282):
            detail32.append(each_line)

    with open("bankstatement" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            output_file.writelines(detail32)


def detail33(record_count):
    detail33 = []

    with open('bankstatement.xml', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 282, 290):
            detail33.append(each_line)

    with open("bankstatement" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            output_file.writelines(detail33)


def detail34(record_count):
    detail34 = []

    with open('bankstatement.xml', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 290, 298):
            detail34.append(each_line)

    with open("bankstatement" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            output_file.writelines(detail34)


def detail35(record_count):
    detail35 = []

    with open('bankstatement.xml', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 298, 306):
            detail35.append(each_line)

    with open("bankstatement" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            output_file.writelines(detail35)


def total1(record_count):
    total1 = []

    with open('bankstatement.xml', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 306, 315):
            total1.append(each_line)

    with open("bankstatement" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            output_file.writelines(total1)


def footer1(record_count):
    footer1 = []

    with open('bankstatement.xml', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 315, 316):
            footer1.append(each_line)

    with open("bankstatement" + "(" + record_count + ")" + "Records.xml", "a") as output_file:
            output_file.writelines("</RECORDNUMBER>")
            output_file.writelines('\n')
            output_file.writelines(footer1)
            output_file.writelines('\n')