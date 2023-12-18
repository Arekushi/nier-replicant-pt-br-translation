<h1 align="center">
  NieR Replicant™ - PT-BR Translation
</h1>

<p align="center">
  <a href="#" target="blank">
    <img src="./assets/emil.png" width="250" alt="Emil" />
  </a>
</p>

<p align="center">
  Application to install and create translations for <a href="https://store.steampowered.com/app/1113560/NieR_Replicant_ver122474487139/">NieR Replicant™ ver.1.22474487139...
  </a><br>
  Versão em português desse README.md <a href="https://github.com/Arekushi/nier-replicant-pt-br-translation/blob/master/README.md">aqui</a>
</p>

<br>

# About the project...
Translation project for PT-BR of the fabulous Nier Replicant ver.1.22474487139, using ChatGPT as support for translation. The project aims to include more people in this gaming masterpiece. As an RPG with various dialogues, not having Brazilian Portuguese as an option tends to push many people away.

The translation was based on English texts, with the support of some Spanish texts to assemble Portuguese text. Once again, an approach using ChatGPT was employed to translate most texts. What was done was **`review`** to ensure that what ChatGPT returned was accurate (and guess what, most texts were indeed accurate).

ChatGPT is a tremendous innovation, greatly aiding in translating the entire game in such a short time. Something that using services like Google Translate or Bing cannot achieve as quickly, given that translations **TO THIS DAY** still raise doubts and are often incorrect.

ChatGPT isn't perfect, but at its current level, it allowed the construction of this application and sharing it with all of you.

It's possible to use this project to translate into other languages; just change the parameters, and ChatGPT will do the work for you—just remember to review the texts. 🎉

This project has **no intention** of replacing other translation projects that are being undertaken. I believe they do a good job; however, doing this manually takes much longer (but as a result, tends to be more careful).

If you'd like to buy me a ☕, here's my PIX key for support: `0dd32e9d-8b78-4978-ad8a-797cbd7380d1`


<br><br>

## How to contribute to the translation?
Check the `texts` folder and look at the files in the `translation` folder (where the translation is located). Make your changes and create a **pull request**. Be clear about why you decided on such changes, and based on that, it will be approved or not.

**All texts** have been carefully reviewed by me, [Caroline Urbano][caroline], and [Cristian Kirsch][omainha]. However, there might be something that slipped through the cracks here and there, so if something like that happens, please inform us.

If you want to discuss more, feel free to reach out to me on some of my social media platforms below:
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
        href="https://steamcommunity.com/id/arekushii">
        <img style="padding: 10px" title="Steam" alt="Steam" width="40px" src="https://i.imgur.com/3qObil8.png">
    </a>
</p>

<br>

## Acknowledgments
I want to thank the people who dedicated themselves to making this project the best possible for true fans.

<br>

[Caroline Urbano][caroline], who works as a translator, took the first steps in the review, evolved a lot with the project, and I imagine she did too. Her social media profiles are listed below.

<p align="center">
    <a
        style="all: unset;"
        target="_blank"
        href="https://www.linkedin.com/in/caroline-urbano-a4110963/">
        <img style="padding: 10px" title="LinkedIn" alt="LinkedIn" width="40px" src="https://i.imgur.com/4qOCXGz.png">
    </a>
</p>

[Cristian Kirsch][omainha], a super nice guy, a huge NieR franchise fan, showed an unprecedented dedication to the review. All of this is a result of his effort, and I am very grateful. His social media profiles are listed below.

<p align="center">
    <a
        style="all: unset;"
        target="_blank"
        href="https://twitter.com/omainha">
        <img style="padding: 10px" title="Twitter" alt="Twitter" width="40px" src="https://i.imgur.com/jlKtG7w.png">
    </a>
    <a
        style="all: unset;"
        target="_blank"
        href="https://www.instagram.com/mainhalisa/">
        <img style="padding: 10px" title="Instagram" alt="Instagram" width="40px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Instagram_icon.png/600px-Instagram_icon.png">
    </a>
    <a
        style="all: unset;"
        target="_blank"
        href="https://www.twitch.tv/omainha">
        <img style="padding: 10px" title="Twitch" alt="Twitch" width="40px" src="https://cdn.iconscout.com/icon/free/png-256/free-twitch-11-461838.png?f=webp">
    </a>
</p>


## How to install the translation?
Here, I'll describe **two ways** to install the translation, using the installer and another manually in case there's an issue with the installation.

