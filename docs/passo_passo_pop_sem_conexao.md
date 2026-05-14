# POP – Procedimento Operacional Padrão

**Provedor:** `NV7 Telecom`  
**Setor:** SAC – Atendimento ao Cliente  
**Versão:** `1.0` | **Data:** `15/03/2026`  
**Responsável:** `Renato Oliveira`

---

## 📋 Seção: Exame Prévio para Abertura de OS

### Categoria: `OPE>REPARO_SEM-CONEXAO`

---

## 1. Objetivo Específico

Padronizar o procedimento de diagnóstico remoto para clientes que relatam "internet totalmente fora do ar", diferenciando problemas locais (equipamento, energia, cabos) de problemas de rede (fibra cortada, CTO offline, manutenção), garantindo que a OS seja aberta com evidências suficientes e direcionada ao setor correto.

---

## 2. Ferramentas e Padrões

| Item | Descrição |
|------|-----------|
| Sistemas | IXC Software (módulos: Login, Log Rádios, Mapa), OLT Cloud (Mapa) |
| Evidência visual | Vídeo obrigatório (preferencial) ou foto nítida |
| Critério geográfico | Múltiplos clientes offline na mesma CTO/horário → Encaminhar para Infraestrutura/Field, não para técnico operacional |
| Escalação | Informar setor responsável (ex: Renato) para análise avançada via terminal/OLT |

---

## 3. Fluxo Operacional – Passo a Passo

> 🟢 INÍCIO: Cliente relata: "Minha internet não funciona de jeito nenhum".

### 🔹 Passo 1: Evidência Visual (OBRIGATÓRIO – PRIMEIRO PASSO)

**Ação:** Solicitar ao cliente (ANTES de qualquer análise sistêmica):
- Preferencialmente: VÍDEO nítido do equipamento
- Mínimo aceitável: FOTO nítida (mas vídeo é fortemente recomendado)

**O que o vídeo/foto DEVE mostrar:**

| Elemento | O que observar |
|----------|---------------|
| Luzes da ONU (prioritário) e do roteador | - Status de PON, LOS, Power, LAN<br>- Padrão de piscagem (fixa, piscando lento, piscando rápido)<br>- Cor das luzes (verde, vermelho, laranja) |
| Parte de trás dos equipamentos | - Cabo de fibra conectado corretamente?<br>- Cabo Ethernet conectado na porta correta da ONU → WAN do roteador?<br>- Cabos aparentam estar danificados ou soltos? |
| Contexto do equipamento | - Onde está posicionado?<br>- Há sinais de dano físico, umidade, interferência de calor? |

 
> Não aceitar: fotos escuras, tremidas, parciais ou que não permitam identificar o status das luzes e conexões.

**Decisão:**
- ✅ Vídeo recebido e analisado? → Avançar para Passo 2.
- ❌ Cliente se recusa ou não consegue enviar? → Orientar novamente. Sem evidência visual, NÃO abrir OS (exceto em casos de queda massiva confirmada por mapa).

---

### 🔹 Passo 2: Análise de Logs no XC Software

**Ação:**
- Acessar IXC Software > Login do cliente > "Log Radius"
- Verificar histórico de quedas/conexões

**Verificação específica:**
- 🔍 Equipamentos TP-Link: Existe padrão de "queda recorrente" conhecido neste modelo? (Problema crônico de firmware)

**Decisão:**
- ✅ Problema crônico identificado (ex: TP-Link com bug)? → Tentar orientação de limpeza de MAC. Se persistir, abrir OS com observação do modelo e log.
- ❌ Sem padrão óbvio nos logs? → Avançar para Passo 3.

---

### 🔹 Passo 3: Análise Geográfica e Temporal (Mapa)

**Ação:**
- Acessar mapa do XC Software ou OLT Cloud
- Localizar o cliente pelo login/CTO
- Observar:
  - Cor do marcador: Vermelho = offline/LOS
  - Horário da última conexão/queda registrado

**Verificação crítica:**
- 🗺️ Existem OUTROS clientes na mesma CTO/região também offline no MESMO horário/dia?

**Decisão:**

| Condição | Ação |
|----------|--------|
| ✅ Múltiplos clientes afetados simultaneamente? | - Provável problema de infraestrutura (fibra cortada, energia na CTO, manutenção)<br>- NÃO abrir OS para técnico operacional<br>- Encaminhar para setor de Infraestrutura/Field<br>- Registrar no sistema: "Queda múltipla na CTO [X] – encaminhado para Infra" |
| ❌ Apenas este cliente offline? | → Avançar para Passo 4 |

---

### 🔹 Passo 4: Verificação de Contexto e Escalação

