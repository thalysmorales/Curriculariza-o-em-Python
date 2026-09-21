# Gerador de Currículos

Projeto desenvolvido em **Python** para criação e gerenciamento de currículos de forma automatizada.

## Sobre o Projeto

O sistema permite que o usuário preencha suas informações pessoais, profissionais e adicionais para gerar automaticamente um currículo em formato **HTML**.

Durante o preenchimento, o usuário pode informar dados como nome, idade, estado civil, cidade, endereço, e-mail, LinkedIn, telefone, objetivo profissional, resumo profissional, formação acadêmica, experiências profissionais, idiomas, qualidades e cursos.

Os dados são armazenados em arquivos `.txt` separados e posteriormente utilizados para gerar o currículo em HTML.

## Funcionalidades

* Cadastro de informações pessoais;
* Cadastro de informações profissionais;
* Cadastro de formação acadêmica;
* Cadastro de experiências profissionais;
* Cadastro de idiomas e nível de proficiência;
* Cadastro de qualidades e características;
* Cadastro de cursos;
* Inclusão de foto de perfil;
* Armazenamento dos dados em arquivos `.txt`;
* Geração automática do currículo em HTML;
* Visualização dos dados cadastrados;
* Possibilidade de editar informações já cadastradas.

## Tecnologias Utilizadas

* **Python**
* **Tkinter** — utilizado para a seleção da foto de perfil;
* **HTML5** — utilizado na geração do currículo;
* **CSS3** — utilizado para estilização do currículo;
* **Manipulação de arquivos** — utilizada para armazenar e recuperar os dados.

## Como Funciona

Ao iniciar o programa, o usuário informa seu nome e escolhe entre:

1. **Cadastrar um novo currículo**
2. **Editar um currículo existente**

No cadastro, o sistema coleta os dados por meio do terminal e permite selecionar uma foto utilizando uma janela de seleção de arquivos.

Após o preenchimento das informações, o sistema lê os dados armazenados e monta automaticamente um arquivo HTML contendo o currículo.

## Estrutura dos Dados

As informações são armazenadas em diferentes arquivos `.txt`, incluindo:

* `NomeCompleto.txt`
* `Idade.txt`
* `EstadoCivil.txt`
* `Cidade.txt`
* `Endereco.txt`
* `Email.txt`
* `LinkedIn.txt`
* `Celular.txt`
* `Foto.txt`
* `Objetivos.txt`
* `ResumoProfissional.txt`
* `Formação.txt`
* `ExperiênciasProfissionais.txt`
* `Idioma.txt`
* `Qualidades.txt`
* `Cursos.txt`

## Resultado

Ao final do processo, é criado um arquivo HTML com as informações fornecidas pelo usuário, estruturado como um currículo profissional. O sistema também aplica estilos CSS diretamente ao documento HTML gerado.

## Objetivo Acadêmico

O projeto foi desenvolvido com o objetivo de praticar conceitos de **programação em Python**, principalmente funções, estruturas de repetição, condicionais, entrada de dados, manipulação de arquivos e integração com HTML/CSS.

## Autor

**Thalys Morales**
