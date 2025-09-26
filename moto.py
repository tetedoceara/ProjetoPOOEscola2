class Moto():
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = 0
    
    def acelerar(self, valor):
        self.velocidade += valor
        print(f"{self.modelo} acelerou para {self.velocidade} km/h!")
        
    def frear(self, valor):
        self.velocidade -= valor
        if self.velocidade < 0:
            self.velocidade = 0
        print(f"{self.modelo} reduziu para {self.velocidade} km/h.")
        
    def detalhes(self):
        return (f"{self.marca} {self.modelo} ({self.ano}) - "
            f"Cor: {self.cor}, Velocidade: {self.velocidade} km/h")
    
moto1 = Moto("Honda", "CG 160 Start", 2025, "Azul")
moto2 = Moto("Yamaha", "MT-03", 2026,"Preto")

print(moto1.detalhes())
print(moto2.detalhes())
moto1.acelerar(80)
moto2.acelerar(60)
moto1.frear(20)
moto2.frear(15)
print(moto1.detalhes())
print(moto2.detalhes()) 
print(f"{moto1.detalhes()} foi a mais rápida")
