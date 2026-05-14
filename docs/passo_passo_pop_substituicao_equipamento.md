# POP – Procedimento Operacional Padrão

**Provedor:** `NV7 Telecom`  
**Setor:** SAC – Atendimento ao Cliente  
**Versão:** `1.0` | **Data:** `15/03/2026`  
**Responsável:** `Renato Oliveira`

---

## 📋 Seção: Exame Prévio para Abertura de OS

### Categoria: `OPE>SUBSTITUICAO_DE_EQUIPAMENTO`

---

## 1. Objetivo Específico

Padronizar o procedimento de diagnóstico para casos de suspeita de defeito físico ou falha recorrente em equipamento (ONU/roteador), garantindo que a substituição seja autorizada apenas quando houver evidência concreta de falha do hardware, evitando trocas desnecessárias e identificando causas externas (energia, ambiente) que podem simular defeito no equipamento.

---

## 2. Ferramentas e Padrões


| Item                  | Descrição                                                     |
| --------------------- | ------------------------------------------------------------- |
| Evidência obrigatória | Vídeo ou foto nítida do equipamento em operação               |
| Critério de falha     | Comportamento recorrente e reproduzível (não evento isolado)  |
| Verificação ambiental | Tomada, umidade, dano físico, temperatura                     |
| Sistemas              | IXC Software (para verificar histórico de autenticação/queda) |


---

## 3. Fluxo Operacional – Passo a Passo

> 🟢 INÍCIO: Cliente relata comportamento anormal no equipamento:
>
> - Wi‑Fi (SSID) some e volta intermitentemente
> - Equipamento desliga/liga sozinho repetidamente
> - Luzes apagam e acendem sem intervenção

### 🔹 Passo 1: Caracterização do Sintoma (Entender o "O Que")

**Perguntas-chave ao cliente:**

- "A rede Wi‑Fi some completamente e depois volta? Com que frequência?"
- "O equipamento desliga sozinho (luzes apagam) ou só a rede some mesmo com ele ligado?"
- "Isso começou recentemente? Após alguma queda de energia, chuva ou mudança de local?"
- "Você consegue reproduzir o problema agora, enquanto estamos na ligação?"

**Objetivo:** Diferenciar entre:

- 🔹 Falha de software/configuração (rede some, equipamento ligado)
- 🔹 Falha de energia/alimentação (equipamento desliga totalmente)
- 🔹 Falha física do hardware (comportamento errático + sinais visíveis)

---

### 🔹 Passo 2: Evidência Visual (OBRIGATÓRIO)

**Ação:** Solicitar VÍDEO nítido (preferencial) ou foto do equipamento:

- Mostrando as luzes durante o evento (piscagem anormal, apagar total)
- Mostrando o momento em que o SSID some (se possível, com celular mostrando a lista de redes ao lado do equipamento)
- Parte de trás: conexões de energia e Ethernet
- Corpo do equipamento: marcas de dano, umidade, queimado, amassado

> Não aceitar: relatos verbais sem evidência visual, exceto se houver histórico sistêmico consistente (ver Passo 4).

---

### 🔹 Passo 3: Verificação de Causas Externas (Eliminar Falsos Positivos)

**3.1 – Fonte de energia:**

- "O equipamento está conectado diretamente na tomada ou em filtro de linha/extensão?"
- "Houve queda de energia recente na residência?"
- Teste sugerido: Conectar o equipamento em outra tomada, preferencialmente em circuito diferente, e observar por 10-15 min.

**3.2 – Condições ambientais:**

- "O equipamento está em local com umidade, perto de janela, banheiro, área externa?"
- "Ele sofreu alguma queda, impacto ou foi derrubado?"
- "Há sinais de oxidação, manchas ou cheiro de queimado?"

**3.3 – Conexões físicas:**

- Verificar (via vídeo) se cabos estão firmes, sem mau contato
- Cabo de energia frouxo pode simular "desligamento intermitente"

**Decisão:**

- ✅ Causa externa identificada (ex: tomada instável)? → Orientar correção. NÃO abrir OS para substituição.
- ❌ Causa externa descartada e evidência visual sugere falha do equipamento? → Avançar para Passo 4.

---

### 🔹 Passo 4: Confirmação Sistêmica (IXC Software / Histórico)

**Ação:**

- Acessar IXC Software > Login do cliente > Histórico/Logs
- Verificar padrão de quedas de autenticação ou reinicializações

**Critério de confirmação:**

- 📊 Padrão recorrente: Múltiplos eventos de "offline/online" em curto período (ex: 3+ vezes em 24h) sem intervenção do cliente
- 📊 Equipamento aparece como "não responde" mesmo com sinal óptico normal (sugere falha interna de processamento)

