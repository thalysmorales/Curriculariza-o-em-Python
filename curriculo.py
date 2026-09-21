import tkinter as tk
from tkinter import filedialog

#Inicialização padrão para o funcionamento da biblioteca Tkinter, faz com que a imagem 
#fique oculta até que a utilização do filedialog seja feita.
janela = tk.Tk()
janela.withdraw() 

def informacoesInicias():
    pergunta = 'S'
    while pergunta.upper() == 'S' or pergunta == 'S':
        nome =        open("NomeCompleto.txt","w")
        idade =       open("Idade.txt","w")
        estadoCivil = open("EstadoCivil.txt","w")
        cidade =      open("Cidade.txt","w")
        endereco =    open("Endereco.txt","w")
        email =       open("Email.txt","w")
        linkedin =    open("LinkedIn.txt","w")
        celular =     open("Celular.txt","w")
        foto =        open("Foto.txt","w")

    
        n =           input("Nome Completo: ")
        i =           input("Idade: ")
        ec =          input("Estado Civil: ")
        c =           input("Cidade Atual: ")
        e =           input("Endereco Atual: ")
        ema =         input("Endereco de E-mail: ")
        link =        input("Nome de Usuário no LinkdIn: ")
        cel =         input("Celular para contato: ")

        incluirFoto = input("Deseja incluir uma foto de perfil? [S/N]: ")
        perfil = ""
        if incluirFoto.upper() == 'S':
            perfil = filedialog.askopenfilename(
            title="Selecione sua foto de perfil:",
            filetypes=[("Imagens", "*.jpg *.jpeg *.png")]
            )
        else:
            print("Observação: A falta de foto no currículo pode interferir na escolha dos gestores.\n")

        pergunta = input("Deseja realizar preenchimento do seus dados iniciais novamente? [S/N]: ")

        nome.write( n + "\n")
        idade.write( i + "\n")
        estadoCivil.write( ec + "\n")
        cidade.write(c + "\n")
        endereco.write( e + "\n")
        email.write( ema + "\n")
        linkedin.write(link + "\n")
        celular.write( cel + "\n")
        foto.write( perfil + "\n")

        nome.close()
        idade.close()
        estadoCivil.close()
        cidade.close()
        endereco.close()
        email.close()
        linkedin.close()
        celular.close()
        foto.close()

def informacoesProfissionais():
    objetivo =    open("Objetivos.txt","w")
    resumo =      open("ResumoProfissional.txt","w")
    formacao =    open("Formação.txt","w")
    experiencia = open("ExperiênciasProfissionais.txt","w")

    o = input("Descreva o seu Objetivo Profissional: ")
    r=  input("Resumo Profissional: ")

    pergunta = 'S'
    while pergunta.upper() == 'S':

        f = input("Formação Acadêmica: ")
        i = input("Instituição: ")
        c = input("Cidade: ")
        p = input("Período: ")

        pergunta = input("Deseja adicionar alguma outra formação acadêmica? [S/N]: ")

   
    pE = 'S'
    while pE.upper() == 'S':
        exP =  input("Experiencia Profissional - Organização/Empresa: ")
        cA =   input("Cargo: ")
        pExp = input("Período: ")
        a =    input("Atividades Desenvolvidas: ")
    
        pE = input("Deseja adicionar alguma outra experiência profissional? [S/N]: ")

        
    objetivo.write( "\n" + o + "\n")
    resumo.write( r + "\n")
    formacao.write( f + "\n" + i + "\n" + c + "\n" + p + "\n")
    experiencia.write( exP + "\n" + cA + "\n" + pExp + "\n" + a + "\n" )

    objetivo.close()
    resumo.close()
    formacao.close()
    experiencia.close()

def informacoesAdicionais():
    idioma =    open("Idioma.txt","w")
    qualidade = open("Qualidades.txt","w")
    curso =     open("Cursos.txt","w")

    pergunta = 'S'
    while pergunta.upper() == 'S':
        id = input("Insira o idioma que você possui domínio: ")
        n =  input("Qual a sua categoria de proeficiência nesse idioma?\n \n Iniciante \n Básico/Elementar \n Intermediário \n Intermediário Superior/Avançado \n Avançado \n Proeficiência Plena/Nativo \n: ")
        pergunta = input("Você possui domínio em mais algum idioma? [S/N]: ")

    perguntaDois = 'S'
    while perguntaDois.upper() == 'S':
        q = input("Qualidade/Característica importante para o mercado de trabalho: ")
        perguntaDois = input("Deseja adicionar outra qualidade/característica? [S/N]: " )

    Cn = ""
    i = ""
    p = ""
    perguntaTres = 'S'
    while perguntaTres.upper() == 'S':
        cur = input("Você possui algum curso comprovado por certificado? [S/N]: ")
        if cur.upper() == 'S':
            Cn = input("Nome do curso: ")
            i = input("Instituição: ")
            p = input("Período em meses: ")
        perguntaTres = input("Você possui mais algum curso que deseja adicionar? [S/N]: ")

    idioma.write( "\n" + id + "\n" + n + "\n")
    qualidade.write( q + "\n")
    curso.write( Cn + "\n" + i + "\n" + p + "\n")

    idioma.close()
    qualidade.close()
    curso.close()

