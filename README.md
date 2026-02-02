# MADPAD
MADPAD is my kinda printed pad  inspired Hackpad version that looks pretty sweet and hopefully runs just as smooth as it looks ( > .> )
## Features

- Seeed XIAO RP2040 microcontroller  
- 0.91" I2C OLED display  
- 3x3 mechanical key layout 
- Direct wiring for every key  

## Hackpad Overview

This shows the full assembly of MADPAD in Fusion 360.  
It demonstrates how the PCB, case, and components fit together.


## Schematic
<img width="647" height="349" alt="Schematics " src="https://github.com/user-attachments/assets/67bfd5a5-4306-4ef2-a5ee-91fac74a1e4a" />

The schematic was designed in KiCad.  
Each switch connects directly to the RP2040.  
The OLED follows GND, VCC, SCL, SDA pin order.

## PCB Layout

The PCB was designed in KiCad PCB Editor.  
It shows component placement and routing.  
The layout focuses on clarity and simplicity.

<img width="590" height="489" alt="MADPAD pcb" src="https://github.com/user-attachments/assets/1e6c22fb-8b5e-408d-8cfb-75f2e00d9f1b" />


## Case Design
<img width="688" height="283" alt="cASE wITH lID" src="https://github.com/user-attachments/assets/d82fdb8a-7ddb-4b2c-acbe-6fd12c1f1452" />

<img width="688" height="421" alt="MADPAD cASED" src="https://github.com/user-attachments/assets/8fecf76a-5854-4f35-9342-12a4edf5d370" />

## Forgot To Mention But the top of the hackpad is made using cut clear acrylic panel that is why it is left hollow ( Grants Required for acrylic panel )

The case was designed in Free Cad .  
Dimensions were taken directly from the PCB.  
All parts were test-fit using 3D models.

## Bill of Materials

| Part | Quantity | Description |
|------|----------|-------------|
| Mechanical key switches | 9 | MX-style |
| Keycaps | 9 | MX-compatible |
| Seeed XIAO RP2040 | 1 | Microcontroller |
| OLED display (0.91") | 1 | I2C |
| PCB | 1 | Double-sided |
| Case | 1 | 3D printed |

## Firmware Instructions

### Flashing

1. Install CircuitPython `.uf2`.
2. Enter bootloader mode.
3. Copy the `.uf2` to the board.

### Libraries

1. Download CircuitPython library bundle.
2. Copy `displayio`, `display_text`, `debouncer`, and `HID`.
3. Upload `code.py`.
4. Test all inputs.

## License

This project is open source under the MIT License.
