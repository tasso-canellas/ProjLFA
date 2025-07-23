from AnalisadorLexico import AnalisadorLexico

analisador = AnalisadorLexico()

testes = [
    "int x = 5;",
    "if (x > 0) { write(x); }",
    "while (x <= 10) { x = x + 1; }",
    "x != y && z || w",
    "# Este é um comentário\nx = 42;",
    "char nome[10];",
    "read(valor);", 
]

print("Testando o Analisador Léxico:")
print("=" * 50)

for i, teste in enumerate(testes, 1):
    print(f"\nTeste {i}: {teste}")
    print("Tokens:", analisador.analisa(teste))
