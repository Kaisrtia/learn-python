me = {
  "name": "Hoang Trung",
  "age": 20,
  "grade": 4.0,
  "isHandsome": True
}
print(me)

your_name = "Hong Ngoc" #input("What is your name?: ")
if(your_name == "Hong Ngoc"):
  print(f"You are mine <3, {me}")
else:
  print("No, i had a girlfriend!")
match your_name:
  case "Hong Ngoc":
    print(f"You are mine <3, {me}")
  case _:
    print("No, i had a girlfriend!")

grade = 9.69696969
print(f"Your grade is: {grade:.3f}")

bad_name = "   hoang trung   "
def clean_name(name: str) -> str:
  return name.strip().title()
cleaned_name = clean_name(bad_name)
print(f"Cleaned name: {cleaned_name}")

try:
  number = int(input("Enter a number: "))
  print(f"You entered: {number}")
except ValueError as e:
  print("That's not a valid number!")
  print(f"Error details: {e}")