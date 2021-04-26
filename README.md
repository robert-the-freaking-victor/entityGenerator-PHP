<h1 align="center">
   <img
      alt="Entity Generator"
      title="EntityGenerator"
      src="https://www.php.net//images/logos/new-php-logo.svg"
      width="150px" />
   &nbsp;<div align="center">Entity Generator</div>
</h1>

<h1>Entity Generator</h1>

<p align="left">
   <!-- <a href="https://github.com/robert-the-freaking-victor">
      <img
         alt="author"
         src="https://img.shields.io/badge/author-robert-the-freaking-victor-0081A7?style=flat-square&labelColor=3f3d56"
      />
   </a> -->
   <img
      alt="languages"
      src="https://img.shields.io/github/languages/count/robert-the-freaking-victor/entityGenerator-PHP?color=0081A7&style=flat-square&labelColor=3f3d56"
   />
   <a href="https://github.com/robert-the-freaking-victor/entityGenerator-PHP/stargazers">
      <img
         alt="stars"
         src="https://img.shields.io/github/stars/robert-the-freaking-victor/entityGenerator-PHP?color=0081A7&style=flat-square&labelColor=3f3d56"/>
   </a>
   <a href="https://github.com/robert-the-freaking-victor/entityGenerator-PHP/network/members">
      <img
         alt="forks"
         src="https://img.shields.io/github/forks/robert-the-freaking-victor/entityGenerator-PHP?color=0081A7&style=flat-square&labelColor=3f3d56"/>
   </a>
   <a href="https://github.com/robert-the-freaking-victor/entityGenerator-PHP/graphs/contributors">
      <img
         alt="contributors"
         src="https://img.shields.io/github/contributors/robert-the-freaking-victor/entityGenerator-PHP?color=0081A7&style=flat-square&labelColor=3f3d56"/>
   </a>
  <img alt="License" src="https://img.shields.io/badge/license-MIT-0081A7?style=flat-square&labelColor=3f3d56">
</p>

<p align="center">
   <!-- <a href="#projeto">Projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
   <a href="#features">Features</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
   <a href="#integrations">Integrations</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;--> 
   <a href="#como-usar">Como usar</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href="#configurações">Configurações</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
   <a href="#license">License</a>
</p>

## Como usar

Verifique no diretório /backend/src/Teknisa/FM/Util do seu projeto, se existe uma subpasta, chamada entityGenerator-PHP. Caso essa pasta não exista, clone esse repositório e o insira dentro do diretório Util citado anteriormente.

Com a pasta inserida, abra um terminal, com o diretório no repositório que foi inserido.

<h1 align="center">
   <img
      alt="exampleTerminal"
      title="ExampleTerminal"
      src="https://i.ibb.co/pWCppgx/Screenshot-from-2021-04-26-14-23-44.png"/>
</h1>

Para criar uma nova entidade, o seguinte comando deve ser dado:

```bash
python3 index.py Checklist
```

Substitua o terceiro argumento (Checklist) pelo nome da entidade que você deseja criar. Assim, automaticamente ele preenche os arquivos XML com as configurações necessárias e cria os arquivos PHP em suas pastas já pré-determinadas.

## Configurações

É recomendado que as configurações não sejam alteradas. Mas caso exista algum motivo excepcional e você precise mudar algo, saiba o que você está fazendo.


| Parametro            | Descrição                                        | Valor padrão                    |
| -------------------- | ------------------------------------------       | ------------------------------- |
| xml{Type}Template    | Caminho para o arquivo XML com o template.       | "./xmlTemplates/{Type}.xml"     |
| php{Type}Template    | Caminho para o arquivo PHP com o template.       | "./phpTemplates/controller.php" |
| php{Type}Output      | Caminho para onde o arquivo PHP vai ser escrito. | "../../{Type}"                  |
| --------------------------------------------------------------------------------------------------------- |

O argumento Type assume os valores "Controller", "Service" e "Factory".