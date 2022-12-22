- [dmyk](#dmyk)
- [Iniciando](#iniciando)
  - [Ambiente virtual](#ambiente-virtual)
- [Configurações](#configurações)

[English](README.md) | [Português Brasil](README-br.md)

# dmyk
Download Music YouTube Kivy [dmyk] é um projeto para baixar músicas e vídeo do 
YouTube, usando as libs pytube e kivy.

# Iniciando

## Ambiente virtual

**Nota:** O projeto utiliza o **python3.11.1** como padrão, portanto é 
desejável a utilização do mesmo.

Windows :

    python -m venv .

    .\Scripts\activate.bat

Linux | Mac :

    python3 -m venv .

    source ./bin/activate

# Configurações

Após a criação e ativação do ambiente virtual rode o *_setup_local.py*, ele
irá mover pacotes para evitar erros, além de fazer a instalação do Kivy para o
python3.11 (pois o mesmo se encontra com um erro de instalação via pip), caso
tenha algum erro e instalar o requirements.txt

Caso queira instalar as dependências de maneira manual:
    
    pip install Cython==0.29.32 Kivy==2.1.0
    pip install -r requirements.txt
