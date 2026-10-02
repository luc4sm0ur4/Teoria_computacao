# Máquina de Turing Multifita - Operações Lógicas ⚙️

Repositório destinado à **Atividade Avaliativa 2** da disciplina de **Teoria da Computação (TC2026.2)** da Universidade Federal do Tocantins (UFT), ministrada pelo Prof. Alexandre Tadeu Rossini da Silva.

## 🎯 Objetivo do Projeto

Projetar e implementar um simulador em Python de uma **Máquina de Turing determinística de duas fitas**, capaz de realizar três operações lógicas bit a bit: **AND, OR e XOR**.

A máquina atende aos seguintes requisitos rigorosos do projeto:

- **Fita 1 (Entrada e Trabalho):** Armazena a entrada inicial no formato `op w1#w2` e permite marcações (utilizando os símbolos `x` e `y`) durante o processamento.
- **Fita 2 (Saída):** Utilizada exclusivamente para escrever o resultado final. Não atua como memória auxiliar em nenhuma etapa.
- **Autonomia da MT:** A operação (AND, OR, XOR) não é definida por variáveis externas ou menus em Python, mas lida do primeiro símbolo da Fita 1 pela própria Máquina de Turing na sua função de transição inicial.
- **Simulação Estrita:** O cálculo não utiliza operadores bit a bit nativos do Python (como `&`, `|` ou `^`). Todo o processamento matemático ocorre puramente através do mapeamento formal das funções de transição de estados (\(\delta\)).

## 🏗️ Arquitetura e Algoritmo

### Alfabetos

- **Alfabeto de Entrada (\(\Sigma\)):** `{A, O, X, 0, 1, #}`
- **Alfabeto da Fita 1 (\(\Gamma_1\)):** `{A, O, X, 0, 1, #, x, y, B}`
- **Alfabeto da Fita 2 (\(\Gamma_2\)):** `{0, 1, B}`

## 📝 Formato da Entrada

A máquina processa cadeias no seguinte formato:

```text
op w1#w2
```

Onde:

- **`op`:** Símbolo da operação (`A` = AND, `O` = OR, `X` = XOR).
- **`w1`, `w2`:** Palavras binárias de mesmo comprimento (exemplo: `101`, `110`).
- **`#`:** Caractere separador das palavras.

### Exemplo do Estado Inicial das Fitas

**Fita 1:**

```text
A101#110BBBB...
```

**Fita 2:**

```text
BBBBBBBBBBB...
```

### Funcionamento do Algoritmo

O algoritmo opera por um método de **marcação e rebobinamento**, no qual a cabeça de leitura avança pela Fita 1 para marcar o bit de `w1`, avança até o bit correspondente em `w2`, opera os dois valores através das transições de estado simuladas, escreve a saída correspondente na Fita 2 (avançando apenas a cabeça da Fita 2) e, então, rebobina a Fita 1 para processar o próximo par de bits.

## 🚀 Como Executar

### Pré-requisitos

- Python 3.x instalado.
- Não há dependências de bibliotecas externas.

### Passos para Execução

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/luc4sm0ur4/Teoria_computacao.git
   ```

2. **Acesse o diretório do projeto:**

   ```bash
   cd Teoria_computacao
   ```

3. **Execute o simulador:**

   ```bash
   python maquina_turing.py
   ```

## 🧪 Casos de Teste e Validação

Ao ser executado, o script processa de forma autônoma a seguinte bateria de testes exigida, imprimindo no terminal o rastreio visual passo a passo, incluindo o estado atual, as posições das cabeças de leitura e o conteúdo de ambas as fitas.

| Operação | Entrada na Fita 1 | Saída Esperada na Fita 2 |
|---|---|---|
| AND | `A0#0` | `0` |
| AND | `A101#110` | `100` |
| OR | `O01#11` | `11` |
| OR | `O101#110` | `111` |
| XOR | `X01#11` | `10` |
| XOR | `X101#110` | `011` |

## 👨‍💻 Autor

**Lucas Carvalho da Luz Moura**

- **Matrícula:** `2020111816`
- **GitHub:** [luc4sm0ur4](https://github.com/luc4sm0ur4)