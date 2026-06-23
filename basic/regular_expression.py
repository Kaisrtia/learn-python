import re

email = input("Enter your email address: ")
regex_DUT = r'^\w+@sv1\.dut\.udn\.vn$'
#example: user@sv1.dut.udn.vn

if re.search(regex_DUT, email):
  print("Valid DUT email address.")
else:
  print("Invalid DUT email address.")