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
    
class Trie:
  def __init__(self):
    self.raiz = No('')
    
  def inserir(self, palavra):
    if self.buscar(palavra):
      return False
    p = self.raiz
    for letra in palavra:
      if letra not in p.filhos:
        p.filhos[letra] = No(letra)
      p = p.filhos[letra]
    p.setPalavra(palavra)
    return True
    
  def buscar(self, palavra):
    p = self.raiz
    for letra in palavra:
      if letra not in p.filhos:
        return False
      p = p.filhos[letra]
    return not (not palavra), p #not not para fazer o cast de str para bool
  
  def incrementar_visita(self, no):
    if no != None:
      no.visitas += 1
  
  def contar_consultas(self, palavra):
    if self.buscar(palavra):
      busca = self.buscar(palavra)[1]
      return busca.visitas
    else:
      return None
    
trie = Trie()
trie.inserir("teste")
#print(trie.buscar("azul"))
print(trie.buscar("teste"))
#print(trie.buscar("teste"))
print(trie.contar_consultas("teste"))
print(trie.contar_consultas("azul"))

    