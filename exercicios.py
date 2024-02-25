### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.

quantidade = int(input("Insira a quantidade de produtos vendidos:"))
preco = int(input("Insira o preco dos produtos vendidos:"))
try:
    quantidade > 0
    preco > 0
    print("Dados válidos.")
except:
    print("Insira valores positivos.")

# avaliando as variáveis quantidade e preço utilizando if else

quantidade_1 = int(input("Insira a quantidade de produtos vendidos:"))
preco_1 = int(input("Insira o preco dos produtos vendidos:"))

if quantidade_1 > 0 and preco_1 > 0:
    print("Valores válidos")
else:
    print("Valores inválidos")

### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

temperatura = int(input("Insira os valores de temperatura"))

if temperatura < 0:
    print(f"A temperatura {temperatura} é baixa")
elif 18 <= temperatura <= 26:
    print(f"A temperatura {temperatura} é média")
else:
    print(f"A temperatura {temperatura} é alta")

### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

if log['level'] == 'ERROR':
    print(log['message'])
    
### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.
    
idade = int(input("Insira a sua idade:"))
if 18 <= idade <= 65:
    email = input("Insira o seu e-mail:")
    if "@" in email:
        print("E-mail válido.")
    else:
        print("Insira um e-mail válido.")
else:
    print("Insira uma idade válida.")

### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

print("Bem-vindo ao sistema de detecção de transações suspeitas")
transacao = dict()

transacao['valor'] = int(input("Insira o valor da transação: "))
transacao['hora'] = int(input("Insira o horário que aconteceu a transação: "))

if transacao['valor'] > 10000:
    transacao['situacao'] = "suspeita"
else:
    transacao['situacao'] = "normal"

print(f"A sua transação foi considerada {transacao['situacao']}")


### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

texto = "hoje é a nossa segunda aula do bootcamp bootcamp de python"
palavras = texto.split() # se deixar em branco ele separa por espaços já.
contagem_de_palavras = {}

    #eu quero percorrer todas as palavras dentro de palavras e checar se ela já está no meu contagem de palavras

for palavra in palavras:
    if palavra in contagem_de_palavras:
        contagem_de_palavras[palavra] = +1
    else:
        contagem_de_palavras[palavra] = 1
print(contagem_de_palavras)
### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.
        


### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.