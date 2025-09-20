#!/usr/bin/env python3
"""
Script de chat interativo usando Agno + Gemini
"""

import os
from agno.agent import Agent
from agno.models.google import Gemini
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env
load_dotenv()

def setup_agno_gemini():
    """
    Configura e retorna um agente Agno com Gemini
    """
    # Verificar API key
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("❌ GEMINI_API_KEY não encontrada!")
        print("💡 Configure no arquivo .env ou com: $env:GEMINI_API_KEY='sua_chave_aqui'")
        return None
    
    # Obter modelo do .env
    model_id = os.getenv('GEMINI_MODEL', 'gemini-2.5-flash-lite')
    print(f"🔧 Usando modelo: {model_id}")
    
    # Configurar modelo Gemini
    gemini_model = Gemini(
        api_key=api_key,
        id=model_id
    )
    
    # Criar agente
    agent = Agent(
        name="AgnoGemini",
        model=gemini_model,
        description="Assistente inteligente usando Agno + Gemini"
    )
    
    return agent

def chat_interactive():
    """
    Chat interativo com Agno + Gemini
    """
    print("🤖 CHAT INTERATIVO AGNO + GEMINI")
    print("=" * 40)
    print("Digite 'sair' para encerrar")
    print("=" * 40)
    
    # Configurar agente
    agent = setup_agno_gemini()
    if not agent:
        return
    
    print("✅ Agente configurado com sucesso!")
    print("🤖 Olá! Sou seu assistente Agno + Gemini. Como posso ajudar?")
    
    while True:
        try:
            # Obter entrada do usuário
            user_input = input("\n👤 Você: ").strip()
            
            # Verificar se quer sair
            if user_input.lower() in ['sair', 'exit', 'quit', 'bye']:
                print("🤖 Até logo! Foi um prazer conversar com você!")
                break
            
            if not user_input:
                continue
            
            # Obter resposta do agente
            print("🤖 Agno: ", end="", flush=True)
            response = agent.run(user_input)
            
            # Extrair apenas o conteúdo da resposta
            if hasattr(response, 'content'):
                print(response.content)
            else:
                print(response)
                
        except KeyboardInterrupt:
            print("\n\n🤖 Chat encerrado pelo usuário. Até logo!")
            break
        except Exception as e:
            print(f"\n❌ Erro: {str(e)}")

def test_single_message(message):
    """
    Testa uma única mensagem
    """
    agent = setup_agno_gemini()
    if not agent:
        return None
    
    print(f"👤 Usuário: {message}")
    print("🤖 Agno: ", end="", flush=True)
    
    response = agent.run(message)
    
    if hasattr(response, 'content'):
        print(response.content)
        return response.content
    else:
        print(response)
        return str(response)

def main():
    """
    Função principal
    """
    print("🚀 AGNO + GEMINI - Escolha uma opção:")
    print("1. Chat interativo")
    print("2. Teste de mensagem única")
    print("3. Sair")
    
    choice = input("\nEscolha (1-3): ").strip()
    
    if choice == "1":
        chat_interactive()
    elif choice == "2":
        message = input("Digite sua mensagem: ")
        test_single_message(message)
    elif choice == "3":
        print("Tchau!")
    else:
        print("Opção inválida!")

if __name__ == "__main__":
    main()
