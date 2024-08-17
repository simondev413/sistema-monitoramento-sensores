import asyncio
import random

class Sensor:
    def __init__(self,intrevalo_leitura:int,limites:tuple) -> None:
        self.nome = self.__class__.__name__
        self.intrevalo_leitura = intrevalo_leitura
        self.limites = limites

    async def ler(self):
        
        # simular falha de leitura no sensor
        if random.choice([True,False,False,False,False]): # isso dá 20 de chance de falhar
            raise Exception(f"Sensor {self.nome} falhou!")
        
        valor = random.uniform(*self.limites)
        print(f"{self.nome} leu o valor: {valor}")
        
        return valor

class SensorTemperatura(Sensor):
    def __init__(self, intrevalo_leitura: int, limites: tuple) -> None:
        super().__init__(intrevalo_leitura, limites)
    
class SensorUmidade(Sensor):
    def __init__(self, intrevalo_leitura: int, limites: tuple) -> None:
        super().__init__(intrevalo_leitura, limites)

class SensorPressao(Sensor):
    def __init__(self, intrevalo_leitura: int, limites: tuple) -> None:
        super().__init__(intrevalo_leitura, limites)