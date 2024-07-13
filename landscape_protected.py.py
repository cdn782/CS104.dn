import math 
# this is the list i will be using "old_mcdonald,farmingIsLife#1,50"
creadentials = {
    "user": "old_mcdonald" ,
    "pass": "farmingIsLife" ,
    "level": 50 ,
}
user_username = input("Enter your username: ")
user_password = input("Enter your password: ")
authorized = (user_username == creadentials["user"]) and (user_password == creadentials["pass"])
#condition exection with if command
if authorized:
    print(f"Welcome to the Fertilizer Calculator! I will ask you for the length and width of four rectangular\nsections. Please enter your measurements in feet (numbers only, please). If you do not have a \nparticular section, simply enter zero (0) for those dimensions! Press ENTER to start!")
    print()
    L1 = int(input("What is the length of the front section? "))
    W1 = int(input("What is the width of the front section? "))
    L2 = int(input("What is the length of the back section? "))
    W2 = int(input("What is the width of the back section? "))
    L3 = int(input("What is the length of the right section? "))
    W3 = int(input("What is the width of the right section? "))
    L4 = int(input("What is the length of the left section? "))
    W4 = int(input("What is the width of the left section? "))
    print()
    total_area = L1 * W1 + L2 * W2 + L3 * W3 + L4 * W4 
    A_bag_needed =  total_area / 2000 
    Bag_needed = math.ceil(A_bag_needed)
    fertilizer_cost = Bag_needed * 27
    hours_of_labor = math.ceil(total_area / 2500)
    labor_cost = hours_of_labor * 20
    Nitro = A_bag_needed * 1
    Pot = A_bag_needed * .125
    total_cost = fertilizer_cost + labor_cost 
    print()
    print(f"Your application has a total area of {total_area} sq. feet. That will require {Bag_needed} bags of fertilizer. The cost of the fertilizer will be ${fertilizer_cost}.")
    print(f"Our technicians will require {hours_of_labor} hours to finish the job, and the labor cost will be ${labor_cost}. The total cost to the company will be ${total_cost}.")
    print(f"The application will result in {Nitro} pounds of nitrogen and {Pot} pounds of potassium being added to the soil.")
else:
    print("Error: Invalid credentials")