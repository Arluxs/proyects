from itertools import cycle
import numpy as np
import sys
verificar = True
flags = True
banasient = True
preciosgold = []
cangold = []
canplati = []
cansilver = []
preciosilver = []
boletos = {}
preciosplati = []
duenos = []
salir = False


def equis():
  print (' ')
  print ('Visualizar todos los asientos:')

  for fila in range(10):
    linea =''
    for columna in range(10):
      if lst1[fila,columna] == 0:
        caracter = 'X'
      else: 
        caracter = str(lst1[fila,columna])

      if lst1[fila,columna] < 10:
         linea = linea +  caracter + '  ' 
      elif lst1[fila,columna] < 100:
         linea = linea +  caracter + ' '
      else:
         linea = linea +  caracter   
    print(linea) 


def comprar():
  asientos()
  print('BIENVENIDOS A CREATIVOS.CL ESTA HACIENDO FILA PARA ASISTIR AL CONCIERTO DE MICHAEL JAM')
  gente = int(input('¿CUANTAS PERSONAS ASISTIRÁN EN TOTAL A ESCUCHAR A MICHAEL JAM?'))
  if (gente > 1 and gente < 3) or gente == 1:
    equis()
    for x in range(gente): 
      print('POR RAZONES DE SEGURIDAD GUARDAREMOS SU RUN PARA NUESTRA BASE DE DATOS.')
      print('POR RAZONES DE SEGURIDAD GUARDAREMOS SU RUN PARA NUESTRA BASE DE DATOS.')
      nom = input('INGRESE NOMBRE DEL DUEÑO DEL RUT')  
      ed = input('INGRESE EDAD DE LA PERSONA')
      boleto = int(input("INGRESE ASIENTO A COMPRAR: "))  
      for fila in range(9):
        for columna in range(9):
          if lst1[columna,fila] == boleto:
             if lst1[columna,fila] == 0:
               print('El asiento no se encuentra disponible.')
             else:
               lst1[columna,fila] = 0
      if boleto < 20:
        precioplati()
        precio = 120000
        preciosplati.append(precio)
        canplati.append(1)
      elif boleto > 21 and boleto < 50:
        preciogold()
        precio = 80000
        preciosgold.append(precio)
        cangold.append(1)
      elif boleto > 51 and boleto < 100:
        precionormal()
        precio = 50000    
        preciosilver.append(precio)
        cansilver.append(1)  
      rut3 = rutfinal()                 
      duenos.append([rut3, nom,ed, boleto, precio])
      print(duenos)
      for a in duenos:
       print(f'         RESUMEN DE COMPRA N {x+1} de {gente}         ')
       print(f'               DATOS DEL RESPONSABLE                  ')
       print("NOMBRE RESPONSABLE               : ", {a[1]} )
       print("RUN                              : ", {a[0]} )
       print("EDAD                             : ", {a[2]} )
       print("BOLETO COMPRADO                  : ", {a[3]} )
       print("PRECIO DEL BOLETO                : ", {a[4]} )      



def asitentes():
  duenos.sort()
  for a in duenos:
    print(f'               DATOS DEL RESPONSABLE                  ')
    print("NOMBRE RESPONSABLE               : ", {a[1]} )
    print("RUN                              : ", {a[0]} )
    print("EDAD                             : ", {a[2]} )
    print("BOLETO COMPRADO                  : ", {a[3]} )
    print("PRECIO DEL BOLETO                : ", {a[4]} ) 


def ganancia():
   a = sum(preciosplati)
   b = sum(preciosgold)
   c = sum(preciosilver)
   d = sum(canplati)
   e = sum(cangold)
   f = sum(cansilver)
   if a + b + c + d + e + f == 0:
     print('NO HAY DATOS DISPONIBLES')
   else: 
     print('TIPO DE ENTRADA       |     CANTIDAD       |       TOTAL    ')
     print('-------------------------------------------------------------- ')
     print(f'PLATINIUM            |     {d}            |      {a}    ')
     print(f'GOLD                 |     {e}            |      {b}    ')
     print(f'SILVER               |     {f}            |      {c}    ')
     print('---------------------------------------------------------------- ')  
     print(f'TOTAL                |     {d+e+f}        |       {a+b+c}    ')
 


  
    
