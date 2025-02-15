from scipy import stats

# Qx and Qy .txt should contain a single column of data each
# For the small amount of data we have here (8 pairs of columns) this is suitable
with open('Qx.txt', 'r') as file:
    x = [float(line.strip()) for line in file]
with open('Qy.txt', 'r') as file:
    y = [float(line.strip()) for line in file]
x, y = sorted(x), sorted(y)
print("x =",x)
print("y =",y)

r_values = [stats.pearsonr(x[-i:],y[-i:])[0] for i in range(3,len(x)+1)]
# This gives the correlation coefficient for the last "i"th data values

for i in range(len(r_values)-1,-1,-1): # Count from len(r_values)-1 to 0
    if r_values[i] >= 0.9:
        num = i 
        # This is the index of the last value that's greater than 0.9
        # So, the largest number of points included that means => 0.9
        print(f"index {i}, r_value = {r_values[i]} is greater than 0.9")
        break
        
        
# The 10th index is the 9th data point
# The 9th data point is x[8],y[8]

print(f"The {num}th index is the {len(x)-2-num}th data point")
print(f"The {len(x)-2-num}th data point is x = {x[len(x)-3-num]}, y = {y[len(y)-3-num]}")

print(f"The critical current is {y[len(y)-3-num]}mA")
# The critical current is the first data point within Region C
