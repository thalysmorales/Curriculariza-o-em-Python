def informacoesInicias():
   nome =        open(f"{nomeHTML}NomeCompleto.txt","w")
   idade =       open(f"{nomeHTML}Idade.txt","w")
   estadoCivil = open(f"{nomeHTML}EstadoCivil.txt","w")
   cidade =      open(f"{nomeHTML}Cidade.txt","w")
   endereco =    open(f"{nomeHTML}Endereco.txt","w")
   email =       open(f"{nomeHTML}Email.txt","w")
   linkedin =    open(f"{nomeHTML}LinkedIn.txt","w")
   celular =     open(f"{nomeHTML}Celular.txt","w")
   foto =        open(f"{nomeHTML}Foto.txt","w")

    
   n =           input("Nome Completo: ")
   i =           input("Idade: ")
   ec =          input("Estado Civil: ")
   c =           input("Cidade Atual: ")
   e =           input("Endereco Atual: ")
   ema =         input("Endereco de E-mail: ")
   link =        input("Nome de Usuário no LinkdIn: ")
   cel =         input("Celular para contato: ")

   incluirFoto = input("Deseja incluir uma foto de perfil? [S/N]: ")
   if incluirFoto.upper() == 'S':
       perfil = f"img/{nomeHTML}.png"
   else:
       perfil = "img/semFoto.png"
       print("\n\nObservação: A falta de foto no currículo pode interferir na escolha dos gestores.\n\n")

   nome.write("\n" + n + "\n")
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
    objetivo =    open(f"{nomeHTML}Objetivos.txt","w")
    resumo =      open(f"{nomeHTML}ResumoProfissional.txt","w")
    formacao =    open(f"{nomeHTML}Formação.txt","w")
    experiencia = open(f"{nomeHTML}ExperiênciasProfissionais.txt","w")

    o = input("Descreva o seu Objetivo Profissional: ")
    r=  input("Resumo Profissional: ")

    pergunta = 'S'
    while pergunta.upper() == 'S':
        f = input("Formação Acadêmica: ")
        i = input("Instituição: ")
        c = input("Cidade: ")
        p = input("Período: ")
        formacao.write( "\n" + f + " - " + i + " - " + c + " - " + p + "\n\n")
        pergunta = input("Deseja adicionar alguma outra formação acadêmica? [S/N]: ")

    pE = 'S'
    while pE.upper() == 'S':
        exP =  input("Experiencia Profissional - Organização/Empresa: ")
        cA =   input("Cargo: ")
        pExp = input("Período: ")
        a =    input("Atividades Desenvolvidas: ")
        experiencia.write( "\n" + exP + " - " + cA + " - " + pExp + " - " + a + "\n\n" )
        pE = input("Deseja adicionar alguma outra experiência profissional? [S/N]: ")
    
    objetivo.write( "\n" + o + "\n")
    resumo.write( r + "\n")

    objetivo.close()
    resumo.close()
    formacao.close()
    experiencia.close()

def informacoesAdicionais():
    idioma =    open(f"{nomeHTML}Idioma.txt","w")
    qualidade = open(f"{nomeHTML}Qualidades.txt","w")
    curso =     open(f"{nomeHTML}Cursos.txt","w")

    pergunta = 'S'
    while pergunta.upper() == 'S':
        id = input("Insira o idioma que você possui domínio: ")
        n =  input("Qual a sua categoria de proeficiência nesse idioma?\n\n Iniciante - Básico/Elementar - Intermediário \n Intermediário Superior/Avançado - Avançado - Proeficiência Plena/Nativo\n\nEscolha: ")
        idioma.write( "\n" + id + " - " + n + "\n\n")
        pergunta = input("Você possui domínio em mais algum idioma? [S/N]: ")

    perguntaDois = 'S'
    while perguntaDois.upper() == 'S':
        q = input("Qualidade/Característica importante para o mercado de trabalho: ")
        qualidade.write( q + "\n\n")
        perguntaDois = input("Deseja adicionar outra qualidade/característica? [S/N]: " )

    perguntaTres = 'S'
    while perguntaTres.upper() == 'S':
        cur = input("Você possui algum curso comprovado por certificado? [S/N]: ")
        if cur.upper() == 'S':
            Cn = input("Nome do curso: ")
            i = input("Instituição: ")
            p = input("Período em meses: ")
            curso.write( "\n" + Cn + " - " + i + " - " + p + " meses" + "\n\n")
        else:
            print("Ok, vamos continuar com o preenchimento do currículo.\n\n")
            break
        perguntaTres = input("Você possui mais algum curso que deseja adicionar? [S/N]: ")

    idioma.close()
    qualidade.close()
    curso.close()

