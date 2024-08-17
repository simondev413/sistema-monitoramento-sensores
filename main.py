from sensores import (
    SensorPressao,
    SensorTemperatura,
    SensorUmidade)
from sistema import Sistema
import asyncio

async def main():
    sistema = Sistema(tempo_leitura=1)    # configurado para operar por 1 minuto
    sistema.adicionar_sensor(SensorPressao(intrevalo_leitura=7,limites=(950, 1050)))
    sistema.adicionar_sensor(SensorUmidade(intrevalo_leitura=60,limites=(30, 70)))
    sistema.adicionar_sensor(SensorTemperatura(intrevalo_leitura=2,limites=(11, 35)))

    await sistema.start()

if __name__ == '__main__':
    asyncio.run(main())
