import time

class MaquinaTuring:
    def __init__(self, entrada):
        # A fita 1 permite marcações[cite: 2]
        self.fita1 = list(entrada) 
        # A fita 2 começa em branco[cite: 1] e não é memória auxiliar[cite: 2]
        self.fita2 = ["B"] 
        self.cabeca1 = 0
        self.cabeca2 = 0
        self.estado = "q0"
        self.transicoes = self._gerar_transicoes()
        
    def _gerar_transicoes(self):
        """Gera o dicionário de transições δ para as 3 operações simulando uma MT."""
        t = {}
        # Estado Inicial[cite: 1]
        t[("q0", "A", "B")] = ("q_and_find", "A", "B", "R", "S")
        t[("q0", "O", "B")] = ("q_or_find", "O", "B", "R", "S")
        t[("q0", "X", "B")] = ("q_xor_find", "X", "B", "R", "S")

        operacoes = {
            "and": {"simbolo": "A", "logica": {(0,0):0, (0,1):0, (1,0):0, (1,1):1}},
            "or":  {"simbolo": "O", "logica": {(0,0):0, (0,1):1, (1,0):1, (1,1):1}},
            "xor": {"simbolo": "X", "logica": {(0,0):0, (0,1):1, (1,0):1, (1,1):0}}
        }

        for op, dados in operacoes.items():
            simbolo = dados["simbolo"]
            logica = dados["logica"]
            
            # Buscar bit não marcado em w1
            t[(f"q_{op}_find", "x", "B")] = (f"q_{op}_find", "x", "B", "R", "S")
            t[(f"q_{op}_find", "y", "B")] = (f"q_{op}_find", "y", "B", "R", "S")
            t[(f"q_{op}_find", "0", "B")] = (f"q_{op}_0_w1", "x", "B", "R", "S")
            t[(f"q_{op}_find", "1", "B")] = (f"q_{op}_1_w1", "y", "B", "R", "S")
            t[(f"q_{op}_find", "#", "B")] = ("q_accept", "#", "B", "S", "S")

            # Avançar w1 até encontrar o '#'
            for val in ["0", "1"]:
                t[(f"q_{op}_0_w1", val, "B")] = (f"q_{op}_0_w1", val, "B", "R", "S")
                t[(f"q_{op}_1_w1", val, "B")] = (f"q_{op}_1_w1", val, "B", "R", "S")
            t[(f"q_{op}_0_w1", "#", "B")] = (f"q_{op}_0_w2", "#", "B", "R", "S")
            t[(f"q_{op}_1_w1", "#", "B")] = (f"q_{op}_1_w2", "#", "B", "R", "S")

            # Avançar marcadores de w2
            for val in ["x", "y"]:
                t[(f"q_{op}_0_w2", val, "B")] = (f"q_{op}_0_w2", val, "B", "R", "S")
                t[(f"q_{op}_1_w2", val, "B")] = (f"q_{op}_1_w2", val, "B", "R", "S")

            # Processar o bit alvo de w2 e calcular resultado
            res_00 = str(logica[(0,0)])
            res_01 = str(logica[(0,1)])
            res_10 = str(logica[(1,0)])
            res_11 = str(logica[(1,1)])
            
            t[(f"q_{op}_0_w2", "0", "B")] = (f"q_{op}_rewind", "x", res_00, "L", "R")
            t[(f"q_{op}_0_w2", "1", "B")] = (f"q_{op}_rewind", "y", res_01, "L", "R")
            t[(f"q_{op}_1_w2", "0", "B")] = (f"q_{op}_rewind", "x", res_10, "L", "R")
            t[(f"q_{op}_1_w2", "1", "B")] = (f"q_{op}_rewind", "y", res_11, "L", "R")

            # Rebobinar até a primeira posição (operação)
            for val in ["0", "1", "x", "y", "#"]:
                t[(f"q_{op}_rewind", val, "B")] = (f"q_{op}_rewind", val, "B", "L", "S")
            t[(f"q_{op}_rewind", simbolo, "B")] = (f"q_{op}_find", simbolo, "B", "R", "S")

        return t

    def formatar_fita(self, fita, cabeca):
        res = ""
        for i, val in enumerate(fita):
            if i == cabeca: res += f"[{val}]"
            else: res += val
        if cabeca >= len(fita): res += "[B]"
        return res

    def imprimir_estado(self):
        """Imprime a simulação a cada passo"""
        f1_str = self.formatar_fita(self.fita1, self.cabeca1)
        f2_str = self.formatar_fita(self.fita2, self.cabeca2)
        print(f"Estado: {self.estado:<15} | Fita 1: {f1_str:<25} (Pos: {self.cabeca1}) | Fita 2: {f2_str:<15} (Pos: {self.cabeca2})")

    def executar(self, exibir_passos=False):
        if exibir_passos:
            print("\n--- INICIANDO EXECUÇÃO ---")
            self.imprimir_estado()

        while self.estado != "q_accept":
            s1 = self.fita1[self.cabeca1] if self.cabeca1 < len(self.fita1) else "B"
            s2 = self.fita2[self.cabeca2] if self.cabeca2 < len(self.fita2) else "B"

            chave = (self.estado, s1, s2)
            if chave not in self.transicoes:
                print(f"Erro: Transição não definida para {chave}")
                break

            n_estado, n_s1, n_s2, m1, m2 = self.transicoes[chave]

            # Escrever fitas
            if self.cabeca1 < len(self.fita1): self.fita1[self.cabeca1] = n_s1
            else: self.fita1.append(n_s1)

            if self.cabeca2 < len(self.fita2): self.fita2[self.cabeca2] = n_s2
            else: self.fita2.append(n_s2)

            self.estado = n_estado

            # Movimentar cabeças
            if m1 == "R": self.cabeca1 += 1
            elif m1 == "L": self.cabeca1 = max(0, self.cabeca1 - 1)

            if m2 == "R": self.cabeca2 += 1
            elif m2 == "L": self.cabeca2 = max(0, self.cabeca2 - 1)

            if exibir_passos:
                self.imprimir_estado()

        # O resultado na fita 2 (ignora os B's sobressalentes)
        resultado = "".join(self.fita2).replace("B", "")
        return resultado

# ---------------- CASOS DE TESTE ----------------
testes = [
    ("A0#0", "0"),
    ("A101#110", "100"),
    ("O01#11", "11"),
    ("O101#110", "111"),
    ("X01#11", "10"),
    ("X101#110", "011")
] 

print("="*60)
print("EXECUÇÃO DOS CASOS DE TESTE")
print("="*60)

for entrada, esperado in testes:
    # Mostrar os passos apenas para um caso pequeno para não poluir demais o console,
    # mas você pode mudar para True para ver todos detalhados
    exibir_rastreio = True if entrada == "A0#0" else False 
    
    mt = MaquinaTuring(entrada)
    obtido = mt.executar(exibir_passos=exibir_rastreio)
    
    status = "APROVADO" if obtido == esperado else "FALHOU"
    print(f"\nResumo do Teste: {entrada} -> esperado {esperado} -> obtido {obtido} [{status}]")