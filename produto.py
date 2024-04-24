# AND = para ser True tudo tem que ser True
# OR = para ser True apenas um tem que ser True

print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False or False)

saldo = 1000
saque = 200
limite = 100
conta_especial = True

exp = saldo >= saque or saque <= limite
print(exp)

exp2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp2)

saldo_normal_com_saldo_suficiente = (saldo >= saque and saque <= limite) 
conta_especial_com_saldo_suficiente = (conta_especial and saldo >= saque)

exp3 = conta_especial_com_saldo_suficiente or saldo_normal_com_saldo_suficiente
print(exp3)

