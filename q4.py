def print_line_stats(func):
    """
    Decorator function to print statistics for each line of number
    """
    def wrapper(line):
        numbers = [int(num) for num in line.strip().split()]  # Convert lines to list of integer
        count = len(numbers)
        total = sum(numbers)  
        average = total / count if count > 0 else 0  #  Create an average of numbers
        maximum = max(numbers, default=0)
        print("Numbers read:", numbers)
        print("Count:", count)
        print("Average:", average)
        print("Maximum:", maximum)
        print()
    return wrapper

# Function to print statistics for each line in the text file
def printStats(t):
    with open(t, 'r') as file:
        for line in file:
            print_stats_decorator = print_line_stats(lambda line: None)  # Create decorator function
            print_stats_decorator(line)  # Call decorator function with each line of numbers

#print
printStats('numbers.txt')
