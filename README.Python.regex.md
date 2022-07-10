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

## Como transformar um card em um objeto


```py

class Card(object):
  def _init_(self, title):
    self.__title = title

  @property
  def title(self):
    return self.__valor

def main():
    card = Card()
    card.title = "sdvsdvsdvsdv"

if _name_ == "__main__":
    main()

```


https://regex101.com/r/zMOrOl/1