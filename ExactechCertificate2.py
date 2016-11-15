import itertools
import random
from random import randint


def display_file(record_count):
    record_number = 1
    while record_number <= int(record_count):
        with open("ExactechCertificate2" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
            output_file.write("Record Number:" + str(record_number))
            output_file.write('\n')
        header1(record_count)
        details_list = [detail1, detail2, detail3, detail4, detail5, detail6, detail7, detail8, detail9, detail10,
                        detail11, detail12, detail13, detail14, detail15, detail16, detail17, detail18, detail19,
                        detail20, detail21, detail22, detail23, detail24, detail25, detail26, detail27, detail28,
                        detail29, detail30, detail31, detail32, detail33, detail34, detail35, detail36, detail37,
                        detail38, detail39, detail40, detail41, detail42, detail43]
        for x in range(randint(1, 43)):
            random.choice(details_list)(record_count)
        footer1(record_count)
        record_number += 1


def header1(record_count):
    header1 = []

    with open('ExactechCertificate2.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 0, 13):
            header1.append(each_line)

    with open("ExactechCertificate2" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(header1)


def detail1(record_count):
    detail1 = []

    with open('ExactechCertificate2.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 13, 23):
            detail1.append(each_line)

    with open("ExactechCertificate2" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail1)


def detail2(record_count):
    detail2 = []

    with open('ExactechCertificate2.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 24, 29):
            detail2.append(each_line)

    with open("ExactechCertificate2" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail2)


def detail3(record_count):
    detail3 = []

    with open('ExactechCertificate2.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 30, 35):
            detail3.append(each_line)

    with open("ExactechCertificate2" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail3)


def detail4(record_count):
    detail4 = []

    with open('ExactechCertificate2.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 36, 41):
            detail4.append(each_line)

    with open("ExactechCertificate2" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail4)


def detail5(record_count):
    detail5 = []

    with open('ExactechCertificate2.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 42, 53):
            detail5.append(each_line)

    with open("ExactechCertificate2" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail5)


def detail6(record_count):
    detail6 = []

    with open('ExactechCertificate2.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 54, 65):
            detail6.append(each_line)

    with open("ExactechCertificate2" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail6)


def detail7(record_count):
    detail7 = []

    with open('ExactechCertificate2.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 66, 70):
            detail7.append(each_line)

    with open("ExactechCertificate2" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail7)


def detail8(record_count):
    detail8 = []

    with open('ExactechCertificate2.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 71, 75):
            detail8.append(each_line)

    with open("ExactechCertificate2" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail8)


def detail9(record_count):
    detail9 = []

    with open('ExactechCertificate2.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 76, 82):
            detail9.append(each_line)

    with open("ExactechCertificate2" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail9)


def detail10(record_count):
    detail10 = []

    with open('ExactechCertificate2.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 83, 85):
            detail10.append(each_line)

    with open("ExactechCertificate2" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail10)


def detail11(record_count):
    detail11 = []

    with open('ExactechCertificate2.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 86, 97):
            detail11.append(each_line)

    with open("ExactechCertificate2" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail11)


def detail12(record_count):
    detail12 = []

    with open('ExactechCertificate2.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 98, 109):
            detail12.append(each_line)

    with open("ExactechCertificate2" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail12)


def detail13(record_count):
    detail13 = []

    with open('ExactechCertificate2.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 110, 114):
            detail13.append(each_line)

    with open("ExactechCertificate2" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail13)


def detail14(record_count):
    detail14 = []

    with open('ExactechCertificate2.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 115, 117):
            detail14.append(each_line)

    with open("ExactechCertificate2" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail14)


def detail15(record_count):
    detail15 = []

    with open('ExactechCertificate2.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 118, 123):
            detail15.append(each_line)

    with open("ExactechCertificate2" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail15)


def detail16(record_count):
    detail16 = []

    with open('ExactechCertificate2.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 124, 130):
            detail16.append(each_line)

    with open("ExactechCertificate2" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail16)


def detail17(record_count):
    detail17 = []

    with open('ExactechCertificate2.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 131, 134):
            detail17.append(each_line)

    with open("ExactechCertificate2" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail17)


def detail18(record_count):
    detail18 = []

    with open('ExactechCertificate2.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 135, 139):
            detail18.append(each_line)

    with open("ExactechCertificate2" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail18)


def detail19(record_count):
    detail19 = []

    with open('ExactechCertificate2.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 140, 144):
            detail19.append(each_line)

    with open("ExactechCertificate2" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail19)


def detail20(record_count):
    detail20 = []

    with open('ExactechCertificate2.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 145, 152):
            detail20.append(each_line)

    with open("ExactechCertificate2" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail20)


def detail21(record_count):
    detail21 = []

    with open('ExactechCertificate2.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 153, 158):
            detail21.append(each_line)

    with open("ExactechCertificate2" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail21)


def detail22(record_count):
    detail22 = []

    with open('ExactechCertificate2.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 159, 164):
            detail22.append(each_line)

    with open("ExactechCertificate2" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail22)


def detail23(record_count):
    detail23 = []

    with open('ExactechCertificate2.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 165, 170):
            detail23.append(each_line)

    with open("ExactechCertificate2" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail23)


def detail24(record_count):
    detail24 = []

    with open('ExactechCertificate2.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 171, 177):
            detail24.append(each_line)

    with open("ExactechCertificate2" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail24)


def detail25(record_count):
    detail25 = []

    with open('ExactechCertificate2.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 178, 189):
            detail25.append(each_line)

    with open("ExactechCertificate2" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail25)


def detail26(record_count):
    detail26 = []

    with open('ExactechCertificate2.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 190, 194):
            detail26.append(each_line)

    with open("ExactechCertificate2" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail26)


def detail27(record_count):
    detail27 = []

    with open('ExactechCertificate2.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 195, 198):
            detail27.append(each_line)

    with open("ExactechCertificate2" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail27)


def detail28(record_count):
    detail28 = []

    with open('ExactechCertificate2.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 199, 210):
            detail28.append(each_line)

    with open("ExactechCertificate2" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail28)


def detail29(record_count):
    detail29 = []

    with open('ExactechCertificate2.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 211, 216):
            detail29.append(each_line)

    with open("ExactechCertificate2" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail29)


def detail30(record_count):
    detail30 = []

    with open('ExactechCertificate2.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 217, 220):
            detail30.append(each_line)

    with open("ExactechCertificate2" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail30)


def detail31(record_count):
    detail31 = []

    with open('ExactechCertificate2.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 221, 226):
            detail31.append(each_line)

    with open("ExactechCertificate2" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail31)


def detail32(record_count):
    detail32 = []

    with open('ExactechCertificate2.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 227, 238):
            detail32.append(each_line)

    with open("ExactechCertificate2" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail32)


def detail33(record_count):
    detail33 = []

    with open('ExactechCertificate2.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 239, 250):
            detail33.append(each_line)

    with open("ExactechCertificate2" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail33)


def detail34(record_count):
    detail34 = []

    with open('ExactechCertificate2.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 251, 257):
            detail34.append(each_line)

    with open("ExactechCertificate2" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail34)


def detail35(record_count):
    detail35 = []

    with open('ExactechCertificate2.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 258, 263):
            detail35.append(each_line)

    with open("ExactechCertificate2" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail35)


def detail36(record_count):
    detail36 = []

    with open('ExactechCertificate2.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 264, 268):
            detail36.append(each_line)

    with open("ExactechCertificate2" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail36)


def detail37(record_count):
    detail37 = []

    with open('ExactechCertificate2.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 269, 272):
            detail37.append(each_line)

    with open("ExactechCertificate2" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail37)


def detail38(record_count):
    detail38 = []

    with open('ExactechCertificate2.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 273, 279):
            detail38.append(each_line)

    with open("ExactechCertificate2" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail38)


def detail39(record_count):
    detail39 = []

    with open('ExactechCertificate2.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 280, 286):
            detail39.append(each_line)

    with open("ExactechCertificate2" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail39)


def detail40(record_count):
    detail40 = []

    with open('ExactechCertificate2.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 287, 293):
            detail40.append(each_line)

    with open("ExactechCertificate2" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail40)


def detail41(record_count):
    detail41 = []

    with open('ExactechCertificate2.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 294, 305):
            detail41.append(each_line)

    with open("ExactechCertificate2" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail41)


def detail42(record_count):
    detail42 = []

    with open('ExactechCertificate2.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 306, 312):
            detail42.append(each_line)

    with open("ExactechCertificate2" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail42)


def detail43(record_count):
    detail43 = []

    with open('ExactechCertificate2.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 313, 318):
            detail43.append(each_line)

    with open("ExactechCertificate2" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail43)


def footer1(record_count):
    footer1 = []

    with open('ExactechCertificate2.dat', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 319, 321):
            footer1.append(each_line)

    with open("ExactechCertificate2" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(footer1)
