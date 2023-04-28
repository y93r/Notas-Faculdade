# Notas-Faculdade
Meu primeiro projeto em python é baseado em minhas notas faculdade que usa pesos diferentes para cada avaliação.
O primeiro projeto usava if e else, o segundo if,elif e else e o terceiro agreguei o while.

# Abrir o site da faculdade
- Automação usando a biblioteca selenium para abrir o navegador Google Chrome ou Edge;
- Abrir o site da faculdade;
- Digitar login e senha e clicar no botão entrar;
- Clicar na opção AVA;
- Fechar pop-up;
- Seguir para as matérias em andamento

# simulador_notas
Este script é um simulador de notas da faculdade que utiliza a média ponderada, onde cada atividade tem um peso diferente. A APOL 1 e 2 têm peso 15, a atividade prática tem peso 40 e a prova objetiva tem peso 30.
- A interface tem uma janela com seis campos de entrada (para as notas e informações do aluno), dois botões (para calcular as notas e limpar os campos) e um rótulo que exibe o resultado da simulação;
- A função validar_valor() é usada para validar as entradas do usuário, verificando se elas são valores numéricos float válidos entre 0 e 10;
- A função simular_notas() é usada para calcular a média ponderada das notas inseridas e gerar uma mensagem de resultado, que é exibida no rótulo de resultado;
- A função limpar_campos() é usada para limpar todos os campos de entrada e o rótulo de resultado.
- Se o usuário não preencher todos os campos, um aviso será exibido para que preencha corretamente.
- Se o usuário inserir um valor inválido, um aviso também será exibido.
