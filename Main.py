''' THIS IS A PROGRAM CREATED FOR INTERNAL DOCPATH USE.
    THIS IS A SCRIPT FOR BENCHMARK TESTING THAT COPIES
    DETAILS FROM ONE FILE TO ANOTHER. DOCUMENTATION
    LOCATED AT *************
    CREATED BY CORY GRANDSTAFF
'''

import ApplePay
import AlentInvoice
import BankStatement
import DocPathPortale
import ExactechCertificate
import ExactechCertificate2
import ExactechInvoice
import OOIDAMultiPage
import OOIDAMultiPage2
import PurchaseOrder
import TerrebonneCheck
import WKVariableText

def print_welcome_screen():
    print("Welcome. Please choose which script you would like to work with")
    print("1. AlentInvoice \n2. ApplePay \n3. BankStatement \n4. DocPathPortale \n5. ExactechCertificate"
          " \n6. ExactechInvoice \n7. OOIDAMultiPage \n8. PurchaseOrder \n9. TerrebonneCheck \n10. WKVariableText")

def get_script_choice():
    multiple_record_choice = 0

    script_choice = input("Select your choice(1-10):\n")
    while script_choice not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'):
        script_choice = input("Please enter a valid number(1-10):\n")

    if script_choice == '5':
        print("ExactechCertificate has two files, which would you like to work with?")
        print("1. ExactechCertificate.dat \n2. ExactechCertificate2.dat")
        multiple_record_choice = input()
    elif script_choice == '7':
        print("OOIDAMultiPage has two files, which would you like to work with?")
        print("1. OOIDAMultiPage.dat \n2. OOIDAMultiPage2.dat")
        multiple_record_choice = input()

    script_items = {'1': 'AlentInvoice', '2': 'ApplePay', '3': 'BankStatement', '4': 'DocPathPortale',
                   '5': 'ExactechCertificate',
                   '6': 'ExactechInvoice', '7': 'OOIDAMultiPage', '8': 'PurchaseOrder', '9': 'TerrebonneCheck',
                   '10': 'WKVariableText'}

    description_choice = script_items[script_choice]
    return description_choice, multiple_record_choice

def get_record_count():
    custom_record_choice = 0

    print("Please choose the amount of records you would like to produce")
    print("1. 10 \n2. 100 \n3. 1,000 \n4. 10,000 \n5. 100,000 \n6. 500,000 \n7. 1,000,000 \n8. Custom Amount")

    record_choice = input("Select your choice(1-8):\n")
    while record_choice not in ('1', '2', '3', '4', '5', '6', '7', '8'):
        record_choice = input("Please enter a valid number(1-8):\n")

    if record_choice == '8':
        custom_record_choice = input("Please enter a custom record number:")

    record_amounts = {'1': '10', '2': '100', '3': '1000', '4': '10000', '5': '100000',
                     '6': '500000', '7': '1000000', '8': custom_record_choice}

    record_count = record_amounts[record_choice]
    return record_count

def print_data_file(description_choice, record_count, multi_record_choice):
        if description_choice == 'AlentInvoice':
            AlentInvoice.display_file(record_count)
        if description_choice == 'ApplePay':
            ApplePay.display_file(record_count)
        if description_choice == 'BankStatement':
            BankStatement.display_file(record_count)
        if description_choice == 'DocPathPortale':
            DocPathPortale.display_file(record_count)
        if description_choice == 'ExactechCertificate' and multi_record_choice == '1':
            ExactechCertificate.display_file(record_count)
        if description_choice == 'ExactechCertificate' and multi_record_choice == '2':
            ExactechCertificate2.display_file(record_count)
        if description_choice == 'ExactechInvoice':
            ExactechInvoice.display_file(record_count)
        if description_choice == 'OOIDAMultiPage' and multi_record_choice == '1':
            OOIDAMultiPage.display_file(record_count)
        if description_choice == 'OOIDAMultiPage' and multi_record_choice == '2':
            OOIDAMultiPage2.display_file(record_count)
        if description_choice == 'PurchaseOrder':
            PurchaseOrder.display_file(record_count)
        if description_choice == 'TerrebonneCheck':
            TerrebonneCheck.display_file(record_count)
        if description_choice == 'WKVariableText':
            WKVariableText.display_file(record_count)
        print("\n")

def re_run_check():
    answer = input("Would you like to process another data file(Y/N):\n").lower()
    while answer not in ('y', 'n'):
        answer = input("Please enter a valid answer(Y/N):\n").lower()

    if answer == 'y':
        re_run()

def re_run():
    print_welcome_screen()
    description_choice, multi_record_choice = get_script_choice()
    record_count = get_record_count()
    print_data_file(description_choice, record_count, multi_record_choice)
    re_run_check()

print_welcome_screen()
description_choice, multi_record_choice = get_script_choice()
record_count = get_record_count()
print_data_file(description_choice, record_count, multi_record_choice)
re_run_check()