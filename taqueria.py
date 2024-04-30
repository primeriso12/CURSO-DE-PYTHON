#Una de las taquerias mas famosas de Mexico se llama poncho y ofrece platos demasiados ricos, según el diccionario a continuación lo vamos a ver

def main():
    
    menu= {
        "Baja taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla": 8.00
        }
    order_total: 0.0
    while True:
        try:
            item= input("ingrese un articulo de su pedido: ")
        except EOFError:
            break
        item = item.upper() # type: ignore
        if item in menu:
            order_total += menu[item]
        elif item == "CONTROL _ D":
          print(f"el total de su pedido es ${order_total:.2f}")
          break
    else:
        print("articulo invalido")
    
    if __name__ == "__main__":
     main()
        
        

    

