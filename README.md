# Sistema de monitoramento de sensores.

### Descrição:
Este projeto é uma simulação de um sistema de monitoramento de sensores. Com objectivo de aprimorar minhas habilidades em programação assíncrona e melhores práticas de código (Clean Code, SOLID).

### Objetivos:
Desenvolver um sistema de monitoramento em tempo real para uma fábrica. A fábrica possui diversos sensores espalhados por diferentes áreas, como temperatura, umidade, pressão, e nível de vibração.

### O Sistema deve:
1. Ler os dados de múltiplos sensores simultaneamente: 
    - Cada sensor deve ser lido em intrevalos regulares (e.x.: a cada 2 segundos.)
        
2. Detectar condições críticas:
    - Se algum sensor reportar um valor fora do intrevalo normal( por exmplo, temperatura muito alta ou baixa), o sistema deve registrar uma alerta.

3. Registrar os dados:
   - Os dados coletados de todos os sensores devem se armazenados para análise posterior.

1. Simular falhas nos sensores:
    - Alguns sensores podem falhar e parar de responder, o sistema deve detectar essa falha e lidar com ela adequadamente.

### Tarefas:
1. Leitura de sensores:
    - Crie corrotinas que simulem a leitura de diferentes sensores.
    -  Cada sensor deve reportar um valor aleatório dentro de um intrevalo esperado mas ocasionalmente poder gerar valores fora de intrevalo (indicando uma condição crítica).

2. Detenção de falhas:
    - Adicione logica para simular falhas em sensores, onde um sensor pode parar de responder(por exemplo, não retornar nenhum valor após um determinado tempo).

3. Registro de dados e alertas:
    - Simule o registro dos dados coletados e a emissão de alertas quando condições críticas forem detectadas.

### Dicas de implementação:
- Intrevalos regulares: use asyncio.sleep para simular a leitura periódica dos sensores.
- Condições críticas: utilize comparações simples para detectar valores for do intrevalo normal e gerar alertas.
- Falhas simuladas: aleatoriamente faça com que alguns sensores parem de funcionar (por exmplo, lançando uma exceção ou retornando None).
                
