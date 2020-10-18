from unittest import TestCase

from oo.carro import Motor


class CarroTestCase(TestCase):
    def teste_velocidade_inicial(self):
        motor = Motor() # importar a função do Motor()
        self.assertEqual(0, motor.velocidade)

    def teste_acelerar(self):
        motor = Motor() # importar a função do Motor()
        motor.acelerar() # executar o método acelerar()
        self.assertEqual(1, motor.velocidade)