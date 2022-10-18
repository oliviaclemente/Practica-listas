# Ejercicio 1: Utilice las funciones anteriores para agregar elementos faltantes
# Ejercicio 2: Utilice las funciones anteriores para elminar elementos sobrantes

def ejercicio1():      
  lista = ["P", "t"]      
  # TODO       
  assert "".join(lista) == "Python"   
  lista.insert(1,"y")
  lista.pop("h","o","n")  

def ejercicio2():
    lista = [1, 4, 2, 5, 4, 3, 4, 7, 5, 8, 9]
    # TODO
    assert lista == list(range(1, 6))
    lista.remove(4)
    lista.remove(5)
    lista.remove(4)
    lista.remove(7)
    lista.remove(8)
    lista.remove(9)
