class No:
  def __init__(self, chave):
    self.chave = chave
    self.filhos = {}
    self.visitas = 0
    self.palavra = None
    
  def getValor(self):
    return self.valor 
    
  def getPalavra(self):
    return self.palavra
  
  def setPalavra(self, palavra):
    self.palavra = palavra
    
  def incrementar_visitas(self):
    self.visitas += 1
    
class Trie:
  def __init__(self):
    self.raiz = No('')
    self.palavras = []
    
  def inserir(self, palavra): #return bool
    p = self.raiz
    for letra in palavra:
      if letra not in p.filhos:
        p.filhos[letra] = No(letra)
      p = p.filhos[letra]
    if '*' not in p.filhos:
      p.filhos['*'] = No('*')
    p.filhos['*'].setPalavra(palavra)
    self.palavras.append(p.filhos['*'])
    return True
    
  def buscar(self, palavra): # return bool || bool, p
    p = self.raiz
    for letra in palavra:
      if letra not in p.filhos:
        return False, None
      p = p.filhos[letra]
    if '*' not in p.filhos:
      return False, None
    p = p.filhos['*']
    return True, p
  
  def incrementar_visita(self, no): # return None
    if no != None:
      no.visitas += 1
  
  def contar_consultas(self, palavra): # return int || None
    if self.buscar(palavra):
      busca = self.buscar(palavra)[1]
      return busca.visitas
    else:
      return -1
    
  def obter_palavras_mais_buscadas(self): # return array[str], int || bool
    self.palavras.sort(key=lambda no: no.visitas, reverse=True)
    palavras_mais_visitadas = []
    maior_num_visitas = 0
    if not self.palavras:
      return False, None
    for no in self.palavras:
      if no.visitas > maior_num_visitas:
        maior_num_visitas = no.visitas
        palavras_mais_visitadas.clear()
      if no.visitas >= maior_num_visitas:
        palavras_mais_visitadas.append(no.palavra)
    return sorted(palavras_mais_visitadas), maior_num_visitas
  
  def imprimir_palavras_mais_buscadas(self):
    palavras, num_visitas = self.obter_palavras_mais_buscadas()
    if not self.palavras:
        print("trie vazia")
    else:
        print("palavras mais consultadas:")
        for palavra in palavras:
            print(palavra)
        print(f"numero de acessos: {num_visitas}")

  def pre_ordem(self, no=None, prefixo=''):
      if no is None:
          no = self.raiz
          print(f'letra: raiz -', end= ' ')
      else:
          if no.palavra is not None:
              print(f"letra: {no.chave}", end=' ')
          else:
              print(f"letra: {no.chave} -", end=' ')
      filhos = sorted(no.filhos.keys())
      for filho in filhos:
          print(f"{filho}", end=' ')
      print()

      for filho in filhos:
          self.pre_ordem(no.filhos[filho], prefixo + filho)
  

