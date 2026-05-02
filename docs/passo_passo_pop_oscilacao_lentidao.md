# POP – Procedimento Operacional Padrão

**Provedor:** `NV7 Telecom`  
**Setor:** SAC – Atendimento ao Cliente  
**Versão:** `1.0` | **Data:** `15/03/2026`  
**Responsável:** `Renato Oliveira`

---

## 📋 Seção: Exame Prévio para Abertura de OS

### Categoria: `OPE>REPARO_LENTIDAO_OSCILACAO`

---

## 1. Objetivo Específico

Padronizar o procedimento de diagnóstico remoto para reclamações de **lentidão ou oscilação de internet**, diferenciando problemas reais de rede/equipamento de limitações locais (dispositivo do cliente, Wi‑Fi, interferência), evitando aberturas indevidas de OS.

---

## 2. Ferramentas e Padrões

| Item | Descrição |
|------|-----------|
| **Sistemas de monitoramento** | IXC Software e/ou OLT Cloud |
| **Parâmetro crítico** | Potência óptica (dBm) |
| **Faixa aceitável** | Até `-27 dBm` (valores mais negativos = problema) |
| **Exemplo de interpretação** | `-25 dBm` = OK \| `-30 dBm` = fora do padrão → pode abrir OS |
| **Apps de teste recomendados** | Wifiman (Android/iOS), Speedtest.net |
| **Teste de referência** | Via cabo de rede (sempre que possível) |

---

## 3. Fluxo Operacional – Passo a Passo

> 🟢 **INÍCIO:** Cliente relata lentidão ou oscilação na internet.

### 🔹 Passo 1: Verificação da Potência Óptica (CRÍTICO)

**Ação:**
- Acessar **IXC Software** ou **OLT Cloud**
- Localizar o cliente e verificar o valor de potência (dBm)

**Decisão:**

| Condição | Ação |
|----------|--------|
| ❌ Potência **PIOR** que `-27 dBm` (ex: -28, -30, -35) | • Problema de sinal óptico confirmado<br>• Pode abrir OS: `OPE>REPARO_LENTIDAO_OSCILACAO`<br>• Preencher: valor medido, sistema consultado, horário |
| ✅ Potência **DENTRO** do padrão (ex: -15, -20, -27 dBm) | • Sinal óptico OK<br>• Avançar para análise do cenário |

---

### 🔹 Passo 2: Identificar o Escopo do Problema

**Pergunta-chave ao cliente:**
> "O problema acontece em **TODOS** os dispositivos da sua casa ou só em **UM** específico (ex: seu celular)?"

#### Cenário A: Problema em APENAS UM DISPOSITIVO (ex: celular)

**Explicação ao cliente** *(usar linguagem didática)*:
- "As placas Wi‑Fi de celulares são menores e menos potentes que as de computadores, por limitação de espaço interno."
- "Por isso, mesmo colado no roteador, um celular raramente atinge 100% da velocidade contratada."
- "Isso é uma limitação do dispositivo, não da sua internet."

**Ação recomendada:**
- Orientar teste com app **Wifiman** ou **Speedtest.net**
- Comparar resultado com o plano contratado *(expectativa realista)*
- Se possível, orientar teste em outro dispositivo para comparação

**Decisão:**
- ✅ Problema confirmado apenas no dispositivo? → **NÃO abrir OS**. Encerrar com orientação.
- ❌ Cliente insiste que é na rede? → Seguir para **Cenário B**.

#### Cenário B: Problema em MÚLTIPLOS DISPOSITIVOS / REDE TODA
→ Avançar para **Passo 3**.

---

### 🔹 Passo 3: Análise e Ajustes no Roteador (Cenário Rede Toda)

#### 3.1 – Orientar sobre as duas bandas Wi‑Fi

| Banda | Características | Recomendação |
|-------|----------------|--------------|
| **2.4 GHz** | Maior alcance, mais lenta, mais sujeita a interferência (micro-ondas, Bluetooth, redes vizinhas) | Usar para dispositivos distantes do roteador |
| **5 GHz** | Muito mais rápida, menos interferência, alcance menor | Usar para dispositivos próximos ao roteador |

#### 3.2 – Ajustes técnicos possíveis (via acesso remoto)

**Canal Wi‑Fi:**
- `2.4 GHz`: Fixar em **1, 6 ou 11** (menos sobrepostos)
- `5 GHz`: Manter em automático ou fixar canal menos congestionado

