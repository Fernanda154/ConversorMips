binCode = str(input())
opCode = int(binCode[:6:],2)
rsCode = int(binCode[6:11:],2)
rtCode = int(binCode[11:16:],2)
rdCode = int(binCode[16:21:],2)
shamt =  int(binCode[21:26:],2)
funct =  int(binCode[26:32:],2)
addr = int(binCode[6:32:],2)
imm = int(binCode[16:32:],2)

print(opCode);

#Para instruções do tipo I
if(opCode==4):
  op="BEQ"
  print("{} ${}, {}(${})".format(op,rtCode,imm,rsCode))
if(opCode==5):
  op="BNE"
  print("{} ${}, {}(${})".format(op,rtCode,imm,rsCode))
if(opCode==6):
  op="BLEZ"
  print("{} ${}, {}(${})".format(op,rtCode,imm,rsCode))
if(opCode==7):
  op="BGTZ"
  print("{} ${}, {}(${})".format(op,rtCode,imm,rsCode))
if(opCode==33):
  op="LH"
  print("{} ${}, {}(${})".format(op,rtCode,imm,rsCode))
if(opCode==34):
  op="LWL"
  print("{} ${}, {}(${})".format(op,rtCode,imm,rsCode))
if(opCode==35):
  op="LW"
  print("{} ${}, {}(${})".format(op,rtCode,imm,rsCode))
if(opCode==36):
  op="LBU"
  print("{} ${}, {}(${})".format(op,rtCode,imm,rsCode))
if(opCode==37):
  op="LHU"
  print("{} ${}, {}(${})".format(op,rtCode,imm,rsCode))
if(opCode==38):
  op="LWR"
  print("{} ${}, {}(${})".format(op,rtCode,imm,rsCode))
if(opCode==40):
  op="SB"
  print("{} ${}, {}(${})".format(op,rtCode,imm,rsCode))
if(opCode==41):
  op="SH"
  print("{} ${}, {}(${})".format(op,rtCode,imm,rsCode))
if(opCode==42):
  op="SWL"
  print("{} ${}, {}(${})".format(op,rtCode,imm,rsCode))
if(opCode==43):
  op="SW"
  print("{} ${}, {}(${})".format(op,rtCode,imm,rsCode))
if(opCode==46):
  op="SWR"
  print("{} ${}, {}(${})".format(op,rtCode,imm,rsCode))

#Se começar com 0 é do tipo R
if(opCode == 0):
  if(funct == 0):
    op= "SLL"
    print("{} ${}, ${}, ${}".format(op,rdCode,rsCode,rtCode))
  if(funct == 2):
    op= "SRL"
    print("{} ${}, ${}, ${}".format(op,rdCode,rsCode,rtCode))
  if(funct == 3):
    op= "SRA"
    print("{} ${}, ${}, ${}".format(op,rdCode,rsCode,rtCode))
  if(funct == 4):
    op= "SLLV"
    print("{} ${}, ${}, ${}".format(op,rdCode,rsCode,rtCode))
  if(funct == 6):
    op= "SRLV"
    print("{} ${}, ${}, ${}".format(op,rdCode,rsCode,rtCode))
  if(funct == 16):
    op= "MFHI"
    print("{} ${}, ${}, ${}".format(op,rdCode,rsCode,rtCode))
  if(funct == 17):
    op= "MTHI"
    print("{} ${}, ${}, ${}".format(op,rdCode,rsCode,rtCode))
  if(funct == 18):
    op= "MFLO"
    print("{} ${}, ${}, ${}".format(op,rdCode,rsCode,rtCode))
  if(funct == 19):
    op= "MTLO"
    print("{} ${}, ${}, ${}".format(op,rdCode,rsCode,rtCode))
  if(funct == 24):
    op= "MULTI"
    print("{} ${}, ${}, ${}".format(op,rdCode,rsCode,rtCode))
  if(funct == 25):
    op= "MULTU"
    print("{} ${}, ${}, ${}".format(op,rdCode,rsCode,rtCode))
  if(funct == 26):
    op= "DIV"
    print("{} ${}, ${}, ${}".format(op,rdCode,rsCode,rtCode))
  if(funct == 27):
    op= "DIVU"
    print("{} ${}, ${}, ${}".format(op,rdCode,rsCode,rtCode))
  if(funct == 7):
    op= "SRAV"
    print("{} ${}, ${}, ${}".format(op,rdCode,rsCode,rtCode))
  if(funct == 32):
    op= "ADD"
    print("{} ${}, ${}, ${}".format(op,rdCode,rsCode,rtCode))
  if(funct == 33):
    op= "ADDU"
    print("{} ${}, ${}, ${}".format(op,rdCode,rsCode,rtCode))
  if(funct == 34):
    op= "SUB"
    print("{} ${}, ${}, ${}".format(op,rdCode,rsCode,rtCode))
  if(funct == 35):
    op= "SUBU"
    print("{} ${}, ${}, ${}".format(op,rdCode,rsCode,rtCode))
  if(funct == 36):
    op= "AND"
    print("{} ${}, ${}, ${}".format(op,rdCode,rsCode,rtCode))
  if(funct == 37):
    op= "OR"
    print("{} ${}, ${}, ${}".format(op,rdCode,rsCode,rtCode))
  if(funct == 38):
    op= "XOR"
    print("{} ${}, ${}, ${}".format(op,rdCode,rsCode,rtCode))
  if(funct == 42):
    op= "SLT"
    print("{} ${}, ${}, ${}".format(op,rdCode,rsCode,rtCode))
  if(funct == 43):
    op= "SLTI"
    print("{} ${}, ${}, ${}".format(op,rdCode,rsCode,rtCode))
#Tipo J

if(rs == 2):
    op= "JUMP"
    print("{} {}".format(op,addr))
if(rs == 3):
    op= "JAL"
    print("{} {}".format(op,addr))
