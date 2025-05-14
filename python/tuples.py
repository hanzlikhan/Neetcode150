# def main():
#     # ✅ Use a list, not a tuple
#     names = ['Sabeen', 'Justin', 'Mukesh', 'Chen', 
#              'Lucia', 'Devon', 'Yousaf', 'Aisha']
    
#     names[4] = 'Edwin'      # ✅ This works now
#     print(names[4])         # Output: Edwin

# if __name__ == '__main__':
#     main()

# def get_equation(x1, y1, x2, y2):
#     slope = (y2 - y1) / (x2 - x1)
#     intercept = y1 - (slope * x1)
    
#     return slope, intercept
    

# def main():
#     slope, intercept, distance = get_equation(1, 1, 2, 4)
#     print('slope:', slope)
#     print('intercept:', intercept)
#     print('distance:', distance)
    

# if __name__ == '__main__':
#     main()


num = [1,3,5,8,9]

print('------------------  for loop ---- ----- ')
for i in range(len(num)):
    print(num[i])   # range vary 

print('------------------  for each loop ----')
for n in num: 
    print(n)  # one zeroth element last element 

with open('input.txt') as file:
    for line in file: 
        line = line.strip() 
        print(line)# optional

# num[i]
# num[2]
# num[3]

# i -> index 

# for each loop 

# n -> element 


