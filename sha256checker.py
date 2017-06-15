ioc = []

with open('ioc.txt') as fp1:
    for line in fp1:
        ioc.append(line)
        
with open('source.txt') as fp0:
    for line in fp0:
        for item in ioc:
            if line.lower().strip() == item.lower().strip():
                print('MATCH: ' + line)