
<h1 align="center">📋 Teste Técnico - Soluções de Problemas em Python</h1>

<p align="center">
  Bem-vindo(a) ao repositório que contém minhas soluções para o teste técnico! Aqui, resolvo problemas de lógica e algoritmos utilizando a linguagem Python, abordando questões que envolvem cálculos simples, sequências, manipulação de dados em JSON e até mesmo manipulação de strings. 🚀
</p>

---

## 📂 Estrutura do Projeto

Dentro deste projeto, você encontrará cinco classes, cada uma delas desenvolvida para resolver um problema específico. Abaixo, detalho cada uma delas e o que você pode esperar ao executá-las.

### 🚀 Funcionalidades Implementadas

1. **Somador**: Classe que calcula a soma de números consecutivos até o valor de um índice.
2. **Fibonacci**: Verifica se um número informado pertence à sequência de Fibonacci.
3. **FaturamentoDistribuidora**: Lê dados de faturamento diário a partir de um arquivo JSON, calculando o menor, maior faturamento, a média mensal e dias acima da média.
4. **FaturamentoPorEstado**: Calcula o percentual de faturamento de uma distribuidora por estado com base em dados fornecidos.
5. **InversorString**: Inverte uma string informada sem o uso de funções nativas como `reverse`.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**: Linguagem principal utilizada para a implementação dos algoritmos.
- **JSON**: Utilizado para simular dados de faturamento diários da distribuidora.
- **Jupyter Notebook (Opcional)**: Ideal para visualizar e executar o código passo a passo, mas o projeto pode ser rodado diretamente no terminal.

---

## 🎯 Como Executar o Projeto

### Pré-requisitos:

- [Python 3.x](https://www.python.org/downloads/) instalado na sua máquina.
- Um ambiente virtual é recomendado para instalar pacotes e rodar o projeto.

### Passos:

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/teste-tecnico.git

2. Entre no diretório do projeto:
   ```bash
   cd teste-tecnico

3. Execute os scripts individuais conforme cada problema. Por exemplo, para rodar o script de Fibonacci:
   ```bash
   python fibonacci.py

---

## 📄 Descrição das Soluções

### 1. **Somador**
   - Esta classe realiza a soma dos números inteiros até um determinado índice. A lógica é simples, mas eficiente para o propósito de somas consecutivas. 
   - Cuidados: Ao utilizar loops em Python, certifique-se de não ultrapassar o índice final, evitando loops infinitos que possam causar travamentos.

### 2. **Fibonacci**
   - Aqui, resolvemos a verificação de sequência de Fibonacci. Dado um número, ele retorna se o número pertence à sequência. Além disso, o algoritmo é otimizado para evitar cálculos desnecessários.
   - Dica: Python lida bem com números grandes, mas em alguns casos, calcular Fibonacci para números muito altos pode exigir técnicas de memoização para melhorar a performance.

### 3. **FaturamentoDistribuidora**
   - Lê dados de faturamento diário a partir de um arquivo JSON e faz os seguintes cálculos:
     - Menor valor de faturamento.
     - Maior valor de faturamento.
     - Dias com faturamento superior à média mensal.
   - **Importante**: Dias com faturamento `0` (final de semana ou feriados) são ignorados no cálculo da média mensal.
   - Cuidados: Para processar dados JSON, certifique-se de que o arquivo esteja no formato correto e que o código trate exceções, como arquivos faltantes ou malformados.

### 4. **FaturamentoPorEstado**
   - Utiliza um dicionário com dados de faturamento por estado e calcula o percentual de participação de cada um no faturamento total.
   - Dica: Certifique-se de que todos os valores do dicionário estão corretos e consistentes. É útil validar os dados antes de realizar cálculos.

### 5. **InversorString**
   - Recebe uma string como entrada e retorna sua versão invertida, sem usar funções prontas como `reverse`.
   - Cuidados: Ao lidar com strings de grandes tamanhos, o uso excessivo de concatenação pode impactar a performance. Em Python, é melhor usar listas e depois unir os elementos usando `"".join(lista)`.

---

## 🚀 Próximos Passos

- Melhorar a leitura de arquivos JSON para que possam ser facilmente configuráveis pelo usuário.
- Adicionar testes unitários para validar as soluções de maneira automatizada.
- Permitir a entrada de dados via linha de comando, tornando o código mais interativo.

---

<p align="center">
  <strong>Contribuições são bem-vindas!</strong> 😊 Se quiser aprimorar algo ou sugerir melhorias, fique à vontade para abrir issues ou enviar pull requests.
</p>

---

### 📧 Contato

Em caso de dúvidas ou sugestões, entre em contato:

- **LinkedIn**: [Gabriel Moreira](https://www.linkedin.com/in/gabriel-moreira-85b162251/)

---

<p align="center">
  Espero que o código seja útil e fácil de entender. Fique à vontade para explorar e modificar!
</p>
