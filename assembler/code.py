"""
code.py

Traduz os campos mnemônicos (dest, comp, jump) das instruções C, e
os valores das instruções A, para os respectivos campos binários,
conforme a especificação da arquitetura Hack.
"""

# comp (7 bits: bit "a" + 6 bits de operação), assumindo a=0 (usa A)
_COMP_A0 = {
    "0":   "0101010",
    "1":   "0111111",
    "-1":  "0111010",
    "D":   "0001100",
    "A":   "0110000",
    "!D":  "0001101",
    "!A":  "0110001",
    "-D":  "0001111",
    "-A":  "0110011",
    "D+1": "0011111",
    "A+1": "0110111",
    "D-1": "0001110",
    "A-1": "0110010",
    "D+A": "0000010",
    "D-A": "0010011",
    "A-D": "0000111",
    "D&A": "0000000",
    "D|A": "0010101",
}

# Mesmas operações, trocando A por M (a=1)
_COMP_A1 = {
    "M":   "1110000",
    "!M":  "1110001",
    "-M":  "1110011",
    "M+1": "1110111",
    "M-1": "1110010",
    "D+M": "1000010",
    "D-M": "1010011",
    "M-D": "1000111",
    "D&M": "1000000",
    "D|M": "1010101",
}

COMP_TABLE = {**_COMP_A0, **_COMP_A1}

DEST_TABLE = {
    "":    "000",
    "M":   "001",
    "D":   "010",
    "MD":  "011",
    "A":   "100",
    "AM":  "101",
    "AD":  "110",
    "AMD": "111",
}

JUMP_TABLE = {
    "":    "000",
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JMP": "111",
}


def comp(mnemonic: str) -> str:
    """Retorna os 7 bits (a + c1..c6) correspondentes ao campo comp."""
    try:
        return COMP_TABLE[mnemonic]
    except KeyError:
        raise ValueError(f"Mnemônico comp inválido: '{mnemonic}'")


def dest(mnemonic: str) -> str:
    """Retorna os 3 bits correspondentes ao campo dest."""
    try:
        return DEST_TABLE[mnemonic]
    except KeyError:
        raise ValueError(f"Mnemônico dest inválido: '{mnemonic}'")


def jump(mnemonic: str) -> str:
    """Retorna os 3 bits correspondentes ao campo jump."""
    try:
        return JUMP_TABLE[mnemonic]
    except KeyError:
        raise ValueError(f"Mnemônico jump inválido: '{mnemonic}'")