**Largura de banda (Channel Width):**
- `2.4 GHz`: Aumentar de **20 MHz** para **40 MHz** *(se o ambiente permitir)*
- `5 GHz`: Manter em **80 MHz** *(ou 120 MHz, se suportado)*

**Band Steering / Unificação de SSID:**
- Ativar, se disponível, para que o roteador escolha a melhor banda automaticamente para cada dispositivo
- Explicar ao cliente: *"Seu roteador vai decidir sozinho qual rede é melhor para cada aparelho"*

#### 3.3 – Solicitar evidência visual (OBRIGATÓRIO para OS)

**Pedir ao cliente: foto ou vídeo NÍTIDO do equipamento mostrando:**
- ✅ Luzes da ONU e do roteador *(status e padrão de piscagem)*
- ✅ Parte de trás: conexão dos cabos *(fibra, energia, Ethernet)*
- ✅ Ambiente: onde o roteador está posicionado

> ⚠️ **Não aceitar:** fotos escuras, tremidas ou parciais. Sem evidência clara, não é possível diagnosticar remotamente.

---

### 🔹 Passo 4: Decisão Final – Abrir OS?

#### ✅ Critérios para abrir `OPE>REPARO_LENTIDAO_OSCILACAO`

- [ ] Potência óptica pior que `-27 dBm` *(confirmado em IXC ou OLT Cloud)*
- [ ] **OU:** Potência OK, **MAS**:
  - [ ] Problema afeta múltiplos dispositivos
  - [ ] Ajustes de canal/banda foram aplicados e não resolveram
  - [ ] Teste via cabo *(se realizado)* também apresenta lentidão/oscilação
  - [ ] Cliente enviou foto/vídeo nítido do equipamento

#### 📝 Informações obrigatórias na OS

| Campo | Exemplo de preenchimento |
|-------|-------------------------|
| Valor da potência óptica medida | `"-32 dBm"` |
| Sistema consultado | `IXC Software` ou `OLT Cloud` |
| Resultado do teste de velocidade | `Wifiman: 45 Mbps download` |
| Dispositivos afetados | `"todos"` ou lista específica |
| Ajustes realizados no roteador | `Canal 6 fixo, banda 40 MHz, SSID unificado` |
| Banda utilizada no teste | `2.4 GHz` ou `5 GHz` |
| Evidência visual recebida? | `Sim` / `Não` |

#### 🚫 NÃO abrir OS se:

- [ ] Problema restrito a um único dispositivo *(especialmente celular)* sem evidência de problema na rede
- [ ] Cliente está testando apenas na rede `2.4 GHz` em ambiente com muita interferência, sem ter tentado `5 GHz`
- [ ] Ajustes de roteador ainda não foram aplicados/testados
- [ ] Potência óptica está dentro do padrão (`-27 dBm` ou melhor) e não há outros indicadores de problema de rede

---

## 4. Alertas e Boas Práticas


>​ **Potência óptica é o primeiro filtro.** Se estiver ruim, não perca tempo com ajustes de Wi‑Fi: abra OS com o valor documentado.
​

>​ **Celular NÃO é referência para teste de velocidade máxima.** Sempre contextualize a limitação da placa Wi‑Fi móvel.


>​ **2.4 GHz é naturalmente mais lenta e instável.** Oriente o cliente a usar `5 GHz` sempre que estiver próximo ao roteador.


> **Foto/vídeo do equipamento é OBRIGATÓRIO para abertura de OS.** Sem evidência visual, a equipe técnica pode perder tempo em visita desnecessária.


>​ **Unificação de banda (Band Steering)** ajuda clientes leigos, mas explique que o roteador "escolhe por ele". Isso reduz chamados futuros sobre "minha rede sumiu".

---

## 5. Referências

- 📎 **Anexo A:** Tabela de conversão e interpretação de dBm
- 📎 **Anexo B:** Script de explicação sobre limitações de Wi‑Fi em celulares
- 📎 **Anexo C:** Guia rápido de canais Wi‑Fi menos congestionados por região
- 📎 **Anexo D:** Modelo de solicitação de foto/vídeo do equipamento

---

> 📄 **Metadados do documento**  
> *Arquivo:* `passo_passo_pop_oscilacao_lentidao.md`  
> *Última atualização:* `15/03/2026` 