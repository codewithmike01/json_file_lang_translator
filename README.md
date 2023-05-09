# Json File Translator from soure to target language

Translation of json file from source language to a target langauge
using Google translation library in python.

## Preview

![image](https://github.com/Ginohmk/json_file_lang_translator/assets/58771507/af014bf1-4fea-4904-945a-e20909992760)

## Set up

- Clone the repository

```bash
 git clone https://github.com/Ginohmk/json_file_lang_translator.git
```

- Cd into the folder

```bash
cd json_file_lang_translator

```

## Folder structure

```bash
.
├── data (holds json file)
│ ├── source.json
│
├── lib
│ ├── __pycache__.py
│ ├── translator.py
│
├── app.py
├── mock (For testing purpose)
│ ├── source.json
├── test.py
└── README.md
```

## How to use

- You need to place your source json file inside of data folder and name it source.json

- Run the program

```bash
python3 app.py

```

- Follow thw prompt

  - Enter the abbreviation of the source language (For English en )
  - Enter the abbreviation of the target language (For Spanish es)

- Allow it to run the program, your output target json translation will be in the data folder, with the `bash
<target abbrviation name>.json`
