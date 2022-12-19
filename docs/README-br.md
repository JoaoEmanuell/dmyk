- [dmyk](#dmyk)
- [Iniciando](#iniciando)
  - [Ambiente virtual](#ambiente-virtual)
  - [Instalando dependências](#instalando-dependências)
- [Configurações](#configurações)

[English](README.md) | [Português Brasil](README-br.md)

# dmyk
Download Music YouTube Kivy [dmyk] é um projeto para baixar músicas e vídeo do 
YouTube, usando as libs pytube e kivy.

# Iniciando

## Ambiente virtual

Windows :

    python -m venv .

    .\Scripts\activate.bat

Linux | Mac :

    python3 -m venv .

    source ./bin/activate

## Instalando dependências

    pip install -r requirements.txt

# Configurações

Diretórios específicos necessitam de configurações específicas.

Uma vez que o kivy no android da alguns [muitos] bugs relacionados a falta de módulos, mesmos eles estando instalados, acaba sendo necessário adicionar eles ao projeto de forma manual, caso não sejam, eles podem até funcionar no windows e no Linux, mas no android é quase certo que irão falhar.

Para isso basta rodar o *_setup_local.py* caso não tenha rodado antes, ele movera os diretórios, assim evitando que bugs ocorram.