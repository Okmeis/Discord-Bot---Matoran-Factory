# Discord Bot - Matoran Factory
A discord bot that produces a MNOG2 style matoran based on your input.

## Tested on:
- - Win11
  - Python 3.11.6
    - discord 2.3.2
    - discord.py 2.3.2
    - Pillow 10.1.0


## Before Execution
- install required libraries
- follow the key insertion instruction in `DiscordMatoranCreatorBot.py`

## Execute it with
`python DiscordMatoranCreatorBot.py`

## Usage of the Bot
DM the the following command to the bot or post it into a channel where the bot can read messages and post pictures:
```html
!matoran <torsoColor> <footColor> <eyeColor> <maskColor> <maskName>
```
With the colors written in HEX color code format and the mask name simly being one of the names of the six Toa Mata masks or one of the masks of their six Turaga.

### Example:
```python
!matoran #420A55 #042069 #FFFFFF #B00B69 kaukau
```
What you will get is the matoran Hahli, but in the colors of the bi-pride flag.
