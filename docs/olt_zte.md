# 📡 CHEAT SHEET ZTE OLT - COMPLETO E EXPLICADO

## 🧠 1. CONHEÇA SUA OLT
* `show card` - **Lista todas placas/slots** (CtrlBoard, LineCards, PSUs)
* ~~show interface brief~~ - **REMOVIDO** (não existe na ZTE)
* `show gpon onu ?` - **Mostra sintaxe exata** das suas interfaces GPON

## 🔍 2. STATUS DAS ONUs
* `show gpon onu state gpon-olt_1/1/4` - **Status Admin/OMCC/Phase** de todas ONUs na PON
* `show gpon onu uncfg gpon-olt_1/3/1` - **ONUs novas detectadas** (AutoFind, aguardando cadastro)
* `show gpon onu by sn ZTEGCXXXXXX ` - **Busca ONU por SN em toda OLT**
## 📋 3. DADOS DAS ONUs
* `show gpon onu baseinfo gpon-olt_1/3/1` - **SN, modelo, fabricante** de todas ONUs na PON
* `show gpon onu detail-info gpon-olt_1/3/1` - **Config completa** (VLANs, GEM ports, perfis)

## ⚡ 4. POTÊNCIAS ÓPTICAS
* `show pon power olt-rx gpon-olt_1/3/1` - **Rx OLT** (potência que OLT recebe de cada ONU)
* `show pon power onu-rx gpon-olt_1/3/1` - **Rx ONUs** (potência que cada ONU recebe da OLT)
* `show pon power olt-tx gpon-olt_1/3/1` - **Tx OLT** (potência que OLT transmite)

## 📊 5. CONFIG ATIVA
* `show service-port onu gpon-olt_1/3/1` - **Service-ports ativos** (VLANs dos clientes)
* `show gpon onu summary` - **Resumo total** (quantas ONUs online/offline por status)

## 🚨 6. MONITORAMENTO
* `show gpon statistics gpon-olt_1/3/1` - **Tráfego/contadores** (bytes/packets da PON)
* `show alarm active` - **Alarmes ativos** (LOS, LOF, potências ruins)
* `show gpon onu gemport gpon-olt_1/3/1` - **GEM ports** (mapeamento tráfego ONU→VLAN)

---

## 🎯 CHECK RÁPIDO (2min por PON)
* `show gpon onu state [PON]` - **Status geral**
* `show pon power olt-rx [PON]` - **Potências recebidas**
* `show gpon onu uncfg [PON]` - **Novas ONUs**

## 💡 TRUQUES ZTE CLI
* `?` - **Ajuda contexto** (sempre use!)
* `TAB` - **Autocomplete**
* `show ?` - **Todos comandos disponíveis**

---

**🔥 EXECUTE AGORA:**
