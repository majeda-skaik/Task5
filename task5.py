#1Ask the user to input his (name, age, street, city, and country)
name=input("Enter your name:")
age=input("Enter your age:")
street=input("Enter your street:")
city=input("Enter your city:")
country=input("Enter your country:")
#2(related to question 1) Print the output on the console, it should look like this:
print('"Name: ', name,'"')
print('"Age: ', age,'"')
print('"Adress: ',street,"," ,city, "," ,country,'"')
#3(related to question 1) Print the next output with dynamic data:
new_age=int(age)-5
print('"'"Hello "'{',name,'}',"Your age is",new_age,"Years Old, Your Address is",street,"," ,city, "," ,country,'."')
#4(related to question 1) Print the type of the above 5 variables:
print(type(name),type(age))
print(type(street),type(city))
print("      ",type(country))
#5(related to question 1) Print the next output with dynamic data:
print('"''Hello ',name,','"How Are You?",  "\ " ,'"""' ,"Your Age Is",'"',new_age,'""' " + " "And Your Country Is:",country)
#6Print the same previous output (in question 5 ) but with a multi-line string.
print('"''Hello ',"'",name,"'",','"How Are You?",  "\ " )
print('"""' ,"Your Age Is",'"',new_age,'""' " + " "And")
print( "Your City Is:",city)
#7Create a variable( name = 'ITF Gsg Python') and print the next output:
name='ITF Gsg Python'
print("First Letter Is ",'"',name[0],'"')
print("Third Letter Is ",'"',name[2],'"')
print("Last Letter Is ",'"',name[-1],'"')
#8(related to question 7) Print the next output:
print(name[-3:])
print(name[0:3])
print(name[0:7:2])
print(name[-1:-7:-1])
#9Remove the symbols (before and after) the name:
name = "$&$&Mohammed$&$&"
print(name.strip("$&"))
#10Create a variable with the next value, Replace all matches of the symbol (%7) with the (Love) word.
msg = "I %7 Python And Although I %7 GSG with Zakaria"
print(msg.replace("%7","Love"))
#11Create 6 variables with the next values, and print the next output:
num1 = "4"
num2 = "56"
num3 = "963"
num4 = "385"
num5 = "8719"
num6 = "87190"
print(num1.zfill(5))
print(num2.zfill(5))
print(num3.zfill(5))
print(num4.zfill(5))
print(num5.zfill(5))
print(num6.zfill(5))


#13What is the difference between (title) and (capitalize) methods in Python string methods? (give me 2 examples to clarify the point)
#(title): make the first letter in each word uppercase for example,
my_name="my name is majeda"
print(my_name.title())
#the output is: My Name Is Majeda

#but (capitalize) method :just make the first letter in the statment uppercase
my_name="my name is majeda"
print(my_name.capitalize())
#the output is: My name is majeda

#14Create a variable with your name value, and print the next output:
first_name = "Dana"
print("*"*11+first_name)
print("*"*11+first_name+"*"*11)
print(first_name+"*"*11)

#15-Create 2 variables with the next values, and print the next output:
name_one = "SaMER"
name_two = "Abed"
print(name_one.swapcase())
print(name_two.swapcase())
print(name_one.lower())
print(name_two.upper())
#16(related to question 14) How can we Check if name_one contains Only Upper Case letters, and name_two contains Only Lower Case letters?
print(name_one.isupper())
print(name_two.islower())
#17(related to question 14) How can we Check if name_one starts with (S) letters or Not ? and name_two ends with (HD) letters or Not?
print(name_one[0]=="S")
print(name_two[-2:]=="HD")

#18Create a variable with the next value, and print how many times (Love) word and the letter (t) within the string:
msg = "I Love Python And Although I Love GSG with Zakaria"
x=msg.count("Love")
y=msg.count("t")
print("Number of <Love> is :",x)
print("Number of <t> is :",y)
#19Create a variable with the next value, and replace Only the first match of the symbol (%7) with the (Love) word:
msg = "I %7 Python And Although I %7 GSG with Zakaria"
new_msg=msg.replace("%7","love",1)
print(new_msg)

#q20
test1 = "ZakZak"
test2 = "Zakaria"
test3 = "A war at Tarawa."
test4 = "madam"
import re
def is_symmetrical_and_palindrome(s):
    s = re.sub(r'[ .,]', '', s)
    s = s.lower()
    is_symmetrical = s == s[::-1]
    is_palindrome = s == s[::-1]
    return is_symmetrical, is_palindrome
result1 = is_symmetrical_and_palindrome(test1)
result2 = is_symmetrical_and_palindrome(test2)
result3 = is_symmetrical_and_palindrome(test3)
result4 = is_symmetrical_and_palindrome(test4)
print(f"{test1} is {'symmetrical' if result1[0] else 'NOT symmetrical'}, but {test1} is {'a palindrome.' if result1[1] else 'NOT a palindrome.'}")
print(f"{test2} is {'symmetrical' if result2[0] else 'NOT symmetrical'}, and {test2} is {'a palindrome.' if result2[1] else 'NOT a palindrome.'}")
print(f"{test3} is {'symmetrical' if result3[0] else 'NOT symmetrical'}, but {test3} is {'a palindrome.' if result3[1] else 'NOT a palindrome.'}")
print(f"{test4} is {'symmetrical' if result4[0] else 'NOT symmetrical'}, and {test4} is {'a palindrome.' if result4[1] else 'NOT a palindrome.'}")














