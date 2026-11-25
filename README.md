# Challenge_Motiva_2026

Integrantes:
Deborah Santos Palavicini | RM 575785

Centro Inteligente de Monitoramento de Ativos Rodoviários (CMA)
Challenge 2026.2 — FIAP + Motiva
- Tema: Manutenção Preditiva Inteligente
- Sprint: 1 — Pesquisa, modelagem e proposta de solução

1. Problema e objetivo
Os equipamentos tecnológicos de uma rodovia têm funções diferentes, mas todos ajudam a manter a operação segura e funcionando. As câmeras de CFTV permitem acompanhar o que acontece na pista; os Painéis de Mensagens Variáveis (PMV) levam avisos aos motoristas; os sistemas de análise de tráfego (SAT) registram informações sobre os veículos; as estações do SCA acompanham as condições ambientais; e os Callboxes oferecem um canal de comunicação em situações de emergência.

Cada equipamento gera informações sobre seu funcionamento. Podem ser registros de alarmes, medições, interrupções, ocorrências ou serviços de manutenção. O problema aparece quando esses dados ficam separados em sistemas e planilhas: fica mais difícil enxergar o histórico completo de um ativo e decidir qual situação merece atenção primeiro.

Também não basta contar alarmes. Um equipamento pode gerar vários avisos de baixa gravidade e continuar operando, enquanto outro pode apresentar poucos sinais, mas estar perdendo desempenho aos poucos. Para decidir o que fazer, é preciso olhar para a condição do equipamento, para os sinais de falha e para o impacto que sua indisponibilidade teria na rodovia.

O que queremos resolver com o CMA: reunir essas informações, verificar se os dados são confiáveis e acompanhar a condição dos ativos. A intenção é ajudar a equipe a decidir o que precisa ser verificado primeiro. Para isso, cada recomendação virá acompanhada dos indicadores e das ocorrências que levaram àquela conclusão.

Para organizar esse caminho, seguimos as cinco camadas apresentadas no kickoff da Motiva: aquisição, tratamento, modelagem, diagnóstico e decisão. O histórico centralizado e o painel operacional dão suporte a todas elas.

2. Frente 1 — Contexto e problema

2.1 Equipamentos analisados
Para o aprofundamento da Frente 1, escolhemos a Opção A e vamos olhar com mais atenção para três equipamentos: CFTV, PMV e SCA. Eles foram escolhidos porque representam funções diferentes na operação — monitoramento visual, comunicação com o motorista e acompanhamento das condições ambientais. O SAT e o Callbox continuam no contexto do projeto e podem entrar em uma próxima versão.

2.1.1 CFTV — Circuito Fechado de Televisão
Para que serve na rodovia
- Câmeras instaladas ao longo da rodovia transmitem imagens ao Centro de Controle Operacional (CCO).
- Câmeras PTZ permitem movimentar a visualização horizontal e verticalmente e aproximar a imagem.
- As imagens ajudam o operador a verificar acidentes, veículos parados, congestionamentos, obstáculos e outras ocorrências.
- O CFTV contribui para a consciência situacional e para o acionamento das equipes de atendimento. A ANTT descreve o uso do monitoramento por câmeras no acompanhamento da operação e na articulação de respostas a ocorrências.
O que pode dar errado e como perceber
Falha ou degradação	Dados/sinais que podem identificar o problema	Consequência operacional possível
Câmera sem imagem ou transmissão interrompida	Disponibilidade, último contato, perda de pacotes, latência, taxa de quadros, estado do link e alarmes de vídeo	O CCO perde a visão daquele trecho e pode demorar mais para confirmar uma ocorrência
Imagem escura, desfocada, suja ou obstruída	Indicador de qualidade da imagem, contraste, foco, imagem diurna/noturna e registro de inspeção/limpeza	Dificuldade para identificar veículos, obstáculos e detalhes de uma ocorrência
Falha no mecanismo PTZ	Resultado dos comandos de pan, tilt e zoom, tempo de resposta, posição informada e falhas de controle	O operador não consegue direcionar a câmera para o ponto necessário
Falha de energia, conectores ou proteção elétrica	Tensão, estado da fonte, reinicializações, alarmes elétricos e inspeções de cabos/conectores	Indisponibilidade intermitente ou total do equipamento
Umidade, corrosão, ventilação ou temperatura inadequadas no gabinete	Temperatura interna, estado de ventiladores/filtros, alarmes ambientais e inspeções	Degradação progressiva e maior chance de falha dos componentes


Informações que vale reunir no CMA: identificador da câmera, localização/quilômetro, coordenadas, estado do vídeo, disponibilidade, qualidade da imagem, comandos PTZ, latência, estado da comunicação, alarmes por severidade, temperatura do gabinete quando disponível, última limpeza/inspeção, ordens de serviço e tempo de indisponibilidade.

A FHWA descreve procedimentos de manutenção de CFTV que incluem inspeção da carcaça, limpeza do vidro, verificação do mecanismo pan/tilt, cabos e conectores, proteção contra surtos, limpadores, termostato, alimentação elétrica e qualidade do vídeo. Esses itens sustentam a escolha dos sinais de acompanhamento; os intervalos do documento norte-americano são exemplos e não devem ser tratados como calendário oficial da Motiva.

2.1.2 PMV — Painel de Mensagens Variáveis
Para que serve na rodovia
- Painéis eletrônicos, geralmente com matriz de LEDs, exibem mensagens aos motoristas.
- Podem informar acidentes, interdições, obras, lentidão, neblina, condições da pista e orientações de segurança.
- O CCO seleciona ou programa mensagens com base em informações de câmeras, telefonia de emergência, inspeção de tráfego e outras fontes.
- O equipamento precisa exibir a mensagem correta, legível e no momento adequado. Uma falha técnica pode comprometer a comunicação com o usuário.
O que pode dar errado e como perceber
Falha ou degradação	Dados/sinais que podem identificar o problema	Consequência operacional possível
LEDs/pixels apagados ou com luminosidade irregular	Quantidade/localização de pixels defeituosos, teste de linhas e colunas, intensidade luminosa e resultado do autoteste	Mensagem parcialmente ilegível ou incompleta
Painel não recebe ou não executa a mensagem	Mensagem enviada, confirmação de execução, código de erro, estado do controlador, watchdog e comunicação	Motorista pode não receber o aviso esperado ou visualizar informação desatualizada
Sensor de luminosidade/photocell com defeito	Leitura do sensor de luz, faixa de brilho, alarmes do sensor	Mensagem pode ficar pouco visível ou excessivamente brilhante
Falha de energia, bateria ou fonte	Tensão, fonte ativa, estado da bateria, reinicializações e alarmes de alimentação	Perda total ou intermitente do painel
Temperatura, umidade ou ventilação inadequadas	Temperatura e umidade do gabinete, estado de ventiladores, filtros e termostatos	Redução da confiabilidade e falha de componentes eletrônicos
Porta do gabinete aberta ou falha do controlador	Estado de portas, falhas de software/controlador, alarmes de acesso	Risco de indisponibilidade, manutenção não autorizada ou alteração indevida


