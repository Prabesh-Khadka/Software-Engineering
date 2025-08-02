def Sum_odd_and_print_evens():
    num = int(input("Please enter a postive number: "))

    #case handing for the negative number
    if num < 1 :
        print("Please enter a Postive {num}")
        return

    odd_sum = 0 # initialize a variable to store the sum of odd  numbers
    even_numbers = [] # initialize to keep track of the even numbers
    even_sums = 0 # intializing the sum of evens as well

    # loop for all the numbers from 1 to number
    for i in range(1, num+1):
        if i % 2 == 1:
            odd_sum += i
        else:
            even_numbers.append(i)
            even_sums += i

    # After the loop print all the even numbers found to the sum
    print("Even numbers are between 1 and {num}:", even_numbers)

    #After the total sum of the odd numbers
    print("Sum of total odd numbers are:", odd_sum)

    #the sum of total even numbers as well
    print("Sum of total even numbers are:", even_sums)

#standard python format
if __name__ == "__main__":
    Sum_odd_and_print_evens()