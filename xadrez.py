class Torre:
    def movimento_valido(self, li, ci, lf, cf):
        return li == lf or ci == cf


class Bispo:
    def movimento_valido(self, li, ci, lf, cf):
        return abs(li - lf) == abs(ci - cf)


class Cavalo:
    def movimento_valido(self, li, ci, lf, cf):
        dl = abs(li - lf)
        dc = abs(ci - cf)
        return (dl == 2 and dc == 1) or (dl == 1 and dc == 2)


class Rainha:
    def movimento_valido(self, li, ci, lf, cf):
        return (
            li == lf or
            ci == cf or
            abs(li - lf) == abs(ci - cf)
        )


class Rei:
    def movimento_valido(self, li, ci, lf, cf):
        return abs(li - lf) <= 1 and abs(ci - cf) <= 1


class Peao:
    def movimento_valido(self, li, ci, lf, cf):
        return ci == cf and lf == li + 1


def testar(peca, nome, li, ci, lf, cf):
    if peca.movimento_valido(li, ci, lf, cf):
        print(f"{nome}: movimento VÁLIDO")
    else:
        print(f"{nome}: movimento INVÁLIDO")


# Testes simples (obrigatório para correção)
if __name__ == "__main__":
    testar(Torre(), "Torre", 1, 1, 1, 8)
    testar(Bispo(), "Bispo", 2, 2, 5, 5)
    testar(Cavalo(), "Cavalo", 1, 2, 2, 4)
    testar(Rainha(), "Rainha", 4, 4, 4, 7)
    testar(Rei(), "Rei", 5, 5, 6, 6)
    testar(Peao(), "Peão", 2, 2, 3, 2)
