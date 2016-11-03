import itertools
import random
from random import randint

def display_file(record_count):
    generate_details(record_count)

def generate_details(record_count):
    get_header(record_count)
    details_list = [get_first_detail, get_second_detail, get_third_detail, get_fourth_detail, get_fifth_detail,
                    get_sixth_detail, get_seventh_detail, get_eighth_detail, get_ninth_detail, get_tenth_detail,
                    get_eleventh_detail, get_twelfth_detail, get_thirteenth_detail, get_fourteenth_detail,
                    get_fifteenth_detail, get_sixteenth_detail, get_seventeenth_detail, get_eighteenth_detail,
                    get_nineteenth_detail]
    for x in range(randint(1, 19)):
        random.choice(details_list)(record_count)
    get_footer(record_count)

def get_header(record_count):
    header = []

    with open('DocPathPortale.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 0, 8):
            header.append(each_line)
        for element in header:
            print(element, end="")

    with open ("DocPathPortale" + record_count + "Records.txt", "a") as output_file:
            output_file.writelines(header)

def get_first_detail(record_count):
    first_detail = []

    with open('DocPathPortale.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 8, 11):
            first_detail.append(each_line)
        for element in first_detail:
            print(element, end="")

    with open ("DocPathPortale" + record_count + "Records.txt", "a") as output_file:
            output_file.writelines(first_detail)

def get_second_detail(record_count):
    second_detail = []

    with open('DocPathPortale.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 11, 14):
            second_detail.append(each_line)
        for element in second_detail:
            print(element, end="")

    with open ("DocPathPortale" + record_count + "Records.txt", "a") as output_file:
            output_file.writelines(second_detail)

def get_third_detail(record_count):
    third_detail = []

    with open('DocPathPortale.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 14, 17):
            third_detail.append(each_line)
        for element in third_detail:
            print(element, end="")

    with open ("DocPathPortale" + record_count + "Records.txt", "a") as output_file:
            output_file.writelines(third_detail)

def get_fourth_detail(record_count):
    fourth_detail = []

    with open('DocPathPortale.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 17, 20):
            fourth_detail.append(each_line)
        for element in fourth_detail:
            print(element, end="")

    with open ("DocPathPortale" + record_count + "Records.txt", "a") as output_file:
            output_file.writelines(fourth_detail)

def get_fifth_detail(record_count):
    fifth_detail = []

    with open('DocPathPortale.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 20, 23):
            fifth_detail.append(each_line)
        for element in fifth_detail:
            print(element, end="")

    with open ("DocPathPortale" + record_count + "Records.txt", "a") as output_file:
            output_file.writelines(fifth_detail)

def get_sixth_detail(record_count):
    sixth_detail = []

    with open('DocPathPortale.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 23, 26):
            sixth_detail.append(each_line)
        for element in sixth_detail:
            print(element, end="")

    with open ("DocPathPortale" + record_count + "Records.txt", "a") as output_file:
            output_file.writelines(sixth_detail)

def get_seventh_detail(record_count):
    seventh_detail = []

    with open('DocPathPortale.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 26, 29):
            seventh_detail.append(each_line)
        for element in seventh_detail:
            print(element, end="")

    with open ("DocPathPortale" + record_count + "Records.txt", "a") as output_file:
            output_file.writelines(seventh_detail)

def get_eighth_detail(record_count):
    eighth_detail = []

    with open('DocPathPortale.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 29, 32):
            eighth_detail.append(each_line)
        for element in eighth_detail:
            print(element, end="")

    with open ("DocPathPortale" + record_count + "Records.txt", "a") as output_file:
            output_file.writelines(eighth_detail)

def get_ninth_detail(record_count):
    ninth_detail = []

    with open('DocPathPortale.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 32, 35):
            ninth_detail.append(each_line)
        for element in ninth_detail:
            print(element, end="")

    with open ("DocPathPortale" + record_count + "Records.txt", "a") as output_file:
            output_file.writelines(ninth_detail)

def get_tenth_detail(record_count):
    tenth_detail = []

    with open('DocPathPortale.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 35, 38):
            tenth_detail.append(each_line)
        for element in tenth_detail:
            print(element, end="")

    with open ("DocPathPortale" + record_count + "Records.txt", "a") as output_file:
            output_file.writelines(tenth_detail)

def get_eleventh_detail(record_count):
    eleventh_detail = []

    with open('DocPathPortale.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 38, 41):
            eleventh_detail.append(each_line)
        for element in eleventh_detail:
            print(element, end="")

    with open ("DocPathPortale" + record_count + "Records.txt", "a") as output_file:
            output_file.writelines(eleventh_detail)

def get_twelfth_detail(record_count):
    twelfth_detail = []

    with open('DocPathPortale.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 41, 44):
            twelfth_detail.append(each_line)
        for element in twelfth_detail:
            print(element, end="")

    with open ("DocPathPortale" + record_count + "Records.txt", "a") as output_file:
            output_file.writelines(twelfth_detail)

def get_thirteenth_detail(record_count):
    thirteenth_detail = []

    with open('DocPathPortale.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 44, 47):
            thirteenth_detail.append(each_line)
        for element in thirteenth_detail:
            print(element, end="")

    with open ("DocPathPortale" + record_count + "Records.txt", "a") as output_file:
            output_file.writelines(thirteenth_detail)

def get_fourteenth_detail(record_count):
    fourteenth_detail = []

    with open('DocPathPortale.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 47, 50):
            fourteenth_detail.append(each_line)
        for element in fourteenth_detail:
            print(element, end="")

    with open ("DocPathPortale" + record_count + "Records.txt", "a") as output_file:
            output_file.writelines(fourteenth_detail)

def get_fifteenth_detail(record_count):
    fifteenth_detail = []

    with open('DocPathPortale.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 50, 53):
            fifteenth_detail.append(each_line)
        for element in fifteenth_detail:
            print(element, end="")

    with open ("DocPathPortale" + record_count + "Records.txt", "a") as output_file:
            output_file.writelines(fifteenth_detail)

def get_sixteenth_detail(record_count):
    sixteenth_detail = []

    with open('DocPathPortale.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 53, 56):
            sixteenth_detail.append(each_line)
        for element in sixteenth_detail:
            print(element, end="")

    with open ("DocPathPortale" + record_count + "Records.txt", "a") as output_file:
            output_file.writelines(sixteenth_detail)

def get_seventeenth_detail(record_count):
    seventeenth_detail = []

    with open('DocPathPortale.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 56, 59):
            seventeenth_detail.append(each_line)
        for element in seventeenth_detail:
            print(element, end="")

    with open ("DocPathPortale" + record_count + "Records.txt", "a") as output_file:
            output_file.writelines(seventeenth_detail)

def get_eighteenth_detail(record_count):
    eighteenth_detail = []

    with open('DocPathPortale.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 59, 62):
            eighteenth_detail.append(each_line)
        for element in eighteenth_detail:
            print(element, end="")

    with open ("DocPathPortale" + record_count + "Records.txt", "a") as output_file:
            output_file.writelines(eighteenth_detail)

def get_nineteenth_detail(record_count):
    nineteenth_detail = []

    with open('DocPathPortale.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 62, 65):
            nineteenth_detail.append(each_line)
        for element in nineteenth_detail:
            print(element, end="")

    with open ("DocPathPortale" + record_count + "Records.txt", "a") as output_file:
            output_file.writelines(nineteenth_detail)

def get_footer(record_count):
    footer = []

    with open('DocPathPortale.txt', 'rt') as input_file:
        for each_line in itertools.islice(input_file, 65, 70):
            footer.append(each_line)
        for element in footer:
            print(element, end="")

    with open ("DocPathPortale" + record_count + "Records.txt", "a") as output_file:
            output_file.writelines(footer)