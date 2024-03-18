#AUTHOR: JOSE DANIEL RIVAS
#CAJA REGISTRADORA - LISTAR PRODUCTOS E INVENTARIO
def menu():
    print('---------------------------------')
    print('#        TIENDA LA +SURTIDA      #')
    print('---------------------------------')
    print('A1 - 🍌 Guineros 1kg - $2.00')
    print('A2 - 🍎 Manzana Gala 1kg - $4.00')
    print('A3 - 🍇 Uva Globe 1kg - $7.00')
    print('A4 - 🍓 Fresa 1kg - $8.00')
    print('B1 - 🍗 Pollo 1lb - $2.50')
    print('B2 - 🥩 Carne 1lb - $3.50')
    print('C1 - 🧋 Te frío con Tapioca 24onz - $5.00')
    print('X1 - 🍩 Dona glaseada - $1.00')
    print('---------------------------------')
    print('E0 - COBRAR')
    print('E1 - IMPRIMIR TICKET')
    print('E2 - RESETEAR CAJA [SALIR]')
    print('---------------------------------')
#lineas solo para organizar
lines = '---------------------------------'
lista = [] #llenara la lista de productos
#llamamos al menu
menu()

inventario = {
    'A1': 2.00,
    'A2': 4.00,
    'A3': 7.00,
    'A4': 8.00,
    'B1': 2.50,
    'B2': 3.50,
    'C1': 5.00,
    'X1': 1.00
}

productos = {
    'A1': '🍌 Guineros 1kg - $2.00',
    'A2': '🍎 Manzana Gala 1kg - $4.00',
    'A3': '🍇 Uva Globe 1kg - $7.00',
    'A4': '🍓 Fresa 1kg - $8.00',
    'B1': '🍗 Pollo 1lb - $2.50',
    'B2': '🥩 Carne 1lb - $3.50',
    'C1': '🧋 Te frío con Tapioca 24onz - $5.00',
    'X1': '🍩 Dona glaseada - $1.00'
}

total = 0.00 #Total inicial

while 1 == 1:
  codigoInput = input('Ingrese un código y presiona <<ENTER>>:\n')
  codigo = codigoInput.upper() #convirtiendo entrada a Mayusculas
  print(lines)
  if codigo == 'E2' :
    total = 0.00
    lista=[]
    print(lines)
    print(f"Total reseteado a {total}")
    break
  elif codigo == "E0" :
        lines = '---------------------------------'
        print('---------------------------------')
        print('#            COBRANZA           #')
        print('---------------------------------')
        #total = float(input('Ingrese importe a pagar en USD \n'))
        print(lines)
        print('------    Formas de Pago   ------')
        print(lines)
        print('A - 💵 Efectivo')
        print('B - 💳 Tarjeta de Crédito')
        print(lines)
        inputfp = input('Ingrese la forma de pago: ')
        fp = inputfp.upper()
        if fp == 'A' :
            pago=float(input('Ingrese efectivo: '))
            if pago < total :
                print(lines)
                print('❌ Saldo insuficiente para realizar el pago')
            else :
                cambio=pago-total
                print(lines)
                print(f'Su cambio es: {str(cambio)}')
                print(lines)
                resp = input('Desea volver al menu, presione << si >> o << no >>\n')
                if(resp == 'si') :
                   menu()
                elif(resp == 'no') :
                   break
                else :
                   print('❌ Opción invalida')
        elif fp == 'B' :
            tarjeta = input('Ingrese número de tarjeta: ')
            print(lines)
            nip = input("Ingrese NIP: ")
            print(lines)
            print(f'Se ha cobrado {str(total)} de Dolar de su tarjeta ')
            resp = input('Desea volver al menu, presione << si >> o << no >>\n')
            if(resp == 'si') :
                menu()
            elif(resp == 'no') :
                break
            else :
                print('❌ Opción invalida')
        else:
            print('❌ FORMA DE PAGO NO VÁLIDA')
  elif codigo == "E1":
        tamano = len(lista)  # Usar lista en lugar de listaProductos
        print('---------------------------------')
        print('#        TIENDA LA +SURTIDA      #')
        print('---------------------------------')
        print('#          TICKET #0001          ')
        for i in range(tamano):
            print(lines)
            print(str(lista[i]))
        print(lines)
        print(f'#       TOTAL A PAGAR: {str(total)}        #')
         # Verificar si fp está definida antes de imprimir detalles de pago
        if 'fp' in locals():
            if fp == 'A':
                print(lines)
                print(f'#   CAMBIO: {str(cambio)} DE {str(pago)} #')
            elif fp == 'B':
                print(lines)
                print(f'#   Metodo de pago con Tarjeta #')
        else:
            print(lines)
            print('#    Pago pendiente de procesar    #')
        print(lines)

  else:
    precioP=inventario.get(codigo, 0)#buscar codigo
    listaProductos=productos.get(codigo, 0)#buscar codigo
    if precioP==0 :
      print(f'Código ingresado {codigo} no existe')
      print(lines)
      print(f'NO SE SUMO PRODUCTO \n TOTAL EN FACTURA: {str(total)}')
      print(lines)
    else:
      total +=precioP #Sumatoria acumulada
      lista.append(listaProductos)
      print(f'TOTAL EN FACTURA: {str(total)}')
      print(lines)
