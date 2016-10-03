import unittest
from figuras import Figuras

class TestFiguras(unittest.TestCase):

	def setUp(self):
		self.figura = Figuras()

	def test_area_cuadrado_lado_5(self):
		figura = Figuras()
		resultado = self.figura.cuadrado(5)
		self.assertEqual(25, resultado)

	def test_area_cuadrado_lado_6(self):
		figura = Figuras()
		resultado = self.figura.cuadrado(6)
		self.assertEqual(36, resultado)

	def test_area_cuadrado_lado_g(self):
		figura = Figuras()
		resultado = self.figura.cuadrado('g')
		self.assertEqual('dato incorrecto', resultado)

	def test_area_cuadrado_lado_4_5(self):
		figura = Figuras()
		resultado = self.figura.cuadrado(4.5)
		self.assertEqual(20.25, resultado)

	def tearDown(self):
		pass

if __name__ == '__main__':
	unittest.main()