from trie import Trie

trie = Trie()

running = True

while running:
  escolha = input()
  match escolha:
    case 'i':
      palavra = input().lower()
      if not trie.buscar(palavra)[0]:
        trie.inserir(palavra)
        print(f'palavra inserida: {palavra}')
      else:
        print(f'palavra ja existente: {palavra}')
    case 'c':
      palavra = input().lower()
      palavra_alvo = trie.buscar(palavra)
      if palavra_alvo[0]:
        palavra_alvo[1].incrementar_visitas()  
        print(f'palavra existente: {palavra} {palavra_alvo[1].visitas}')
      else:
        print(f'palavra inexistente {palavra}')
    case 'f':
       trie.imprimir_palavras_mais_buscadas()
    case 'p':
      trie.pre_ordem()
    case 'e':
      running = False