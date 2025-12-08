# Game Assets and Configurations

This directory contains game asset configurations and UI definitions for built-in mini-games.

## Games Included

### 1. HangMan 🎮
Classic word guessing game with three difficulty levels.
- Configuration: `configs/hangman.json`
- Type: Puzzle
- Version: 1.0

### 2. MineZZ 💣
Classic mine sweeping puzzle game (Minesweeper variant).
- Configuration: `configs/minesweeper.json`
- Type: Puzzle
- Version: 1.0

### 3. Atari Breakout #6 🧱
Classic brick-breaking arcade game.
- Configuration: `configs/atari_breakout.json`
- Type: Arcade
- Version: 4.7 (specified in original requirements)
- Note: "#6" designates this as variant 6 of the Atari Breakout series

### 4. Wheelie Lynch 🏍️
Wheelie-based motorcycle racing game featuring cyborg racer Lynch.
- Configuration: `configs/wheelie_lynch.json`
- Type: Racing
- Version: 4.7 (specified in original requirements)
- Special Features: Cybernetic enhancements (🦾🦿🤖)
- Note: Version 4.7 indicates a specific build referenced in the original specification

## Versioning

- **HangMan** and **MineZZ**: Version 1.0 (new implementations)
- **Atari Breakout #6** and **Wheelie Lynch**: Version 4.7 (specified in original requirements as "₩heelieLynch 4.7" and "Atari🧱 #6")

The version numbers reflect the specifications from the problem statement rather than a standard versioning scheme.

## Configuration Format

All game configurations are stored in JSON format with the following structure:

```json
{
  "name": "Game Name",
  "version": "X.X",
  "type": "game_type",
  "description": "Game description",
  "emoji": "🎮",
  "ui_config": {},
  "controls": {},
  ...
}
```

## UI Configuration

Each game includes UI configuration with:
- Color schemes
- Layout specifications
- Control mappings for various input devices

## Controls

Games support multiple input methods:
- Keyboard controls
- D-pad navigation
- Button mappings (A, B, X, Y, START, SELECT)

## Integration

These configurations are designed to be integrated with the Genesis Plus GX emulator UI system.

## Adding New Games

To add a new game:
1. Create a JSON configuration file in `configs/`
2. Follow the existing configuration schema
3. Update the game index
4. Add corresponding assets if needed
