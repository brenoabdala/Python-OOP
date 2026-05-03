# Projeto Frota OOP: Guia de Estudos em Python

Este projeto utiliza o domínio de **carros** para demonstrar como a Programação Orientada a Objetos (OOP) estrutura sistemas complexos de forma modular e reutilizável[cite: 1, 3].

## Detalhamento dos 4 Pilares

### 1. Abstração (Foco no Essencial)
A Abstração esconde os detalhes técnicos complexos e expõe apenas o que é necessário para o uso[cite: 1, 2].
* **No Código:** Criamos métodos como `ligar()` e `dirigir()`[cite: 1].
* **Na Prática:** O motorista não precisa entender a física da combustão ou a voltagem da bateria para operar o veículo. Ele interage apenas com a "interface" (volante e pedais).

### 2. Herança (Especialização de Código)
Permite que uma classe filha herde atributos e métodos de uma classe pai, evitando a duplicidade de código[cite: 1, 2].
* **No Código:** A classe `CarroEletrico` herda de `Carro`[cite: 1, 3].
* **O papel do `super()`:** Utilizamos o `super().__init__(marca, modelo)` para garantir que a lógica de construção definida na classe pai seja executada antes de adicionarmos as especificidades da classe filha (como a bateria)[cite: 1].

### 3. Encapsulamento (Proteção e Segurança)
O Encapsulamento restringe o acesso direto aos dados internos do objeto para evitar modificações indevidas[cite: 1, 2].
* **Atributos Protegidos (`_`):** Indica que a variável não deve ser acessada fora da classe (ex: `_ligado`)[cite: 1].
* **Atributos Privados (`__`):** O Python "esconde" o atributo (ex: `__hodometro`) para garantir que a quilometragem só aumente através do método `dirigir()`, impedindo fraudes ou erros manuais no dado[cite: 1].

### 4. Polimorfismo (Flexibilidade de Comportamento)
Permite que o mesmo nome de método tenha comportamentos diferentes dependendo do tipo do objeto[cite: 1, 2].
* **No Código:** O método `ligar()` existe tanto em `Carro` quanto em `CarroEletrico`[cite: 1, 3].
* **A Diferença:** Enquanto o carro comum emite um som de motor térmico, o elétrico inicia os sistemas digitais silenciosamente[cite: 1]. O comando é o mesmo, mas a execução é única para cada um.

---

## Estrutura do Projeto

O sistema foi desenhado pensando na escalabilidade que um **Engenheiro de Dados** precisa para criar conectores e pipelines[cite: 1, 2].
```python
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False      # Encapsulamento (Protegido)
        self.__hodometro = 0      # Encapsulamento (Privado)

    def ligar(self):
        self._ligado = True
        return f"{self.modelo} ligado."

class CarroEletrico(Carro):       # Herança
    def __init__(self, marca, modelo, bateria):
        super().__init__(marca, modelo) # Uso do super()
        self.bateria = bateria

    def ligar(self):              # Polimorfismo
        self._ligado = True
        return f"{self.modelo} elétrico iniciado com sucesso."
