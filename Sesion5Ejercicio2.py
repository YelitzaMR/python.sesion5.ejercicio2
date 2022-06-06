def numPrimo(num: int):
    if num==1:
        print('Por convenio, el número',num,'no se considera primo ni compuesto')
    if num >1:
        for i in range(2,num):
            if num % i ==0:
                print('El número',num, 'no es primo')
                return
   
        print('El número',num, 'es primo')
        return

numPrimo(1)
numPrimo(2)
numPrimo(3)
numPrimo(7)
numPrimo(30)


