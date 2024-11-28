import unittest

from app.scripts.charfun import es_palindromo

class TestEsPartest(unittest.TestCase):
    def test_numeros_pares(self):
        numeros_pares = [0, 2, -4, 4.0, 100]  # Lista de números pares
        for numero in numeros_pares:
            resultado = es_palindromo(numero)
            self.assertTrue(
                resultado,
                f"El número {numero} debería ser par, pero la función devolvió {resultado}."
            )
    
    def test_numeros_impares(self):
        numeros_impares = [1, -1, 3, 5.0, 101]  # Lista de números impares
        for numero in numeros_impares:
            resultado = es_par(numero)
            self.assertFalse(
                resultado,
                f"El número {numero} debería ser impar, pero la función devolvió {resultado}."
            )
    
    def test_excepciones_tipo_incorrecto(self):
        entradas_invalidas = ["texto", [1, 2, 3], {"clave": "valor"}, None]
        for entrada in entradas_invalidas:
            try:
                es_par(entrada)
                self.fail(f"Se esperaba TypeError con la entrada {entrada}, pero no se lanzó una excepción.")
            except TypeError:
                pass  # La excepción fue lanzada correctamente, no hacemos nada

if __name__ == "__main__":
    unittest.main()