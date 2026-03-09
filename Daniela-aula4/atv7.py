lata = (int(input("Quantas latas 350ml você comprou? ")))
garrafa = (int(input("Quantas garrafa 600ml você comprou? ")))
litro = (int(input("Quantas garrafa 2l você comprou? ")))

lataquantidade = lata * 0.35
garrafaquantidade = garrafa * 0.60
litroquantidade = litro * 2

total = lataquantidade + garrafaquantidade + litroquantidade

print("Você tem o total de ", total, " litros.")