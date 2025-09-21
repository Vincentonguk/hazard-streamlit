# 🔒 Hazard Security – Data Protection Impact Assessment (DPIA)

## Objetivo
Este documento descreve como o **Hazard Security** lida com dados coletados, garantindo conformidade com o **GDPR** e demais regulamentos de privacidade.

---

## Escopo
- Monitoramento de dispositivos próximos via sinais **Wi-Fi/Bluetooth**.
- Registro de metadados técnicos para análise de risco.
- Não há coleta de **informações pessoais identificáveis (PII)**.

---

## Dados Coletados
- **Hash do identificador do dispositivo** (MAC address com salt).
- **Horário da primeira e última detecção**.
- **Duração da permanência (dwell time)**.
- **Local/Site** onde foi detectado.
- **Nível de risco atribuído**.

---

## Proteções Aplicadas
- **Pseudonimização**: MAC address nunca armazenado em claro → convertido para hash.
- **Criptografia em trânsito**: todos os dados enviados via HTTPS (porta 443).
- **Criptografia em repouso**: banco de dados protegido com criptografia nativa.
- **Controle de acesso**: apenas administradores autorizados podem ver alertas completos.

---

## Retenção de Dados
- Dados de **deteções brutas**: até 30 dias.
- Dados de **alertas consolidados**: até 1 ano.
- Logs de auditoria: até 2 anos.
- Após expiração → dados são automaticamente removidos.

---

## Direitos do Usuário
- **Direito de acesso**: membros podem solicitar resumo dos dados.
- **Direito de exclusão**: dispositivo pode ser colocado em lista de exclusão.
- **Direito de portabilidade**: exportação dos alertas em CSV.

---

## Riscos Identificados
- Possibilidade de reidentificação se combinados com dados externos.
- Uso indevido por administradores sem auditoria adequada.
- Mitigação: limitar acesso, auditoria regular, políticas de uso.

---

## Conclusão
O **Hazard Security** foi projetado para respeitar a privacidade, coletando apenas dados técnicos mínimos necessários para fins de segurança.  
A coleta é proporcional, pseudonimizada e sujeita a auditoria contínua.
