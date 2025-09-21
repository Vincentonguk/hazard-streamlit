# ✅ Hazard Security – User Acceptance Test (UAT) Checklist

## Objetivo
Garantir que o sistema Hazard Security funciona conforme esperado antes da entrada em produção.

---

## Testes Funcionais
- [ ] Dwell ≥ 20 min gera alerta em até 60s.
- [ ] Sair da área fecha alerta em até 60s.
- [ ] Reentrada retoma o mesmo `device_id` (sem duplicar).
- [ ] Escalonamento de risco funciona (Low → Medium → High).
- [ ] Botão de emergência cria incidente e notifica.
- [ ] Dashboard exibe métricas atualizadas corretamente.

---

## Testes de Relatórios
- [ ] Exportação CSV disponível e completa.
- [ ] Dados incluem histórico de alertas e status do sistema.

---

## Testes de Resiliência
- [ ] Perda de internet por 10 min → dados reenviados após reconexão.
- [ ] Agente inválido é rejeitado (API Key incorreta).
- [ ] Logs de falha registrados.

---

## Aprovação
- Cliente: _____________________
- Data: ________________________
- Assinatura: __________________
