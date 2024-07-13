import math #this is for maths functions 
def main():
    while True: #this bealon function set to true 
        try:
            number = int(input("Please enter a whole number(i.e., an integer): "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid whole number.")

    print(f"The number you entered is {number}.")
    if number % 2 == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")

    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)

    print(f"The factors of {number} are {', '.join(map(str, factors))}.")

    if number ** 0.5 % 1 == 0:
        print(f"{number} has a perfect square root.")
    else:
        print(f"{number} does not have a perfect square root.")

    play_again = input("Would you like to enter another number? (Y/N): ")
    if play_again.upper() != "Y":
        print("Thank you for playing!")

if __name__ == "__main__":
    main()
