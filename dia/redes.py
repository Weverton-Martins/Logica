'''Um pouco de base pra automação basica com Redes / Cybersecutiry'''

#Exercício 1: Varredura de Logs (Listas, For e Condicionais)

logs = [200, 404, 500, 200, 401, 401, 200, 401]
alertas = 0

for erro in logs:
    if erro == 401:
        alertas +=1

print(f'O Total de alertas encontrados foi: {alertas}')

#Exercício 2: Consulta Segura de Ativos (Funções, Dicionários e Try/Except)

servidor = {
    'hostname' : 'srv-web01',
    'ip': '10.0.0.5'
}

def buscarDados(chave):
    try:
        print(servidor[chave])
    
    except KeyError:
        print('Atenção: Dado não encontrado no sistema.')

buscarDados('ip')

#Exercício 3: Filtrando Alertas Estruturados

eventos = [
    {"ip": "192.168.1.10", "acao": "login", "status": "sucesso"},
    {"ip": "10.0.0.5", "acao": "login", "status": "falha"},
    {"ip": "172.16.0.8", "acao": "download", "status": "sucesso"},
    {"ip": "10.0.0.5", "acao": "login", "status": "falha"}
]

for item in eventos:
    if item['status'] == 'falha':
        print(f'Alerta falha detectada no IP:{item["ip"]}')

# Exercício 4: Detecção de Força Bruta (Agrupamento)

logs_firewall = [
    {"ip": "10.0.0.22", "acao": "login", "status": "falha"},
    {"ip": "192.168.1.10", "acao": "login", "status": "sucesso"},
    {"ip": "10.0.0.22", "acao": "login", "status": "falha"},
    {"ip": "10.0.0.22", "acao": "login", "status": "falha"},
    {"ip": "172.16.0.8", "acao": "login", "status": "falha"}
]

alertas_IP = {}

for item in logs_firewall:
    if item['status'] == 'falha':
        if item["ip"] in alertas_IP:
            alertas_IP[item["ip"]] +=1
        else:
            alertas_IP[item["ip"]] =1

print(alertas_IP)
        