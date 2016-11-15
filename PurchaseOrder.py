import itertools
import random
from random import randint


def display_file(record_count):
    record_number = 1
    while record_number <= int(record_count):
        with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
            output_file.write("Record Number:" + str(record_number))
            output_file.write('\n')
        header_list = [header1, header2, header3]
        random.choice(header_list)(record_count)
        details_list = [detail1, detail2, detail3, detail4, detail5, detail6, detail7, detail8, detail9, detail10,
                        detail11, detail12, detail13, detail14, detail15, detail16, detail17, detail18, detail19,
                        detail20, detail21, detail22, detail23, detail24, detail25, detail26, detail27, detail28,
                        detail29, detail30, detail31, detail32, detail33, detail34, detail35, detail36, detail37,
                        detail38, detail39, detail40, detail41, detail42, detail43, detail44, detail45, detail46,
                        detail47, detail48]
        random_number = randint(1, 48)
        if random_number > 8:
            for x in range(8):
                random.choice(details_list)(record_count)
                random_number -= 1
            header4(record_count)
            if random_number > 8:
                for x in range(8):
                    random.choice(details_list)(record_count)
                    random_number -= 1
                header5(record_count)
                if random_number > 8:
                    for x in range(8):
                        random.choice(details_list)(record_count)
                        random_number -= 1
                    header6(record_count)
                    if random_number > 8:
                        for x in range(8):
                            random.choice(details_list)(record_count)
                            random_number -= 1
                        header7(record_count)
                        if random_number > 8:
                            for x in range(8):
                                random.choice(details_list)(record_count)
                                random_number -= 1
                            header8(record_count)
        for x in range(random_number):
            random.choice(details_list)(record_count)
        footer_list = [footer1, footer2, footer3]
        random.choice(footer_list)(record_count)
        record_number += 1


def header1(record_count):
    header1 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 0, 27):
            header1.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(header1)


def header2(record_count):
    header2 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 65, 92):
            header2.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(header2)


def header3(record_count):
    header3 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 122, 149):
            header3.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(header3)


def header4(record_count):
    header4 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 188, 215):
            header4.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(header4)


def header5(record_count):
    header5 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 254, 281):
            header5.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(header5)


def header6(record_count):
    header6 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 320, 347):
            header6.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(header6)


def header7(record_count):
    header7 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 386, 413):
            header7.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(header7)


def header8(record_count):
    header8 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 448, 475):
            header8.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(header8)


def detail1(record_count):
    detail1 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 27, 32):
            detail1.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(detail1)


def detail2(record_count):
    detail2 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 32, 37):
            detail2.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(detail2)


def detail3(record_count):
    detail3 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 37, 42):
            detail3.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(detail3)


def detail4(record_count):
    detail4 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 42, 47):
            detail4.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(detail4)


def detail5(record_count):
    detail5 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 92, 97):
            detail5.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(detail5)


def detail6(record_count):
    detail6 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 97, 103):
            detail6.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(detail6)


def detail7(record_count):
    detail7 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 103, 108):
            detail7.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(detail7)


def detail8(record_count):
    detail8 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 108, 113):
            detail8.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(detail8)


def detail9(record_count):
    detail9 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 149, 154):
            detail9.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(detail9)


def detail10(record_count):
    detail10 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 154, 159):
            detail10.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(detail10)


def detail11(record_count):
    detail11 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 159, 164):
            detail11.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(detail11)


def detail12(record_count):
    detail12 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 164, 169):
            detail12.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(detail12)


def detail13(record_count):
    detail13 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 169, 174):
            detail13.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(detail13)


def detail14(record_count):
    detail14 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 174, 179):
            detail14.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(detail14)


def detail15(record_count):
    detail15 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 179, 184):
            detail15.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(detail15)


def detail16(record_count):
    detail16 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 184, 188):
            detail16.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(detail16)


def detail17(record_count):
    detail17 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 215, 220):
            detail17.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(detail17)


def detail18(record_count):
    detail18 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 220, 225):
            detail18.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(detail18)


def detail19(record_count):
    detail19 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 225, 230):
            detail19.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(detail19)


def detail20(record_count):
    detail20 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 230, 235):
            detail20.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(detail20)


def detail21(record_count):
    detail21 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 235, 240):
            detail21.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(detail21)


def detail22(record_count):
    detail22 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 240, 245):
            detail22.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(detail22)


def detail23(record_count):
    detail23 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 245, 250):
            detail23.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(detail23)


def detail24(record_count):
    detail24 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 250, 254):
            detail24.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(detail24)


def detail25(record_count):
    detail25 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 281, 286):
            detail25.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(detail25)


def detail26(record_count):
    detail26 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 286, 291):
            detail26.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(detail26)


def detail27(record_count):
    detail27 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 291, 296):
            detail27.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(detail27)


def detail28(record_count):
    detail28 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 296, 301):
            detail28.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(detail28)


def detail29(record_count):
    detail29 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 301, 306):
            detail29.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(detail29)


def detail30(record_count):
    detail30 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 306, 311):
            detail30.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(detail30)


def detail31(record_count):
    detail31 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 311, 316):
            detail31.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(detail31)


def detail32(record_count):
    detail32 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 316, 320):
            detail32.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(detail32)


def detail33(record_count):
    detail33 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 347, 352):
            detail33.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(detail33)


def detail34(record_count):
    detail34 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 352, 357):
            detail34.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(detail34)


def detail35(record_count):
    detail35 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 357, 362):
            detail35.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(detail35)


def detail36(record_count):
    detail36 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 362, 367):
            detail36.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(detail36)


def detail37(record_count):
    detail37 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 367, 372):
            detail37.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(detail37)


def detail38(record_count):
    detail38 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 372, 377):
            detail38.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(detail38)


def detail39(record_count):
    detail39 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 377, 382):
            detail39.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(detail39)


def detail40(record_count):
    detail40 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 382, 386):
            detail40.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(detail40)


def detail41(record_count):
    detail41 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 414, 419):
            detail41.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(detail41)


def detail42(record_count):
    detail42 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 419, 424):
            detail42.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(detail42)


def detail43(record_count):
    detail43 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 424, 429):
            detail43.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(detail43)


def detail44(record_count):
    detail44 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 429, 434):
            detail44.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(detail44)


def detail45(record_count):
    detail45 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 434, 439):
            detail45.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(detail45)


def detail46(record_count):
    detail46 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 439, 444):
            detail46.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(detail46)


def detail47(record_count):
    detail47 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 444, 448):
            detail47.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(detail47)


def detail48(record_count):
    detail48 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 475, 480):
            detail48.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(detail48)


def footer1(record_count):
    footer1 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 61, 65):
            footer1.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(footer1)


def footer2(record_count):
    footer2 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 118, 122):
            footer2.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(footer2)


def footer3(record_count):
    footer3 = []

    with open('PurchaseOrder.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 480, 484):
            footer3.append(each_line)

    with open("PurchaseOrder" + "(" + record_count + ")" + "Records.txt", "a") as output_file:
        output_file.writelines(footer3)
