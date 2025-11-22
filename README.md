# イナズマクロ

イナズマイレブン V 用の面倒な特訓類のマクロを作成してここを置き場にします。<br>
キーボードマクロになります。マクロコンなしで利用できる代わりにPC版以外では利用できません。

## DEMO

[デモ動画](https://x.com/i/status/1991926686229860812)

## Requirement

- Python 実行環境
  - 必要なモジュールは以下
    - `pyautogui`
    - `keyboard`

## Installation
お使いのターミナルで以下の順に実行します。
```bash
$ git clone https://github.com/2clchino/inzmacro.git
$ cd inzmacro
$ mamba env create --file env.yaml -n inzmacro
$ mamba activate inzmacro
```
Windows ユーザーで git がないよと言われる場合は [git bash](https://git-scm.com/install/windows) をインストールします。(インストール後 cmd を再起動すれば使えるようになるはず)<br>
mamba がないよと言われる場合は以下を実行
```
$ curl -L -o Miniforge3-Windows-x86_64.exe https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe
$ set "PATH=%USERPROFILE%\miniforge3;%USERPROFILE%\miniforge3\Scripts;%PATH%"
$ conda --version
```
ここまでできたら
```
conda install -n base mamba -y
mamba --version
```

## Usage
```bash
$ python base.py
```
を実行したのちに、イナズマイレブン V のウインドウをアクティブにし、百目階段特訓ポータルにアクセスできる位置で F8 キーを押下

## Issue
- 1分の待ち時間に他の特訓ができないか
- AI 監督による自動試合マクロ等の追加

## Author

Cl2CHINO
