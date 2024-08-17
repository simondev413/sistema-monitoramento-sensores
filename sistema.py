import asyncio
import time
from database import sensor_table

class Sistema:
    """
    tempo_leitura deve ser fornecido em minutos.
    """
    def __init__(self,tempo_leitura) -> None:
        self.dados = []
        self.log_erros = []
        self.sensores = []
        self.tarefas = []
        self.tempo_funcionamento = tempo_leitura*60
        

    def adicionar_sensor(self,sensor):
        self.sensores.append(sensor)

    async def ler_sensores(self,sensor):
        while True:
            try:
                valor = await sensor.ler()
                leitura = {'Time':time.strftime('%H:%M:%S'),'Sensor':sensor.nome,'valor':valor}

                sensor_table.min_val, sensor_table.max_val = sensor.limites
                sensor_table.ocorreu_erro = False
                sensor_table.nome = sensor.nome
                sensor_table.valor = valor
                sensor_table.intrevalo_leitura = sensor.intrevalo_leitura
                                
                self.dados.append(leitura)
            except Exception as e:
                sensor_table.ocorreu_erro = True
                self.log_erros.append({'sensor-nome':sensor.nome,'erro':str(e)})
                print(e)
            try:
                sensor_table.save()
            except Exception as e:
                raise e("Ocorreu um erro ao salvar os dados na base de dados.")
            
            await asyncio.sleep(sensor.intrevalo_leitura)

    async def start(self):             
        tarefas = [asyncio.create_task(self.ler_sensores(sensor)) for sensor in self.sensores]
        await asyncio.sleep(self.tempo_funcionamento)

        for tarefa in tarefas:
            tarefa.cancel()

        self.exibir_resumo()

    def exibir_resumo(self):
        print('\nResumo dos dados coletados:')
        for dado in self.dados:
            print(dado)

        print('\nLog de erros:')
        for erro in self.log_erros:
            print(erro)