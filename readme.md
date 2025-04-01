```markdown
# Telegram for CRAG

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Telegram](https://img.shields.io/badge/Telegram-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)

## Sobre o Projeto

O **Telegram for CRAG** é um bot do Telegram desenvolvido para integrar funcionalidades do CRAG (Custom Resource Allocation Generator) diretamente na plataforma de mensagens. Ele permite que usuários interajam com o CRAG de forma prática e automatizada, utilizando comandos no Telegram.

---

## Tecnologias Principais

- **Python**: Linguagem base do projeto
- **Telegram Bot API**: Integração com o Telegram
- **Docker**: Containerização da aplicação

---

## Requisitos

- Python 3.8+
- Docker
- Token de API do Telegram (obtenha criando um bot com o [BotFather](https://core.telegram.org/bots#botfather))

---

## Instalação

1. Clone o repositório:
   ```
   git clone https://github.com/PrimeRibs2501/telegram_for_crag.git
   cd telegram_for_crag
   ```

2. Instale as dependências utilizando Poetry:
   ```
   poetry lock
   poetry install
   ```

3. Configure as variáveis de ambiente:
   - Crie um arquivo `.env` na raiz do projeto.
   - Adicione a seguinte configuração:
     ```
     TELEGRAM_TOKEN=
     ```

4. Execute o bot:
   ```
   python bot/main.py
   ```

---

## Uso

### Localmente

1. Certifique-se de que todas as dependências estão instaladas e o token do Telegram está configurado.
2. Execute o comando acima para iniciar o bot.
3. No Telegram, envie mensagens para o seu bot para interagir com as funcionalidades do CRAG.

### Com Docker

1. Construa a imagem Docker:
   ```
   docker build -t telegram_for_crag .
   ```

2. Execute o container:
   ```
   docker run --env-file .env telegram_for_crag
   ```

---

## Estrutura do Projeto

```
telegram_for_crag/
├── bot/                  # Código principal do bot
│   ├── handlers.py       # Manipuladores de comandos e mensagens
│   ├── main.py           # Script principal para iniciar o bot
│   └── utils.py          # Funções auxiliares
├── docker/               # Arquivos relacionados ao Docker
├── .env                  # Variáveis de ambiente (não versionado)
├── .gitignore            # Regras de exclusão do Git
├── poetry.lock           # Arquivo de bloqueio de dependências (Poetry)
├── pyproject.toml        # Configuração do projeto (Poetry)
└── README.md             # Documentação do projeto
```

---

## Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do repositório.
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`).
3. Commit suas alterações (`git commit -m 'Add some AmazingFeature'`).
4. Push para a branch (`git push origin feature/AmazingFeature`).
5. Abra um Pull Request.