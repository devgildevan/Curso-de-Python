'''
CONSTANTE =     'Variáveis' que não vão Mudar
AS CONTANTES SÃO DECLARADAS COM LETRAS MAIUSCULAS

Muitas condições no mesmo if (é ruim)
    <- Contagem de complexidade (ruim)
'''

velocidade = 100 # Velocidade atual do carro
local_carro = 99  # Local em que o carro está na entrada

SEMAFARO_1 = 60      #Valocidade máxima do radar 1
LOCAL_1 = 100     #Local onde o Radar está
SEMAFORO_RANGER = 1  # A distância onde o radar vai pegar

vel_carro_pass_radar_1 = velocidade > SEMAFARO_1
if vel_carro_pass_radar_1:
    print('Velocidade do carro passou o radar 1 ')

if local_carro >= (LOCAL_1 - SEMAFORO_RANGER) and \
    local_carro <= (LOCAL_1 + SEMAFORO_RANGER) and \
        velocidade > SEMAFARO_1:
    print('Carro multado')