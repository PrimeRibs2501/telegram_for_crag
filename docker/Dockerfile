# Use uma imagem base com Python 3.12
FROM python:3.12-slim

# Defina variáveis de ambiente
ENV POETRY_HOME="/home/poetry"
ENV VENV_PATH="/home/api/.venv"
ENV USER="api"
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"
ENV POETRY_VIRTUALENVS_CREATE=false

# Instala todas as dependências necessárias
RUN useradd $USER && \
  apt-get update && \
  apt-get install -y git build-essential locales curl dos2unix && \
  pip3 install --upgrade pip && \
  pip3 install poetry

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /home/$USER

# Configura o locale
RUN sed -i '/pt_BR.UTF-8/s/^# //g' /etc/locale.gen && \
  locale-gen && \
  locale

# Copia os arquivos necessários
COPY --chown=$USER:$USER ./pyproject.toml ./poetry.lock* ./
COPY --chown=$USER:$USER .env .env
COPY --chown=$USER:$USER ./bot/ ./bot/

# Instala as dependências
RUN poetry install --no-root --no-interaction --no-ansi

# Instala o pytelegrambotapi diretamente no ambiente global (opcional)
RUN pip3 install pytelegrambotapi

# Cria o diretório de cache do Poetry e ajusta permissões
RUN mkdir -p /home/api/.cache/pypoetry && \
    chown -R api:api /home/api/.cache

# Mude para o usuário não-root
USER $USER

# Defina o comando de entrada para iniciar o bot
CMD ["poetry", "run", "python", "bot/create_bot.py"]