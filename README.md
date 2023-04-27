# Plotagem de Gráficos

Este é um programa em Python que permite ao usuário carregar um arquivo CSV e plotar gráficos a partir dos dados contidos no arquivo. O programa foi construído utilizando a biblioteca tkinter para criar a interface gráfica e as bibliotecas pandas e matplotlib para manipular os dados e gerar os gráficos.

## Requisitos

Para executar este programa, você precisa ter o Python 3 e as seguintes bibliotecas instaladas:

- tkinter
- pandas
- matplotlib

## Como usar

1. Abra o terminal e navegue até o diretório onde o arquivo plot_graphs.py está localizado.
2. Digite o seguinte comando para executar o programa:


python plot_graphs.py


3. Clique no botão Carregar CSV para selecionar o arquivo CSV que deseja carregar.
4. Selecione o tipo de gráfico que deseja plotar no menu suspenso Tipo de Gráfico.
5. Clique no botão Plotar Gráfico para gerar o gráfico correspondente aos dados do arquivo CSV carregado.

## Funcionamento

Ao clicar no botão Carregar CSV, uma janela de seleção de arquivo será aberta para que o usuário possa escolher o arquivo CSV que deseja carregar. Quando o arquivo é carregado, suas colunas são armazenadas em uma lista e uma mensagem de confirmação é exibida na tela.

Depois que o arquivo CSV é carregado, o botão Plotar Gráfico é ativado e o usuário pode selecionar o tipo de gráfico que deseja plotar no menu suspenso Tipo de Gráfico. Quando o botão Plotar Gráfico é clicado, o programa chama a função correspondente ao tipo de gráfico selecionado e o gráfico é gerado utilizando os dados do arquivo CSV.

## Limitações

Atualmente, o programa só pode plotar gráficos a partir de arquivos CSV que contêm duas ou mais colunas de dados. Se o arquivo CSV contiver apenas uma coluna de dados, o programa só será capaz de plotar um gráfico de barras simples. Além disso, o programa pode ter problemas para plotar gráficos a partir de arquivos CSV muito grandes, pois a biblioteca pandas carrega todo o arquivo na memória RAM.
