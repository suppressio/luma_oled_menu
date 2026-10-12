🌐 **English** | [Italiano](README.it.md)

# luma OLED menu

A graphic menu for a 256×64 OLED display on a Raspberry Pi, driven by a rotary encoder: a grid of icons with the description of the selected one, read from an XML file. Built on [luma.oled](https://github.com/rm-hull/luma.oled).

> **Prototype.** The menu is drawn and the encoder moves the selection, but choosing an item does not run its command yet, and the main loop has a known timing problem. It will be picked up again.

## Hardware

| Part | Connection |
|---|---|
| OLED display, SSD1322 controller, 256×64 | SPI port 0, device 0 |
| Rotary encoder with push button | CLK → GPIO 17, DT → GPIO 18, SW → GPIO 27 (BCM numbering) |

## Install

On the Raspberry Pi, with SPI enabled (`sudo raspi-config` → Interface Options → SPI):

```bash
git clone https://github.com/suppressio/luma_oled_menu.git
cd luma_oled_menu
pip install luma.oled RPi.GPIO
```

The fonts are not in the repository: put them in `resources/fonts/` with these names.

| File | Font | Used for |
|---|---|---|
| `fa-font.otf` | [Font Awesome](https://fontawesome.com) (Free) | menu icons |
| `small_pixel-7.ttf` | Small Pixel 7 | menu descriptions |
| `digital-7-m.ttf`, `digital-7-mi.ttf` | Digital-7 (mono, mono italic) | clock |

## Use

```bash
python3 loop.py     # the menu: turn the encoder to move, press to select
python3 clock.py    # a full-screen digital clock (time, seconds, date)
```

## Configuration

The menu is in `resources/config.xml`. Each `menuGroup` is a level (`lvl`, `name`, `style`: `graphic` for the icon grid, `text`); each `menuElement` has:

- `id`: its position in the grid (8 columns × 2 rows, from 1);
- `icon`: the Font Awesome code point in hex (e.g. `f017` for the clock), with `style="fa-font"`;
- `description`: the text shown under the grid when the item is selected;
- `command`: what the item should do: `<py exec="clock.py"/>` runs a script, `<menu_lk lvl="1"/>` opens another level (not executed yet);
- `<disabled/>`: an item not available yet.

## Files

| File | What |
|---|---|
| `loop.py` | main loop: reads the encoder, draws the menu |
| `menu.py` | drawing of the grid, the selection and the description |
| `xmlConfigs.py` | reading of `resources/config.xml` |
| `clock.py` | stand-alone clock screen |
