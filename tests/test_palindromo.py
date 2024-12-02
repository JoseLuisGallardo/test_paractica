import unittest
from app.scripts.charfun import es_palindromo

class TestEsPalindromo(unittest.TestCase):

    def test_lista(self):
        list = ["ala", "Llell", "Anita lava la tina"]  # Lista de cadenas palíndromas
        for aux in list:
            self.assertTrue(
                es_palindromo(aux),
                f"La cadena '{aux}' debería ser un palíndromo."
            )

    def test_lista_false(self):
        not_chain = ["hola", "frase", "cadena"]  # Lista de cadenas no palíndromas
        for aux in not_chain:
            self.assertFalse(
                es_palindromo(aux),
                f"La cadena '{aux}' no debería ser un palíndromo."
            )

    def test_list_void(self):
        self.assertTrue(
            es_palindromo(""),
            "Una cadena vacía debería ser considerada un palíndromo."
        )

    def test_withspace(self):
        self.assertTrue(
            es_palindromo("Amo la paloma"),
            "La cadena con espacios y mayúsculas debería ser un palíndromo."
        )

    def test_list_incorectType(self):
        listFalse = [12, [1, 2, 3], {"clave": "valor"}, None]
        for aux in listFalse:
            with self.assertRaises(TypeError, msg=f"Se esperaba TypeError con la entrada {aux}."):
                es_palindromo(aux)

    def test_assert_equal(self):
        # Comparar resultados explícitos
        self.assertEqual(
            es_palindromo("reconocer"),
            True,
            "La cadena 'reconocer' debería ser un palíndromo."
        )
        self.assertEqual(
            es_palindromo("python"),
            False,
            "La cadena 'python' no debería ser un palíndromo."
        )

if __name__ == "__main__":
    unittest.main()
