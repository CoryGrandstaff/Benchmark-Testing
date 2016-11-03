def display_file(record_count):
    with open ('ExactechCertificate2.dat', 'rt') as in_file:
        contents = in_file.read()
    with open ("ExactechCertificate2" + record_count + ".dat", "w") as text_file:
        for i in range(int(record_count)):
            text_file.write(contents)
    print(contents)