def rutfinal():
  global verificar
  while verificar:
    rut1s = input('INGRESE RUT, CON DIGITO VERIFICAR Y SIN GUION: ')
    rut01 = rut1s[-1]
    print(rut01)
    if rut01 == 'K' or rut01 == 'k':
      rut2 = 'K'
      if rut2 == 'K':
        #rut2 = str(rut01)
        rut3 = rut1s.rstrip(rut1s[-1])  
        print(rut3)         
        rut4 = str(digito_v(rut3))
        print(rut4)
        print(rut2)
        a = (rut3 +rut2)
        print(a)
        if rut4 == str(10) or rut4 == str(1):
          rut4 = str('K')
          if rut2 is rut4:
            #print(f'Su RUT {rut1} es correcto')
            #verificar = False
            return rut3
          else:
            print('RUT INVALIDO') 
            verificar = True
    else:
      rut2 = int(rut01)
      rut3 = rut1s.rstrip(rut1s[-1])
      rut4 = int(digito_v(rut3))
      if rut2 is rut4:
        return rut3
        #verificar = False
      else:
        print('RUT INVALIDO') 
        verificar = True


def asientos():
 print('AQUÍ TIENE UNA LISTA DE LOS ASIENTOS DISPONIBLES.')
 print(contarcero())
 print('-------------------------------------------')
 print('--------------ESCENARIO------------------')
 print('-----------------------------------------')
 print(f'{lst1[0,:]} = [0]')
 print(f'{lst1[1,:]} = [1]')
 print('----------------------------------[A]')
 print('--------ASIENTO PLATINIUM---------[S]')
 print('----------------------------------')
 print(f'{lst1[2,:]} = [2][F]')
 print(f'{lst1[3,:]} = [3][I]')
 print(f'{lst1[4,:]} = [4][L]')
 print('----------------------------------   [A]')
 print('--------ASIENTO GOLD--------------   [S]')
 print('----------------------------------')
 print(f'{lst1[5,:]} = [5]')
 print(f'{lst1[6,:]} = [6]')
 print(f'{lst1[7,:]} = [7]')
 print(f'{lst1[8,:]} = [8]')
 print(f'{lst1[9,:]} = [9]')
 print('-----------------------------------------------')
 print('-------------ASIENTO SILVER--------------------')
 print('-----------------------------------------------')
 print(' =   =   =   =')
 print(f'[0] [1] [2] [3] [4] [5] [6] [7] [8] [9]')
 print('      -[COLUMNAS]-    ')
  



def precioplati():
  precio = print('ESCOGIO UN ASIENTO PLATINIUM 120.000$')
  print('ASIENTO CONFIRMADO')
def preciogold():
  precio = print('ESCOGIO UN ASIENTO GOLD POR 80.000$')
  print('ASIENTO CONFIRMADO')
    

asiento = np.zeros(shape=(1,101))

lst1 = np.arange(1,101).reshape(10,10)
lst2 = np.arange(1,101).reshape(10,10)
lst3 = np.arange(1,101).reshape(10,10)
lst1

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
 

def digito_v(rut3):
  reversed_digits = map(int, reversed(str(rut3)))
  factors = cycle(range(2,8))
  s =sum(d * f for d, f in zip(reversed_digits, factors))
  return (-s) % 11

def contarcero():
  cerof = np.count_nonzero(lst1)  
  return print(f'HAY UN TOTAL DE {cerof} ASIENTOS DISPONIBLES') 


while not salir:
    print('1. COMPRAR ENTRADAS')  
    print("2. VER ASIENTOS DISPONIBLES")
    print("3. VER LISTADO DE ASITENTES")
    print("4. MOSTRAR GANACIAS TOTALES")
    print("5. SALIR")

     
    print ("Elige una opcion")
 
    opcion = pedirNumeroEntero()
    if opcion == 2:
      equis()
  

    if opcion == 1:
      comprar()

    elif opcion == 3:
      asitentes()
    elif opcion == 4:
      ganancia()
    elif opcion == 5:
      print('GRACIAS POR VISITARNOS, HILDEBRANDO FUENTES, 08-07-2022.')
      salir = True
    else:
      print('ELIGE UN NUMERO DEL 1 AL 5.')