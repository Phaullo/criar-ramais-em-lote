# Criar ramais Asterisk

Código para gerar um arquivo CONF com vários ramais de uma só vez.

## Instalação
Use o pip3 do python para instalar as dependências
```bash
pip3 install secrets string
```

## Como usar

Caso deseje utilizar uma senha padrão para todos os ramais, na linha 27, a variável 'senha', deverá ser preenchida com o seu padrão.

```bash
python3 criarRamais.py
```

Digite a quantidade de ramais a serem criados.
O range dos ramais
E se usará a senha padrão ou se irá utilizar uma senha randômica [ S / N]

## CONF do Asterisk

No final, o arquivo 'ramais.conf' deverá ser copiado para a pasta /etc/asterisk/

## Asterisk

No asterisk, edite o arquivo '/etc/asterisk/sip.conf' e adicione a seguinte linha, pode ser no começo ou no final do arquivo:

#include ramais.conf

Dê um Reload no asterisk

```bash
asterisk -rx 'reload'
```
