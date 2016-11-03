def displayFile(recordCount):
    data = []
    flag = False
    with open('ApplePay.xml', 'r') as f:
        for line in f:
            if line.startswith('  <APPLE-PAY-RECORD RECORD="'):
                flag = True
            if flag:
                data.append(line)
            if line.strip().endswith('">'):
                flag = False

    print(''.join(data))