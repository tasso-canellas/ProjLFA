class AnalisadorLexico:
    tokens_d = {
        "int"    : 'INT',
        "if"     : 'IF',
        "else"   : 'ELSE',
        ":"      : 'COLON',
        "char"   : 'CHAR',
        "write"  : 'WRITE',
        "read"   : 'READ',
        "length" : 'LENGTH',
        "while"  : 'WHILE',

        "(" : 'LPAR',
        ")" : 'RPAR',
        "[" : 'LBRACK',
        "]" : 'RBRACK',
        "{" : 'LBRACE',
        "}" : 'RBRACE',

        ";" : 'SEMICOLON',  
        "," : 'COMMA',

        "+" : 'PLUS',
        "-" : 'MINUS',
        "*" : 'TIMES',
        "/" : 'DIVIDE',
        "%" : 'MOD',

        "="  : 'ASSIGN',
        "==" : 'EQUAL',
        "!=" : 'NEQUAL',

        "!"  : 'NOT',
        ">"  : 'GREATER',
        "<"  : 'LESS',
        "<=" : 'LESSEQUAL',
        ">=" : 'GREATEREQUAL',

        "&&" : 'AND',
        "||" : 'OR',
    }

    def analisa(self, string: str):
        i = 0
        start = 0
        n = len(string)
        tokens = []
        state = 1
        while i < n:
            match state:
                case 8:
                    tokens.append("NUM")
                    i += 1
                    start = i
                    state = 1

                case 7:
                    lexema = string[start:i+1]
                    if lexema in self.tokens_d:
                        tokens.append(self.tokens_d[lexema])
                    elif lexema.isidentifier():
                        tokens.append("ID")
                    else:
                        print(f"Erro Léxico no trecho: {lexema}")
                        return
                    i += 1
                    start = i
                    state = 1

                case 1:
                    if string[i] in [' ', '\t', '\r', '\n']:
                        start = i + 1
                    elif string[i] == '#':
                        state = 2
                    elif string[i] in ['<', '>']:
                        state = 3
                    elif string[i] == '!':
                        state = 4
                    elif string[i] in [';', '+', '-', '*', '/', '%', '=', '(', ')', '[', ']', '{', '}', ',', ':']:
                        state = 7
                        i -= 1
                    elif string[i] == '_' or string[i].isalpha():
                        state = 5
                    elif string[i].isdigit():
                        state = 6
                    elif string[i] == '&' or string[i] == '|':
                        state = 9
                    else:
                        print(f"Erro Léxico no trecho: {string[start:i+1]}")
                        return
                    i += 1

                case 2:
                    if string[i] == '\n':
                        state = 1
                        start = i + 1
                    i += 1

                case 3:
                    if i < n and string[i] == '=':
                        state = 7
                    else:
                        i -= 1
                        state = 7

                case 4:
                    if i < n and string[i] == '=':
                        state = 7
                    else:
                        tokens.append(self.tokens_d.get("!", "NOT"))
                        i += 1
                        start = i
                        state = 1

                case 5:
                    if string[i] == '_' or string[i].isalnum():
                        i += 1
                        continue
                    else:
                        i -= 1
                        state = 7

                case 6:
                    if string[i].isdigit():
                        i += 1
                        continue
                    else:
                        i -= 1
                        state = 8
                
                case 9:
                    if i < n and string[i-1] == string[i]:
                        lexema = string[i-1] + string[i]
                        if lexema in self.tokens_d:
                            tokens.append(self.tokens_d[lexema])
                            i += 1
                            start = i
                            state = 1
                        else:
                            print(f"Erro Léxico no trecho: {lexema}")
                            return
                    else:
                        print(f"Erro Léxico no trecho: {string[i]}")
                        return

        if state == 5: 
            lexema = string[start:]
            if lexema in self.tokens_d:
                tokens.append(self.tokens_d[lexema])
            elif lexema.isidentifier():
                tokens.append("ID")
            else:
                print(f"Erro Léxico no trecho: {lexema}")
                return
        elif state == 6: 
            tokens.append("NUM")

        return tokens

# Ele pode terminar nos estados 5, 6, 7 e 8, mas se chegar em 7 e 8 e a string n tiver terminado, ele volta pro estado 1 para ver o próximo token.