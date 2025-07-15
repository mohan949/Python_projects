
percentage = []
for _ in range(1,4):
    f1 = int(input(f'enter the marks {_} :'))
    percentage.append(f1)
total_percentage = (100*(sum(percentage)))/300
print(f'Total percentage :{total_percentage}')
if(total_percentage>40):
    print(f'Pass : {total_percentage}')
else:
    print(F'Fail : {total_percentage}')