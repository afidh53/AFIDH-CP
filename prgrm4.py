start_range=int(input("enter the starting range(4 digit min):"))
end_range=int(input("enter the ending range(4 digit max):"))
even_digit=[]
for num in range (start_range,end_range+1):
    if all(int(digit)%2==0 for digit in str(num)):
        sqrt=int(num**0.5)
        if sqrt*sqrt==num:
            even_digit.append(num)
if even_digit !=[]:
    print("numbers with all even digits and are perfect squares:")
    print(even_digit)
else:
    print("there are no numbers within the given range.")

