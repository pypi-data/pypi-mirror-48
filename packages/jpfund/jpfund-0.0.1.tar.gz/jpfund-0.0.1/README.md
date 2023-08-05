# jpfund

日本の投資信託の基準価額を読み込みます。

## Usage

``` import.py
import jpfund
```

``` From_Morningstar.py
jpfund.Morningstar("2017092908").get()
```

``` emaxis.py
jpfund.EMaxis("250874").get()
jpfund.EMaxis.get_list()[0].get()
```
