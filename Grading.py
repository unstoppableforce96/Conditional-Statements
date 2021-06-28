# Grading
# Marks
m = int(input())
if(m >= 90): # 85 >= 90 False
    print('A')
if(m >= 80 and m < 90): # 85 >= 80 and 85 < 90 True 
    print('B')
if(m >= 70 and m < 80): # 85 >= 70 and 85 < 80 False
    print('C')
if(m >= 60 and m < 70):
    print('D')
if(m < 60):
    print('Fail')

