
user_name = input("What is your name: ")
quest = input("What is your quest? ")
print("{} seeks {}".format(user_name, quest))

raw_num = input("Enter number: ")  # input is always a string
num = float(raw_num)  # convert to numbers as needed

print("2 times {} is {}".format(num, 2 * num))
