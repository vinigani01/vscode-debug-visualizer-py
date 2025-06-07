from DebugVisualizer import ListVisualizer

# create ListVisualizer instance
viz = ListVisualizer()   

nums = [5, 2, 9, 1, 5, 6]
# use ListVisualizer instance to call visualize() function 
# pass the list to be visualized as argument
viz.visualize(nums)


# insertion sort
for i in range(1, len(nums)):
    key = nums[i]
    j = i - 1
    while j >= 0 and nums[j] > key:
        nums[j + 1] = nums[j]
        j -= 1 
        # call visualize() to visualize the changes
        viz.visualize(nums) 

    nums[j + 1] = key
    viz.visualize(nums)

