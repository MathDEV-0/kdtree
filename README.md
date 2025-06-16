# KdTree Search Benchmark

Este projeto realiza testes de desempenho de buscas em uma KdTree balanceada em 2D. Ele mede o tempo necessário para localizar múltiplos pontos e gera um gráfico com os resultados.

---

## Requisitos

- Python 3.10+
- matplotlib
- numpy
- [Docker Desktop](https://www.docker.com/products/docker-desktop) (para execução via container)

---

## Execução local

1. Instale as dependências:


pip install -r requirements.txt

2.Execute o script:

python kdtree.py

## Execução com Docker

1. Construa a imagem:

docker build -t kdtree-benchmark .

2. Execute o container:

docker run --rm -v ${PWD}:/app kdtree-benchmark

Os arquivos de saída speed.txt e grafico_kdtree.png serão salvos no diretório local.

## O que o script faz?

Gera conjuntos de pontos 2D aleatórios com tamanhos variando de 10.000 a 90.000.

Constrói uma KdTree balanceada com esses pontos.

Realiza 10 testes de busca por conjunto de entrada.

Mede o tempo total de execução de cada teste.

Salva os dados coletados em um arquivo .txt.

Gera um gráfico com os tempos de execução e uma curva de regressão quadrática.

Saídas
speed.txt: contém os tempos de execução de cada teste (em segundos).

grafico_kdtree.png: gráfico "Tempo de Execução x Tamanho da Entrada".

