# ⚙️ Hazard Security – Admin Guide

## Objetivo
Este guia é destinado a administradores responsáveis pela configuração e manutenção do **Hazard Security Dashboard**.

---

## Login e Acesso
- Acesse o link do Dashboard fornecido pela equipe.
- Utilize as credenciais de administrador.
- Verifique o acesso ao **tenant** (empresa) e ao **site** (local monitorado).

---

## Configuração Inicial
1. **Criar Sites**
   - Cada filial/local de operação deve ter um `site_id`.
   - Registre a localização e o nome da unidade.

2. **Registrar Agentes**
   - Instale o agente local em cada site (veja o *Installation Guide*).
   - Confirme que o agente aparece como **ativo** no Dashboard.

3. **Políticas de Alerta**
   - Defina o tempo limite de permanência (padrão: 20 minutos).
   - Configure escalonamento de risco (Low → High).
   - Ajuste janelas de horário (ex.: ignorar fora do expediente).

---

## Monitoramento
- **Métricas principais**:
  - Active Monitors (agentes em operação).
  - Security Alerts (alertas ativos).
  - Community Members (usuários registrados).
  - Detection Rate (eficiência do sistema).
- **Alertas Recentes**:
  - Verifique nível (High/Medium/Low/Info).
  - Revise descrição e local.
  - Marque como resolvido quando encerrado.

---

## Exportação de Dados
- Exporte relatórios em **CSV** para auditoria.
- Inclua histórico de alertas e status do sistema.
- Use esses relatórios para revisões internas ou compliance.

---

## Manutenção
- Verifique atualizações de versão do agente.
- Revise periodicamente as políticas de risco.
- Audite logs de acessos administrativos.

---

## Boas Práticas
- Não compartilhe credenciais administrativas.
- Revise alertas diariamente.
- Atualize contatos de emergência no painel.
