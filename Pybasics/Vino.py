print("Enter the user number")
n = int(input())  # user inputs the number here - type casted to int to use in the for loop
print(type(n))    # gets you the data type of input
series_total = 0  # variable for the sum

for i in range(1, n+1):
    series_total += int(str(n)*i)     # type casted to string inorder to get the sequence 3 33 333 or 4 44 444 4444
                                      # type casted to int again to have it summed
print(series_total)
