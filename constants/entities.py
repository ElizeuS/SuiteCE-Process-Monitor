class Tramitacao():
    def __init__(self, setor=None, inicio=None, situacao=None, tempo_permanencia=None):
        self._inicio = inicio
        self._setor = setor
        self._situacao = situacao
        self._tempo_permanencia = tempo_permanencia
    

    @property
    def setor(self):
        return self._setor

    @setor.setter
    def setor(self, setor):
        self._setor = setor

    @property
    def inicio(self):
        return self._inicio

    @inicio.setter
    def inicio(self, inicio):
        self._inicio = inicio

    @property
    def situacao(self):
        return self._situacao

    @situacao.setter
    def situacao(self, situacao):
        self._situacao = situacao
    
    @property
    def tempo_permanencia(self):
        return self._tempo_permanencia

    @tempo_permanencia.setter
    def tempo_permanencia(self, tempo_permanencia):
        self._tempo_permanencia = tempo_permanencia


class Tramitacoes():
    def __init__(self):
        self._tramitacoes = []

    def adicionar_tramitacao(self, tramitacao):
        if isinstance(tramitacao, Tramitacao):
            self._tramitacoes.append(tramitacao)
        else:
            raise ValueError("O objeto deve ser uma instância de Tramitacao.")
    
    @property
    def tramitacoes(self):
        return self._tramitacoes
    
    def listar_tramitacoes(self):
        if not self._tramitacoes:
            print("Não há processos na lista.")
        else:
            print(f"Total de Tramitações: {len(self._tramitacoes)}")
            for tramitacao in self._tramitacoes:
                print(f"Setor: {tramitacao.setor}")
                print(f"Início: {tramitacao.inicio}")
                print(f"Situação: {tramitacao.situacao}")
                print(f"Tempo de Permanência: {tramitacao.tempo_permanencia}")
                print("-" * 40)
                