Informações que vale reunir no CMA: ID do painel, localização, mensagem solicitada, mensagem confirmada/exibida, horário de envio e confirmação, estado do controlador, disponibilidade, falhas de pixels, resultado dos testes de linhas/colunas, sensor de luminosidade, tensão, bateria, temperatura/umidade do gabinete, comunicação, alarmes e ordens de serviço.

A FHWA documenta diagnósticos remotos para painéis, incluindo falhas de fonte de energia, pixels, sensores de luz, controlador, sensores de temperatura e umidade, ventiladores/aquecedores e erros de dispositivos externos. Também descreve testes de linhas/colunas, todos os pixels ligados/desligados e caracteres alfanuméricos. No Brasil, a Resolução ANTT nº 6.000/2022 descreve o PMV como meio de orientação sobre emergências, incidentes e informações do trajeto, programado pelo CCO com apoio de fontes operacionais. A aplicação dessa regra depende do contrato de concessão e do enquadramento da rodovia.

2.1.3 SCA — Sistema Ambiental / estações meteorológicas
Para que serve na rodovia
- No material do Challenge, o SCA é apresentado como um sistema ambiental composto por estações meteorológicas automatizadas que alertam o CCO sobre mudanças bruscas no clima.
- Para o CMA, o SCA será tratado como ativo que mede condições ambientais relevantes para a operação rodoviária.
- A regulamentação da ANTT menciona, para o sensoriamento meteorológico rodoviário quando aplicável, parâmetros como temperatura, precipitação, umidade e visibilidade. A FHWA descreve sistemas RWIS/ESS que podem reunir sensores atmosféricos, de pavimento e de nível de água.
O que pode dar errado e como perceber
Falha ou degradação	Dados/sinais que podem identificar o problema	Consequência operacional possível
Sensor com leitura travada, ausente ou fora de faixa	Última leitura, frequência de atualização, valores nulos, faixa plausível, comparação com estação próxima e código de erro	O CCO pode receber uma visão incompleta ou incorreta das condições locais
Descalibração ou deriva do sensor	Data da última calibração, diferença em relação a referência, desvios persistentes e histórico de aferição	Alertas podem ser emitidos tarde demais ou sem necessidade
Falha de comunicação/telemetria	Horário do último pacote, perda de comunicação, latência e estado do modem/rede	Dados deixam de chegar ao CCO, mesmo que o sensor esteja funcionando
Falha de alimentação/bateria	Tensão, estado da fonte, carga da bateria e reinicializações	Estação pode ficar indisponível, especialmente em eventos climáticos
Sensor obstruído ou instalação inadequada	Inspeção física, indicador de qualidade, localização, obstrução e histórico de manutenção	Medições deixam de representar adequadamente o trecho rodoviário


Informações que vale reunir no CMA: ID da estação, localização/coordenadas, parâmetros instalados, temperatura, umidade relativa, precipitação, visibilidade e vento quando houver esses sensores, estado da estação, último contato, frequência de atualização, qualidade/validade de cada leitura, alarmes, data de calibração, inspeções, alimentação, comunicação e ordens de serviço.

Um cuidado com esta pesquisa: o kickoff informa que o SCA usa estações meteorológicas automatizadas, mas não detalha o modelo, a quantidade ou a composição exata de sensores instalados pela Motiva. Os parâmetros citados como temperatura, precipitação, umidade e visibilidade têm respaldo em referência regulatória da ANTT e em guias técnicos da FHWA para estações meteorológicas rodoviárias. Sensores de pavimento, nível de água ou outros parâmetros só devem ser incluídos no cadastro se estiverem efetivamente presentes no ativo.

2.2 Outros equipamentos do contexto
- SAT — Sistema de Análise de Tráfego: o kickoff o descreve como sensores e radares que coletam volume, velocidade e classificação de veículos. É um possível ativo para futura ampliação do CMA.
- Callbox: dispositivo de comunicação de emergência, geolocalizado, que permite contato direto com o Centro de Controle. Também poderá ser incluído posteriormente.

2.3 Manutenção corretiva, preventiva e preditiva
Tipo	Como funciona	Exemplo aplicado aos ativos	Vantagens	Limitações
Corretiva	A equipe atua depois de identificar uma falha ou perda de função.	Trocar uma fonte que queimou, reparar a conexão de uma câmera ou substituir módulos de LED que pararam.	É necessária para restaurar a operação e pode ser adequada para falhas raras de baixo impacto.	Pode causar indisponibilidade não planejada, atendimento emergencial, deslocamento urgente e impacto operacional maior.
Preventiva	A equipe executa tarefas em intervalos programados, independentemente de haver uma falha detectada.	Limpar a lente da câmera, inspecionar gabinete, testar LEDs e verificar a estação meteorológica periodicamente.	Reduz problemas associados à falta de inspeção e permite planejar equipe, peças e janelas de serviço.	Pode gerar intervenções desnecessárias e não garante detectar uma degradação que surge entre duas inspeções.
Preditiva	A decisão de manutenção considera o estado medido do ativo, histórico, alarmes e tendências.	Priorizar uma câmera cuja imagem perde qualidade continuamente, ou uma estação cujo sensor apresenta leituras instáveis e falhas repetidas.	Permite antecipar intervenções, direcionar recursos aos ativos em pior condição e reduzir surpresas operacionais.	Depende de dados confiáveis, histórico, sensores/diagnósticos, critérios bem calibrados e validação técnica.


