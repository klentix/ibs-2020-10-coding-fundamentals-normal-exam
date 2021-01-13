# Average temperature
# Write a method which can read and parse a file containing information
# about the average temperature of three European countries to raise awareness of climate change.
# Each line represents the average temperature of each country in the given year. The actual year can be found at the end of each line.
#
# The method should return the first coldest and hottest year in each country.
#
# The application should write the data to the console as key => value pairs.
#
# Example
# Example file can be found here.
#
# Output
#
# France => 1996, 2018
# Sweden => 2004, 2017
# Germany => 2000, 2017




def average_temp(file_name):

    file = open(file_name,'r') # open file
    file_lines = file.readlines()
    for line in file_lines[1:]:
        items = [int(x) for x in line.split()]
    print ('Min', min(items))
    print ('Max', max(items))


average_temp('results.txt')