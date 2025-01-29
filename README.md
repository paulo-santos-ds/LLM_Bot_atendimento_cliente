# Bot de IA para WhatsApp

## 📝 Descrição
Um chatbot baseado em Flask para WhatsApp que integra com a API DeepSeek para fornecer respostas inteligentes às mensagens dos usuários. Este bot processa mensagens recebidas do WhatsApp através de um webhook Twilio e utiliza a API DeepSeek para gerar respostas baseadas em IA.

## 🚀 Funcionalidades
- Integração com mensagens do WhatsApp via Twilio
- Respostas alimentadas por IA usando a API DeepSeek
- Endpoint webhook para processamento de mensagens
- Tratamento de erros para respostas da API

## 📋 Pré-requisitos
- Python 3.x
- Framework web Flask
- Conta Twilio
- Credenciais da API DeepSeek
- Servidor com HTTPS habilitado (para webhook do Twilio)

```bash
Bot de atendimento whatsapp
│
├── .env                      # Arquivo de variáveis de ambiente (credenciais)
├── .gitignore                # Arquivo para ignorar arquivos no Git 
├── README.md                 # Documentação do projeto
│
├── src/                      # Pasta para código-fonte
│   ├── app.py                # Script principal do bot
│   ├── config.py             # Configurações do projeto (não sensíveis)
│   ├── utils/                # Pasta para funções utilitárias
│   │   └── helpers.py        # Funções auxiliares (ex: processamento de texto)
│   └── services/             # Pasta para serviços externos
│       ├── deepseek_api.py   # Integração com a API da DeepSeek
│       └── whatsapp_api.py   # Integração com a API do WhatsApp
│
├── data/                     # Pasta para armazenar dados
│   ├── raw/                  # Dados brutos (ex: logs de conversas)
│   ├── processed/            # Dados processados (ex: conversas limpas)
│   └── models/               # Modelos treinados (se aplicável)
│
├── notebooks/                # Pasta para Jupyter Notebooks
│   └── exploration.ipynb     # Notebook para análise exploratória de dados
│
├── logs/                     # Pasta para logs de execução
│   └── bot.log               # Arquivo de log do bot
│
└── requirements.txt          # Lista de dependências do projeto
```


## 🔧 Instalação

1. Clone o repositório:
```bash
git clone [url-do-repositório]
cd whatsapp-ai-bot
```

2. Instale as dependências necessárias:
```bash
pip install flask twilio requests
```

3. Crie um arquivo `config.py` com suas credenciais:
```python
DEEPSEEK_API_URL = "sua_url_api_deepseek"
DEEPSEEK_API_KEY = "sua_chave_api_deepseek"
```

## ⚙️ Configuração

1. Configure sua conta Twilio:
   - Crie uma conta Twilio
   - Configure um Sandbox do WhatsApp
   - Configure a URL do webhook para o endpoint `/webhook` do seu servidor

2. Certifique-se de que suas credenciais da API DeepSeek estejam configuradas corretamente no `config.py`

## 🚀 Como Usar

1. Inicie o servidor Flask:
```bash
python app.py
```

2. O webhook estará disponível em:
```
http://seu-servidor/webhook
```

3. Configure esta URL nas configurações do Sandbox WhatsApp do Twilio

## 🛠️ Como Funciona

1. Usuário envia uma mensagem pelo WhatsApp
2. Twilio encaminha a mensagem para seu webhook
3. O aplicativo processa a mensagem usando a IA DeepSeek
4. A resposta é enviada de volta ao usuário via WhatsApp

## 📝 Referência da API

### Endpoint Webhook
- **URL**: `/webhook`
- **Método**: `POST`
- **Parâmetros**:
  - `Body`: Conteúdo da mensagem do WhatsApp
  - `From`: Número do WhatsApp do remetente

### Integração com API DeepSeek
- Usa autenticação por token Bearer
- Implementa o modelo de chat DeepSeek
- Trata respostas e erros da API

## 🤝 Contribuindo
Sinta-se à vontade para contribuir com este projeto:
1. Faça um fork do repositório
2. Crie um novo branch
3. Faça suas alterações
4. Envie um pull request

## ⚠️ Notas de Segurança
- Nunca commit o arquivo `config.py` com credenciais reais
- Use variáveis de ambiente para informações sensíveis em produção
- Garanta conexões HTTPS seguras para o webhook

## Conclusão
Este script fornece uma base paracriaçãi de um bot de atendimento ao cliente via WhatsApp, integrando a API da DeepSeek para gerar respostas inteligentes. A estrutura do projeto é modular e facilita a manutenção e expansão do bot.