O CMA não pretende acabar com a manutenção corretiva ou preventiva. Ela complementa as duas com análise de condição e priorização. A abordagem é coerente com as orientações do Departamento de Energia dos Estados Unidos, que diferencia manutenção reativa/corretiva, preventiva baseada em tempo e preditiva baseada na condição, e com a ISO 17359, que orienta programas de monitoramento de condição.
2.4 Por que acompanhar os equipamentos continuamente
1. Detectar perda de disponibilidade ou qualidade antes de uma falha completa.
2. Identificar repetição de alarmes e tendências, em vez de analisar cada evento isoladamente.
3. Comparar equipamentos do mesmo tipo e identificar ativos que se afastam do padrão.
4. Direcionar inspeções e peças de reposição conforme condição e criticidade.
5. Manter histórico de leituras, diagnósticos, recomendações e intervenções para revisar os critérios.
3. Frente 2 — Base técnica e organização dos dados

3.1 Campos do cadastro dos ativos
O cadastro é a ficha de cada equipamento. É nele que ficam as informações necessárias para saber de qual ativo estamos falando e como interpretar suas leituras. Para começar, o cadastro deverá reunir estes campos:
Grupo	Campos sugeridos	Por que são necessários
Identificação	ativo_id, tipo, nome, fabricante, modelo, número de série	Distinguir cada equipamento e consultar suas especificações
Localização	rodovia, concessionária/trecho, km, sentido, município, latitude, longitude, referência do ponto	Relacionar a condição do ativo ao local e exibi-lo no mapa
Instalação	data de instalação, data de início de operação, versão de firmware/software	Avaliar idade, ciclo de vida e compatibilidade
Operação	estado atual, última comunicação, disponibilidade, regime de operação	Saber se o equipamento está operante e se os dados são recentes
Manutenção	responsável, última inspeção, última preventiva, próxima preventiva, OS em aberto	Verificar histórico e pendências
Criticidade	segurança, impacto operacional, redundância/alternativa, classe final de criticidade	Estimar a consequência da indisponibilidade
Configuração	parâmetros monitorados, unidade, limites de referência, periodicidade de leitura	Interpretar corretamente as medições


3.2 Histórico e registros relacionados
Não vamos colocar todas as leituras e ocorrências dentro do cadastro principal. Isso deixaria a consulta confusa e dificultaria acompanhar a evolução do equipamento. A ideia é separar os registros por tipo e relacioná-los pelo ativo_id:
Conjunto	Campos principais
ativos	ID, tipo, rodovia, km, coordenadas, fabricante/modelo, instalação, criticidade, estado
leituras	ID da leitura, ativo_id, data/hora, parâmetro, valor, unidade, origem, qualidade, limite aplicado
alarmes	ID do evento, ativo_id, código, descrição, severidade, início, fim, confirmação e situação
ordens_servico	ID da OS, ativo_id, tipo de manutenção, abertura, execução, causa, serviço, peças, responsável, status
analises_saude	ativo_id, data/hora, versão da fórmula, notas D/P/A/T/M, IH, classificação e justificativa
recomendacoes	ativo_id, data/hora, PF, criticidade, prioridade, regra acionada, ação sugerida, responsável, prazo e status


Cada leitura precisa trazer data e hora, unidade e origem. Uma leitura sem timestamp ou sem unidade pode ser interpretada incorretamente. O sistema também deve registrar quando um dado foi descartado, corrigido ou marcado como suspeito, sem apagar a evidência original.

3.3 Estrutura de dados proposta
Modelo inicial em Python:
- Uma lista de dicionários representa os ativos ou as leituras simuladas.
- Cada dicionário contém pares chave: valor, por exemplo ativo_id, tipo, km e estado.
- O ativo_id funciona como chave de ligação entre cadastro, leituras, alarmes e ordens de serviço.
- Para uma primeira demonstração, os registros podem ser lidos de arquivos CSV.
Exemplo simplificado:
ativos = [
    {"ativo_id": "CFTV-001", "tipo": "CFTV", "km": 45.2,
     "estado": "operacional", "criticidade": 4},
    {"ativo_id": "PMV-014", "tipo": "PMV", "km": 51.8,
     "estado": "operacional", "criticidade": 5},
    {"ativo_id": "SCA-003", "tipo": "SCA", "km": 63.1,
     "estado": "instavel", "criticidade": 4}
]

leituras = [
    {"ativo_id": "CFTV-001", "data_hora": "2026-11-01 10:00",
     "parametro": "disponibilidade", "valor": 98, "unidade": "%"},
    {"ativo_id": "PMV-014", "data_hora": "2026-11-01 10:00",
     "parametro": "disponibilidade", "valor": 94, "unidade": "%"}
]
Evolução para banco de dados: quando a quantidade de registros aumentar, a equipe poderá usar SQLite, com tabelas separadas para ativos, leituras, alarmes, ordens de serviço, análises e recomendações. A chave ativo_id relaciona os registros. Isso evita duplicar dados cadastrais em cada leitura e facilita recuperar o histórico de um equipamento.

3.4 Como consultar e ordenar os registros
Busca por identificação: percorrer uma lista até encontrar o ativo_id desejado. É simples para poucos registros, mas exige examinar os itens até localizar o ativo.

Busca por critérios: percorrer os ativos e selecionar os que estejam em condição crítica, tenham alarmes ativos, estejam sem comunicação ou pertençam a determinado tipo/trecho.

Busca por chave: manter um dicionário indexado pelo ativo_id permite recuperar diretamente o registro associado àquela chave. É adequado para consultas repetidas por identificação.

Ordenação: usar sorted() para criar uma lista ordenada ou .sort() para ordenar a própria lista. Exemplos de ordenação:
- Menor índice de saúde primeiro: localizar os ativos em pior condição.
- Maior prioridade primeiro: apresentar primeiro o ativo que deve receber atendimento.
- Data/hora crescente: reconstruir a evolução das leituras e dos alarmes.
- Criticidade decrescente: visualizar primeiro os ativos com maior consequência operacional.
Exemplo:
ativos_por_saude = sorted(ativos, key=lambda ativo: ativo["indice_saude"])
A documentação oficial do Python explica listas, dicionários, sorted() e list.sort(). Para a Sprint 2, a equipe começará com uma lista de dicionários e poderá migrar o armazenamento para SQLite sem alterar a lógica das regras.

3.5 Como a programação entra no CMA
Recurso	Uso no CMA	Exemplo de aplicação
if / elif / else	Classificar e decidir a ação	Se IH for menor que 60, classificar como crítico; se for menor que 80, atenção; caso contrário, normal
for	Percorrer todos os ativos, leituras e alarmes	Calcular o IH de cada ativo e montar a fila de prioridades
while	Repetir uma rotina enquanto o monitoramento estiver ativo	Em uma versão conectada, consultar periodicamente a fonte de dados enquanto o serviço estiver ligado
def	Separar tarefas em funções reutilizáveis	calcular_indice(), classificar_ativo(), calcular_prioridade() e gerar_recomendacao()


