<h1 align="center">
  NieR Replicant™ - Tradução para PT-BR
</h1>

<p align="center">
  <a href="#" target="blank">
    <img src="./assets/emil.png" width="250" alt="Emil" />
  </a>
</p>

<p align="center">
  Aplicação para instalar e criar traduções para o <a href="https://store.steampowered.com/app/1113560/NieR_Replicant_ver122474487139/">NieR Replicant™ ver.1.22474487139...
  </a>
</p>

<br>

# Sobre o projeto...
Projeto individual de tradução para PT-BR do fabuloso Nier Replicant Remaster/Remake (como queira chamar), desenvolvido em pouco menos de uma semana, utilizei o ChatGPT como suporte para a tradução. O projeto tem como objetivo incluir novas pessoas a essa obra prima dos videojogos, que por conta de ser um RPG onde há várias falas, não ter o português-brasileiro como uma opção de idioma acaba afastando muita gente, inclusive a minha pessoa, que não é fluente ***ainda*** no idioma inglês ou espanhol.

A tradução foi feita em cima dos textos em inglês, com o apoio de alguns textos em espanhol para montar um texto em português. Novamente, utilizei de uma abordagem que utilizava o ChatGPT para traduzir a maioria dos textos para mim, o que fiz foi **`revisar`** para ter certeza que o que o ChatGPT me retornou estava de acordo (e adivinha, a maioria dos textos estava sim de acordo).

É um grande inovação o ChatGPT, ele me ajudou e muito a traduzir o jogo inteiro em tão pouco tempo, algo que utilizando os serviços como Google Tradutor ou Bing não é possível em tempo tão hábil, visto que as traduções **ATÉ HOJE** ainda são de cunho duvidoso e incorreto.

ChatGPT não é perfeito, mas no nível atual já me permitiu construir essa aplicação e compartilhar com todos vocês.

Essa aplicação é de código livre e também peço ajuda de vocês para manter a tradução ainda melhor, sou apenas **uma unidade humana** então preciso de ajuda de mais pessoas para melhorar os textos.

É possível utilizar esse projeto para traduzir para outras línguas, é só mudar os parâmetros que o ChatGPT irá fazer o trabalho por ti, só lembre de revisar os textos. 🎉

Isso **não** substitui a tradução que o grupo Tribo Gamer está fazendo, que imagino que é um trabalho bem mais manual, e que envolve bem mais pessoas, logo um cuidado maior, mas como ainda falta um pedaço razoável para traduzir, resolvi fazer da minha maneira.

Se quiser me comprar um ☕, chave PIX pra fortalecer: `0dd32e9d-8b78-4978-ad8a-797cbd7380d1`


<br><br>

## Como ajudar na tradução?
Olhe a pasta `texts` e olhe os arquivos da pasta `pt` (onde está a minha tradução) e a pasta `raw` onde tem os textos brutos originais sem modificações.
Faça sua alteração e faça um **pull request**, seja claro porquê você decidiu tais alterações e eu irei aprovar ou não.

**Todos os textos** foram revisados por mim com bastante cuidado, mas posso ter deixado escapar alguma coisa ali ou aqui, só peço que se acontecer algo do tipo, me informar.

Se quiser conversar mais sobre, pode me chamar em algumas das minhas redes sociais abaixo:
<p align="center">
    <a
        style="all: unset;"
        target="_blank"
        href="">
        <img style="padding: 10px" title="a r e k u s h i#1445" alt="a r e k u s h i#1445" width="40px" src="https://i.imgur.com/WuqAV26.png">
    </a>
    <a
        style="all: unset;"
        target="_blank"
        href="https://steamcommunity.com/id/arekushii_">
        <img style="padding: 10px" title="Steam" alt="Steam" width="40px" src="https://i.imgur.com/3qObil8.png">
    </a>
</p>

<br>

## Como instalar a tradução?
1. Baixe o executável da aplicação aqui: [Release][release]
   
2. Extraia o arquivo zipado `.zip` para alguma pasta de sua preferência.
   
3. Abra um terminal e vá até a pasta descompactada.
    > **Exemplo:**
    ```cmd
    cd C:\nier-translator
    ```

