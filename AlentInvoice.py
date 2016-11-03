import itertools
import random
from random import randint

def display_file(record_count):
    generate_details(record_count)

def generate_details(record_count):
    header_list = [get_first_header, get_second_header, get_third_header, get_fourth_header]
    random.choice(header_list)(record_count)
    details_list = [get_first_detail, get_second_detail, get_third_detail, get_fourth_detail, get_fifth_detail,
                    get_sixth_detail, get_seventh_detail, get_eighth_detail]
    for x in range(randint(1, 8)):
        random.choice(details_list)(record_count)
    footer_list = [get_first_footer, get_second_footer, get_third_footer, get_fourth_footer]
    random.choice(footer_list)(record_count)

def get_first_header(record_count):
    first_header = []

    with open('AlentInvoice.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 0, 22):
            first_header.append(each_line)
        for element in first_header:
            print(element, end="")

    with open ("AlentInvoice" + record_count + "Records.txt", "a") as output_file:
            output_file.writelines(first_header)

def get_second_header(record_count):
    second_header = []

    with open('AlentInvoice.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 46, 67):
            second_header.append(each_line)
        for element in second_header:
            print(element, end="")

    with open ("AlentInvoice" + record_count + "Records.txt", "a") as output_file:
            output_file.writelines(second_header)

def get_third_header(record_count):
    third_header = []

    with open('AlentInvoice.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 93, 115):
            third_header.append(each_line)
        for element in third_header:
            print(element, end="")

    with open ("AlentInvoice" + record_count + "Records.txt", "a") as output_file:
            output_file.writelines(third_header)

def get_fourth_header(record_count):
    fourth_header = []

    with open('AlentInvoice.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 149, 171):
            fourth_header.append(each_line)
        for element in fourth_header:
            print(element, end="")

    with open ("AlentInvoice" + record_count + "Records.txt", "a") as output_file:
            output_file.writelines(fourth_header)

def get_first_detail(record_count):
    first_detail = []

    with open('AlentInvoice.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 22, 26):
            first_detail.append(each_line)
        for element in first_detail:
            print(element, end="")

    with open ("AlentInvoice" + record_count + "Records.txt", "a") as output_file:
            output_file.writelines(first_detail)

def get_second_detail(record_count):
    second_detail = []

    with open('AlentInvoice.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 26, 42):
            second_detail.append(each_line)
        for element in second_detail:
            print(element, end="")

    with open ("AlentInvoice" + record_count + "Records.txt", "a") as output_file:
            output_file.writelines(second_detail)

def get_third_detail(record_count):
    third_detail = []

    with open('AlentInvoice.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 67, 73):
            third_detail.append(each_line)
        for element in third_detail:
            print(element, end="")

    with open ("AlentInvoice" + record_count + "Records.txt", "a") as output_file:
            output_file.writelines(third_detail)

def get_fourth_detail(record_count):
    fourth_detail = []

    with open('AlentInvoice.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 73, 89 ):
            fourth_detail.append(each_line)
        for element in fourth_detail:
            print(element, end="")

    with open ("AlentInvoice" + record_count + "Records.txt", "a") as output_file:
            output_file.writelines(fourth_detail)

def get_fifth_detail(record_count):
    fifth_detail = []

    with open('AlentInvoice.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 115, 131):
            fifth_detail.append(each_line)
        for element in fifth_detail:
            print(element, end="")

    with open ("AlentInvoice" + record_count + "Records.txt", "a") as output_file:
            output_file.writelines(fifth_detail)

def get_sixth_detail(record_count):
    sixth_detail = []

    with open('AlentInvoice.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 131, 145):
            sixth_detail.append(each_line)
        for element in sixth_detail:
            print(element, end="")

    with open ("AlentInvoice" + record_count + "Records.txt", "a") as output_file:
            output_file.writelines(sixth_detail)

def get_seventh_detail(record_count):
    seventh_detail = []

    with open('AlentInvoice.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 171, 177):
            seventh_detail.append(each_line)
        for element in seventh_detail:
            print(element, end="")

    with open ("AlentInvoice" + record_count + "Records.txt", "a") as output_file:
            output_file.writelines(seventh_detail)

def get_eighth_detail(record_count):
    eighth_detail = []

    with open('AlentInvoice.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 177, 196 ):
            eighth_detail.append(each_line)
        for element in eighth_detail:
            print(element, end="")

    with open ("AlentInvoice" + record_count + "Records.txt", "a") as output_file:
            output_file.writelines(eighth_detail)

def get_first_footer(record_count):
    first_footer = []

    with open('AlentInvoice.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 42, 46):
            first_footer.append(each_line)
        for element in first_footer:
            print(element, end="")

    with open ("AlentInvoice" + record_count + "Records.txt", "a") as output_file:
            output_file.writelines(first_footer)

def get_second_footer(record_count):
    second_footer = []

    with open('AlentInvoice.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 89, 93):
            second_footer.append(each_line)
        for element in second_footer:
            print(element, end="")

    with open ("AlentInvoice" + record_count + "Records.txt", "a") as output_file:
            output_file.writelines(second_footer)

def get_third_footer(record_count):
    third_footer = []

    with open('AlentInvoice.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 145, 149):
            third_footer.append(each_line)
        for element in third_footer:
            print(element, end="")

    with open ("AlentInvoice" + record_count + "Records.txt", "a") as output_file:
            output_file.writelines(third_footer)

def get_fourth_footer(record_count):
    fourth_footer = []

    with open('AlentInvoice.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 196, 200):
            fourth_footer.append(each_line)
        for element in fourth_footer:
            print(element, end="")

    with open ("AlentInvoice" + record_count + "Records.txt", "a") as output_file:
            output_file.writelines(fourth_footer)