Ao deixar cada tarefa em uma função, evitamos copiar o mesmo cálculo em vários lugares. A rotina principal percorre os ativos, chama as funções necessárias, guarda os resultados e atualiza as informações que aparecem no painel.

4. Índice de Saúde do Ativo (0 a 100)

4.1 Objetivo e interpretação
O Índice de Saúde (IH) reúne diferentes sinais do equipamento em uma nota de 0 a 100. Uma nota mais alta indica uma condição melhor segundo os critérios escolhidos. Não estamos dizendo que um ativo com IH 80 tem 80% de chance de continuar funcionando: o índice é uma pontuação de condição, não uma probabilidade de falha. Ele serve para comparar os ativos e apoiar o diagnóstico.

4.2 Variáveis propostas
Todas as variáveis são convertidas para a escala de 0 a 100, em que 100 representa a melhor condição.
Variável	Peso	Como calcular	Justificativa
D — Disponibilidade	30%	Percentual de tempo em que o equipamento esteve disponível no período	A indisponibilidade afeta diretamente o serviço que o ativo presta
P — Desempenho técnico	25%	Nota de 0 a 100 obtida em testes próprios para cada tipo de equipamento	Verifica se o ativo ainda executa sua função com qualidade; os testes podem variar por tipo, mas a nota é normalizada
A — Condição dos alarmes	20%	max(0, 100 - 10B - 20Med - 40Alta), sendo B/Med/Alta a quantidade de alarmes validados de baixa/média/alta severidade no período	Considera a recorrência e a severidade, sem deixar que um alarme isolado decida tudo
T — Tendência	15%	max(0, 100 - 10 × ΔP30), em que ΔP30 = max(0, P anterior − P atual), isto é, a queda positiva, em pontos, do desempenho técnico nos últimos 30 dias	Dá peso à degradação progressiva, característica importante da manutenção preditiva
M — Histórico de manutenção	10%	Nota pela regularidade das inspeções e preventivas e pela existência de pendências/reincidências	Considera se há tarefas vencidas ou problemas recorrentes; tem peso menor porque manutenção registrada não prova, sozinha, a condição real


Faixas sugeridas para M: 100 = preventivas em dia e sem pendência relevante; 80 = uma preventiva não crítica vencida; 50 = pendência vencida associada a reincidência; 0 = ordem crítica de reparo vencida ou falha grave sem tratamento. A aplicação deve guardar a regra que gerou a nota.

Fórmula proposta:
IH = 0,30D + 0,25P + 0,20A + 0,15T + 0,10M

4.3 Por que escolhemos esses pesos
- Disponibilidade recebe o maior peso porque indica por quanto tempo o equipamento conseguiu prestar o serviço.
- Desempenho técnico também recebe peso elevado para não considerar saudável um equipamento que permanece conectado, mas executa mal sua função.
- Alarmes recebem 20%, pois são sinais importantes, mas precisam ser validados e interpretados pelo contexto.
- Tendência recebe 15% para que uma piora contínua seja percebida mesmo antes de uma indisponibilidade completa.
- Histórico de manutenção recebe 10% porque ajuda a contextualizar o ativo, mas pode estar incompleto ou atrasado.
Escolhemos esses pesos para começar com um modelo simples de explicar e de conferir manualmente. Não foram estimados a partir de uma base histórica real da Motiva. Antes de uso operacional, devem ser calibrados com falhas confirmadas, dados históricos, especificações dos fabricantes e avaliação dos profissionais de manutenção.

4.4 Regras de classificação
Condição	Regra pelo IH	Interpretação	Ação inicial
Normal	80 a 100	Condição satisfatória pelos indicadores disponíveis	Manter monitoramento e rotina preventiva
Atenção	60 a 79,99	Há perda de desempenho, recorrência de alarmes ou tendência de piora	Verificar os sinais e programar inspeção
Crítico	0 a 59,99	Conjunto de indicadores aponta condição ruim	Avaliação prioritária e intervenção conforme risco
Sem dados	Dados ausentes, vencidos ou inválidos	Não é possível afirmar que o ativo está saudável	Verificar comunicação/sensor e buscar fonte alternativa


Regras de segurança adicionais: (1) ativo confirmado como indisponível recebe classificação crítica, independentemente do IH calculado; (2) alarme de alta severidade confirmado, com efeito operacional relevante, pode elevar a classificação; (3) dados atrasados ou sem qualidade suficiente recebem o estado “sem dados”, não “normal”. Essas regras evitam que a média esconda uma falha importante ou que a ausência de telemetria seja interpretada como bom funcionamento.
5. Frente 3 — Arquitetura e inteligência de decisão
5.1 Como organizamos a arquitetura
Organizamos a arquitetura a partir das cinco camadas mostradas no kickoff da Motiva: Aquisição, Tratamento, Modelagem, Diagnóstico e Decisão. O repositório central, os controles de qualidade, o painel e a validação humana dão suporte ao fluxo.

[Diagrama em formato Graphviz](docs/arquitetura_CMA.dot)
1. Aquisição: recebe dados de sensores, telemetria, sistemas supervisórios/SCADA, alarmes, cadastro dos ativos, inspeções e ordens de serviço. No protótipo, também recebe arquivos CSV e dados simulados. Cada registro deve chegar com ativo_id, data/hora, parâmetro, valor, unidade e origem.
2. Tratamento: valida o identificador, os campos, as unidades e os timestamps; identifica ausências, duplicidades, dados atrasados e valores suspeitos; registra a qualidade e a origem da informação. Dados ausentes não serão tratados como zero nem como condição normal.
3. Modelagem: calcula disponibilidade, desempenho técnico, score de alarmes, tendência e Índice de Saúde (0–100). Também pode manter uma representação digital simplificada do estado do ativo e, em etapas futuras, incorporar modelos de séries temporais, degradação e aprendizado de máquina. Esses recursos aparecem como possibilidades no kickoff, mas não são necessários para a primeira versão funcional.
4. Diagnóstico: classifica os ativos como normal, atenção, crítico ou sem dados; identifica anomalias e sinais de degradação; estima uma faixa ordinal de propensão à falha; registra quais indicadores e regras justificaram o diagnóstico.
5. Decisão: combina condição, propensão à falha e criticidade; calcula o índice de prioridade; gera uma recomendação e sua justificativa; registra data, versão da regra e responsável pela validação.
Repositório central / histórico: componente de suporte às cinco camadas. Guarda cadastro de ativos, leituras brutas e tratadas, alarmes, inspeções, ordens de serviço, análises de saúde, recomendações e decisões. O ativo_id relaciona os registros. Para a Sprint 2, a proposta é iniciar com CSV e evoluir para SQLite.

