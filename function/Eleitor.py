from dados.dados import lista_candidatos,lista_voto
from time import sleep

class Eleitor:

    nome = input("Qual o nome do Eleitor: ").strip()
    n_titulo = input("Digite o número do título: ").strip()
    voto_presidente = int(input("Digite seu voto: ").strip())

    def __init__(self,nome_eleitor,titulo=False):
        self.nome_eleitor = nome_eleitor
        self.titulo = titulo

    def eleitor_atual(self):
        if self.nome_eleitor.isnumeric():
            self.nome = input("Nome incorreto!! Digite apenas letra: ")

        self.logado = True

    def verificar_titulo(self):
        while True:
            if len(self.n_titulo) == 12:
                self.titulo = True
                break
            else:
                self.n_titulo = input("Digite por favor o número do titulo corretamente: ")
                continue

    def voto(self):

        for i,v in lista_candidatos.items():
            if self.voto_presidente == v:
                confirmar = input(f"Confirmar voto em {i} [S/N]: ").upper()
                if confirmar == "S":
                    print("...")
                    sleep(1)
                    print("\033[32mVoto Registrado!!")

            if self.voto_presidente not in lista_candidatos.values():
                print("Candidato inválido!!")
                self.voto_presidente = int(input("Seu voto: "))
                lista_voto.append(self.voto_presidente)
