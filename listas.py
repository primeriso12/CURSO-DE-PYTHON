#En esta ocasión vamos a trabajar con un concepto fundamental en Python y en cualquier mensaje de programación
#LAS LISTAS vamos a crear una aplicación sencilla para gestionar nuestra lista de compras, empecemos:

def main():
    shopping_list = []

    while True:
        print("\n---lista de compras---")
        print("1. Agregar artículo")
        print("2. Eliminar artículo")
        print("3. Ver lista")
        print("4. Salir")

        option = input ("Por favor introduzca una opción")

        if option == "1":
           item = input ("Introduce el nombre del artículo que quieres agregar: ")
           shopping_list.append(item)
        elif option == "2":
            item = input ("Introduce el nombre del artículo que quieres eliminar: ")
            if item in shopping_list:
                shopping_list.remove(item)
            else:
               print("El artículo no se encuentra en la lista.")
        elif option == "3":
             print("\nTu lista de compra es:")
             for item in shopping_list:
                print("- "+item)
        elif option == "4":
             break
        else:
            print("opcion inválida. Por favor, intenta de nuevo.")
if __name__== "__main__":
    main()


                

        
  