Controles transversais: identificador único, data/hora, origem, unidade, qualidade, permissões de acesso, logs, tratamento de erros e versionamento das fórmulas e regras.

Validação humana: o painel apresenta recomendações para o CCO e a manutenção. O CMA não executa a intervenção. A equipe responsável avalia a recomendação, define quem ficará encarregado e em que prazo, e depois registra o que foi feito.

O fluxo detalhado, responsabilidades, dados de entrada e saída e tratamento de exceções estão em [`docs/arquitetura_e_painel_operacional.md`](docs/arquitetura_e_painel_operacional.md).

5.2 Critérios de criticidade operacional
A criticidade representa a consequência de uma falha, não a probabilidade de ela ocorrer. Neste projeto, vamos avaliar três dimensões, cada uma de 1 a 5:
- S — Segurança: quanto a indisponibilidade pode afetar a segurança viária, a detecção de incidentes ou a informação necessária ao usuário.
- O — Operação: quanto a falha pode interromper ou degradar a continuidade do serviço e a capacidade de resposta do CCO.
- R — Redundância: facilidade de substituir a função do ativo por outro equipamento ou procedimento. Nota 5 significa que não existe alternativa funcional adequada; nota 1 significa que há redundância suficiente.
Fórmula de criticidade proposta:
C = 0,50S + 0,30O + 0,20R
Converter o resultado para a classe inteira mais próxima, usando as faixas: 1,00–1,80 = C1; 1,81–2,60 = C2; 2,61–3,40 = C3; 3,41–4,20 = C4; 4,21–5,00 = C5.
Classe	Significado	Exemplo de interpretação
C1	Muito baixa	Falha localizada, sem impacto relevante e com alternativa
C2	Baixa	Impacto limitado, com alternativa operacional
C3	Média	Degradação perceptível do serviço ou cobertura local
C4	Alta	Ativo importante para segurança ou resposta em trecho relevante, com pouca redundância
C5	Muito alta	Falha pode comprometer informação essencial/serviço crítico e não há alternativa adequada


A nota precisa levar em conta onde o equipamento está instalado e qual função ele exerce naquele trecho. Duas câmeras do mesmo modelo, por exemplo, podem ter criticidades diferentes se uma delas cobrir um ponto mais sensível e não houver outra câmera na região.

5.3 Estimativa da probabilidade de falha
Como não há histórico real suficiente para estimar uma probabilidade estatística, o protótipo utilizará uma escala ordinal de probabilidade/propensão, de 1 a 5. Ela não será apresentada como porcentagem.
Nota PF	Interpretação	Regra inicial baseada no IH
1	Muito baixa	IH ≥ 90
2	Baixa	80 ≤ IH < 90
3	Moderada	70 ≤ IH < 80
4	Alta	60 ≤ IH < 70
5	Muito alta	IH < 60


A regra pode ser elevada por evidências confirmadas: falha total, alarme crítico ativo, leituras inválidas persistentes ou degradação acelerada. A regra acionada deve ser registrada no histórico para que o operador entenda por que a nota mudou.

5.4 Regra de priorização
Para montar a fila de atendimento, a equipe propõe combinar probabilidade e criticidade:
IP = PF × C
O Índice de Prioridade (IP) varia de 1 a 25. É importante não confundir os indicadores: o IH mostra a condição atual do equipamento; PF representa a propensão estimada à falha; C expressa o impacto de uma eventual falha. O IP combina PF e C para ajudar a ordenar os atendimentos.
IP	Prioridade	Ação recomendada
1–4	Baixa	Manter monitoramento e preventiva planejada
5–9	Média	Abrir/verificar solicitação e programar inspeção; prazo sugerido de até 7 dias
10–16	Alta	Programar inspeção/intervenção em curto prazo; prazo sugerido de até 48 horas, sujeito à avaliação do CCO
17–25	Crítica	Acionar avaliação prioritária/plantão, aplicar contingência operacional e registrar decisão


Os prazos são metas ilustrativas da proposta acadêmica, não SLA oficial da Motiva. Em uma aplicação real, os prazos devem ser definidos pelos procedimentos de segurança, contratos, equipes e responsáveis pela operação.

5.5 Exemplos de recomendações
- CFTV normal, prioridade baixa: manter monitoramento. Como houve um alarme de baixa severidade, conferir a estabilidade do vídeo e incluir limpeza da lente e teste PTZ na rotina seguinte.
- PMV em atenção, prioridade alta: solicitar inspeção de matriz LED, executar teste de linhas/colunas, conferir sensor de luminosidade, controlador, comunicação e tensão. Confirmar no CCO se a mensagem exibida está correta e legível. Programar correção em curto prazo.
- SCA crítico, prioridade crítica: acionar equipe para verificar alimentação, comunicação e sensores; validar calibração e qualidade das leituras; comparar com uma fonte meteorológica alternativa; informar o CCO de que a estação está com dados não confiáveis até a validação. A recomendação não deve inventar uma condição climática — deve comunicar a incerteza do dado.
5.6 Como será o painel operacional
O painel não foi pensado apenas para mostrar números. Ele precisa ajudar o operador a responder três perguntas: o equipamento está piorando? Como ele se compara aos demais? Onde está localizado? Por isso, mantivemos as três visões pedidas no kickoff da Motiva: (1) gráfico de tendência com alertas por ativo; (2) comparação do índice de saúde; e (3) mapa georreferenciado com destaque dos ativos críticos. Também incluímos um resumo da situação geral e uma fila de atendimento.

A imagem é apenas um rascunho da interface que propomos; não se trata de um sistema utilizado pela Motiva. Os ativos, valores e séries temporais são simulados. O mapa é esquemático por quilômetro; para georreferenciamento real, o cadastro precisará conter latitude e longitude verificadas.

Filtros gerais: período, tipo de ativo, rodovia/concessionária/trecho, situação, estado de comunicação e busca por ID ou localização. Os filtros devem atualizar cards, gráfico, comparação, mapa e fila com o mesmo recorte.

