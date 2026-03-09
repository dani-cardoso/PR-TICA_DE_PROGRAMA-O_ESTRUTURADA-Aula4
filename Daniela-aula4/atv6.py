horanormal = float(input("Quantas horas normais você trabalhou? "))
horaextra = float(input("QUantas horas extras você fez? "))

salariobrutonormal = horanormal * 10
salariobrutoextra = horaextra * 15

salariobruto = salariobrutonormal + salariobrutoextra

salarioliquido = salariobruto * 0.9

print("O salario bruto é igual ", salariobruto, "e o salario liquido é de ", salarioliquido)