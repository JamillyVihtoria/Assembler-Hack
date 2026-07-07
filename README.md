# Assembler Hack (Nand2Tetris — Project 6)

Implementação em **Python 3** de um montador (assembler) que traduz
programas em Assembly Hack (`.asm`) para código de máquina binário
(`.hack`), executável no CPU Emulator do Nand2Tetris.

## Integrantes

| Nome Completo | Matrícula |
|--------------|-----------|
| Jamilly Vitoria Ferreira Barbosa | 20250071213 |
| Marcos Vinicius Jansem Oliveira | 20250071278 |

---

## Linguagem

- Python 3.10+ (não requer bibliotecas externas)

## Estrutura do projeto

```
.
├── parser.py         # Leitura do .asm e extração de instruções/componentes
├── symbol_table.py   # Tabela de símbolos (predefinidos, labels e variáveis)
├── code.py           # Tabelas de tradução comp/dest/jump para binário
├── main.py           # Orquestrador (duas passagens)
├── tests/            # Arquivos .asm de exemplo para validação
└── README.md
```

## Como executar

```bash
python main.py caminho/para/arquivo.asm
```

Isso gera um arquivo `.hack` no mesmo diretório do `.asm`, com o mesmo
nome base. Por exemplo:

```bash
python main.py tests/maxL.asm
# gera tests/maxL.hack
```

Depois, abra o **CPU Emulator** do Nand2Tetris e carregue o `.hack`
gerado para validar o comportamento.

## Como funciona

O assembler realiza **duas passagens** sobre o arquivo fonte:

1. **Primeira passagem**: percorre todas as instruções apenas para
   registrar o endereço ROM de cada label (`(LABEL)`) na tabela de
   símbolos. Labels não geram código, então não incrementam o
   contador de endereço.
2. **Segunda passagem**: traduz cada instrução A ou C para binário de
   16 bits. Símbolos que não são labels nem números (variáveis) são
   alocados a partir do endereço RAM 16, na ordem em que aparecem.

### Formato das instruções

| Tipo          | Formato binário     |
|---------------|----------------------|
| A-instruction | `0vvvvvvvvvvvvvvv`   |
| C-instruction | `111acccccc dddjjj`  |

## Exemplos de uso incluídos em `tests/`

- `add.asm` — soma R0 + R1 → R2
- `maxL.asm` — máximo entre R0 e R1 → R2, usando labels
- `var_test.asm` — exercita a alocação de variáveis a partir do
  endereço 16

## Vídeo de Apresentação

_(inserir aqui o link do vídeo de demonstração, conforme exigido pela
atividade)_
