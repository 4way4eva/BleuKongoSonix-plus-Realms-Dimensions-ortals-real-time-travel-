# UI Assets Directory

This directory contains visual assets for the game collection.

## Directory Structure

```
assets/
├── icons/          # Game icons and menu symbols
├── sprites/        # Game sprites and animations
├── backgrounds/    # Background images and patterns
└── fonts/          # Custom fonts (if needed)
```

## Asset Guidelines

### Icons
- Format: PNG with transparency
- Size: 64x64 px (standard), 128x128 px (high-res)
- Naming: `{game_name}_icon.png`

### Sprites
- Format: PNG with transparency
- Size: Variable based on game requirements
- Naming: `{game_name}_{sprite_name}.png`

### Backgrounds
- Format: PNG or JPEG
- Size: 640x480 px (Genesis resolution), scalable
- Naming: `{game_name}_bg.png`

### Fonts
- Format: TTF or OTF
- Should include full ASCII character set
- Monospace preferred for retro aesthetic

## Usage

Assets are loaded based on the game configuration:

```c
char icon_path[256];
snprintf(icon_path, sizeof(icon_path), 
         "games/ui/assets/icons/%s_icon.png", game_name);
```

## Creating New Assets

When adding new games:
1. Create a subdirectory for each asset type if needed
2. Follow naming conventions
3. Optimize file sizes for embedded systems
4. Test on target platforms (GameCube, Wii, etc.)

## Placeholder Assets

Currently, this directory serves as a placeholder for future asset integration.
Actual sprite and image assets should be added based on specific implementation needs.
