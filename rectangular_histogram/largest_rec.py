# [2,1,5,6,2,3]

def largest_rectangle_area(heights):
    # first calculate by brute force approach
    max_area = 0
    for i in range(len(heights)):
        for j in range(i, len(heights)):
            min_height = min(heights[i:j+1])
            area = min_height * (j - i + 1)
            max_area = max(max_area, area)