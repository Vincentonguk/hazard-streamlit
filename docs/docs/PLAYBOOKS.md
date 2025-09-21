# 📖 Hazard Security – Playbooks de Suporte

## Objetivo
Este documento fornece procedimentos rápidos para lidar com problemas comuns no **Hazard Security**.  
Deve ser usado por operadores e administradores em caso de falhas ou incidentes.

---

## 🔌 1. Sem dados chegando no Dashboard
**Sintomas:**
- Métricas não atualizam.
- Nenhum alerta novo aparece.

**Ações:**
1. Verificar se o agente local está em execução (`python agent.py --status`).
2. Conferir conexão com a internet.
3. Validar se a `API_KEY` está correta no `.env`.
4. Checar logs do agente em `logs/agent.log`.
5. Se persistir → acionar suporte técnico.

---

## 🚨 2. Muitos falsos positivos
**Sintomas:**
- Alertas aparecem mesmo sem atividade suspeita.
- Volume de alertas muito acima do esperado.

**Ações:**
1. Revisar **políticas de dwell time** (padrão: 20 min).
2. Ajustar limiares de proximidade.
3. Conferir se o site está configurado corretamente.
4. Documentar caso e reportar para equipe de risco.

---

## 🔑 3. Erro de autenticação do agente
**Sintomas:**
- Agente rejeitado pela API.
- Logs mostram `Unauthorized`.

**Ações:**
1. Conferir se a `API_KEY` não expirou.
2. Substituir `.env` com chave válida.
3. Reiniciar agente.
4. Se falhar → regenerar chave no painel de admin.

---

## 🌐 4. Perda de conexão com a internet
**Sintomas:**
- Dados param de ser enviados.
- Retomada não acontece automaticamente.

**Ações:**
1. Confirmar conectividade com outros sites (ping google.com).
2. Checar proxy/firewall da empresa.
3. Reiniciar agente após restabelecimento.
4. Dados devem ser reenviados automaticamente (fila local).

---

## 🆘 5. Botão de Emergência acionado por engano
**Sintomas:**
- Usuário clicou acidentalmente.
- Autoridades foram notificadas sem necessidade.

**Ações:**
1. Marcar incidente como **“False Alarm”** no Dashboard.
2. Comunicar equipe de segurança local.
3. Atualizar treinamento do usuário envolvido.
4. Revisar se o botão precisa de **confirmação dupla**.

---

## 📋 6. Checklist de Escalada
Se o problema não for resolvido localmente:
- Contatar **Administrador Local**.
- Acionar **Equipe Técnica Central**.
- Registrar incidente em sistema interno
