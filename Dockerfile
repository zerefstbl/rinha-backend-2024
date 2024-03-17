# Use a imagem oficial do Python 3.11
FROM python:3.11-slim-buster

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Instale as dependências necessárias
RUN apt-get update \
    && apt-get install -y gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copie o arquivo requirements.txt para o contêiner
COPY requirements.txt .

# Instale as dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copie o conteúdo do diretório local para o diretório de trabalho no contêiner
COPY . .

RUN chmod +x /app/wait-for-it.sh

# Exponha a porta 8000 para permitir que o aplicativo seja acessado externamente
EXPOSE 8000

