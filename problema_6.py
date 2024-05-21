class Moto:
    def __init__ (self,marca,modelo,cilindrada):
        self.marca = marca
        self.modelo = modelo
        self.cilindrada = cilindrada

moto = Moto("Italika","DM",250)
dic_moto = vars(moto)
print(dic_moto)