🚨 Análise Exploratória de Dados – Acidentes Rodoviários (PRF 2023-2024)
📋 Contexto e Motivação
Os acidentes nas rodovias federais representam um grave problema de segurança pública e saúde.
A Polícia Rodoviária Federal (PRF) atua diretamente na prevenção, fiscalização e resposta a esses eventos.

A análise de dados históricos pode apoiar a PRF a:

Direcionar operações e fiscalizações para pontos e horários críticos;
Identificar causas predominantes de acidentes;
Otimizar recursos humanos e logísticos;
Reduzir fatalidades e custos operacionais;
Diminuir gastos públicos com saúde e resposta a emergências.
🎯 Objetivo do Projeto
Realizar uma Análise Exploratória de Dados (EDA) sobre os registros de acidentes da PRF nos anos de 2023 e 2024, com o objetivo de identificar padrões, tendências e fatores de risco que possam apoiar ações preventivas e de gestão operacional.

🔍 Metodologia (CRISP-DM)
Fase	Descrição
1. Business Understanding	Definição dos objetivos, perguntas de negócio e impacto esperado.
2. Data Understanding	Coleta e exploração inicial dos dados, diagnóstico de qualidade e estrutura.
3. Data Preparation	Limpeza, padronização, tratamento de nulos, criação de novas variáveis.
4. Modeling (opcional)	Aplicação de modelos simples para previsão de padrões ou agrupamentos.
5. Evaluation	Interpretação dos resultados, validação de hipóteses e conclusões.
6. Deployment / Recommendations	Comunicação dos resultados e sugestões práticas para a PRF.
❓ Perguntas de Negócio
#	Pergunta	Por que importa
1	Quais estados e rodovias concentram o maior número de acidentes?	Identifica regiões prioritárias para fiscalização.
2	Quais são os horários e dias da semana com mais acidentes?	Apoia escalas operacionais e campanhas educativas.
3	Os acidentes aumentaram ou diminuíram de 2023 para 2024?	Mede impacto de políticas e operações da PRF.
4	Quais causas presumidas mais contribuem para acidentes fatais?	Direciona campanhas de conscientização.
5	Quais condições meteorológicas estão mais associadas a acidentes?	Permite reforçar alertas em condições climáticas adversas.
6	Quais municípios apresentaram maior crescimento percentual de acidentes?	Identifica áreas emergentes de risco.
7	Qual o perfil temporal dos acidentes por turno (manhã, tarde, noite, madrugada)?	Entende o comportamento do risco ao longo do dia.
8	Existe relação entre número de vítimas e tipo de acidente?	Prioriza ações de prevenção conforme gravidade.
🧮 Dados Utilizados
Fonte: Dados públicos da Polícia Rodoviária Federal (PRF)
Período: 2023 e 2024
Registros: 140.922 linhas
Colunas: 31 variáveis, incluindo informações sobre local, data, tipo, causas e gravidade do acidente.
Arquivo consolidado: dados_prf_consolidados.csv
🧹 Etapas de Preparação de Dados
Durante a fase de Data Preparation, serão realizados:

Remoção e tratamento de valores nulos e inconsistentes;
Padronização de tipos de dados e formatações (datas, coordenadas, UF, BR, etc.);
Criação de variáveis derivadas;
Detecção e tratamento de outliers;
Enriquecimento geográfico (ex: mapas e clusters por rodovia).
🧠 Possíveis Aplicações Práticas para a PRF
Planejamento de operações de fiscalização preventiva;
Identificação de trechos críticos e pontos de engenharia viária;
Campanhas educativas direcionadas conforme causa predominante;
Apoio à alocação de efetivo e viaturas em períodos e locais de maior risco.
📚 Tecnologias Utilizadas
Python (Pandas, NumPy, Matplotlib, Seaborn)
Jupyter Notebook
Git / GitHub para versionamento
(Futuro) Power BI ou Streamlit para dashboard interativo
