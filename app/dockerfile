FROM python:3.11-slim
# A base da minha imagem

WORKDIR /app
# o diretório que ele vai trabalhar

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt
# Instalando as dependências necessárias

COPY . .

EXPOSE 5000
# Porta que o docker vai rodar

CMD ["python", "./__init__.py"]
# Comandos que serão executados dentro do docker.
