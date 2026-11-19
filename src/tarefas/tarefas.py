"""Lógica de negócio: regras sobre tarefas.

Regras importantes:
- NÃO use print() nem input() aqui. Essas funções recebem dados e retornam
  dados (ou levantam exceções). Quem fala com o usuário é a interface (cli.py).
- Isso torna cada função fácil de testar.

TODO (semana 4, escreva os testes ANTES, em tests/):
- adicionar(tarefas, titulo): retorna a lista com a nova tarefa.
- listar(tarefas, apenas_pendentes=False)
- concluir(tarefas, id)
- remover(tarefas, id)
"""
