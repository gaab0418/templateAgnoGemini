#!/usr/bin/env python3
"""
Script de teste para verificar configuração do .env
"""

import os
from dotenv import load_dotenv

def test_env_config():
    """
    Testa se as configurações do .env estão carregadas corretamente
    """
    print("🧪 TESTE DE CONFIGURAÇÃO .ENV")
    print("=" * 40)
    
    # Carregar variáveis do .env
    load_dotenv()
    
    # Verificar API key
    api_key = os.getenv('GEMINI_API_KEY')
    if api_key:
        print(f"✅ GEMINI_API_KEY: {api_key[:10]}...")
    else:
        print("❌ GEMINI_API_KEY: Não encontrada")
    
    # Verificar modelo
    model = os.getenv('GEMINI_MODEL')
    if model:
        print(f"✅ GEMINI_MODEL: {model}")
    else:
        print("❌ GEMINI_MODEL: Não encontrada (usando padrão)")
    
    # Verificar se arquivo .env existe
    if os.path.exists('.env'):
        print("✅ Arquivo .env encontrado")
    else:
        print("❌ Arquivo .env não encontrado")
        print("💡 Copie config.env para .env e configure suas variáveis")
    
    print("\n" + "=" * 40)
    if api_key and model:
        print("🎉 CONFIGURAÇÃO COMPLETA!")
        print("✅ Pronto para usar o chat interativo")
    else:
        print("⚠️  CONFIGURAÇÃO INCOMPLETA")
        print("💡 Configure o arquivo .env com suas chaves")

if __name__ == "__main__":
    test_env_config()
