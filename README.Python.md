# Python, alguns exemplos de código

## Como criar uma classe

```py

# -*- coding: UTF-8 -*-
# orcamento.py
class Orcamento(object):
  def _init_(self, valor):
    self.__valor = valor

  @property
  def valor(self):
    return self.__valor
```

## Como criar uma classe main

```py

def main():
    print("Hello World!")

if _name_ == "__main__":
    main()

```