def htmlInserir():
    nome =        open("NomeCompleto.txt","r")
    idade =       open("Idade.txt","r")
    estadoCivil = open("EstadoCivil.txt","r")
    cidade =      open("Cidade.txt","r")
    endereco =    open("Endereco.txt","r")
    email =       open("Email.txt","r")
    linkedin =    open("LinkedIn.txt","r")
    celular =     open("Celular.txt","r")
    foto =        open("Foto.txt","r")

    objetivo =    open("Objetivos.txt","r")
    resumo =      open("ResumoProfissional.txt","r")
    formacao =    open("Formação.txt","r")
    experiencia = open("ExperiênciasProfissionais.txt","r")

    idioma =      open("Idioma.txt","r")
    qualidade =   open("Qualidades.txt","r")
    curso =       open("Cursos.txt","r")

    nomeArq = nome.read().strip()
    idadeArq = idade.read().strip()
    estadoCivilArq = estadoCivil.read().strip()
    cidadeArq = cidade.read().strip()
    enderecoArq = endereco.read().strip()
    emailArq = email.read().strip()
    linkedinArq = linkedin.read().strip()
    celularArq = celular.read().strip()
    fotoArq = foto.read().strip()

    objetivoArq = objetivo.read().strip()
    resumoArq = resumo.read().strip()

    linhaFormacao = formacao.read().split("\n")
    formacaoArq = ""
    for linha in linhaFormacao:
        if linha.strip() != "":
            formacaoArq += "<li>" + linha.strip() + "</li>"


    linhaExperiencia = experiencia.read().split("\n")
    experienciaArq = ""
    for linha in linhaExperiencia:
        if linha.strip() != "":
            experienciaArq += "<li>"+ linha.strip() + "</li>"

    linhaIdioma = idioma.read().split("\n")
    idiomaArq = ""
    for linha in linhaIdioma:
        if linha.strip() != "":
            idiomaArq += "<li>" + linha.strip() + "</li>"

    linhaQualidade = qualidade.read().split("\n")
    qualidadeArq = ""
    for linha in linhaQualidade:
        if linha.strip() != "":
            qualidadeArq += "<li>" + linha.strip() + "</li>"

    linhaCurso = curso.read().split("\n")
    cursoArq = ""
    for linha in linhaCurso:
        if linha.strip() != "":
            cursoArq += "<li>" + linha.strip() + "</li>" 
           
    html = open(f"Curriculo_{nomeHTML}.html","w", encoding="utf-8")
    htmlCodigo = (f"""

    <!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Currículo {nomeHTML}</title>
    <style>
        * {{
            font-size: 16px;
            font-family: 'Times New Roman', Times, serif;
        }}

        body {{
            margin: 0;
            margin-top: 0;
        }}

        .cabecalho {{
            background-color: rgb(1, 1, 154);
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            color: #fff;
            padding: 1rem;
        }}

        .cabecalho h1 {{
            margin: 0;
            padding-top: 1rem;
            font-size: 3rem;
        }}

        .cabecalho img {{
            width: 3rem;
            height: 4rem;
            object-fit: cover;
            border-radius: 0.2rem;
        }}

        .textoCa {{
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 40rem;
        }}

        .corpoCurriculo {{
            padding-top: 1rem;
            color: #fff;
            margin-left: 3rem;
            margin-right: 3rem;
        }}

        .corpoCurriculo p {{
            font-family: Arial, Helvetica, sans-serif;
            text-align: justify;
        }}

        .corpoCurriculo hr {{
            background-color: rgb(0, 0, 0, 0.8);
            border: none;
            height: 0.2rem;
            width: auto;
            padding-top: 0;
            padding-bottom: 0.1rem;
        }}

        .corpoCurriculo h1 {{
            color: rgb(1, 1, 154);
            font-size: 1.5rem;
            padding-bottom: 0;
        }}
    </style>
</head>

<body>
    <div class="cabecalho">

        <h1>{nomeArq}</h1>
        <img src="{fotoArq}" alt="Foto 3x4">

        <div class="textoCa">

            <div>
                <p>{estadoCivilArq}, {idadeArq}</p>
                <p>{enderecoArq}</p>
                <p>{cidadeArq}</p>
            </div>
            <div>
                <p>E-mail: {emailArq}</p>
                <p>LinkdIn: linkedin.com/in/{linkedinArq}</p>
                <p>Celular:{celularArq}</p>
            </div>

        </div>
    </div>
    <div class="corpoCurriculo">
        <h1>Objetivos Profissional</h1>
        <hr>
        <p>{objetivoArq}</p>

        <h1>Resumo Profissional</h1>
        <hr>
        <p>{resumoArq}</p>


        <h1>Formação Acadêmica</h1>
        <hr>
        <ul>
            <li>{formacaoArq}</li>
        </ul>


        <h1>Experiências Profissionais</h1>
        <hr>
        <ul>
            <li>{experienciaArq}</li>
        </ul>

        <h1>Idiomas</h1>
        <hr>
        <ul>
            <li>{idiomaArq}</li>
        </ul>


        <h1>Principais Qualidades/Características</h1>
        <hr>
        <ul>
            <li>{qualidadeArq}</li>
        </ul>

        <h1>Cursos</h1>
        <hr>
        <ul>
            <li>{cursoArq}</li>
        </ul>
    </div>
</body>

</html>

                 """)
    html.write(htmlCodigo)
    html.close()

    nome.close()
    idade.close()
    estadoCivil.close()
    cidade.close()
    endereco.close()
    email.close()
    linkedin.close()
    celular.close()
    foto.close()

    objetivo.close()
    resumo.close()
    formacao.close()
    experiencia.close()

    idioma.close()
    qualidade.close()
    curso.close()

    

