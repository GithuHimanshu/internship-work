# for number in range(1,21):
#     if number % 2 ==0  :
            # print(number)

# ---------------or---------------
print("<---------print even number----------->")
def print_even_number(number):
    for number in range(1,number+1):
        if number % 2 ==0  :
            print(number)
            
# print(type(input("enter a number : "))) str
number = int(input("enter a number : "))

print_even_number(number)