**4.1 – Verificar comunicações da Infraestrutura**
- [ ] Há aviso de manutenção programada na região do cliente?
- [ ] Há relato de queda de energia na área?
- Se SIM → Não abrir OS. Informar cliente sobre previsão.

**4.2 – Perguntas complementares ao cliente**

> • "Houve queda de energia na sua residência recentemente?"  
> • "O equipamento está conectado em tomada/filtro de linha que está funcionando?"  
> • "Alguém mexeu nos cabos ou no equipamento?"

**4.3 – Escalação para análise avançada (CRÍTICO)**

 
> Ao constatar que é um caso isolado e as etapas anteriores não identificaram a causa, INFORMAR o setor responsável (ex: Renato) antes de abrir OS.

**Motivo:** Setor avançado pode acessar terminal da OLT e verificar:
- Status do PON port que alimenta o cliente
- Logs de autenticação da ONU
- Se há outros clientes na mesma porta com problema
- Timestamp exato do evento de queda

**Decisão:**
- ✅ Setor avançado confirmou problema no equipamento/cliente? → Abrir OS com as evidências consolidadas.
- ❌ Setor avançado identificou problema de rede? → Encaminhar para Infraestrutura, sem abrir OS operacional.

---

### 🔹 Passo 5: Decisão Final – Abrir OS?

**✅ Critérios para abrir `OPE>REPARO_SEM-CONEXAO`**

- [ ] Evidência visual (vídeo/foto) recebida e analisada
- [ ] Potência óptica ausente ou LOS vermelho confirmado (se visível)
- [ ] Cliente isolado no mapa (não há queda múltipla na CTO)
- [ ] Sem aviso de manutenção/energia na região
- [ ] Logs não indicam problema crônico resolúvel remotamente
- [ ] Escalação para setor avançado realizada (quando aplicável)

**📝 Informações obrigatórias na OS**

| Campo | Exemplo de preenchimento |
|-------|-------------------------|
| Status das luzes da ONU (conforme vídeo/foto) | "LOS vermelho fixo", "PON apagada", "Power verde, LOS vermelho" |
| Conexões físicas | "Fibra conectada na PON, Ethernet na LAN1 → WAN do roteador" |
| Modelo da ONU/roteador | "ONU FiberHome HG8245H, Roteador TP-Link Archer C6" |
| Horário da queda registrado no sistema | "14/03 22:15" |
| Resultado da análise de mapa | "Cliente isolado" ou "2 vizinhos também offline" |
| Ações remotas tentadas | "Orientado reinício, sem sucesso" |
| Confirmação: Escalado para setor avançado? | Sim / Não + nome/responsável |

**🚫 NÃO abrir OS se:**

- [ ] Cliente não enviou evidência visual (vídeo/foto) e não há queda massiva confirmada por mapa
- [ ] Múltiplos clientes na mesma CTO offline no mesmo horário → Encaminhar para Infraestrutura
- [ ] Há aviso de manutenção/energia na região → Agendar retorno
- [ ] Problema identificado como crônico de modelo (ex: TP-Link) e pode ser resolvido com orientação de reset/reconfiguração

---

## 4. Alertas e Boas Práticas


> Vídeo é superior à foto: A piscagem das luzes em tempo real pode indicar se a ONU está tentando autenticar (PON piscando) ou se há perda total de sinal (LOS vermelho fixo).


> Conexão física é a causa mais comum de "sem conexão": Verifique SEMPRE se o cabo Ethernet está na porta WAN do roteador e se a fibra está bem encaixada na ONU.


> Mapa é sua bússola geográfica: Um cliente isolado offline é um problema provável no equipamento/local. Múltiplos clientes offline na mesma CTO/horário é problema de infraestrutura.


> Escalação não é "passar a bola": Informar o setor avançado (ex: Renato) antes de abrir OS evita visitas técnicas desnecessárias e acelera a resolução quando o problema é complexo.


> Energia é um fator esquecido: Sempre pergunte sobre queda de energia na residência. ONU sem energia = sem conexão, óbvio, mas o cliente nem sempre percebe que o equipamento desligou.

---

## 5. Referências

- 📎 Anexo A: Guia visual de interpretação das luzes da ONU (por modelo)
- 📎 Anexo B: Script de solicitação de vídeo/foto nítida ao cliente
- 📎 Anexo C: Lista de modelos com problemas crônicos conhecidos (ex: TP-Link com queda recorrente)
- 📎 Anexo D: Fluxograma de decisão: Operacional vs. Infraestrutura
- 📎 Anexo E: Contatos do setor avançado para escalonamento

---

> 📄 Metadados do documento  
> Arquivo: `passo_passo_pop_sem_conexao.md`  
> Última atualização: `15/03/2026`  
