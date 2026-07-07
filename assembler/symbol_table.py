co"""
symbol_table.py

"""


class SymbolTable:
    """Tabela de símbolos do Assembler Hack."""

    def __init__(self):
        # Símbolos predefinidos da plataforma Hack
        self.symbols = {
            "SP": 0,
            "LCL": 1,
            "ARG": 2,
            "THIS": 3,
            "THAT": 4,
            "SCREEN": 16384,
            "KBD": 24576,
        }
        for i in range(16):
            self.symbols[f"R{i}"] = i

        # Próximo endereço livre para variáveis (a partir de 16)
        self.next_address = 16

    def add_entry(self, symbol: str, address: int) -> None:
        """Registra um símbolo (tipicamente um label) com um endereço."""
        self.symbols[symbol] = address

    def contains(self, symbol: str) -> bool:
        """Indica se o símbolo já está na tabela."""
        return symbol in self.symbols

    def get_address(self, symbol: str) -> int:
        """Retorna o endereço associado a um símbolo."""
        return self.symbols[symbol]

    def add_variable(self, symbol: str) -> int:
        """
        Se o símbolo ainda não existir, aloca o próximo endereço livre
        (a partir de 16) e o registra. Retorna o endereço final.
        """
        if symbol not in self.symbols:
            self.symbols[symbol] = self.next_address
            self.next_address += 1
        return self.symbols[symbol]
