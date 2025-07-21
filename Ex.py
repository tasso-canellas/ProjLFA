def conta_comment(string):
    n = len(string)
    count = 0
    i = 0
    state = 1
    while i <  n-1:
        if state == 3:
            count +=1
            state = 1
        elif state == 1 and string[i] == '/' and string[i+1] == '*':
            state = 2
            i += 2        
        elif state == 2 and string[i] == '*' and string[i+1] == '/':
            state = 3
            i+=2
        else: i+=1
    return count

if __name__ == "__main__":
    codigo = """
    """
    print(conta_comment(codigo))