# ProjLFA - Analisador Léxico

Este projeto implementa um analisador léxico (lexer) para uma linguagem de programação simples.

## Descrição

O analisador léxico é responsável por quebrar o código fonte em tokens, identificando palavras-chave, identificadores, números, operadores e símbolos especiais.

## Estrutura do Projeto

- `AnalisadorLexico.py` - Implementação principal do analisador léxico
- `Ex.py` - Exemplos de uso
- `teste_analisador.py` - Testes para o analisador

## Tokens Suportados

### Palavras-chave
- `int`, `char` - tipos de dados
- `if`, `else` - estruturas condicionais
- `while` - laços
- `read`, `write` - operações de entrada e saída
- `length` - função de comprimento

### Operadores
- Aritméticos: `+`, `-`, `*`, `/`, `%`
- Relacionais: `==`, `!=`, `>`, `<`, `>=`, `<=`
- Lógicos: `&&`, `||`, `!`
- Atribuição: `=`

### Símbolos Especiais
- Parênteses: `(`, `)`
- Colchetes: `[`, `]`
- Chaves: `{`, `}`
- Outros: `;`, `,`, `:`

### Tokens
- `ID` - Identificadores
- `NUM` - Números inteiros

## Como usar

```python
from AnalisadorLexico import AnalisadorLexico

analisador = AnalisadorLexico()
tokens = analisador.analisa("int x = 10;")
print(tokens)  # ['INT', 'ID', 'ASSIGN', 'NUM', 'SEMICOLON']
```

## Funcionalidades

- Reconhecimento de comentários (iniciados com `#`)
- Ignorar espaços em branco e quebras de linha
- Tratamento de erros léxicos
- Suporte a identificadores e números

## Estados do Autômato

O analisador utiliza um autômato finito com os seguintes estados:
1. Estado inicial
2. Comentário
3. Operadores relacionais (`<`, `>`)
4. Negação (`!`)
5. Identificadores
6. Números
7. Tokens simples
8. Finalização de números
9. Operadores lógicos (`&&`, `||`)
