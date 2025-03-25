with open('first.txt','r') as file:
    numbers=file.readlines()
sq_num=(str(int(num.strip())**2)+"\n" for num in numbers)
with open('output.txt','w') as file:
    file.writelines(sq_num)
    