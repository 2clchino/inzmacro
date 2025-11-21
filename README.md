# イナズマクロ

イナズマイレブン V 用の面倒な特訓類のマクロを作成してここを置き場にします。
キーボードマクロになります。マクロコンなしで利用できる代わりにPC版以外では利用できません。

## DEMO

ここに後でTwitterの動画のっける

## Requirement

- Python 実行環境
  - 必要なモジュールは以下
    - `pyautogui`
    - `keyboard`

## Installation

```bash
$ git clone https://github.com/2clchino/inzmacro.git
$ cd inzmacro
$ mamba env create --file env.yaml -n inzmacro
$ mamba activate inzmacro
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