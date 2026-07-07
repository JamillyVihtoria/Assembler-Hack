"""
main.py

Orquestrador do Assembler Hack (Project 06 - Nand2Tetris).

Uso:
    python main.py caminho/para/arquivo.asm

Gera um arquivo .hack no mesmo diretório, com o mesmo nome base.
"""

import sys
import os

import code as Code
from parser import Parser, A_INSTRUCTION, C_INSTRUCTION, L_INSTRUCTION
from symbol_table import SymbolTable


def first_pass(filename: str, symbol_table: SymbolTable) -> None:
    """
    Primeira passagem: percorre o arquivo apenas para registrar os
    endereços dos labels (pseudo-instruções (LABEL)) na tabela de
    símbolos. Instruções A e C incrementam o contador de endereço;
    labels não geram código e, portanto, não incrementam.
    """
    parser = Parser(filename)
    rom_address = 0

    while parser.has_more_lines():
        parser.advance()
        itype = parser.instruction_type()

        if itype == L_INSTRUCTION:
            label = parser.symbol()
            symbol_table.add_entry(label, rom_address)
        else:
            rom_address += 1


def second_pass(filename: str, output_file: str, symbol_table: SymbolTable) -> None:
    """
    Segunda passagem: traduz cada instrução A ou C para binário,
    resolvendo variáveis (alocando a partir do endereço 16) e
    ignorando labels (já tratados na primeira passagem).
    """
    parser = Parser(filename)

    with open(output_file, "w", encoding="utf-8") as out:
        while parser.has_more_lines():
            parser.advance()
            itype = parser.instruction_type()

            if itype == L_INSTRUCTION:
                continue

            if itype == A_INSTRUCTION:
                symbol = parser.symbol()
                if symbol.isdigit():
                    value = int(symbol)
                else:
                    value = symbol_table.add_variable(symbol)
                binary = "0" + format(value, "015b")

            else:  # C_INSTRUCTION
                d = Code.dest(parser.dest())
                c = Code.comp(parser.comp())
                j = Code.jump(parser.jump())
                binary = "111" + c + d + j

            out.write(binary + "\n")


def assemble(input_file: str) -> str:
    """Executa as duas passagens e retorna o caminho do arquivo .hack gerado."""
    if not input_file.endswith(".asm"):
        raise ValueError("O arquivo de entrada deve ter extensão .asm")

    output_file = input_file[:-4] + ".hack"

    symbol_table = SymbolTable()
    first_pass(input_file, symbol_table)
    second_pass(input_file, output_file, symbol_table)

    return output_file


def main():
    if len(sys.argv) != 2:
        print("Uso: python main.py caminho/para/arquivo.asm")
        sys.exit(1)

    input_file = sys.argv[1]

    if not os.path.isfile(input_file):
        print(f"Erro: arquivo não encontrado: {input_file}")
        sys.exit(1)

    try:
        output_file = assemble(input_file)
    except ValueError as e:
        print(f"Erro: {e}")
        sys.exit(1)

    print(f"Assembler concluído: {output_file}")


if __name__ == "__main__":
    main()
