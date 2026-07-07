"""
parser.py

Responsável por ler o arquivo fonte .asm, remover comentários e
espaços em branco, e expor cada instrução válida junto com seus
componentes (símbolo, dest, comp, jump).
"""

A_INSTRUCTION = "A_INSTRUCTION"
C_INSTRUCTION = "C_INSTRUCTION"
L_INSTRUCTION = "L_INSTRUCTION"  # pseudo-instrução (label)


class Parser:
    """Encapsula o acesso a um arquivo .asm, instrução por instrução."""

    def __init__(self, filename: str):
        with open(filename, "r", encoding="utf-8") as f:
            raw_lines = f.readlines()

        cleaned = []
        for line in raw_lines:
            # remove comentários (tudo depois de "//") e espaços nas pontas
            line = line.split("//")[0].strip()
            if line:
                cleaned.append(line)

        self.lines = cleaned
        self.index = -1          # índice da instrução atual (-1 = antes da primeira)
        self.current_instruction = ""

    # ------------------------------------------------------------------
    # Navegação
    # ------------------------------------------------------------------
    def has_more_lines(self) -> bool:
        """Indica se ainda há instruções a serem processadas."""
        return self.index + 1 < len(self.lines)

    def advance(self) -> None:
        """Avança para a próxima instrução, tornando-a a instrução atual."""
        self.index += 1
        self.current_instruction = self.lines[self.index]

    def reset(self) -> None:
        """Volta ao início do arquivo (útil para a segunda passagem)."""
        self.index = -1
        self.current_instruction = ""

    # ------------------------------------------------------------------
    # Consultas sobre a instrução atual
    # ------------------------------------------------------------------
    def instruction_type(self) -> str:
        line = self.current_instruction
        if line.startswith("@"):
            return A_INSTRUCTION
        if line.startswith("(") and line.endswith(")"):
            return L_INSTRUCTION
        return C_INSTRUCTION

    def symbol(self) -> str:
        """
        Retorna o símbolo ou valor decimal de uma instrução @xxx ou (xxx).
        Só deve ser chamado quando instruction_type() for A_INSTRUCTION
        ou L_INSTRUCTION.
        """
        line = self.current_instruction
        if line.startswith("@"):
            return line[1:]
        return line[1:-1]

    def dest(self) -> str:
        """Retorna o campo dest de uma instrução C (ou '' se ausente)."""
        line = self.current_instruction
        if "=" in line:
            return line.split("=")[0]
        return ""

    def comp(self) -> str:
        """Retorna o campo comp de uma instrução C."""
        line = self.current_instruction
        if "=" in line:
            line = line.split("=")[1]
        if ";" in line:
            line = line.split(";")[0]
        return line

    def jump(self) -> str:
        """Retorna o campo jump de uma instrução C (ou '' se ausente)."""
        line = self.current_instruction
        if ";" in line:
            return line.split(";")[1]
        return ""