def funcoes():
    escolha = (input("O que deseja fazer? \n1 - Cadastrar um novo currículo. \n2 - Editar um currículo."))
    if escolha == '1':
        pergunta = input("Deseja iniciar o preenchimento do seu curriculo? [S/N]:")
        if pergunta.upper() == 'S':
            informacoesInicias()
            informacoesProfissionais()
            informacoesAdicionais()
            htmlInserir()
        else: 
            print("Operação cancelada. Tente novamente iniciando o programa.")
    elif escolha == '2':
#leitura dos dados inseridos para verificar onde, e se, a atualização será realizada
        nome =        open("NomeCompleto.txt","r")
        idade =       open("Idade.txt","r")
        estadoCivil = open("EstadoCivil.txt","r")
        cidade =      open("Cidade.txt","r")
        endereco =    open("Endereco.txt","r")
        email =       open("Email.txt","r")
        linkedin =    open("LinkedIn.txt","r")
        celular =     open("Celular.txt","r")
        foto =        open("Foto.txt","r")

        objetivo =    open("Objetivos.txt","r")
        resumo =      open("ResumoProfissional.txt","r")
        formacao =    open("Formação.txt","r")
        experiencia = open("ExperiênciasProfissionais.txt","r")

        idioma =      open("Idioma.txt","r")
        qualidade =   open("Qualidades.txt","r")
        curso =       open("Cursos.txt","r")

        print("Dados Inciais:\n")
        print(nome.read())
        print(idade.read())
        print(estadoCivil.read())
        print(cidade.read())
        print(endereco.read())
        print(email.read())
        print(linkedin.read())
        print(celular.read())
        print(foto.read())

        print("\nDados Profissionais:\n")
        print(objetivo.read())
        print(resumo.read())
        print(formacao.read())
        print(experiencia.read())

        print("\nDados Adicionais:\n")
        print(idioma.read())
        print(qualidade.read())
        print(curso.read())
        
        nome.close()
        idade.close()
        estadoCivil.close()
        cidade.close()
        endereco.close()
        email.close()
        linkedin.close()
        celular.close()
        foto.close()
        objetivo.close()
        resumo.close()
        formacao.close()
        experiencia.close()
        idioma.close()
        qualidade.close()
        curso.close()

        escolhaDois = (input("Em qual(ais) campo(os) você deseja realizar alterações?\n1 - Dados Iniciais\n2 - Dados Profissionais\n3 - Informações adicionais\n4- Todos os campos\n5-Nenhum campo\n  "))
        if escolhaDois == '1':
            informacoesInicias()
        elif escolhaDois == '2':
            informacoesProfissionais()
        elif escolhaDois == '3':
            informacoesAdicionais()
        elif escolhaDois == '4':
            informacoesInicias()
            informacoesProfissionais()
            informacoesAdicionais()

        htmlInserir()

nomeHTML = input("Para começarmos, insira o seu nome: ")
funcoes()
