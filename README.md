<!-- ![image](https://github.com/gcastro-vish/tradepack-calculator/assets/94566922/bcae3b9f-4983-4624-af90-9d788e2600d1) -->
<div align="center"><img src="https://github.com/gcastro-vish/tradepack-calculator/assets/94566922/bcae3b9f-4983-4624-af90-9d788e2600d1" width="600" height="375"></div>
<div align="center"><sub>(Print retirado de <a href="https://ravendawn.online/pt/">Ravendawn</a>)</sub></div>

# Raven Stats
Aplicação utilizando Python e Streamlit 🎈 para fazer calculos de eficiência em Ravendawn.

## Conteúdos

  * [Calculadora de Tradepacks](#calculadora-de-tradepacks)
  * [Pré Requisitos](#pré-requisitos)
  * [Preparação do Ambiente](#preparação-do-ambiente)
  * [Execução do aplicativo](#execução-do-aplicativo)
  * [Execução sem o Python](#execução-sem-o-python)
  * [Como salvar os dados](#como-salvar-os-dados)
  * [Como incluir novos dados](#como-incluir-novos-dados)
  * [Contribuições](#contribuições)

# Pré Requisitos
  - [Instalação do Python](https://www.python.org/downloads/)
  - [Instalação do Git](https://git-scm.com/downloads)

# Preparação do Ambiente
  1. [Clone](https://docs.github.com/pt/repositories/creating-and-managing-repositories/cloning-a-repository) este repositório em uma pasta local
  2. Rode o arquivo `00 config python venv.bat`

# Execução do aplicativo
  1. Rode o arquivo `app.bat`

# Execução sem o Python
  É possível utilizar o aplicativo sem o Python através deste [link](https://tradepack-calculator.streamlit.app/). Note que esta aplicação pode apresentar instabilidades em caso de muitos acessos, por ter sido feita de forma gratuita.

# Como salvar os dados
  Após atualização dos preços e das demandas no próprio aplicativo, utilize o botão de download na lateral esquerda para salvar os dados. Caso queira utilizá-los novamente, basta fazer o upload dos arquivos, também na lateral esquerda, que o aplicativo utilizará os valores dos arquivos. É uma boa prática salvar os dados para evitar re-trabalho de ficar atualizando o preço de itens menos voláteis.

# Como incluir novos dados
  Qualquer dado (composição dos tradepacks, valor dos materiais e demanda dos tradepacks) pode ser atualizado manualmente em caso de atualização do jogo (por exemplo, um novo tradepack). Para isso, basta fazer o download dos dados utilizando os botões do lado esquerdo do aplicativo e adicionar manualmente, via Excel, seguindo o padrão:
  - Composição dos tradepacks (botão "Download Tradepacks"): `tradepacks.xlsx`
    - Coluna A: nome do tradepacks (letras iniciais maiúsculas)
    - Coluna B: composição do tradepacks, com padrão `{'NomeDoMaterial1':QuantidadeDoMaterial1,'NomeDoMaterial2':QuantidadeDoMaterial2,...}` (nomes dos materiais entre aspas simples e com letras iniciais maiúsculas no nome dos materiais)
  - Preço dos materiais (botão "Download Preços"): `precos.xlsx`
    - Coluna A: nome do material (letras iniciais maiúsculas)
    - Coluna B: custo de mercado do material
  - Demanda dos tradepacks (botão "Download Demandas"): `demandas.xlsx`
    - Coluna A: nome do tradepacks (letras iniciais maiúsculas)
    - Coluna B: demanda do tradepack
  
  Em caso de dúvida, estes padrões podem ser vistos nos próprios arquivos, ou me procure no jogo (nick Vish Tankao) ou no discord (vish5067).

# Contribuições
  Toda contribuição é bem-vinda! Para sugerir modificações, crie e um _fork_ deste projeto, crie uma branch da _feature_ e faça as modificações.
  1. Crie um _fork_
  2. Crie a branch da _feature_ (git checkout -b feature/AmazingFeature)
  3. Dê commit nas mudanças (git commit -m 'Add some AmazingFeature')
  4. Faça o push (git push origin feature/AmazingFeature)
  5. Abra um Pull Request

  Mais informações sobre como fazer isso estão disponíveis [aqui](https://docs.github.com/en/get-started/quickstart/contributing-to-projects)
