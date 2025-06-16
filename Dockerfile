# Imagem base com Python
FROM python:3.10-slim 

# Define diretório de trabalho
WORKDIR /app

# Copia os arquivos para o container
COPY requirements.txt .
COPY kdtree.py .

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Comando padrão ao rodar o container
CMD ["python", "kdtree.py"]
