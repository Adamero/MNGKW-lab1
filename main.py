import re


class Excel:

    def __init__(self, publisher_value: str, details_value: str):
        self.publisher_value = publisher_value
        self.details_value = details_value

    def regex(self, expression: list , column: list) -> str:

        check = re.search(expression[0], column)

        if check is not None:
            if len(expression) > 1:

                for i in range(1, len(expression)):
                    check = re.search(expression[i], check.group(0))

                if check is not None:
                    return check.group(0)
                else:
                    return ""
            else:
                return check.group(0)
        else:
            return ""

    def publisher(self):
        return self.publisher_value

    def details(self):
        return self.details_value

    def no(self):
        return self.regex(['((nr \d*)|((No|no)\W \d*)|(num\W \d*))|(iss\W \d*)', '\d*$'], self.details_value)

    def vol(self):
        return self.regex(['((vol.)|(Vol.)|(T\S))+ +((\d*))|( t. \d*)', '\d*$'], self.details_value)

    def articleNo(self):
        return self.regex(['(art. \w*)', 'e\d*'], self.details_value)

    def pagesInRange(self):
        return self.regex(['((\d*)(-)(\d*))(\d)'], self.details_value)

    def publisherName(self):
        return self.regex(['( : )\w*(.)*(,|\\\)', '\w*(.)*(\w|\\\)', '\w(\w*( |-|,|\S))*(\w*(\w*))$'],self.publisher_value)

    def publisherLocation(self):
        return self.regex(['^\w*'], self.publisher_value)

    def publisherYear(self):
        return self.regex(['(\w*)(\d\d\d\d)'], self.publisher_value)