Indicadores de resumo: total de ativos, quantidade crítica, quantidade em atenção, ativos sem dados/desatualizados e recomendações abertas. A situação Sem dados deve aparecer separadamente e nunca ser interpretada como normal.

Visão 1 — tendência e alertas por ativo:
- gráfico de linha do IH ao longo do período;
- faixas de referência em 80 e 60, conforme o modelo acadêmico atual;
- marcadores de alarmes, indisponibilidades, inspeções e ordens de serviço;
- indicação da última leitura e da qualidade dos dados;
- opção de abrir os componentes do IH (D, P, A, T e M).
Quando faltarem leituras, o gráfico deverá mostrar a lacuna ou sinalizar o intervalo sem dados. Não deverá criar continuidade fictícia entre medições separadas por falha de coleta.

Visão 2 — comparação do índice de saúde:
- barras horizontais ordenadas inicialmente do menor IH para o maior;
- valor numérico e classificação escrita ao lado da barra;
- filtros por tipo, rodovia e trecho;
- acesso à ficha detalhada do ativo.
O gráfico de IH mostra quais equipamentos estão em pior condição. Já a fila usa o IP, que também considera propensão à falha e criticidade. Por isso, o ativo com o menor índice de saúde nem sempre será o primeiro a receber atendimento.

Visão 3 — mapa georreferenciado:
- marcadores a partir de latitude e longitude verificadas;
- identificação por ID, tipo, rodovia, km e sentido;
- destaque de ativos críticos, sem comunicação e com recomendações abertas;
- filtros por tipo e situação;
- seleção de um marcador para abrir o resumo e a ficha do ativo.
O conjunto simulado atual não possui coordenadas reais. Até que elas sejam incluídas no cadastro, o mapa de demonstração será identificado como esquemático, sem sugerir que os pontos representam locais reais.

Fila de prioridade e recomendações: tabela ordenada por IP decrescente, contendo posição, ID/tipo, localização, IH, PF, criticidade, IP, ação sugerida, responsável, prazo e estado da recomendação. Ao abrir uma linha, o operador deve visualizar os indicadores, alarmes e regras que justificaram a recomendação.

Ficha detalhada do ativo: cadastro, localização, estado de comunicação, última leitura, indicadores, IH, histórico de alarmes, inspeções, ordens de serviço, classificação, PF, criticidade, IP, recomendação atual e decisões anteriores.
5.7 Como o operador usará o painel
1. O operador abre o painel e verifica os indicadores gerais e os ativos críticos.
2. Aplica filtros para selecionar um tipo de equipamento, trecho ou período.
3. Observa a tendência do IH e os eventos associados.
4. Compara a condição do ativo com os demais equipamentos.
5. Localiza o ativo no mapa e abre sua ficha.
6. Consulta a justificativa da prioridade e da recomendação.
7. O CCO ou a equipe de manutenção pode aceitar, ajustar ou rejeitar a recomendação. Em qualquer caso, o motivo da decisão fica registrado.
8. Após a intervenção, a equipe registra a causa confirmada, o serviço executado e o resultado.

5.8 Regras de apresentação e rastreabilidade
- Sempre exibir valor numérico e texto junto da cor de situação.
- Mostrar a data/hora e a origem dos dados utilizados.
- Separar alarmes recebidos de recomendações calculadas pelo CMA.
- Identificar dados ausentes, suspeitos e atrasados.
- Mostrar a versão da fórmula e da regra de classificação.
- Registrar quem validou a recomendação, quando e com qual justificativa.
- Não permitir que uma recomendação pendente seja apresentada como ordem de serviço executada.

5.9 Ferramentas previstas para o protótipo
Componente	Tecnologia	Uso previsto
Regras e cálculos	Python	Validação, IH, classificação, criticidade e recomendação
Base inicial	CSV	Importação e testes com dados simulados
Persistência	SQLite	Histórico de ativos, leituras, alarmes, análises e recomendações
Interface	Streamlit	Construção do painel usando Python
Gráficos	Plotly	Tendências e comparação interativa do IH
Mapa	Folium/Leaflet	Marcadores geográficos a partir das coordenadas


5.10 Critérios de aceitação do painel na Sprint 2
Vamos considerar o primeiro painel pronto quando:
- os filtros atualizarem os indicadores, gráficos, mapa e tabela ao mesmo tempo;
- o gráfico mostrar a evolução do IH e deixar claros os períodos sem leitura;
- a comparação exibir o índice e o nome da classificação;
- o mapa permitir abrir a ficha do ativo quando houver coordenadas válidas;
- a fila aparecer ordenada pelo IP, do maior para o menor;
- cada recomendação vier acompanhada de uma justificativa;
- os ativos sem dados aparecerem separados dos ativos normais;
- o operador conseguir registrar a validação e o resultado da manutenção;
- cada análise puder ser ligada ao ativo, ao período e à versão das regras utilizadas.
A descrição ampliada da arquitetura e da interface está em [`docs/arquitetura_e_painel_operacional.md`](docs/arquitetura_e_painel_operacional.md).

6. Teste do modelo com três ativos simulados
Sobre os exemplos: os três registros abaixo são fictícios. Criamos esses valores para testar as fórmulas e mostrar como o CMA reagiria a equipamentos em condições diferentes. Eles não são medições reais nem dados internos da Motiva.

6.1 Dados de entrada
Ativo	Tipo	Disponibilidade D	Desempenho P	Alarmes validados em 30 dias	Score A	Queda de P em 30 dias	Score T	Manutenção M
CFTV-001	CFTV	98%	92	1 baixa	90	1 ponto	90	100
PMV-014	PMV	94%	72	2 médias	60	3 pontos	70	80
SCA-003	SCA	70%	55	1 alta + 1 média	40	6,5 pontos	35	50


Para ler a tabela: D é a disponibilidade nos últimos 30 dias; P é a nota do teste técnico próprio de cada equipamento; A considera a quantidade e a severidade dos alarmes; T representa a queda do desempenho no período; e M resume a situação das inspeções e manutenções registradas.

6.2 Cálculos do Índice de Saúde
CFTV-001
IH = 0,30(98) + 0,25(92) + 0,20(90) + 0,15(90) + 0,10(100)
IH = 29,40 + 23,00 + 18,00 + 13,50 + 10,00
IH = 93,90
Resultado: 93,9 — Normal.

PMV-014
IH = 0,30(94) + 0,25(72) + 0,20(60) + 0,15(70) + 0,10(80)
IH = 28,20 + 18,00 + 12,00 + 10,50 + 8,00
IH = 76,70
Resultado: 76,7 — Atenção.

