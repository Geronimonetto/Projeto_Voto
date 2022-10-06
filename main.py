from function.Eleitor import Eleitor
if __name__ == "__main__":
    principal = Eleitor(Eleitor.nome,Eleitor.n_titulo)
    principal.eleitor_atual()
    principal.verificar_titulo()
    principal.voto()
