import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from maquina_cafe import MaquinaCafe

class TestMaquinaCafe(unittest.TestCase):

    def setUp(self):
        self.maquina = MaquinaCafe()

    def test_seleccionar_tamano_vaso(self):
        self.assertEqual(self.maquina.tamaño_vaso("pequeño"), "3 Oz")
        self.assertEqual(self.maquina.tamaño_vaso("mediano"), "5 Oz")
        self.assertEqual(self.maquina.tamaño_vaso("grande"), "7 Oz")

    def test_seleccionar_cantidad_azucar(self):
        self.assertEqual(self.maquina.cantidad_azucar(2), "2 cucharadas")

    def test_recoger_vaso(self):
        self.assertEqual(self.maquina.recoger_vaso(), "Vaso recogido")

    def test_mostrar_mensaje_faltante(self):
        self.assertEqual(self.maquina.verificar_ingredientes(False, True, True), "No hay vasos disponibles")
        self.assertEqual(self.maquina.verificar_ingredientes(True, False, True), "No hay azúcar disponible")
        self.assertEqual(self.maquina.verificar_ingredientes(True, True, False), "No hay café disponible")

if __name__ == "__main__":
    unittest.main()


#git