SCA-003
IH = 0,30(70) + 0,25(55) + 0,20(40) + 0,15(35) + 0,10(50)
IH = 21,00 + 13,75 + 8,00 + 5,25 + 5,00
IH = 53,00
Resultado: 53,0 — Crítico.

6.3 Criticidade, probabilidade e prioridade
Ativo	Segurança S	Operação O	Sem redundância R	Cálculo de C	C	PF pelo IH	IP = PF × C	Prioridade
CFTV-001	4	3	4	0,50(4)+0,30(3)+0,20(4)=3,70	4	1	4	Baixa
PMV-014	5	4	5	0,50(5)+0,30(4)+0,20(5)=4,70	5	3	15	Alta
SCA-003	4	4	4	0,50(4)+0,30(4)+0,20(4)=4,00	4	5	20	Crítica


O resultado ajuda a mostrar por que a fila não é montada apenas pelo índice de saúde. O CFTV-001 tem criticidade alta por causa do local onde foi simulado, mas está em boa condição e apresenta baixa propensão à falha. O PMV-014 perdeu desempenho e tem criticidade muito alta, então precisa de inspeção em curto prazo. Já o SCA-003 aparece primeiro porque reúne baixa disponibilidade, piora no desempenho e problemas recorrentes.

6.4 Recomendações geradas
Ativo	Diagnóstico	Recomendação
CFTV-001	Normal; IP 4 (baixo)	Continuar monitorando. Conferir o alarme de baixa severidade e manter limpeza da lente e teste PTZ na rotina preventiva.
PMV-014	Atenção; IP 15 (alto)	Abrir inspeção de curto prazo. Testar matriz LED, linhas/colunas, sensor de luz, controlador, comunicação, tensão e confirmação da mensagem no CCO.
SCA-003	Crítico; IP 20 (crítico)	Acionar equipe prioritariamente. Conferir energia e comunicação, avaliar sensores e calibração, validar qualidade das leituras com uma fonte alternativa e sinalizar ao CCO que os dados locais estão não confiáveis até a correção.


7. Como vamos cuidar da qualidade e do histórico dos dados
Para que seja possível conferir uma análise depois, o sistema precisa guardar: ativo, horário de processamento, dados utilizados, valores dos componentes D/P/A/T/M, pesos e versão da fórmula, IH final, classe, criticidade, PF, IP, recomendação, regra acionada e responsável pela validação.

Antes do cálculo, o CMA deve:
1. Validar se o ativo existe no cadastro e se o parâmetro pertence àquele tipo de equipamento.
2. Verificar timestamp, unidade e intervalo plausível.
3. Identificar duplicidades e leituras repetidas.
4. Sinalizar valores ausentes, fora de faixa ou antigos.
5. Preservar o dado original e guardar a razão de qualquer descarte ou correção.
6. Não atribuir IH normal quando não há informação confiável suficiente.
Essa abordagem é compatível com a finalidade da ISO 13374, que trata do processamento, comunicação e apresentação de informações de monitoramento e diagnóstico, e com a ISO 17359, que orienta programas de monitoramento de condição.
8. Uso da programação e da Inteligência Artificial
Análise computacional: será responsável por percorrer os registros, validar os dados, calcular os indicadores, classificar os ativos e montar a fila de prioridades. No início, vamos usar regras fixas e fáceis de conferir. Assim, quando o CMA recomendar uma inspeção, será possível mostrar exatamente quais condições acionaram essa recomendação.

Inteligência Artificial: pode ser útil mais adiante para procurar padrões que não sejam tão fáceis de perceber por regras simples, analisar imagens ou estudar tendências. Mas não faz sentido começar por um modelo de IA sem ter dados confiáveis e históricos suficientes. Nesta primeira versão, as regras serão explícitas e a decisão de intervir continuará com os profissionais responsáveis. Se um modelo de IA for acrescentado, seus resultados precisarão ser comparados com diagnósticos confirmados.

Regressão linear: não foi a opção de aprofundamento escolhida para a Frente 3. Mesmo assim, podemos testar esse recurso na Sprint 2 para observar a tendência de um indicador, desde que tenhamos uma sequência de dados suficiente. Com apenas dois ou três registros, a linha calculada seria uma demonstração, não uma previsão confiável.
9. O que pretendemos desenvolver na Sprint 2
Na Sprint 2, a ideia é transformar esta proposta em um protótipo que funcione com dados simulados. Não vamos tentar integrar todos os equipamentos reais logo de início; primeiro precisamos validar os cálculos e a lógica do CMA.
9.1 Funcionalidades previstas
1. Cadastro de ativos CFTV, PMV e SCA.
2. Importação de dados simulados por CSV.
3. Validação de campos, unidades, timestamps, duplicidades e dados antigos.
4. Cálculo automático de D, P, A, T, M e IH.
5. Classificação em Normal, Atenção, Crítico ou Sem dados.
6. Cálculo de criticidade, PF e IP.
7. Geração de recomendações com justificativa e regra acionada.
8. Histórico das análises e recomendações.
9. Painel com gráfico de tendência, comparação dos índices e mapa.
9.2 Sequência de implementação
Etapa	Entrega	Critério de conclusão
1. Preparar projeto	Repositório, pastas, ambiente Python e README atualizado	Projeto executa localmente e tem instruções claras
2. Criar dados simulados	CSV com cadastro, leituras, alarmes e manutenção de pelo menos três ativos	Dados têm timestamps, unidades e situações normal/atenção/crítica
3. Implementar leitura e validação	Importador e verificações de qualidade	Dados inválidos ou antigos são sinalizados, não tratados como normais
4. Implementar indicadores	Funções para D, P, A, T, M e IH	Cálculos batem com os exemplos documentados
5. Implementar diagnóstico	Regras de classificação e exceções	Testes de limites e de falha total passam
6. Implementar priorização	Cálculo de S/O/R, C, PF e IP	Fila fica ordenada por prioridade e mostra justificativa
7. Guardar histórico	Persistência inicial em CSV ou SQLite	Análises anteriores podem ser consultadas
8. Criar painel	Três visualizações exigidas no kickoff	Tendência, comparação e mapa aparecem com filtros
9. Testar e revisar	Casos de teste, correções e demonstração	Resultados reproduzíveis e conhecidos pela equipe


