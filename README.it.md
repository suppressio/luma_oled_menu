🌐 [English](README.md) | **Italiano**

# luma OLED menu

Un menu grafico per un display OLED 256×64 su Raspberry Pi, comandato da un encoder rotativo: una griglia di icone con la descrizione di quella selezionata, letta da un file XML. Basato su [luma.oled](https://github.com/rm-hull/luma.oled).

> **Prototipo.** Il menu viene disegnato e l'encoder sposta la selezione, ma scegliere una voce non esegue ancora il suo comando, e il ciclo principale ha un problema di temporizzazione noto. Verrà ripreso.

## Hardware

| Componente | Collegamento |
|---|---|
| Display OLED, controller SSD1322, 256×64 | SPI porta 0, device 0 |
| Encoder rotativo con pulsante | CLK → GPIO 17, DT → GPIO 18, SW → GPIO 27 (numerazione BCM) |

## Installazione

Sul Raspberry Pi, con SPI attivo (`sudo raspi-config` → Interface Options → SPI):

```bash
git clone https://github.com/suppressio/luma_oled_menu.git
cd luma_oled_menu
pip install luma.oled RPi.GPIO
```

I font non sono nel repository: vanno messi in `resources/fonts/` con questi nomi.

| File | Font | Uso |
|---|---|---|
| `fa-font.otf` | [Font Awesome](https://fontawesome.com) (Free) | icone del menu |
| `small_pixel-7.ttf` | Small Pixel 7 | descrizioni del menu |
| `digital-7-m.ttf`, `digital-7-mi.ttf` | Digital-7 (mono, mono corsivo) | orologio |

## Uso

```bash
python3 loop.py     # il menu: ruota l'encoder per spostarti, premi per selezionare
python3 clock.py    # un orologio digitale a tutto schermo (ora, secondi, data)
```

## Configurazione

Il menu è in `resources/config.xml`. Ogni `menuGroup` è un livello (`lvl`, `name`, `style`: `graphic` per la griglia di icone, `text`); ogni `menuElement` ha:

- `id`: la sua posizione nella griglia (8 colonne × 2 righe, da 1);
- `icon`: il code point Font Awesome in esadecimale (es. `f017` per l'orologio), con `style="fa-font"`;
- `description`: il testo mostrato sotto la griglia quando la voce è selezionata;
- `command`: cosa deve fare la voce: `<py exec="clock.py"/>` avvia uno script, `<menu_lk lvl="1"/>` apre un altro livello (non ancora eseguito);
- `<disabled/>`: una voce non ancora disponibile.

## File

| File | Cosa |
|---|---|
| `loop.py` | ciclo principale: legge l'encoder, disegna il menu |
| `menu.py` | disegno della griglia, della selezione e della descrizione |
| `xmlConfigs.py` | lettura di `resources/config.xml` |
| `clock.py` | schermata orologio autonoma |
