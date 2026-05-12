### script para ordens de servico
  Sem foto da caixa depois da instalação com o ID do cliente
  Sem foto da acomodação do(s) equipamento(s) dentro da residência
  Sem foto da Potência do Sinal na residência
  Sem foto do documento do responsável que recebeu o técnico
  Sem acesso remoto ativo

### acessos ao netplanety IXC
  `Usuários Opa:`
    noc01@nex3.com.br
    prvZ3#00XdntVI6coR=zsu3QCKMIR'^rV;Qcd(nm+D~;!DD$-]

    noc02@nex3.com.br
    n~VYSC+Ep[u3MaX&}.2,[W7WgFGSS~KI

    noc03@nex3.com.br
    prvZ3#00XdntVI6coR=zsu3QCKM$B's&


  `Usuários Ixc:`
    noc01@nex3.com.br
    B1ED9;sn9qu@RFl2[OMZ~iWToHdSxi_M

    noc02@nex3.com.br
    ~vl,i!rUCI@PQfYlREfWFbh34F-&Fhc#

    noc03@nex3.com.br
    K9UFnK@zVh9#9Zo[ozRDe]B;o}q,6h.z

### Senhora
  Olá! A senhora ainda está por aqui? Gostaria de continuar nosso atendimento. 😊👋

  Fui informado de que a senhora está enfrentando problemas com sua conexão. Procede?

### Senhor
  Olá! O senhor ainda está por aqui? Gostaria de continuar nosso atendimento. 😊👋
  
  Fui informado de que o senhor está enfrentando problemas com sua conexão. Procede?

### Perguntar para a cliente se ela ainda ta ativa no chat
 
### Card de apresentação
Eu me chamo Renato, sou do setor de tecnlogia do seu provedor de internet, NV7.

### Template mensagem para sem contato com a cliente
  Estou entrando em contato com a senhora para informar que nossos técnicos estão à disposição para realizar o ajuste da rede em sua residência.
  Porém, até o momento, não conseguiram contato com a senhora.


### FibeHome OLT Comandos
`especificacoes (slots)`
  OLT-FH-VDS-01# show all_card_serial 
  SLOT    SERIAL_NUM
------------------------------
  1       150534210246
  3       121137050110 
  5       121350640477
  10      12133298003218
  19      121337700115

system device version is:V104R002
CARD            NAME          HARDVER           SOFEVER    
 10           HSWA    WKE2.115.331R1A           RP1200
 11           GCOB    WKE2.201.168S1B           RP1200
 19           HU1A   WKE2.170.846R3B1           RP0300
 26            CIO   WKE2.200.352R1B1           RP0100

### Numeros dos tecnicos operacional( ope ) + area de atuacao
 `Jardim Carapina`
    Jhefferson(27 99728-2109)
    Wesley(27 99603-2036)

  `Jardim Tropical`
    Michel(27 99582-6063)
    Saulo(27 99998-8756)
    Jonata - Auxiliar(27 99577-3785)
    Reinaldo - Auxiliar(27 99298-9443)

  `Vila Nova/Feu rosa e Jacaraípe`
    Elton Jhon(27 99590-2019)
    Marcelo(27 99935-2572)
    Kevin(27 98889-0414)

  `Balneário`
    Eder Junior(27 99628-6953)

  `Novo Horizonte`
    Danilo(27 99795-6968)

  `Vitória`
    Renan(27 99853-2514)
    Dione Max - Auxiliar(27 99966-8465)

  `Vista da Serra`

----

### Numeros dos tecnicos infraestrutura( field )
  `EQUIPE 1`
    Breno(99764-6970)
    Auxiliar

  `EQUIPE 2`
    Carlos(99978-0394)
    Dalmo(99797-4403)

  `EQUIPE 3`
    Ivan(99789-7879)
    Júlio(99632-8724)

  `EQUIPE 4`
    Luís(99796-8705)
    Auxiliar

  `EQUIPE 5`
    Edilson
    João Victor - Auxiliar(99655-1673)

-----------

### Assunto de instalacao em OS's
  OPE>INSTALAÇÃO_NOVA>EXECUÇÃO

### Exercicio de trablho de cada tecnico por regiao
  `Jardim Carapina`
    Jhefferson: Instalação-260
    Wesley: Reparo-229

  `Tropical`
    Michel : Instalação e reparo
    Saulo:Instalação e reparo
    Intercalar entre eles

  `Vitória`
    Renan e Dione Mex(auxiliar): Instalação e reparo-89

  `Balneário`
    Danilo: Instalação-180
    Éder Júnior: Reparo-181

  `VNC`
    Elton: Instalação-248
    Marcelo e Kevin: reparo-78

### Modelo de exercicio feito por cada tecnico 
`Jardim Carapina`
  260 Jhefferson: Instalação
  229 Wesley: Reparo

`Tropical`
  43 Michel : Instalação e reparo
  87 Saulo:Instalação e reparo
  Intercalar entre eles

`Vitória`
  89 Renan e Dione Mex(auxiliar): Instalação e reparo 
  *obs: é dado apenas um total de 2 ordens de servico de instalção por dia*

`Balneário`
  180 Danilo: Instalação
  181 Éder Júnior: Reparo 

`VNC`
  248 Elton: Instalação
  78 Marcelo e Kevin: reparo

### Padrao de busca de caixas NV7
  CTO-*E10*-13.7
  *E<numero> = PON*

### caso
  Quando for Alteração, tranferencia, instalacao ou reestruracao voltar para jakeline
   alterar o setor para 19, resposavel 25, jakeline

### Token do IXC para API
  eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE3NzIwMzc5NzAsImlzcyI6Il8iLCJuYmYiOjE3NzIwMzc5NzAsImlkIjoiMjgwIiwiY2xhc3MiOiJ1c3VhcmlvIiwidHlwZSI6eyJtb2R1bGUiOiJxdWVyeS1idWlsZGVyIiwidXJsUm91dGUiOiIvYXV0aGVudGljYXRpb24vcXVlcnktYnVpbGRlci9nZW5lcmF0ZS10b2tlbnMiLCJ1cmxBY3Rpb25Sb3V0ZSI6IkF1dGguZ2VuZXJhdGVUb2tlbnMiLCJ1cmxHcm91cFJvdXRlIjoiYXV0aGVudGljYXRpb24ifX0.QzwCAxtpJBvKrGVA_d9MxdiyxxyoxUqUkwcVoVmaqh1P3Q8IrrGa6dA3Banh25YnsjOVa1_qJ_3GbZEP-oVh0g

[{"TB":"view_funcionarios_setor.funcionario","OP":"L","P":"gobbo"},{"TB":"su_oss_chamado.status","OP":"IN","P":"'A','DS','AN','EX','EN','AS','RAG','AG'"},{"TB":"su_oss_chamado.prioridade","OP":"IN","P":"'B','N','A','C'"}]

### Horario dos novatos
Yasmin, Luis Henrique e eu entramos às 8 e saímos às 14

Saulo,
Jhefferson,
Eder,
Elton,
Renan

'protocolo': 202603742726', 'endereco': 'ES Serra 29161-748 Jardim Carapina - Rua Baixo Guandu, 30', 'complemento': '', 'id_condominio': '0', 'latitude': '-20.235375', 'bloco': '', 'longitude': '-40.287705', 'apartamento': '', 'bairro': 'Jardim Carapina', 'referencia': 'portão marrom grande',

### Novo padrão de atendimento:
  No final do turno, quando os tecnicos deixarem OS para serem feitas no outro dia por conta
  de termino de expediente, `DEVEMOS` ligar para os clientes, e deixar registrado nos
  atendimentos, que foi feita tentativa de contato com o cliente no dia seguinte.

### Novo padrão de atendimento:
  Quando temos clientes com `OS` de `Sem Conexão` e ela volta ao normal no em algum momento
  pedir para o atendimento entrar em contato para saber melhor sobre a situação do cliente,
  Se normalizou mesmo.

  
### Ideias de implementação:
  Implementar um lider de campo




Fak@as7348JHa

ZTEGCC5BF216

### SAUDAÇÃO
Olá! Meu nome é Renato, sou do setor de tecnologia do seu provedor de internet, NV7. Tudo bem?

### CONTATO ANTECIPADO
Olá, Camile, correto?

Estou entrando em contato pois existe uma visita técnica agendada para hoje no período da manhã. O atendimento nesse horário é possível para você?

Certo! Assim que o técnico estiver a caminho da sua residência, faremos uma ligação ou enviaremos uma mensagem por aqui pelo WhatsApp, ok?

Informarei ao técnico que o contato foi realizado pela manhã e que a disponibilidade para o atendimento foi confirmada.

### INATIVIDADE NO CHAT
Olá! Você ainda está por aqui? Gostaria de continuar nosso atendimento. 😊👋

### PROBLAMAS COM CONEXÃO
Fui informado de que está ocorrendo um problema com a conexão. Procede?



[
  {
    "TB":"su_oss_chamado.data_agenda","OP":"BE","P":"2026-05-12 00:00:00","P2":"2026-05-12 23:59:59"
    },
    {
      "TB":"view_funcionarios_setor.funcionario","OP":"L","P":"renato"},
      {
        "TB":"su_oss_chamado.status","OP":"IN","P":"'A','DS','AN','EX','EN','AS','RAG','AG'"
        },
        {"TB":"su_oss_assunto.assunto","OP":"L","P":"reparo"},{"TB":"su_oss_chamado.prioridade","OP":"IN","P":"'B','N','A','C'"}]
