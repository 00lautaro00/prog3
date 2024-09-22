numberList = [1,5,6]
number = 10
while(number > 9 or number < 0):
    number = int(input("ingrese numero entre 0 a 9: "))
    if(number > 9 or number < 0 ):
        print('fuera de ranngo')

for num in numberList:
    if(num == number):
        print("numero ya existe en la lista")