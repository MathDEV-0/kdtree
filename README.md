Requisitos
Python 3.10+

matplotlib

numpy

Execução local
Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txt
Execute o script:

bash
Copiar
Editar
python kdtree.py
Execução com Docker
Construa a imagem:

bash
Copiar
Editar
docker build -t kdtree-benchmark .
Execute o container:

bash
Copiar
Editar
docker run --rm -v ${PWD}:/app kdtree-benchmark
Os arquivos de saída speed.txt e grafico_kdtree.png serão salvos no diretório local.

O que o script faz
Gera conjuntos de pontos 2D aleatórios com tamanhos variando de 10.000 a 90.000.

Constrói uma KdTree balanceada com esses pontos.

Realiza 10 testes de busca por conjunto de entrada.

Mede o tempo total de execução de cada teste.

Salva os dados coletados em um arquivo .txt e gera um gráfico com regressão quadrática.
