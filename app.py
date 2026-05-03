class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        # Atributo protegido (Encapsulamento)
        self._ligado = False 
        # Atributo privado (Encapsulamento restrito)
        self.__hodometro = 0  
    def ligar(self):
        self._ligado = True
        return f"O {self.modelo} ligou o motor térmico."

    def dirigir(self, km):
        if self._ligado:
            self.__hodometro += km
            return f"{self.modelo} rodou {km}km. Total: {self.__hodometro}km."
        return "Não é possível dirigir: o carro está desligado."

# Herança e uso do super()
class CarroEletrico(Carro):
    def __init__(self, marca, modelo, bateria_kwh):
        # super() inicializa marca e modelo na classe pai
        super().__init__(marca, modelo)
        self.bateria = bateria_kwh

    # Polimorfismo: alterando o comportamento do método ligar
    def ligar(self):
        self._ligado = True
        # Chamamos o comportamento original e adicionamos algo novo
        return f"O {self.modelo} iniciou o sistema elétrico."

    def carregar(self):
        return f"Carregando bateria de {self.bateria}kWh."


# Criando instâncias
meu_popular = Carro("Fiat", "Uno")
meu_tesla = CarroEletrico("Tesla", "Model 3", 75)

print(meu_popular.ligar())
print(meu_popular.dirigir(50))
print(meu_tesla.ligar()) 
print(meu_tesla.carregar())
print(meu_tesla.dirigir(100))

print(meu_tesla.ligar())  # Note o Polimorfismo aqui
print(meu_tesla.carregar())
print(meu_tesla.dirigir(100)) # Reuso da lógica da classe pai
