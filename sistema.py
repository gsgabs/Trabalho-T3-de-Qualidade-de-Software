# sistema.py

class Cliente:
    def __init__(self, perfil_id, estado_uf):
        self.perfil_id = perfil_id
        # Garante que o estado fique minusculo e sem espaços
        self.estado_uf = estado_uf.lower().strip()


class CalculadoraPedidoService:
    ESTADOS_SUDESTE = ["sp", "mg", "es", "rj"]

    # Lista completa para validação
    ESTADOS_BRASIL = [
        "ac", "al", "ap", "am", "ba", "ce", "df", "es", "go",
        "ma", "mt", "ms", "mg", "pa", "pb", "pr", "pe", "pi",
        "rj", "rn", "rs", "ro", "rr", "sc", "sp", "se", "to"
    ]

    def calcular_desconto(self, cliente: Cliente) -> float:
        # RN01
        if cliente.perfil_id == 0:  # Basico
            return 0.0
        elif cliente.perfil_id == 1:  # Bronze
            return 0.03
        elif cliente.perfil_id == 2:  # Prata
            return 0.05
        elif cliente.perfil_id == 3:  # Ouro
            return 0.1
        else:
            raise ValueError(f"Erro: Perfil '{cliente.perfil_id}' inválido. O programa será encerrado.")

    def calcular_frete(self, cliente: Cliente) -> float:

        # RN02
        if cliente.estado_uf == "sp":
            return 0.0
        elif cliente.estado_uf in self.ESTADOS_SUDESTE:
            return 0.05
        elif cliente.estado_uf in self.ESTADOS_BRASIL:
            return 0.08
        else:
            raise ValueError(f"Erro: Região '{cliente.estado_uf}' desconhecida ou fora do Brasil.")


    def processar_pedido(self, cliente: Cliente, valor_pedido: float) -> float:
        desconto = self.calcular_desconto(cliente)
        taxa_frete = self.calcular_frete(cliente)

        valor_com_desconto = valor_pedido - (valor_pedido * desconto)
        valor_do_frete = valor_pedido * taxa_frete

        return valor_com_desconto + valor_do_frete