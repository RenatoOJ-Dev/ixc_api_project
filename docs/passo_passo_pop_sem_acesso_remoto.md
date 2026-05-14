# POP – Procedimento Operacional Padrão

**Provedor:** `NV7 Telecom`  
**Setor:** SAC – Atendimento ao Cliente  
**Versão:** `1.0` | **Data:** `15/03/2026`  
**Responsável:** `Renato Oliveira`

---

## 📋 Seção: Exame Prévio para Abertura de OS

### Categoria: `OPE>REPARO_SEM-ACESSO-REMOTO`

---

## 1. Objetivo Específico

Padronizar o procedimento de verificação de acesso remoto ao roteador do cliente **ANTES** de abrir uma OS, evitando aberturas indevidas por falsos negativos (ex: falha na automação do IIXC Soft, alerta de segurança do navegador, etc.).

---

## 2. Ferramentas e Padrões

| Item | Descrição |
|------|-----------|
| **Ferramenta principal** | IXC Soft (módulo Logins) |
| **Porta padrão da operação** | `8091` (HTTP) |
| **Formato de acesso manual** | `http://[IP_DO_CLIENTE]:8091` |
| **Navegadores suportados** | Chrome, Edge, Firefox |

---

## 3. Fluxo Operacional – Passo a Passo

> 🟢 **INÍCIO:** Atendente precisa acessar o roteador do cliente para alteração ou verificação remota.

### 🔹 Passo 1: Tentativa Automatizada (IXC Soft)

**Ação:**
- No IXC Soft, acessar: `Logins` > Selecionar cliente > Clicar em `"Acessar"`
- O sistema tentará conectar automaticamente em `http://IP:8091`

**Resultado:**

| Condição | Ação |
|----------|--------|
| ✅ Conectou? | → Prosseguir com a alteração necessária. **ENCERRAR**. |
| ❌ Falhou? | → **NÃO abrir OS ainda**. Avançar para o **Passo 2**. |


> O XC Soft pode tentar portas diferentes da nossa padrão (`8091`). Uma falha aqui **NÃO confirma** falta de acesso remoto.

---

### 🔹 Passo 2: Validação Manual (OBRIGATÓRIA em caso de falha no Passo 1)

**Por que fazer:**
- Eliminar falso negativo causado pela automação do IXC Soft
- Confirmar se o acesso funciona na porta oficial da operação (`8091`)

**Ação:**
1. Copiar o IP de gerenciamento do cliente (ex: `192.168.100.1`)
2. Abrir navegador (Chrome, Edge, etc.)
3. Na barra de endereços, digitar manualmente:
Exemplo: `http://192.168.100.1:8091`
4. Pressionar **Enter**


**Resultado:**

| Condição | Ação |
|----------|--------|
| ✅ Página carregou (mesmo com aviso de segurança)? | → Acesso remoto **FUNCIONA**. Usar esta sessão para a alteração. **ENCERRAR**. |
| ❌ "Site não pode ser alcançado" / Timeout? | → Avançar para o **Passo 3**. |

---

### 🔹 Passo 3: Tratamento de Casos Específicos (Falsos Negativos)

#### ┌─ CASO A: Alerta de Segurança (Comum em roteadores Mercusys)

**Sintoma:**
- Página inicia carregamento, mas exibe:
  - `"Sua conexão não é particular"` ou
  - `"This connection is not private"`

**Ação Correta:**
1. Clicar em `"Avançado"` ou `"Detalhes"`
2. Clicar em `"Continuar para [IP] (não seguro)"`
3. A interface do roteador deve carregar normalmente


> Isso **NÃO é falta de acesso remoto**. É comportamento esperado do firmware. **Não abrir OS por este motivo.**

**Resultado:**
- ✅ Interface carregou após "Continuar"? → Acesso OK. **ENCERRAR**.
- ❌ Ainda não carregou? → Seguir para ações de recuperação.

#### └─ CASO B: Timeout / Carregamento Infinito / "Site não alcançado"

**Ações de Recuperação** *(executar nesta ordem)*:

| Ordem | Ação |
|-------|------|
| 1 | Fechar a aba de acesso e tentar novamente manualmente (`IP:8091`) |
| 2 | No IXC Soft > Aba Logins > Clicar em `"Atualizar"` > Tentar acessar |
| 3 | Reiniciar o equipamento do cliente *(via sistema ou orientar)* > Aguardar 2-3 minutos > Tentar acesso novamente |

**Resultado:**
- ✅ Funcionou após alguma tentativa? → Acesso restaurado. **ENCERRAR**.
- ❌ Todas as tentativas falharam? → Avançar para **Passo 4**.

---

### 🔹 Passo 4: Decisão Final – Abrir OS?

#### ✅ Critérios para abrir `OPE>REPARO_SEM-ACESSO-REMOTO`

- [ ] XC Soft falhou na tentativa de acesso pela porta `8091`
- [ ] Acesso manual via `http://IP:8091` também falhou *(timeout/sem resposta)*
- [ ] Ações de recuperação foram esgotadas *(refresh no IXC Soft + reinício)*
- [ ] Cliente **NÃO** está em manutenção programada na região

#### 📝 Informações obrigatórias no campo de observação da OS

| Campo | Exemplo de preenchimento |
|-------|-------------------------|
| IP de gerenciamento testado | `192.168.100.1` |
| Porta testada | `8091` |
| Métodos de teste utilizados | `Automatizado (IXC Soft) + Manual (browser)` |
| Ações de recuperação tentadas | `Refresh no IXC Soft, reinício do equipamento` |
| Modelo do equipamento *(se relevante)* | `Mercusys XXX` |

#### 🚫 NÃO abrir OS se:

- [ ] O acesso funcionou manualmente *(mesmo falhando no XC Soft)*
- [ ] Era apenas alerta de segurança do navegador *(Mercusys)* e o atendente não clicou em `"Avançado > Continuar"`
- [ ] O atendente não realizou a tentativa manual com `IP:8091`
- [ ] O problema foi resolvido após reinício ou refresh

---

## 4. Alertas e Boas Práticas


> **A porta `8091` é o padrão oficial.** Mesmo que o IXC Soft tente outras portas, o critério de validação é o acesso em `IP:8091`.


> **O IXC Soft pode induzir a falso negativo.** Sempre validar manualmente em caso de falha na automação.


> **Alerta "Conexão não particular" em roteadores Mercusys** é comportamento esperado do firmware, não erro de acesso. Orientar o atendente a clicar em `"Avançado > Continuar"`.


> **Sequência de recuperação obrigatória antes de abrir OS:**  
> `(1) Tentativa manual` → `(2) Refresh no XC Soft` → `(3) Reinício do equipamento`.

---

## 5. Referências

- 📎 **Anexo A:** Significado das luzes da ONU/roteador
- 📎 **Anexo B:** Script de perguntas guiadas para diagnóstico remoto
- 📎 **Anexo C:** Lista de modelos de roteadores com comportamento específico

---

> 📄 **Metadados do documento**  
> *Arquivo:* `passo_passo_pop_sem_acesso_remoto.md`  
> *Última atualização:* `15/03/2016`  