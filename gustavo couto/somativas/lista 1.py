#Somativa


# 1. Registro de Veículo
# print("--- 1. Registro de Veículo ---")
# modelo = input("Digite o modelo do veículo: ")
# placa = input("Digite a placa do veículo: ")
# print(f"Veículo {modelo} de placa {placa} registrado no sistema. Boa viagem!")

# 2. Cálculo de Autonomia
# print("--- 2. Cálculo de Autonomia ---")
# capacidade_tanque = float(input("Digite a capacidade do tanque (litros): "))
# consumo_medio = float(input("Digite o consumo médio do caminhão (km/l): "))
# resposta = capacidade_tanque/consumo_medio
# print(f"O veículo pode percorrer {resposta:} km com o tanque cheio.\n")

# 3. Conversor de Moeda (Frete Internacional)
# print("--- 3. Conversor de Moeda ---")
# valor_usd = float(input("Digite o valor do frete em Dólar (USD): "))
# taxa_conversao = 5.00
# valor_brl = valor_usd * taxa_conversao
# print(f"Valor do frete em Real: R$ {valor_brl:}\n")

# 4. Média de Entrega
# print("--- 4. Média de Entrega ---")
# tempo1 = float(input("Tempo da 1ª rota (horas): "))
# tempo2 = float(input("Tempo da 2ª rota (horas): "))
# tempo3 = float(input("Tempo da 3ª rota (horas): "))
# media_tempo = (tempo1 + tempo2 + tempo3) / 3
# print(f"A média de tempo das entregas é: {media_tempo}")

#5. Peça o peso atual de um caminhão em toneladas.
#print("---5. Peça o peso atual de um caminhão em toneladas---")

# peso = float(input("Digite o peso atual do caminhão (t): "))

# if peso < 10:
#     print("Carga Leve")
# elif 10 <= peso <= 25:
#     print("Carga Padrão")
# else:
#     print("ALERTA: Excesso de Peso!")

#6. Classificador de Destino
#print("---6. Classificador de Destino---")
# codigo = input("Digite o código da carga: ")

# if codigo == ("N"):
#     print("Região Norte")
# elif codigo == ("S"):
#     print("Região Sul")
# else:
#     print("Região Internacional")

#7. Liberação de Saída
# print("---7. Liberação de Saída---")
# checklist = input("O checklist está concluído? (sim/nao): ")
# motorista_identificado = input("Motorista identificado? (sim/nao): ")

# if checklist == ("sim") and motorista_identificado == ("sim"):
#     print("Veículo AUTORIZADO a iniciar a rota.")
# else:
#     print("Veículo NÃO autorizado. Verifique as pendências.")

#8. Cálculo de Atrasos
# print("---8. Cálculo de Atrasos---")
# entregas_total = int(input("Total de entregas agendadas: "))
# entregas_atraso = int(input("Total de entregas com atraso: "))

# if entregas_total > 0:
#    indice_atraso = (entregas_atraso / entregas_total) * 100
#    if indice_atraso > 10:
#         print("Necessário Otimizar Rotas")
#    else:
#         print("Logística Eficiente")
# else:
#     print("Nenhuma entrega registrada.")

#9. Validação de Calibragem
# print("---9. Validação de Calibragem---")
# pressao = float(input("Digite a pressão do pneu (PSI): "))

# if 100 <= pressao <= 110:
#     print("Dentro do padrão")
# elif pressao < 100:
#     print("Abaixo do recomendado")
# else:
#     print("Acima do recomendado")

# #10.Contagem de Embarque
# print("---10.Contagem de Embarque---")

# import time

# for i in range(5, 0, -1):
#     print(f"Portão fecha em {i}...")
#     time.sleep(1)

# print("Portão Trancado!")

#11.Somatório de Fretes (Acumulador)
# print("---11.Somatório de Fretes (Acumulador)---")
# faturamento_total = 0
# valor_frete = -1 

# while valor_frete != 0:
#     valor_frete = float(input("Digite o valor do frete (ou 0 para encerrar): "))
#     faturamento_total += valor_frete

# print(f"Faturamento total acumulado: R$ {faturamento_total:}")

#12.Monitoramento de Frota
# print("---12.Monitoramento de Frota---")
# maior_km = 0

# for i in range(1, 6):
#     km = float(input(f"Digite a quilometragem do veículo {i}: "))
#     if km > maior_km:
#         maior_km = km

# print(f"A maior quilometragem registrada foi: {maior_km} km")


#13.Sistema de Rastreio track99
# print("---3.Sistema de Rastreio track99---")
# codigo_correto = "track99"
# tentativas = 0
# max_tentativas = 3

# while tentativas < max_tentativas:
#     codigo_input = input("Digite o código de acesso do rastreador: ")
    
#     if codigo_input == codigo_correto:
#         print("Acesso Permitido. Iniciando rastreamento...")
#         break
#     else:
#         tentativas += 1
#         print("Acesso Negado.")
#         if tentativas < max_tentativas:
#             print(f"Tentativas restantes: {max_tentativas - tentativas}")

# else:
#     print("Rastreamento Bloqueado.")

