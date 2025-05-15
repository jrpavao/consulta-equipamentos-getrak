import json
import os
from services import get_token, get_equipamentos

# 🔧 CONFIGURAÇÃO
PASTA_SAIDA = r"C:\Users\ADMAc\OneDrive - GRUPO ASTRAN\bd_pavon\dbGetrak\Equipamentos"  # caminho da pasta onde os arquivos serão salvos

# Função para salvar o JSON no disco
def salvar_em_arquivo(dados, tipo):
    nome_arquivo = f"equipamentos_{'ativos' if tipo == 'Y' else 'inativos'}.json"
    caminho_arquivo = os.path.join(PASTA_SAIDA, nome_arquivo)
    os.makedirs(os.path.dirname(caminho_arquivo), exist_ok=True)
    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)
    print(f"✅ {len(dados)} registros salvos em: {caminho_arquivo}")

# Execução principal
if __name__ == "__main__":
    print("🔐 Gerando token...")
    token = get_token()

    for tipo in ["Y", "N"]:
        print(f"\n📡 Consultando equipamentos {'ativos' if tipo == 'Y' else 'inativos'}...")
        dados = get_equipamentos(token, ativo=tipo)
        salvar_em_arquivo(dados, tipo)

    print("\n🏁 Exportação concluída com sucesso!")
