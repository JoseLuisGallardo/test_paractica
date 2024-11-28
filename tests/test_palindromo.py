import unittest
from app.scripts.charfun import es_palindromo 


class Test_EsPalindromo(unittest.TestCase):

    def test_cadena_pal(self):
        cadenas_pal = ["elle","llell","iiiiii"]  # Lista de cadenas palíndromas
        for i in cadenas_pal:
            resultado = es_palindromo(i)
            self.assertTrue(
                resultado,
                f"La cadena {i} debería ser un palíndromo, pero la función devolvió {resultado}."
            )
    
    def test_cadena_nopal(self):
        cadenas_nopal = ["hola","frase","cadena","nopal","fasasdas"]  # Lista de cadenas no palíndromas
        for i in cadenas_nopal:
            resultado = es_palindromo(i)
            self.assertFalse(
                resultado,
                f"La cadena {i} no debería ser un palíndromo, pero la función devolvió {resultado}."
            )
    
    def test_excepciones_tipo_incorrecto(self):
        entradas_invalidas = [12, [1, 2, 3], {"clave": "valor"}, None]
        for entrada in entradas_invalidas:
            try:
                es_palindromo(entrada)
                self.fail(f"Se esperaba TypeError con la entrada {entrada}, pero no se lanzó una excepción.")
            except TypeError:
                pass  # La excepción fue lanzada correctamente, no hacemos nada

    def test_mayus(self):
        self.assertEqual('foo'.upper(), 'FOO') # Igualación entre mayúsculas y minúsculas

if __name__ == "__main__":
    unittest.main()