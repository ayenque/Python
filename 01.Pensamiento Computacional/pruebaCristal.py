import unittest


def es_mayor_edad(edad):
    if edad >= 18:
        return  False  #cambiamos la funcion por error
    else:
        return  False


class Prueba_de_Cristal_Test (unittest.TestCase):

    def test_es_mayor_edad(self):
        edad = 20

        resultado = es_mayor_edad(edad)

        self.assertEqual(resultado,True)


    def test_es_menor_edad(self):
        edad = 17

        resultado = es_mayor_edad(edad)

        self.assertEqual(resultado,False)



if  __name__ == '__main__':
    unittest.main(verbosity=2) #Se le puede agregar el parámetro verbosity=2 al método unittest.main
                                # para que el resultado en la consola sea mas detallado.

