# Locadora de Carros Com Agente Virtual
### Objetivo
#### Desenvolver um agente virtual para atender clientes de uma locadora de carros de forma dinâmica.

### Estrutura
#### Base do projeto
Foi desenvolvido um sistema que tem como principal intuito estruturar uma conexão MCP para facilitar a integração com diversos Clients de IA para atender os clientes.

O server MCP é o núcleo do projeto por ser o ponto comum entre todos as integrações que poderão surgir, logo, a lógica de negócios e permissões estariam centralizadas nesse server. Assim, podemos disponibilizar as lógicas de consultas ao banco de dados por meio de Tools para os Clients que desejarmos integrar.

Nesse server MCP podemos definir quais Tools ou funções teriam a necessidade de acesso ao banco de dados, simplesmente utilizando o decorador desenvolvido para indicar essa necessidade. Assim, não exige que o Client seja o responsável por definir o acesso ao banco de dados e utilizá-lo como um dos parâmetros, facilitando assim a alternância de Clients de forma mais fácil de acordo com o mais apto do mercado.

Para o desenvolvimento do server MCP utilizei o framework FastMCP que facilitou a definição de simples funções como Tools.

#### Client Utilizado
Para esse sistema, acredito que seria mais eficaz como Client um sistema web com um chatbot ou "terminal interativo" mais amigável. Porém, como foi solicitado que o sistema fosse desenvolvido para o terminal ou prompt de comando, fiz algumas adaptações no código com a ajuda de uma IA para encaixar com o contexto exigido.

Para o Client utilizei o modelo de IA da OpenAI gpt-4o. Para utilizá-lo mais facilmente visando possível alteração de modelo ou provedor posteriormente, utilizei o LangChain para acessar o modelo e conectar ao server MCP desenvolvido.

### Como Utilizar
Antes de executar o sistema, é necessário fazer algumas configurações.

#### 1. Instalar Dependências
Crie um ambiente virtual python e realize as instalações de dependências utilizando o seguinte comando 'pip' ou qualquer outro gerenciador de pacotes.

'pip install -r requirements.txt'

#### 2. Adicionar Sua API KEY da OpenAI ao Código
Como o sistema desenvolvido tem o intuito de viabilizar experiências de forma mais fácil à outros usuários, mantive fixado o local para adicionar a API KEY da OpenAI. Porém, em situações gerais eu utilizaria e recomendo a utilização de um arquivo .env contendo variáveis de ambientes para ocultar essas informações sensíveis do sistema.

Sendo assim, para acrescentar sua API KEY da OpenAI, acesse a pasta 'client' e o arquivo 'client_setup.py'.

Na linha 54 você encontrará um texto escrito '<<YOUR OPENAI API KEY>>' que é exatamente o que deve ser substituído pela sua API KEY da OpenAI.

#### 3. Iniciar o Sistema
Após essas configurações já é possível iniciar o sistema.

Execute o arquivo 'main.py' com seu ambiente virtual ativo.

Ao executar o arquivo, o banco de dados sqlite será criado e populado com 100 instâncias de carros aleatórios. Caso queira entender mais sobre essa criação aleatória consulte o arquivo 'automotive_model.py' dentro da pasta 'models'.