from prgrm8c  import armstrong_number
number=int(input("Enter the number to check if it is an armstrong number:"))
if armstrong_number(number):
    print(f"{number} is an armstrong number.")
else:
    print(f"{number} is not an armstrong number.")