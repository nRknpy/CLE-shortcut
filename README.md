# CLE-shortcut

ログイン作業を自動化して CLE に直接アクセスするソフトウェア

## requirements

[pip](https://pip.pypa.io/en/stable/installation/)

[chrome webdriver](https://chromedriver.chromium.org/downloads)

## 環境構築

```
$ pip install pipenv
$ pipenv install
```

## 操作

### 仮想環境に入る

```
$ pipenv shell
```

### exe ファイル書き出し

```
$ pyinstaller index.py --onefile --noconsole
```
