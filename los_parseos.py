nombre = "Enzo"
apellido = "Acosta jr"
edad = 19 
peso = 68

# array

print("El nombre es {}, el apellido{}".format(nombre, apellido))
print(type(nombre))
print(type(edad))
print(type(peso))

# intentar el parsing
edad_en_string = str(edad)
print(f"""La edad anterior era {type(edad)},
      La edad parseada de este person  
      {type(edad_en_string)}""")
