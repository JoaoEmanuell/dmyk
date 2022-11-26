- [dmyk](#dmyk)
- [Starting](#starting)
  - [Virtual environment](#virtual-environment)
  - [Installing dependencies](#installing-dependencies)
- [Configurations](#configurations)

[English](README.md) | [Português Brasil](README-br.md)

# dmyk
Download Music YouTube Kivy [dmyk] is a project to download music and videos 
from YouTube, using pytube lib and kivy.

# Starting

## Virtual environment

Windows :
    
    python -m venv .

    .\Scripts\activate.bat

Linux | Mac :

    python3 -m venv .

    source ./bin/activate

## Installing dependencies

    pip install -r requirements.txt

# Configurations

Specific directories need specific settings.

Since kivy on android gives some [many] bugs related to the lack of modules, even though they are installed, it ends up being necessary to add them to the project manually, if they aren't, they can work on windows and Linux, but on android are almost certain to fail.

To do this, just run *_setup_local.py* if it hasn't run before, it will move the directories, thus preventing bugs from occurring.