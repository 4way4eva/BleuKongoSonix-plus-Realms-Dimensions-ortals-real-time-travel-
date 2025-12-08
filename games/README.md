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
- Version: 4.7

### 4. Wheelie Lynch 🏍️
Wheelie-based motorcycle racing game featuring cyborg racer Lynch.
- Configuration: `configs/wheelie_lynch.json`
- Type: Racing
- Version: 4.7
- Special Features: Cybernetic enhancements (🦾🦿🤖)

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
