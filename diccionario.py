# En esta unidad vamos abordar como se programa desde los diccionarios

#Crear un diccionario
puntajes = {"Juan": 45, "María": 67, "Pedro": 78, "Ana": 50}

# Acceder a valores por clave
print(puntajes["María"]) #Salida 67

#Modificar Valores
puntajes["Pedro"] = 82 
print(puntajes) #salida {"Juan": 45, "María": 67, "Pedro": 82, "Ana": 50}

#Agregar Nuevos elementos
puntajes["Carlos"] = 88 
print(puntajes) #salida {"Juan": 45, "María": 67, "Pedro": 82, "Ana": 50 "Carlos": 88}

#Eliminar elementos por clave
del puntajes["Ana"]
print (puntajes) #salidas {"Juan": 45, "María": 67, "Pedro": 82, "Carlos": 88}