9.3 Tecnologias sugeridas
- Python 3: regras, processamento e cálculos. É a tecnologia principal da implementação.
- CSV: formato inicial para os dados simulados e fácil conferência manual.
- SQLite: armazenamento local de cadastro, leituras, alarmes, análises e recomendações, caso a equipe avance além dos arquivos CSV.
- Streamlit: construção de um painel web simples com Python.
- Plotly: gráficos interativos de tendência e comparação.
- Mapa: componente de mapa do Streamlit ou biblioteca de mapas compatível, usando coordenadas fictícias claramente identificadas.
- Git/GitHub: versionamento do código, documentação, diagramas e dados de demonstração.
Vamos começar pela versão mais simples e acrescentar recursos só depois que o fluxo principal estiver funcionando. Se houver pouco tempo, Python + CSV + Streamlit são suficientes para demonstrar a lógica antes de adicionar banco de dados e integrações.
9.4 Testes mínimos da Sprint 2
- IH exatamente em 60 e 80, para verificar as fronteiras de classificação.
- IH abaixo de 60 e acima de 90.
- Ativo indisponível mesmo que os demais indicadores ainda estejam altos.
- Alarme crítico confirmado.
- Dados atrasados ou sem timestamp.
- Leituras duplicadas e fora de faixa.
- Ativo sem histórico de manutenção.
- Ativo com criticidade alta e boa saúde, para confirmar que não é automaticamente crítico.
- Dois ativos com a mesma prioridade, para conferir o critério de desempate (por exemplo, menor IH e depois maior tempo de indisponibilidade).
- Conferência manual dos três cálculos simulados desta Sprint.
9.5 Resultado esperado
Ao final da Sprint 2, queremos ter um protótipo que carregue os três ativos simulados, calcule seus indicadores, mostre a classificação de cada um e monte uma fila de atendimento. O operador também deverá conseguir consultar o motivo de cada recomendação e visualizar as três partes principais do painel.
10. Referências
1. FIAP; MOTIVA. Apresentação Kickoff Motiva — Challenge 2026.2, Ciência da Computação. Material fornecido à equipe, especialmente slides 7 e 11–16 (equipamentos, Tema 1, problema, objetivos, camadas do CMA e painel).
2. AGÊNCIA NACIONAL DE TRANSPORTES TERRESTRES (ANTT). Resolução nº 6.000, de 1º de dezembro de 2022. Regulamento das Concessões Rodoviárias. Consultar a versão consolidada e as alterações aplicáveis ao contrato da concessão. Disponível em: https://anttlegis.antt.gov.br/action/TematicaAction.php?acao=abrirVinculos&cod_menu=7220&cod_modulo=392&cotematica=20632069
3. ANTT. Estrutura Física do Centro Nacional de Supervisão Operacional (CNSO). Monitoramento em tempo real, imagens de CFTV e acompanhamento de indicadores. Disponível em: https://www.gov.br/antt/pt-br/assuntos/centro-nacional-de-supervisao-operacional-cnso/estrutura-fisica-cnso
4. FEDERAL HIGHWAY ADMINISTRATION (FHWA). TMC/EOC/FC Handbook — 3.1 Transportation-Related Information Managed/Used by TMCs. Uso de imagens de câmeras para confirmar situações e apoiar a resposta a incidentes. Disponível em: https://ops-dr.fhwa.dot.gov/publications/fhwahop09003/tmc3_1.htm
5. FHWA. Guidelines for Transportation Management Systems Maintenance Concept and Plans — Appendix B: Maintenance Procedures for ITS Devices. Procedimentos de manutenção de CFTV e PMV. Disponível em: https://ops.fhwa.dot.gov/docs/TMSMaintCptandPlans/appendix-b.htm
6. FHWA. Model Systems Engineering Documents for Dynamic Message Sign (DMS) Systems — Appendix B. Requisitos de diagnóstico de pixels, energia, sensores, temperatura, umidade e controladores. Disponível em: https://ops.fhwa.dot.gov/publications/fhwahop18080/appb.htm
7. FHWA. Road Weather Management — Frequently Asked Questions. Descrição de RWIS/ESS e dados atmosféricos, de pavimento e de nível de água. Disponível em: https://ops.fhwa.dot.gov/Weather/faq.htm
8. FHWA. Road Weather Information System — Environmental Sensor Station Siting Guidelines. Informações sobre aquisição, transmissão, processamento e disseminação de dados meteorológicos rodoviários. Disponível em: https://ops.fhwa.dot.gov/publications/ess05/ess0501.htm
9. U.S. DEPARTMENT OF ENERGY. Operations and Maintenance Challenges and Solutions. Diferenças entre manutenção corretiva/reativa, preventiva e preditiva. Disponível em: https://www.energy.gov/cmei/femp/operations-and-maintenance-challenges-and-solutions
10. INTERNATIONAL ORGANIZATION FOR STANDARDIZATION (ISO). ISO 17359:2018 — Condition monitoring and diagnostics of machines — General guidelines. Disponível em: https://www.iso.org/standard/71194.html
11. ISO. ISO 13374-1:2003 — Condition monitoring and diagnostics of machines — Data processing, communication and presentation — Part 1: General guidelines. Disponível em: https://www.iso.org/standard/21832.html
12. ISO. ISO 31000:2018 — Risk management — Guidelines. Disponível em: https://www.iso.org/standard/31000
13. PYTHON SOFTWARE FOUNDATION. Python Tutorial — Data Structures. Listas e dicionários. Disponível em: https://docs.python.org/3/tutorial/datastructures.html
14. PYTHON SOFTWARE FOUNDATION. Sorting Techniques. sorted() e list.sort(). Disponível em: https://docs.python.org/3/howto/sorting.html
15. ARTESP. Registro de Mensagens em Painéis — Portal de Dados Abertos. Base pública com registros de mensagens em PMVs de rodovias estaduais concedidas; pode servir como fonte complementar para experimentos, após verificar o conteúdo e a estrutura dos arquivos. Disponível em: https://dadosabertos.artesp.sp.gov.br/dataset/registro-de-mensagens-em-paineis
16. STREAMLIT. Streamlit documentation. Disponível em: https://docs.streamlit.io/ . Consulta em 24 nov. 2026.
17. PLOTLY. Plotly Python graphing library. Disponível em: https://plotly.com/python/ . Consulta em 24 nov. 2026.
18. FOLIUM. Folium documentation. Disponível em: https://folium.readthedocs.io/en/latest/ . Consulta em 24 nov. 2026.
