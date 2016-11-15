import itertools


def display_file(record_count):
    record_number = 1
    while record_number <= int(record_count):
        header1(record_count)
        with open("OOIDAMultiPage2" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
            output_file.write("  Record Number:" + str(record_number))
            output_file.write('\n')
        detail1(record_count)
        record_number += 1


def header1(record_count):
    header1 = []

    with open('OOIDAMultiPage2.DAT', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 0, 1):
            header1.append(each_line.strip())

    with open("OOIDAMultiPage2" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(header1)


def detail1(record_count):
    detail1 = []

    with open('OOIDAMultiPage2.DAT', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 1, 138):
            detail1.append(each_line)

    with open("OOIDAMultiPage2" + "(" + record_count + ")" + "Records.dat", "a") as output_file:
        output_file.writelines(detail1)
