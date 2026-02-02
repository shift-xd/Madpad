# MADPAD
MADPAD is my kinda printed pad  inspired Hackpad version that looks pretty sweet and hopefully runs just as smooth as it looks (>_>)
## Features

- Seeed XIAO RP2040 microcontroller  
- 0.91" I2C OLED display  
- 3x3 mechanical key layout 
- Direct wiring for every key  

## Hackpad Overview

This shows the full assembly of MADPAD in Fusion 360.  
It demonstrates how the PCB, case, and components fit together.


## Schematic

<img width="713" height="394" alt="Pasted image" src="https://github.com/user-attachments/assets/06b95682-f3e4-4ce9-940d-0b761ee2572f" />

The schematic was designed in KiCad.  
Each switch connects directly to the RP2040.  
The OLED follows GND, VCC, SCL, SDA pin order.

## PCB Layout

The PCB was designed in KiCad PCB Editor.  
It shows component placement and routing.  
The layout focuses on clarity and simplicity.

<img width="345" height="428" alt="Screenshot From 2026-02-02 14-22-07" src="https://github.com/user-attachments/assets/a5780475-1dca-450f-a9c3-a8e362f04fab" />

## Case Design
<img width="713" height="448" alt="Screenshot From 2026-02-02 15-53-24" src="https://github.com/user-attachments/assets/6ae33323-6305-462d-86f0-c3ef35f16336" />


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
