import matplotlib.pyplot as plt

def count_occurrences(arr, start, end):
    """Count the number of occurrences of integers in the specified range withing the given array."""
    count = 0
    for x in arr:
        if start <= x <= end:
            count += 1
    return count

def graphSnowfall(t):
    """Read snowfall data from a text file and aggregates the data into the range of 10 cm and display the information in a bar diagram"""
    #Read data from file
    with open(t, 'r') as file:
        snowfall_data = [int(line.strip()) for line in file.readlines()]

    #Define ranges and calculate frequencies
    ranges = ["0-10cms", "11-20cms", "21-30cms", "31-40cms", '41-50cms']
    frequencies = [count_occurrences(snowfall_data, 0, 10),
                   count_occurrences(snowfall_data, 11, 20),
                   count_occurrences(snowfall_data, 21, 30),
                   count_occurrences(snowfall_data, 31, 40),
                   count_occurrences(snowfall_data, 41, 50)]

    #Create horizontal bar chart
    plt.barh(ranges, frequencies, color='skyblue')
    
    #Add text labels to each bar
    for index, value in enumerate(frequencies):
        plt.text(value, index, str(value))
    
    #Set x-axis limit
    plt.xlim(0, max(frequencies) + 1)

    #Set labels and title
    plt.xlabel('Occurrences')
    plt.ylabel('Snowfall Ranges (cms)')
    plt.title('Snowfall Accumulation')

    #Save graph image
    plt.savefig("snowfall_chart.png")

    #Show graph
    plt.show()

#Print
graphSnowfall('snowfall_data.txt')
