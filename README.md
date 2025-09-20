# Agno + Gemini - Teste de Comunicação

Este projeto demonstra como usar a biblioteca **Agno** com o modelo **Gemini** do Google para criar agentes de IA conversacionais.

## 📋 Pré-requisitos

1. **Python 3.7+** instalado
2. **API Key do Gemini** (obtenha em: https://aistudio.google.com/app/apikey)

## 🚀 Instalação e Configuração

### 1. Criar ambiente virtual
```bash
python -m venv .venv
```

### 2. Ativar ambiente virtual
**Windows (PowerShell):**
```powershell
.venv\Scripts\activate
```

**Windows (CMD):**
```cmd
.venv\Scripts\activate.bat
```

**Linux/Mac:**
```bash
source .venv/bin/activate
```

### 3. Instalar dependências
```bash
pip install -U google-genai agno python-dotenv
```

### 4. Configurar arquivo .env
Copie o arquivo de exemplo e configure suas variáveis:
```bash
copy config.env .env
```

Edite o arquivo `.env` e configure:
- **GEMINI_API_KEY**: Sua chave da API do Gemini
- **GEMINI_MODEL**: Modelo desejado (descomente a linha correspondente)

**Modelos disponíveis:**
- `gemini-1.5-flash` - Modelo rápido e eficiente
- `gemini-2.0-flash` - Versão 2.0 do Flash
- `gemini-2.5-flash-lite` - Versão lite mais leve
- `gemini-2.5-flash` - Versão completa 2.5
- `gemini-2.5-pro` - Modelo mais avançado
- `gemini-2.5-flash-image-preview` - Com suporte a imagens

**Exemplo de .env:**
```env
GEMINI_API_KEY=sua_chave_do_gemini_aqui
GEMINI_MODEL=gemini-2.5-flash-lite
```

### 5. Configuração alternativa (variáveis de ambiente)
**Windows (PowerShell):**
```powershell
$env:GEMINI_API_KEY='sua_chave_do_gemini_aqui'
$env:GEMINI_MODEL='gemini-2.5-flash-lite'
```

**Windows (CMD):**
```cmd
set GEMINI_API_KEY=sua_chave_do_gemini_aqui
set GEMINI_MODEL=gemini-2.5-flash-lite
```

**Linux/Mac:**
```bash
export GEMINI_API_KEY='sua_chave_do_gemini_aqui'
export GEMINI_MODEL='gemini-2.5-flash-lite'
```

### 6. Executar scripts

#### Chat interativo:
```bash
python agno_gemini_chat.py
```

#### Teste de configuração:
```bash
python test_config.py
```

#### Teste rápido:
```bash
python agno_gemini_chat.py
# Escolha opção 2 para teste de mensagem única
```

## 📁 Arquivos do projeto

- `agno_gemini_chat.py` - Chat interativo principal
- `test_config.py` - Script de teste de configuração
- `config.env` - Arquivo de exemplo para configuração
- `README.md` - Esta documentação
- `.gitignore` - Arquivos ignorados pelo Git

## 🔧 Configuração técnica

### Import correto:
```python
import os
from agno.agent import Agent
from agno.models.google import Gemini
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env
load_dotenv()
```

### Configuração do modelo:
```python
# Obter configurações do .env
api_key = os.getenv('GEMINI_API_KEY')
model_id = os.getenv('GEMINI_MODEL', 'gemini-2.5-flash-lite')

gemini_model = Gemini(
    api_key=api_key,
    id=model_id
)

agent = Agent(
    name="MeuAgente",
    model=gemini_model
)
```

### Uso básico:
```python
response = agent.run("Sua mensagem aqui")
print(response.content)  # Conteúdo da resposta
```

## 🐛 Solução de problemas

### Erro: "GEMINI_API_KEY not found"
- Certifique-se de que o arquivo `.env` existe e está configurado
- Configure a variável de ambiente: `$env:GEMINI_API_KEY='sua_chave'`
- Verifique se a API key é válida

### Erro: "ImportError: cannot import name 'Gemini'"
- Instale as dependências: `pip install -U google-genai agno python-dotenv`
- Use: `from agno.models.google import Gemini`

### Erro: "unexpected keyword argument 'model'"
- Use `id` em vez de `model`: `Gemini(id="gemini-2.5-flash-lite")`

### Erro: "ModuleNotFoundError"
- Ative o ambiente virtual: `.venv\Scripts\activate`
- Reinstale as dependências: `pip install -U google-genai agno python-dotenv`

### Erro: "No module named 'dotenv'"
- Instale o python-dotenv: `pip install python-dotenv`

### Erro: "GEMINI_MODEL not found"
- Configure no arquivo `.env`: `GEMINI_MODEL=gemini-2.5-flash-lite`
- Verifique se o arquivo `.env` está no diretório correto

## 📚 Documentação

- [Agno Documentation](https://docs.agno.com)
- [Google AI Studio](https://aistudio.google.com)
- [Gemini API Reference](https://ai.google.dev/docs)

