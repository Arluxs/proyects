from itertools import cycle
from datetime import datetime
from collections import defaultdict
automotora = {}
duenos = []
duef = 0
def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
     
    return num
 
salir = False
opcion = 0
def digito_v(rut3):
  reversed_digits = map(int, reversed(str(rut3)))
  factors = cycle(range(2,8))
  s =sum(d * f for d, f in zip(reversed_digits, factors))
  return (-s) % 11
flag1 = True  
fecha = True
verificar = True
verificarp = True
def duenosmayor():
  print('                        HISTORIAL DE AUTO                          ')
  print("NOMBRE                                  : ", automotora[f'{patente}'][0] )
  print("RUT DUEÑO ACTUAL                        : ", automotora[f'{patente}'][1] )
  print("PRECIO COMERCIALIZADO                   : ", automotora[f'{patente}'][2] )
  print("MARCA DEL VEHICULO                      : ", automotora[f'{patente}'][3] )
  print("FECHA DE REGISTRO                       : ", automotora[f'{patente}'][4] )
  print("NUMERO DE DUEÑOS ACTUALES               : ", automotora[f'{patente}'][5])
  for a in duenos:
    if a[0] == patente:
      print(f'DUEÑO ANTERIOR                          : ', {a[1]} )


verificarpr = True

def duenosmenor():
  print('                        HISTORIAL DE AUTO                          ')
  print("NOMBRE                                  : ", automotora[f'{patente}'][0] )
  print("RUT DUEÑO ACTUAL                        : ", automotora[f'{patente}'][1] )
  print("PRECIO COMERCIALIZADO                   : ", automotora[f'{patente}'][2] )
  print("MARCA DEL VEHICULO                      : ", automotora[f'{patente}'][3] )
  print("FECHA DE REGISTRO                       : ", automotora[f'{patente}'][4] )


def certificado():
  if patec == patente:
    print('             CERTIFICADO DE CONTAMINANTES Y ANOTCIONES VIGENTES             ')
    print('----------------------------------------------------------------------------------')
    print(f'PATENTE DEL VEHICULO:                             :    {patente} ')
    print("DUEÑO (A) ACTUAL                                  : ", automotora[f'{patente}'][0] )
    print("MARCA DEL VEHICULO                                : ", automotora[f'{patente}'][3] )
    print('----------------------------------------------------------------------------------')
    print('                             AUTOMOTORA AUTO SEGURO                              ')



while not salir:
    print("1. GRABAR DATOS")
    print("2. BUSCAR VEHICULOS.")
    print("3. IMPRIMIR CERTIFICADOS CON SU PATENTE.")
    print("4. SALIR")
     
    print ("Elige una opcion")
 
    opcion = pedirNumeroEntero()
    if opcion == 1:
      while verificar:
        rut1 = input('INGRESE UN RUT: ')
        rut01 = rut1[-1]
        if rut01 == 'K' or rut01 == 'k':
         rut2 = str(rut01)
         if rut2 == 'k':
           rut2 = 'K'
           rut3 = rut1.rstrip(rut1[-1])  
           rutd = int(rut3)         
           rut4 = str(digito_v(rut3))
           if rut4 == str(10) or rut4 == str(1):
             rut4 = str('K')
           if rut2 is rut4:
             print(f'Su RUT {rut1} es correcto')
             verificar = False
           else:
             print('RUT INVALIDO') 
             verificar = True
        else:
         rut2 = int(rut01)
         rut3 = rut1.rstrip(rut1[-1])
         rutd = int(rut3)
         rut4 = int(digito_v(rut3))
         if digito_v(rut3) == 10:
           digito_v(rut3) == 'K'
         if rut2 is rut4:
           print(f'Su RUT {rut1} es correcto')
           verificar = False
         else:
            print('RUT INVALIDO') 
            verificar = True
      nom = input('INGRESE NOMBRE COMPLETO DEL DUEÑO').upper()
      while flag1:
        try:
          marc = input('INGRESE MARCA DEL AUTO: ')
          if len(marc) >= 2 and len(marc) <= 15:
            marca = marc
            flag1 = False
            marc.upper()
          else:
              print('INGRESE UNA MARCA VALIDA')
        except ValueError:
            print('INGRESE UNA MARCA VALIDA NO SUPERIOR A 15 CARACTERES.')
            flag = True
      while verificarpr == True:
        prec = int(input('INGRESE PRECIO DEL VEHICULO: '))
        if prec < 5000000:
          print('INGRESE UN PRECIO SUPERIOR A 5000000$.')
        else:
          print(f'PRECIO {prec} INGRESADO A SISTEMA.')
          verificarpr = False
      while fecha:
        try:
         fechr = input("INGRESE FECHA DE REGISTRO DEL AUTO. AAAA-MM-DD: ")
         datetime.strptime(fechr, '%Y-%m-%d')
         print("Fecha validada")
         fecha = False
        except ValueError:
          print("Fecha inválida")          
      patente = input('INGRESE PATENTE DEL AUTO: ')
      due = int(input('¿CUANTOS DUEÑOS A TENIDO EL AUTO. (A PARTE DEL ACTUAL): '))
      if due > 1:
       for x in range(due):
         print(f'INGRESE DUEÑO {x+1} DE {due} APARTE DEL DUEÑO ACTUAL')
         duenosf = input('INGRESE DUEÑO')
         duenos.append([patente,duenosf])
         due2 = str(due)   
         duef = due + 1
      elif due == 0:
        duef == 1
      automotora[f'{patente}'] = [nom, rut1, prec,marc, fechr, duef]  
      print(f'VEHICULO AGENDADO CON PATENTE: {patente}.')
    elif opcion == 2:
      patec = input('INGRESE PATENTE DEL AUTO: ')
      if patec == patente:
        if due > 1:
          duenosmayor()
        elif due == 0:
          duenosmenor()  

    elif opcion == 3:
      patec = input('INGRESE PATENTE A CONSULTAR: ')
      if patec == patente:
        certificado()

    elif opcion == 4:
      ul = input('¿Salir del sistema?. (S/N)')
      if ul == 'S' or ul == 's':
        print(f'Gracias por visitar NUESTRA AUTOMOTORA {nom}. VERSION 1.01.')
        salir = True
      if ul =='N' or ul == 'n':
       print('SERÁ REDIRIGIDO AL MENÚ PRINCIPAL.')
      salir = False    
    else:
      print ("Introduce un numero entre 1 y 4")
 
print ("Fin")