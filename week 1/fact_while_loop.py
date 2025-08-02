def factorial():
    #Ask the user for postive number to be input
    num = int(input("Please enter the postive number:"))

    #handle the case for 0 and 1 and negative case
    if num < 0:
        return "unidentified number below 1 or negative"

    elif num == 0 or num == 1:
        return f"The factorial of {num} is 1"
    
    #while loop executed for number above for factorial
    result = 1
    i = 1
    while i <= num:
        result *= i
        i += 1   

    return f"The factorial of {num} is {result}"

#entry point
if __name__ == "__main__":
    answer = factorial()
    print(answer)