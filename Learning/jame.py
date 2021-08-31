import re

string = 'While d the string in message d d64 is short in this example, it could be millionsof characters the program would still run21 less than a second. Asimilar program that finds phone numbers using regular expressions wouldalso run less than a second, but regular expressions make it quicker towrite these programs'
san = r'analyd de46t de46t  $deo \dc9t dj dj t'
print(re.findall(r'(?P<na>\b\w+\b)\s(?P=na)', san))

