import csv
import re


def read(c1, c2):
    column1 = c1
    column2 = c2
    with open("details.csv", "r", encoding="utf-8") as file:
        csv_read = csv.reader(file)
        for line in csv_read:
            column1.append(line[0])
            column2.append(line[1])


def regex(reg, column):
    output = []

    for search in column:
        test = re.search(reg, search)
        if test is None:
            output.append(" ")
        else:
            if reg == '( : )\w*(.)*(,|\\\)':
                test = test.group(0)
                output.append(test[3:])
            else:
                output.append(test.group(0))
    return output


def write(result, file):
    co1 = result[0]
    co2 = result[1]
    co3 = result[2]
    co4 = result[3]
    co5 = result[4]
    co6 = result[5]
    co7 = result[6]
    co8 = result[7]
    co9 = result[8]
    rows = zip(co1, co2, co3, co4, co5, co6, co7, co8, co9)
    # print(co7[0])
    with open(file, 'w', newline="", encoding='utf-8') as file_write:
        f_write = csv.writer(file_write, delimiter=" ")

        for row in rows:
            f_write.writerow(row)

    # dict = {'column1': co1,'column2':co2,'column3':co3}
    # df = pd.DataFrame(co1 ,columns=["colummn,test"])
    # df.to_csv("test.csv",index=False)
    # df = pd.DataFrame(dict)
    # df.to_csv('test.csv')


def main():
    column1 = []
    column2 = []
    read(column1, column2)

    re3 = '((nr \d*)|((No|no)\W \d*)|(num\W \d*))|(iss\W \d*)'
    re3v2 = '\d*$'
    re4 = '((vol.)|(Vol.)|(T\S))+ +((\d*))|( t. \d*)'
    re5 = 'art. \w*'
    re5v2 = 'e\d*'
    re6 = '((\d*)(-)(\d*))(\d)'
    re8 = '( : )\w*(.)*(,|\\\)'  # ( : )\w*(.)*(,|\\)
    re8v2 = '\w*(.)*(\w|\\\)'
    re9 = '^\w*'
    re10 = '(\w*)(\d\d\d\d)'
    col3 = regex(re3, column2)
    col3 = regex(re3v2, col3)
    col4 = regex(re4, column2)
    col4 = regex(re3v2, col4)
    col5 = regex(re5, column2)
    col5 = regex(re5v2, col5)
    col6 = regex(re6, column2)
    col8 = regex(re8, column1)
    col8 = regex(re8v2, col8)
    col9 = regex(re9, column1)
    col10 = regex(re10, column1)
    # print(col8)
            # ok     #ok           #ok   #ok          #ok  #ok    #ok
    write([column1, column2, col3, col4, col5, col6, col8, col9, col10], 'hdfc_test_2.csv')


if __name__ == "__main__":
    main()
