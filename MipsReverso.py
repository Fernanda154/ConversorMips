instrucao = str(input())

# separa a instrução por espaços
argumentos = instrucao.split(' ')

op = ''
rs = ''
rt = ''
rd = ''
IMM = ''
tipo = ''
opCode = 0
shamt = 0
funct = ''
addr = ''
# Checando o tamanho da instrução para saber o qual o tipo
if len(argumentos) == 4:
    ultimo_argumento = argumentos[3]

    # Para instruções do tipo R
    if '$' in ultimo_argumento:
        print('Formato R')
        print(argumentos)
        tipo = 'R'
        # converte o op todo para MAIUSCULO
        op = argumentos[0].upper()
        # remove $s e vírgula do primeiro argumento
        rd = argumentos[1].replace('$s', '').replace(',', '')
        # remove $s e vírgula do segundo argumento
        rs = argumentos[2].replace('$s', '').replace(',', '')
        # remove $s e vírgula do terceiro argumento
        rt = argumentos[3].replace('$s', '').replace(',', '')

        print(op, rd, rs, rt)

    # Para instruções do tipo I
    if ultimo_argumento.isdigit():
        print('Formato I')
        print(argumentos)
        tipo = 'I'
        # converte o op todo para MAIUSCULO
        op = argumentos[0].upper()
        # remove $s e vírgula do primeiro argumento
        rs = argumentos[1].replace('$s', '').replace(',', '')
        # remove $s e vírgula do segundo argumento
        rt = argumentos[2].replace('$s', '').replace(',', '')
        # definindo o IMM como terceiro argumento
        IMM = argumentos[3]

# Para instruções do tipo J
if len(argumentos) == 2:
    print('Formato J')
    print(argumentos)
    tipo = 'J'
    # converte o op todo para MAIUSCULO
    op = argumentos[0].upper()
    # definindo o add como segundo argumento
    addr = argumentos[1]


# Convertendo operação para opCode
# Para instruções do tipo I
if op == "BEQ":
    opCode = 4
if op == "BNE":
    opCode = 5
if op == "SLTI":
    opCode = 10
if op == "BLEZ":
    opCode = 6
if op == "BGTZ":
    opCode = 7
if op == "LH":
    opCode = 33
if op == "LWL":
    opCode = 34
if op == "LW":
    opCode = 35
if op == "LBU":
    opCode = 36
if op == "LB":
    opCode = 32
if op == "LHU":
    opCode = 37
if op == "LWR":
    opCode = 38
if op == "SB":
    opCode = 40
if op == "SH":
    opCode = 41
if op == "SWL":
    opCode = 42
if op == "SW":
    opCode = 43
if op == "SWR":
    opCode = 46
if op == "ADDI":
    opCode = 8
if op == "ADDIU":
    opCode = 9
if op == "SLTIU":
    opCode = 11
if op == "ANDI":
    opCode = 12
if op == "ORI":
    opCode = 13
if op == "LUI":
    opCode = 15
# Para instruções do tipo R
if tipo == 'R':
    #  O opCode é 0 por padrão
    opCode = 0
    if op == "SLL":
        funct = 0
    if op == "SRL":
        funct = 2
    if op == "SRA":
        funct = 3
    if op == "JR":
        funct = 8
    if op == "SLLV":
        funct = 4
    if op == "SRLV":
        funct = 6
    if op == "MFHI":
        funct = 16
    if op == "MTHI":
        funct = 17
    if op == "MFLO":
        funct = 18
    if op == "MTLO":
        funct = 19
    if op == "MULT":
        funct = 24
    if op == "MULTU":
        funct = 25
    if op == "DIV":
        funct = 26
    if op == "DIVU":
        funct = 27
    if op == "SRAV":
        funct = 7
    if op == "ADD":
        funct = 32
    if op == "ADDU":
        funct = 33
    if op == "SUB":
        funct = 34
    if op == "SUBU":
        funct = 35
    if op == "AND":
        funct = 36
    if op == "OR":
        funct = 37
    if op == "XOR":
        funct = 38
    if op == "SLT":
        funct = 42
    if op == "MFC0":
        funct = 10
# Para instruções do tipo J
if op == "JUMP":
    rs = 2
if op == "JAL":
    rs = 3

# mostrando tipo I
if tipo == 'I':
    # convertendo opCode para 6 bits
    opCode = format(opCode, '06b')
    # convertendo rt para 5 bits
    rt = format(int(rt), '05b')
    # convertendo rs para 5 bits
    rs = format(int(rs), '05b')
    # convertendo IMM para 16 bits
    IMM = format(int(IMM), '016b')
    print('{}{}{}{}'.format(opCode, rt, rs, IMM))

# mostrando tipo R
if tipo == 'R':
    # convertendo opCode para 6 bits
    opCode = format(opCode, '06b')
    # convertendo rt para 5 bits
    rt = format(int(rt), '05b')
    # convertendo rs para 5 bits
    rs = format(int(rs), '05b')
    # convertendo rd para 5 bits
    rd = format(int(rd), '05b')
    # convertendo shift(shamt) para 5 bits
    shamt = format(shamt, '05b')
    # convertendo funct para 6 bis
    funct = format(int(funct), '06b')
    print('{}{}{}{}{}{}'.format(opCode, rs, rt, rd, shamt, funct))

# mostrando tipo J
if tipo == 'J':
    # convertendo opCode para 6 bits
    opCode = format(opCode, '06b')
    # convertendo addr para 26 bits
    addr = format(int(addr), '026b')
    print('{}{}'.format(opCode, addr))