def htmlInserir():
    nome =        open(f"{nomeHTML}NomeCompleto.txt","r")
    idade =       open(f"{nomeHTML}Idade.txt","r")
    estadoCivil = open(f"{nomeHTML}EstadoCivil.txt","r")
    cidade =      open(f"{nomeHTML}Cidade.txt","r")
    endereco =    open(f"{nomeHTML}Endereco.txt","r")
    email =       open(f"{nomeHTML}Email.txt","r")
    linkedin =    open(f"{nomeHTML}LinkedIn.txt","r")
    celular =     open(f"{nomeHTML}Celular.txt","r")
    foto =        open(f"{nomeHTML}Foto.txt","r")

    objetivo =    open(f"{nomeHTML}Objetivos.txt","r")
    resumo =      open(f"{nomeHTML}ResumoProfissional.txt","r")
    formacao =    open(f"{nomeHTML}Formação.txt","r")
    experiencia = open(f"{nomeHTML}ExperiênciasProfissionais.txt","r")

    idioma =      open(f"{nomeHTML}Idioma.txt","r")
    qualidade =   open(f"{nomeHTML}Qualidades.txt","r")
    curso =       open(f"{nomeHTML}Cursos.txt","r")

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
            background-color: dimgray;
            display:flex;
            justify-content:center;
        }}

        .curriculoPDF{{
            width: 50rem;
            height: auto;
            background-color:#FFF;
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
            width: 6rem;
            height: 7rem;
            object-fit: cover;
            border-radius: 0.2rem;
            padding:1rem;
        }}

        .textoCa {{
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 10rem;
        }}

        .corpoCurriculo {{
            display: flex;
            flex-direction: column;
            justify-content: center;
            padding-top: 1rem;
            color: #000;
            padding-left: 4rem;
            padding-right: 3rem;
            width:40rem;
        }}

        .corpoCurriculo p {{
            font-family: Arial, Helvetica, sans-serif;
            text-align: justify;
            color: rgb(0, 0, 0);
           
            padding:1rem;
        }}

        .corpoCurriculo hr {{
            background-color: rgb(0, 0, 0, 0.8);
            border: none;
            height: 0.2rem;
            width: 100%;
            padding-top: 0;
            padding-bottom: 0.1rem;
        }}

        .corpoCurriculo h1 {{
            color: rgb(1, 1, 154);
            font-size: 1.5rem;
            padding-bottom: 0;
            background-color: rgb(120, 120, 241);
            border-left:0.2rem solid rgb(246, 234, 175);
            padding-left:0.5rem;
            margin:0;
        }}
    </style>
</head>

<body>
<div class="curriculoPDF">
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
            {formacaoArq}
        </ul>


        <h1>Experiências Profissionais</h1>
        <hr>
        <ul>
            {experienciaArq}
        </ul>

        <h1>Idiomas</h1>
        <hr>
        <ul>
            {idiomaArq}
        </ul>


        <h1>Principais Qualidades/Características</h1>
        <hr>
        <ul>
            {qualidadeArq}
        </ul>

        <h1>Cursos</h1>
        <hr>
        <ul>
           {cursoArq}
        </ul>
    </div>
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
    escolha = (input("O que deseja fazer? \n1 - Cadastrar um novo currículo. \n2 - Editar um currículo. \n3 - Sair do programa\n\n Escolha: "))
    if escolha == '1':
        pergunta = input("Deseja iniciar o preenchimento do seu curriculo? [S/N]:")
        if pergunta.upper() == 'S':
            informacoesInicias()
            informacoesProfissionais()
            informacoesAdicionais()
            htmlInserir()
        else: 
            print("Operação cancelada. Tente novamente reiniciando o programa.\n\n")
            funcoes()

    elif escolha == '2':
        try:
            arquivo = open(f"{nomeHTML}NomeCompleto.txt","r")
            arquivo.close()
            print("Currículo encontrado!\n\n\n")
                
            nome =        open(f"{nomeHTML}NomeCompleto.txt","r")
            idade =       open(f"{nomeHTML}Idade.txt","r")
            estadoCivil = open(f"{nomeHTML}EstadoCivil.txt","r")
            cidade =      open(f"{nomeHTML}Cidade.txt","r")
            endereco =    open(f"{nomeHTML}Endereco.txt","r")
            email =       open(f"{nomeHTML}Email.txt","r")
            linkedin =    open(f"{nomeHTML}LinkedIn.txt","r")
            celular =     open(f"{nomeHTML}Celular.txt","r")
            foto =        open(f"{nomeHTML}Foto.txt","r")
    
            objetivo =    open(f"{nomeHTML}Objetivos.txt","r")
            resumo =      open(f"{nomeHTML}ResumoProfissional.txt","r")
            formacao =    open(f"{nomeHTML}Formação.txt","r")
            experiencia = open(f"{nomeHTML}ExperiênciasProfissionais.txt","r")
    
            idioma =      open(f"{nomeHTML}Idioma.txt","r")
            qualidade =   open(f"{nomeHTML}Qualidades.txt","r")
            curso =       open(f"{nomeHTML}Cursos.txt","r")
    
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
    
            escolhaDois = (input("\nEm qual campo você deseja realizar alterações?\n1 - Dados Iniciais\n2 - Dados Profissionais\n3 - Informações adicionais\n4- Todos os campos\n5-Nenhum campo\n  "))
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
            
        except:
            print("Currículo não encontrado.\nConfira se o nome do arquivo está correto ou se você tem um currículo cadastrado no sistema.\n")
            funcoes()
    else:
        print("Programa encerrado. Até logo!\n\n\n")

nomeHTML = input("Para começarmos, insira o seu nome: ")
funcoes()