4. Execute o seguinte comando:
    ```cmd
    nier-translator.exe manager install
    ```
5. O programa irá executar e solicitar o caminho até o diretório do NieR Replicant ver.1.22474487139
    > **Exemplo** de caminho
    ```
    C:\SteamLibrary\steamapps\common\NieR Replicant ver.1.22474487139
    ```
6. Irá ser questionado se você deseja apagar ou não a pasta `data` dos arquivos do jogo (não é necessário, mas fica a seu critério)
7. Prontinho, só aguardar a finalização e iniciar o jogo já traduzido. 🎉

<br>

## Lista de comandos uteis
1. Ajuda com os comandos
    ```cmd
    nier-translator.exe manager --help
    ```

2. Instalar
    ```cmd
    nier-translator.exe manager install
    ```

3. Desinstalar
    ```cmd
    nier-translator.exe manager uninstall
    ```
    
4. Atualizar a tradução
    ```cmd
    nier-translator.exe manager update
    ```

<br>

# Para desenvolvedores...

## Construído com
- [Python 3.10.9][python]

<br>

## Ferramentas de apoio
Esse projeto só foi possível graças a esses dois repositórios
* Ferramenta para extração dos assets - [kaine][kaine]
* Ferramenta para extração dos textos - [NieR-Text-Tool][ntt]

<br>

## Primeiros passos
Se quiser o projeto para desenvolver, alguns pré-requisitos são necessários.

### Pré-requisitos (Windows)
* Python
  1. Você pode baixar aqui: [Python][python_url]
  2. Aqui tem um tutorial passo-a-passo. [(Tutorial)][python_tutorial_url]
     1. Tutorial com Miniconda. [(Tutorial)][miniconda_tutorial]
* Poetry
  1. Você pode instalar aqui: [Poetry][poetry_url]

<br>

### Variáveis do .secrets.toml
Eu guardo algumas variáveis sensíveis nesse arquivo dentro da pasta `config`, crie esse arquivo lá **se** for usar o ChatGPT para traduzir, caso contrário apenas ignore.
```toml
[KEYS]
OPENAI_API_KEY = "..." # Só criar uma conta e ir nesse link: https://platform.openai.com/account/api-keys

ORG_ID = "..." # Você consegue esse ID aqui: https://platform.openai.com/account/org-settings

SESSION_TOKEN = "..." # Necessário apenas se você não for usar a API do OpenAI
```

### Variávels do settings.toml
Eu guardo bastante informação dentro do `settings.toml` que fica dentro da pasta `config`, algumas delas são sobre as mensagens que mando para o ChatGPT para a tradução, se quiser customizar a aplicação, recomendo dar uma olhada lá!

<br>

### Instalação e Uso
1. Clone o repositório.
    ```sh
    git clone https://github.com/Arekushi/nier-replicant-pt-br-translation.git
    ```

2. Instale os pacotes com o `Poetry`
    ```sh
    poetry install
    ```

3. Execute:
    ```sh
    python main.py --help
    ```

4. Prontinho, você já pode desenvolver 🎉

<br>

## Roadmap
> Será feito em breve...

<br>

## Video
> Será feito em breve...

<br>

## Contribuidores
| [<div><img width=115 src="https://avatars.githubusercontent.com/u/54884313?v=4"><br><sub>Alexandre Ferreira de Lima</sub></div>][arekushi] <div title="Código e Tradução">💻</div> |
| :---: |

<!-- [Build With] -->
[release]: https://github.com/Arekushi/nier-replicant-pt-br-translation/releases/download/1.0.3/nier-translator.zip
[python]: https://www.python.org/downloads/

<!-- [Some links] -->
[python_url]: https://www.python.org/downloads/
[python_tutorial_url]: https://www.digitalocean.com/community/tutorials/install-python-windows-10
[miniconda_tutorial]: https://katiekodes.com/setup-python-windows-miniconda/
[poetry_url]: https://python-poetry.org/docs/#installation
[kaine]: https://github.com/yretenai/kaine
[ntt]: https://github.com/lehieugch68/NieR-Text-Tool

<!-- [Constributors] -->
[arekushi]: https://github.com/Arekushi
