from hashlib import md5

global code 
print('\nBienvenido a AteneaFlagger 1.0, un generador de flags para Atenea.\n')
code = input('Introduce el flag: ')
print('El flag (plano) es: ' + code)
print('El flag (md5) es: \n\nflag{' + md5(code.encode('utf-8')).hexdigest() + '} \n')

exit()