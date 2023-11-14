import unittest
from Examen2 import MiClase
class TestMiClaseMethods(unittest.TestCase):
    def setUp(self):
        # Crear un objeto de la clase MiClase con valores iniciales
        self.objeto = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])

    def test_ObtieneValencia(self):
        self.assertEqual(self.objeto.ObtieneValencia(1234567), 4)
        # Agrega más casos de prueba
        self.assertEqual(self.objeto.ObtieneValencia(24680), 0)
        self.assertEqual(self.objeto.ObtieneValencia(13579), 5)

    def test_DivisibleTempo(self):
        self.assertEqual(self.objeto.DivisibleTempo(10), [1, 2, 5, 10])
        # Agrega más casos de prueba
        self.assertEqual(self.objeto.DivisibleTempo(7), [1, 7])
        self.assertEqual(self.objeto.DivisibleTempo(15), [1, 3, 5, 15])

    def test_ObtieneMasBailable(self):
        self.assertEqual(self.objeto.ObtieneMasBailable([0.8, 0.9, 0.7]), 0.9)
        # Agrega más casos de prueba
        self.assertEqual(self.objeto.ObtieneMasBailable([0.5, 0.6, 0.4]), 0.6)
        self.assertEqual(self.objeto.ObtieneMasBailable([0.1, 0.2, 0.3]), 0.3)

    def test_VerificaListaCanciones(self):
        self.assertTrue(self.objeto.VerificaListaCanciones(["Canción 1", "Canción 2", "Canción 3"]))
        # Agrega más casos de prueba
        self.assertFalse(self.objeto.VerificaListaCanciones([None, "Canción 2", "Canción 3"]))
        self.assertTrue(self.objeto.VerificaListaCanciones(["Canción 1", "Canción 2", "Canción 3", "Canción 4"]))

    def test_Encuentra(self):
        lista = [1, 5, 8]
        elemento = 7
        self.assertTrue(self.objeto.Encuentra(lista, elemento))
        #
        self.assertFalse(self.objeto.Encuentra(lista, 10))
        self.assertTrue(self.objeto.Encuentra([10, 20, 30], 30))

if __name__ == '__main__':
    unittest.main()
