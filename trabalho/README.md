# Fila de supermercado

Este trabalho simula uma fila de clientes em um caixa de supermercado com atendimento normal e atendimento preferencial.

A fila preferencial tem prioridade absoluta: todos os clientes preferenciais devem ser atendidos antes dos clientes da fila normal.

## Estrutura de arquivos

- `main.py`: inicializa o programa.
- `pessoa.py`: possui a classe `Pessoa`.
- `usuario.py`: possui as classes `Usuario` e `UsuarioP`.
- `fila.py`: possui as classes `Fila` e `FilaPreferencial`, usando `collections.deque`.
- `menu.py`: controla a interacao com o usuario pelo terminal.

## Como executar

Entre na pasta do projeto:

```bash
cd Aula1/fila_supermercado
```

Execute:

```bash
python main.py
```

## Classes

### Pessoa

Representa uma pessoa com o atributo `nome`.

### Usuario

Representa um cliente da fila normal.

### UsuarioP

Representa um cliente da fila preferencial e guarda o tipo de preferencia informado.

### Fila

Representa a fila normal. Usa `deque`, adicionando com `append()` e removendo com `popleft()`.

### FilaPreferencial

Representa a fila preferencial. Tambem usa `deque`, adicionando com `append()` e removendo com `popleft()`.

### Menu

Mostra as opcoes do sistema e chama as acoes de entrada na fila, atendimento, visualizacao das filas, quantidade e saida.

## O que ainda pode ser desenvolvido pelo grupo

- Melhorar as mensagens exibidas para o usuario.
- Ajustar nomes de metodos ou atributos conforme orientacao do professor.
- Fazer mais testes manuais com diferentes entradas.
