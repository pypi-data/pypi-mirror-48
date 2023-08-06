# pyfortune

Fortune Musicをスクレイピングして情報を取得するためのライブラリ

# Install

## RequirePackage

* python3 (>=3.2)

## install command

```
$ python3 setup.py install
```

or

```
$ pip install .
```

PyPIには登録していないしする予定もない

# Usage

## クイックスタート

```
>>> from pyfortune.session import Session
>>> s = Session()
>>> s.status()
'logout'
>>> s.login('username', 'password')
'username'
>>> s.status()
'login'
```
