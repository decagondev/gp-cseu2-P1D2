# Return the "centered" average of a list of ints, 
# which we'll say is the mean average of the values, 
# except ignoring the largest and smallest values in the array. 
# if there are multiple copies of largest or smallest values. ignore only 1 of min / max respectively
# the input list may be unsorted
# you may assume that the list is length 3 or more

# you can make your own sort or you can use a sort function built in
def centered_average(ints):
    # get the smallest and largest numbers
    smallest = min(ints)
    largest = max(ints)

    # set an initial value of the sum
    sum = 0
    # itterate over the ints
    for i in ints:

        # sum up the ints
        sum += i
    
    # set the sum to the sum - smallest - largest
    sum = sum - smallest - largest
    # return sum / (len(ints) - 2)
    return int(sum / (len(ints) - 2))

a = centered_average([1, 2, 3, 4, 100]) # → 3
b = centered_average([1, 1, 5, 5, 10, 8, 7]) # → 5
c = centered_average([-10, -4, -2, -4, -2, 0]) # → -3

print(a)
print(b)
print(c)



