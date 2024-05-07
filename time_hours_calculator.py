# Michelle Nguyen
# 2024-05-06


def open_file(file_name):
    '''
    Opens a file
    
    Parameters:
        file_name (str): the name of the text file
    Returns:
        [] (str): Each line in the text file separated into an element of a list
    '''
    try:
        file = open(file_name + ".txt", "r")
        text = []
        for line in file:
            text.append(line[:len(line)-1])	# Remove the \n
        file.close()
        return text
    except:
        print("File does not exist.")


def get_hour(time):
    '''
    Gets the 24 hour int value of a time
    
    Parameters:
        time (str): The time represented as a str
    Returns:
        int: The int value of the hour in 24-hr time
    '''
    ampm = time[5:].casefold()
    hour = int(time[:2])
    if ampm == "am" and hour == 12:
        hour = 0
    if ampm == "pm":
        hour += 12
    return hour


def get_minute(time):
    '''
    Gets the minute int value of a time
    
    Parameters:
        time (str): The time represented as a str
    Returns:
        int: The int value of the minute
    '''
    return int(time[3:5])


def calculate_time(first, second):
    '''
    Calculates the interval between two times
    
    Parameters:
        first (str): The first time represented as a str
        second (str): The second time represented as a str
    Returns:
        (): number of hours elapsed (int), number of minutes elapsed (int)
    '''
    hr1 = get_hour(first)
    hr2 = get_hour(second)
    hours = 0
    minutes = 0
    if hr1 < hr2:
        hours = (hr2 - hr1)
    elif hr1 > hr2:
        hours = (24 - hr1) + hr2
    minutes = get_minute(second) - get_minute(first)
    total = hours*60 + minutes
    return total // 60, total % 60


def get_times(text):
    '''
    Calculates the interval between times in a text file
    
    Parameters:
        text [] (str): All of the times from a text file stored in a list
    Returns:
        (): number of hours elapsed (int), number of minutes elapsed (int)
    '''
    minutes = 0
    for line in text:
        first = line[:7]
        second = line[10:]
        time = calculate_time(first, second)
        minutes += time[0] * 60 + time[1]
    return minutes // 60, minutes % 60


def print_time(time_elapsed):
    '''
    Prints the elapsed time
    
    Parameters:
        time_elapsed (tuple): hours (int), minutes (int)
    '''
    print("TIME ELAPSED:", time_elapsed[0], "hours and", time_elapsed[1], "minutes")


def main():
    choice = ""
    while (choice.casefold() not in ["q", "quit"]):
        choice = input("Command: ")
        # Manually input times
        if choice.casefold() == "manual":
            print("Please enter the times, in the form 00:00AM, or PM. ex. 02:00PM")
            first = input("First: ")
            second = input("Second: ")
            try:
                time_elapsed = calculate_time(first, second)
                print_time(time_elapsed)
            except:
                print("A time was not entered correctly.")
        # Grabs times from a file
        elif choice.casefold() == "file":
            # Example of proper text file format
            print("The text file should be formatted as:")
            print("-------------------------------------")
            print("10:00AM - 02:00AM\n11:01PM - 11:23AM\n")
            print("-------------------------------------")
            print("Note that the end of the text file needs an empty new line.")
            print("Refer to the sample times.txt for more details.")
            print("Please enter the name of the text file, excluding the .txt")
            file_name = input("File Name: ")
            try:
                time_elapsed = get_times(open_file(file_name))
                print_time(time_elapsed)
            except:
                print("Something went wrong. Please check your text file again and that everything is correct.")
        # End of a command
        print()
    print("END OF PROGRAM")


# PROGRAM
main()