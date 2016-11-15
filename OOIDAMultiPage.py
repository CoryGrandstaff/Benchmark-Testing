import itertools
import random


def display_file(record_count):
    record_number = 1
    while record_number <= int(record_count):
        if record_number < 10:
            with open("OOIDAMultiPage" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
                output_file.write("1 Record Number:" + str(record_number))
                output_file.write("                       ")
        if record_number >= 10 and record_number < 100:
            with open("OOIDAMultiPage" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
                output_file.write("1 Record Number:" + str(record_number))
                output_file.write("                      ")
        if record_number >= 100 and record_number < 1000:
            with open("OOIDAMultiPage" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
                output_file.write("1 Record Number:" + str(record_number))
                output_file.write("                     ")
        if record_number >= 1000 and record_number < 10000:
            with open("OOIDAMultiPage" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
                output_file.write("1 Record Number:" + str(record_number))
                output_file.write("                    ")
        if record_number >= 10000 and record_number < 100000:
            with open("OOIDAMultiPage" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
                output_file.write("1 Record Number:" + str(record_number))
                output_file.write("                   ")
        if record_number >= 100000 and record_number < 1000000:
            with open("OOIDAMultiPage" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
                output_file.write("1 Record Number:" + str(record_number))
                output_file.write("                  ")
        if record_number >= 1000000:
            with open("OOIDAMultiPage" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
                output_file.write("1 Record Number:" + str(record_number))
                output_file.write("                 ")
        header_list = [header1, header2, header3, header4, header5, header6, header7, header8, header9, header10,
                       header11, header12]
        random.choice(header_list)(record_count)
        detail1(record_count)

        header13(record_count)
        detail13(record_count)

        header14(record_count)
        detail14(record_count)

        header15(record_count)
        detail15(record_count)

        header16(record_count)
        detail16(record_count)

        header17(record_count)
        detail17(record_count)

        header18(record_count)
        detail18(record_count)

        header2_list = [header20, header22, header24, header26, header28]
        random.choice(header2_list)(record_count)
        detail2(record_count)

        random.choice(header2_list)(record_count)
        detail3(record_count)

        header29(record_count)
        detail29(record_count)

        record_number += 1


def header1(record_count):
    header1 = []

    with open('OOIDAMultiPage.DAT', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 0, 1):
            lastchars = each_line[-81:]
            header1.append(lastchars)

    with open("OOIDAMultiPage" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(header1)


def header2(record_count):
    header2 = []

    with open('OOIDAMultiPage.DAT', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 51, 52):
            lastchars = each_line[-81:]
            header2.append(lastchars)

    with open("OOIDAMultiPage" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(header2)


def header3(record_count):
    header3 = []

    with open('OOIDAMultiPage.DAT', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 102, 103):
            lastchars = each_line[-81:]
            header3.append(lastchars)

    with open("OOIDAMultiPage" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(header3)


def header4(record_count):
    header4 = []

    with open('OOIDAMultiPage.DAT', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 153, 154):
            lastchars = each_line[-81:]
            header4.append(lastchars)

    with open("OOIDAMultiPage" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(header4)


def header5(record_count):
    header5 = []

    with open('OOIDAMultiPage.DAT', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 204, 205):
            lastchars = each_line[-81:]
            header5.append(lastchars)

    with open("OOIDAMultiPage" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(header5)


def header6(record_count):
    header6 = []

    with open('OOIDAMultiPage.DAT', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 255, 256):
            lastchars = each_line[-81:]
            header6.append(lastchars)

    with open("OOIDAMultiPage" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(header6)


def header7(record_count):
    header7 = []

    with open('OOIDAMultiPage.DAT', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 306, 307):
            lastchars = each_line[-81:]
            header7.append(lastchars)

    with open("OOIDAMultiPage" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(header7)


def header8(record_count):
    header8 = []

    with open('OOIDAMultiPage.DAT', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 357, 358):
            lastchars = each_line[-81:]
            header8.append(lastchars)

    with open("OOIDAMultiPage" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(header8)


def header9(record_count):
    header9 = []

    with open('OOIDAMultiPage.DAT', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 408, 409):
            lastchars = each_line[-81:]
            header9.append(lastchars)

    with open("OOIDAMultiPage" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(header9)


def header10(record_count):
    header10 = []

    with open('OOIDAMultiPage.DAT', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 459, 460):
            lastchars = each_line[-81:]
            header10.append(lastchars)

    with open("OOIDAMultiPage" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(header10)


def header11(record_count):
    header11 = []

    with open('OOIDAMultiPage.DAT', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 510, 511):
            lastchars = each_line[-81:]
            header11.append(lastchars)

    with open("OOIDAMultiPage" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(header11)


def header12(record_count):
    header12 = []

    with open('OOIDAMultiPage.DAT', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 561, 562):
            lastchars = each_line[-81:]
            header12.append(lastchars)

    with open("OOIDAMultiPage" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(header12)


def header13(record_count):
    header13 = []

    with open('OOIDAMultiPage.DAT', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 612, 613):
            lastchars = each_line
            header13.append(lastchars)

    with open("OOIDAMultiPage" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(header13)


def header14(record_count):
    header14 = []

    with open('OOIDAMultiPage.DAT', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 644, 645):
            lastchars = each_line
            header14.append(lastchars)

    with open("OOIDAMultiPage" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(header14)


def header15(record_count):
    header15 = []

    with open('OOIDAMultiPage.DAT', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 694, 695):
            lastchars = each_line
            header15.append(lastchars)

    with open("OOIDAMultiPage" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(header15)


def header16(record_count):
    header16 = []

    with open('OOIDAMultiPage.DAT', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 738, 739):
            lastchars = each_line
            header16.append(lastchars)

    with open("OOIDAMultiPage" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(header16)


def header17(record_count):
    header17 = []

    with open('OOIDAMultiPage.DAT', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 772, 773):
            lastchars = each_line
            header17.append(lastchars)

    with open("OOIDAMultiPage" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(header17)


def header18(record_count):
    header18 = []

    with open('OOIDAMultiPage.DAT', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 811, 812):
            lastchars = each_line
            header18.append(lastchars)

    with open("OOIDAMultiPage" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(header18)


def header20(record_count):
    header20 = []

    with open('OOIDAMultiPage.DAT', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 882, 883):
            lastchars = each_line
            header20.append(lastchars)

    with open("OOIDAMultiPage" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(header20)


def header22(record_count):
    header22 = []

    with open('OOIDAMultiPage.DAT', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 953, 954):
            lastchars = each_line
            header22.append(lastchars)

    with open("OOIDAMultiPage" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(header22)


def header24(record_count):
    header24 = []

    with open('OOIDAMultiPage.DAT', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 1024, 1025):
            lastchars = each_line
            header24.append(lastchars)

    with open("OOIDAMultiPage" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(header24)


def header26(record_count):
    header26 = []

    with open('OOIDAMultiPage.DAT', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 1095, 1096):
            lastchars = each_line
            header26.append(lastchars)

    with open("OOIDAMultiPage" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(header26)


def header28(record_count):
    header28 = []

    with open('OOIDAMultiPage.DAT', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 1166, 1167):
            lastchars = each_line
            header28.append(lastchars)

    with open("OOIDAMultiPage" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(header28)


def header29(record_count):
    header29 = []

    with open('OOIDAMultiPage.DAT', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 1198, 1199):
            lastchars = each_line
            header29.append(lastchars)

    with open("OOIDAMultiPage" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(header29)


def detail1(record_count):
    detail1 = []

    with open('OOIDAMultiPage.DAT', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 1, 51):
            detail1.append(each_line)

    with open("OOIDAMultiPage" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail1)


def detail2(record_count):
    detail2 = []

    with open('OOIDAMultiPage.DAT', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 844, 882):
            detail2.append(each_line)

    with open("OOIDAMultiPage" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail2)


def detail3(record_count):
    detail3 = []

    with open('OOIDAMultiPage.DAT', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 883, 914):
            detail3.append(each_line)

    with open("OOIDAMultiPage" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail3)


def detail13(record_count):
    detail13 = []

    with open('OOIDAMultiPage.DAT', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 613, 644):
            detail13.append(each_line)

    with open("OOIDAMultiPage" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail13)


def detail14(record_count):
    detail14 = []

    with open('OOIDAMultiPage.DAT', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 645, 694):
            detail14.append(each_line)

    with open("OOIDAMultiPage" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail14)


def detail15(record_count):
    detail15 = []

    with open('OOIDAMultiPage.DAT', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 695, 738):
            detail15.append(each_line)

    with open("OOIDAMultiPage" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail15)


def detail16(record_count):
    detail16 = []

    with open('OOIDAMultiPage.DAT', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 739, 772):
            detail16.append(each_line)

    with open("OOIDAMultiPage" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail16)


def detail17(record_count):
    detail17 = []

    with open('OOIDAMultiPage.DAT', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 773, 811):
            detail17.append(each_line)

    with open("OOIDAMultiPage" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail17)


def detail18(record_count):
    detail18 = []

    with open('OOIDAMultiPage.DAT', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 812, 843):
            detail18.append(each_line)

    with open("OOIDAMultiPage" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail18)


def detail29(record_count):
    detail29 = []

    with open('OOIDAMultiPage.DAT', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 1199, 1220):
            detail29.append(each_line)

    with open("OOIDAMultiPage" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail29)
