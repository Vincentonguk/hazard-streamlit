# 🛠️ Hazard Security – Installation Guide

## Requirements
- Windows 10/11 ou Linux (Ubuntu 22+)
- Conexão Wi-Fi / Bluetooth disponível
- Python 3.10+
- Internet com porta 443 liberada (HTTPS)

## Steps
1. Baixar o pacote do agente (`hazard-agent.zip`).
2. Descompactar em `C:\Hazard\Agent` (ou `/opt/hazard/agent` no Linux).
3. Copiar o arquivo `.env.example` para `.env`.
   - Preencher `API_KEY` e `SITE_ID` fornecidos pela equipe.
4. Instalar dependências (no terminal/PowerShell):
   ```bash
   pip install -r requirements.txt