**Decisão:**

- ✅ Histórico sistêmico + evidência visual + causas externas descartadas = Falha de equipamento confirmada.
- ❌ Evento isolado ou sem padrão claro = Orientar monitoramento por 24-48h. Reavaliar se persistir.

---

### 🔹 Passo 5: Verificações Complementares (Adicionais Sugeridas)

**🔹 Firmware/Software:**

- O equipamento está com firmware desatualizado?
- Há nota de release conhecida para o modelo que corrige instabilidade? → Tentar atualização remota antes de substituir.

**🔹 Modelo/Lote:**

- Este modelo/lote tem problema crônico conhecido?
- Consultar base interna de "modelos com defeito de fábrica".

**🔹 Garantia/Comodato:**

- Equipamento ainda está em período de garantia?
- É comodato da operadora ou equipamento do cliente? (Isso define quem arca com a troca e o procedimento logístico)

**🔹 Teste de isolamento (se viável remotamente):**

- Se o cliente tiver outro roteador, orientar teste substituto para confirmar que o problema está no equipamento original.

---

### 🔹 Passo 6: Decisão Final – Abrir OS para Substituição?

**✅ Critérios para abrir `OPE>SUBSTITUICAO_DE_EQUIPAMENTO`:**

- Evidência visual (vídeo/foto) mostrando comportamento anormal recorrente (SSID some/volta, desligamento espontâneo)
- Causas externas descartadas (tomada testada, ambiente adequado, cabos firmes)
- Histórico sistêmico (IXC Software) corrobora instabilidade recorrente
- Firmware atualizado ou atualização não resolveu (se aplicável)
- Modelo/lote não possui correção conhecida por software

**📝 Informações obrigatórias na OS:**


| Campo                          | Exemplo de preenchimento                                                                                    |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------- |
| Descrição detalhada do sintoma | "SSID some por 30s e volta, 4x/hora, conforme vídeo em anexo"                                               |
| Evidência visual               | "Vídeo recebido em DD/MM HH:MM – mostrar luz PON apagando intermitentemente"                                |
| Verificações de causa externa  | "Tomada testada em outro ponto: problema persiste" / "Equipamento em local seco, sem sinais de dano físico" |
| Modelo e número de série       | "TP-Link Archer C6, S/N: XXXXXXX"                                                                           |
| Histórico sistêmico            | "IXC Software: 7 quedas de autenticação nas últimas 24h sem intervenção"                                    |
| Firmware                       | "Versão atual: X.Y.Z – atualização tentada? Sim/Não"                                                        |
| Tipo de equipamento            | "Comodato ISP" ou "Equipamento do cliente"                                                                  |


**🚫 NÃO abrir OS para substituição se:**

- Relato verbal sem evidência visual e sem padrão sistêmico
- Causa externa provável (tomada instável, umidade, cabo frouxo) não foi testada/corrigida
- Evento isolado sem recorrência (orientar monitoramento)
- Problema pode ser resolvido por atualização de firmware ou reconfiguração remota
- Equipamento é do cliente e não há diagnóstico conclusivo de defeito (evitar responsabilidade indevida da operadora)

---

## 4. Alertas e Boas Práticas

> "Some e volta" pode ser software ou hardware: Sempre tente atualização de firmware ou reset de configuração antes de autorizar substituição, se o sintoma permitir.

> Energia instável é a causa mais comum de "desligamento aleatório": Testar em outra tomada é um passo barato que evita troca desnecessária.

> Vídeo > Foto > Relato verbal: Quanto mais rica a evidência, menor a chance de o técnico chegar no local e não reproduzir o problema.

> Documente o padrão, não o evento: "Acontece 3x por dia" é mais útil para diagnóstico do que "aconteceu uma vez".

> Equipamento do cliente vs. comodato: Deixe claro na OS de quem é a responsabilidade pela troca, para evitar conflito na visita técnica.

---

## 5. Referências

- 📎 Anexo A: Guia de identificação de danos físicos em equipamentos (manchas, oxidação, conector solto)
- 📎 Anexo B: Script de solicitação de vídeo demonstrativo ao cliente
- 📎 Anexo C: Lista de modelos com defeitos crônicos conhecidos e procedimentos específicos
- 📎 Anexo D: Fluxograma: Substituição vs. Reparo vs. Orientação
- 📎 Anexo E: Procedimento logístico para troca de comodato (coleta/entrega)

---

> 📄 Metadados do documento  
> Arquivo: `passo_passo_pop_substituicao_equipamento.md`  
> Última atualização: `15/03/2026`  

