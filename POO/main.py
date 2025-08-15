class Veiculo:
    def __init__(self, marca, ano_fab, cor, qtd_portas, modelo):
       self.marca = marca
       self.ano_fab = ano_fab
       self.cor = cor
       self.qtd_portas = qtd_portas
       self.modelo = modelo


    def andar(self):
        print(f"{self.modelo}Estou andando ")
    
    def parar(self):
        print(f"{self.modelo} parado")

    def imprimir(self):
         print(
             f"""O Veiculo tem as seguintes caracteristicas:\n
             Marca: {self.marca}\n
             Ano de fabricação: {self.ano_fab}\n
             Cor: {self.cor}\n
             tem {self.qtd_portas} portas\n""" )

###################################################################

class Carro(Veiculo):
     def __init__(self, marca, ano_fab, cor, qtd_portas, modelo, tam_portaMalas):
        super().__init__(marca, ano_fab, cor, qtd_portas, modelo)
        self.tam_portaMalas = tam_portaMalas

     def pau(self):
          print(f"{self.modelo} estou dando cavalinho de pau")

###########################################################################


class Caminhao(Veiculo):
     def __init__(self, marca, ano_fab, cor, qtd_portas, modelo, carga, qtd_rodas):
          super().__init__(marca, ano_fab, cor, qtd_portas, modelo)
          self.carga = carga
          self.qtd_rodas = qtd_rodas

     def asas(self):
          print(f"{self.modelo} quebrando asa")

###################################################################################

class Moto(Veiculo):
     def __init__(self, marca, ano_fab, cor, qtd_portas, modelo, bau):
          super().__init__(marca, ano_fab, cor, qtd_portas, modelo)
          self.bau = bau

     def ran(self):
          print(f"{self.modelo} randandandandadnadnad")

#################################################################################

def main():
        carro1 = Carro("Honda", 2024, "Azul", 4, "Civic", "40 kg")
        carro1.imprimir()
        carro1.pau()
        moto1 = Moto("Honda", 2013, "Preto", 0, "Tiger", "10 kg")
        moto1.imprimir()
        moto1.ran()
        caminhao1 = Caminhao("Scania", 2013, "Preto", 2, "Truck", "Madeira", 6)
        caminhao1.imprimir()
        caminhao1.asas()
main()

