import unittest
from charfun import es_palindromo

class TestEsPalindromo(unittest.TestCase):

    def test_cadena_palindroma(self):
        cadenas_pal = ["elle", "Llell", "Anita lava la tina"]  # Lista de cadenas palíndromas
        for cadena in cadenas_pal:
            self.assertTrue(
                es_palindromo(cadena),
                f"La cadena '{cadena}' debería ser un palíndromo."
            )

    def test_cadena_no_palindroma(self):
        cadenas_no_pal = ["hola", "frase", "cadena"]  # Lista de cadenas no palíndromas
        for cadena in cadenas_no_pal:
            self.assertFalse(
                es_palindromo(cadena),
                f"La cadena '{cadena}' no debería ser un palíndromo."
            )

    def test_cadena_vacia(self):
        self.assertTrue(
            es_palindromo(""),
            "Una cadena vacía debería ser considerada un palíndromo."
        )

    def test_cadena_con_espacios_y_tildes(self):
        self.assertTrue(
            es_palindromo("Amo la paloma"),
            "La cadena con espacios y mayúsculas debería ser un palíndromo."
        )

    def test_excepciones_tipo_incorrecto(self):
        entradas_invalidas = [12, [1, 2, 3], {"clave": "valor"}, None]
        for entrada in entradas_invalidas:
            with self.assertRaises(TypeError, msg=f"Se esperaba TypeError con la entrada {entrada}."):
                es_palindromo(entrada)

if __name__ == "__main__":
    unittest.main()