### Tutorial using the installer
> NieR Replicant™ ver. 1.22 - PT-BR Translation
[![NieR Replicant™ ver. 1.22 - PT-BR Translation](https://img.youtube.com/vi/3BiVi_KfGbA/0.jpg?)](https://www.youtube.com/watch?v=3BiVi_KfGbA)


1. Download the application executable here: [Release][release]
   
2. Extract the zipped `.zip` file to a preferred folder.

3. Run the `install.bat` file.

4. The program will execute and prompt for the directory path to NieR Replicant ver.1.22474487139.
    > **Example** of path
    ```
    C:\SteamLibrary\steamapps\common\NieR Replicant ver.1.22474487139
    ```

5. That's it, just wait for the completion and start the game already translated. 🎉

<br>

### Tutorial without the installer
1. Download the necessary files here: [data][data]

2. Extract the zipped `.zip` file to a preferred folder.

3. Open the directory where your NieR Replicant is installed.
    > **Example** of path
    ```
    C:\SteamLibrary\steamapps\common\NieR Replicant ver.1.22474487139
    ```

4. Open the `data` folder.

5. The zipped file you downloaded contains two files - `common.arc` and `info.arc`. Place both inside the `data` folder.
    > It will obviously replace the original files, if possible, make a backup of them.

6. That's it, now just start the game. 🎉

## Useful commands list
1. Install
    ```cmd
    nier-translator.exe manager install
    ```

2. Uninstall
    ```cmd
    nier-translator.exe manager uninstall
    ```

3. Update the translation
    ```cmd
    nier-translator.exe manager update
    ```

<br>

# For developers...

## Built with
- [Python 3.10.9][python]

<br>

## Supporting tools
This project was made possible thanks to these two repositories:
* Tool for asset extraction - [kaine][kaine]
* Tool for text extraction - [NieR-Text-Tool][ntt]

<br>

## Getting started
If you want the project for development, some prerequisites are necessary.

### Prerequisites (Windows)
* Python
  1. You can download it here: [Python][python_url]
  2. Here's a step-by-step tutorial. [(Tutorial)][python_tutorial_url]
     1. Tutorial with Miniconda. [(Tutorial)][miniconda_tutorial]
* Poetry
  1. You can install it here: [Poetry][poetry_url]

<br>

### .secrets.toml variables
I keep some sensitive variables in this file inside the `config/toml` folder. Create this file there **if** you're going to use ChatGPT for translation; otherwise, just ignore it.
```toml
[KEYS]
OPENAI_API_KEY = "..." # Simply create an account and go to this link: https://platform.openai.com/account/api-keys

ORG_ID = "..." # You can obtain this ID here: https://platform.openai.com/account/org-settings

SESSION_TOKEN = "..." # Only necessary if you're not using the OpenAI API
```

### Variables in `.toml` Files
I store a lot of information in `.toml` files within the `toml` folder located in the `config` directory. Some of them pertain to the messages I send to ChatGPT for translation. If you want to customize the application, I recommend taking a look there!

<br>

### Installation and Usage
1. Clone the repository.
    ```sh
    git clone https://github.com/Arekushi/nier-replicant-pt-br-translation.git
    ```

2. Install packages using `Poetry`
    ```sh
    poetry install
    ```

3. Run:
    ```sh
    python main.py --help
    ```

4. You're all set to start developing! 🎉

### Useful Commands
I've set up some commands to ease the translation creation process; I'll list and describe a few here:

1. Extract Texts
    ```cmd
    python main.py builder extract-texts
    ```
    This command initiates the process of extracting texts from the game.

    Before starting, it checks if the game's `assets` have already been extracted. If not, it first extracts the `assets` and then proceeds to extract the texts into a .CSV format, which is more user-friendly than the binary format from asset extraction.

    The texts will be found in the `texts/raw` folder.

2. Creating Translation Folder
    ```cmd
    python main.py builder make-translation-folder
    ```
    This command processes the `raw` text files, creating new .CSV files containing only the textual content for translation.

    To facilitate and aid in translation, it creates a .CSV with three columns:
    1. Translation column
    2. Source language column for translation
    3. Support language column for translation

    If you wish to edit the source and support languages, go to the `settings.toml` file and edit the variables:
    1. `target_language`
    2. `source_language`
    3. `secondary_language`

    This way, it's easy to refer to the original texts and translate right away.

    An important tip: if you want to create a new translation, I recommend either:
    1. Deleting the `text/translations` folder
    2. Modifying the name of the `translations` folder in the `settings.toml` file under the variables:
        1. `paths_to_translate`
        2. `translation_folder_name`

3. AI-Based Translation
    ```cmd
    python main.py builder translate
    ```
    This command starts the translation process of the `translation` folder, so it's crucial to execute the previous command before starting this one.

    There are two methods for translation: **ChatGPT** or **Google Translate**.

    #### Google
    Translation via Google is quick but often inaccurate. I've kept this module, although it's not actively used in the project anymore.

    Nonetheless, to translate using Google Translate, add a flag indicating this in the method that will be executed:

    ```cmd
    nier-translator.exe builder translate --google
    ```

    #### ChatGPT
    When it comes to ChatGPT, it's essential to decide whether you'll use a WebCrawler or the OpenAI API.

    ##### WebCrawler

    If you opt for a WebCrawler, edit/create the `.secrets.toml` file within the `config/toml` folder and add the `SESSION_TOKEN` obtained from logging into the ChatGPT page.

    > If you encounter issues with the WebCrawler related to the Google Chrome version, I recommend downloading the ChromeDriver version from this [link][chrome_drive_url].

    > After that, edit the `driver.py` file in the `UnlimitedGPT` library. There's a Driver constructor; edit it to something like this:
    ```python
        super().__init__(
            options=options,
            headless=headless,
            desired_capabilities=caps,
            driver_executable_path='F:\path_to_driver\chromedriver.exe'
        )
    ```

    ##### API

    If you choose to use the API, edit/create the `.secrets.toml` file within the `config/toml` folder and add `OPENAI_API_KEY` and `ORG_ID`. In this case, you'll need to use a flag to indicate to the method to use the API instead of the WebCrawler.
    ```cmd
    python main.py builder translate --api
    ```

    Also, pay attention to the `chat-gpt.toml` file; there, I define how the messages sent in the chat will be, for example, specifying that I want a translation from English to Brazilian Portuguese.

    **DO NOT** recommend modifying what's between the diamonds `<>` if you're unsure.

4. Generating .arc Files
    ```cmd
    python main.py builder generate
    ```
    Finally, after making changes to the files in the `translation` folder, whether through automatic or manual translation, we arrive at the stage of reversing the process and generating the files that the game reads, which are the .ARC files.

    Executing this command will start the process and generate a result inside the `patch/data` folder. There, you'll find the files with your changes already made.

    To apply the changes, simply use the command
    ```cmd
    python main.py manager update --local
    ```

    This way, the files from the `patch/data` folder will be copied to your game's location. Otherwise, you can perform the process manually.

<br>

## Contributors
| [<div><img width=115 src="https://avatars.githubusercontent.com/u/54884313?v=4"><br><sub>Alexandre Ferreira de Lima</sub></div>][arekushi] <div title="Código e Tradução">💻</div> | [<div><img width=115 src="https://avatars.githubusercontent.com/u/129787311?v=4"><br><sub>Caroline Urbano</sub></div>][caroline] <div title="Tradução e Revisão">📚</div> | [<div><img width=115 src="https://avatars.githubusercontent.com/u/131723671?v=4"><br><sub>Cristian Kirsch</sub></div>][omainha] <div title="Tradução e Revisão">📚</div> |
| :---: | :---: | :---: |

<!-- [Build With] -->
[release]: https://github.com/Arekushi/nier-replicant-pt-br-translation/releases/download/2.0.0/nier-translator.zip
[data]: https://github.com/Arekushi/nier-replicant-pt-br-translation/releases/download/2.0.0/data.zip
[python]: https://www.python.org/downloads/

<!-- [Some links] -->
[python_url]: https://www.python.org/downloads/
[python_tutorial_url]: https://www.digitalocean.com/community/tutorials/install-python-windows-10
[miniconda_tutorial]: https://katiekodes.com/setup-python-windows-miniconda/
[poetry_url]: https://python-poetry.org/docs/#installation
[kaine]: https://github.com/yretenai/kaine
[ntt]: https://github.com/lehieugch68/NieR-Text-Tool
[chrome_drive_url]: https://googlechromelabs.github.io/chrome-for-testing/#stable

<!-- [Constributors] -->
[arekushi]: https://github.com/Arekushi
[caroline]: https://github.com/CarolineUrbano
[omainha]: https://github.com/MainhaLisa
