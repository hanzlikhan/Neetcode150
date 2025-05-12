def average(num1, num2):
    '''
    average two numbers together and return the result 
    params: 
        num1, num2 (ints or floats): numbers to average
    return: average of num1 and num2
    '''
    result = (num1 + num2) / 2
    return result


# def two_goodmornings():


def two_goodmornings(count):
    '''
    prints "Good Morning" a max of two times
    params: 
        count (int): the number of times to print "Good Morning" (max of two)
    '''
    for i in range(count):  # 0 , 1 , 2
        if i == 2:
            return 
        print("Good Morning!")

# This function has no return statement
def count_to_ten():
    '''prints out numbers 1 through 10'''
    for i in range(10):
        print(i)


# This is the main function, the one we call first
def main():
    # First we'll count to ten
    count_to_ten()

    # Then we'll try to say good morning three times
    # but we can only say it twice
    print(two_goodmornings(3))

    # Finally, we want the average of two numbers, and
    # we're going to store the result in a variable
    num1 = 5
    num2 = 10
    my_average = average(num1, num2)
	
    # Now, if we print my_average, we'll see the result of
    # the 'average' function
    print(my_average)


# Below is the first line the program runs
# because everything else is inside of a function
# definition. Here we call the main function which
# gets our program rolling!
if __name__ == "__main__":
    main()