# UI Integration Guide

## Overview
This guide explains how to integrate the game configurations with the Genesis Plus GX emulator UI.

## Theme System

### Loading Themes
The theme system uses JSON configuration files located in `ui/themes/`.

Example usage:
```c
// Load theme configuration
Theme* load_theme(const char* theme_name) {
    char path[256];
    snprintf(path, sizeof(path), "games/ui/themes/%s.json", theme_name);
    // Parse JSON and return theme structure
}
```

### Available Themes
- **bleu_kongo_classic.json** - Dark retro gaming theme (default)

## Game Configuration Integration

### Loading Game Configs
```c
// Example: Load game configuration
GameConfig* load_game_config(const char* game_name) {
    char path[256];
    snprintf(path, sizeof(path), "games/configs/%s.json", game_name);
    // Parse JSON and return game config
}
```

### Game Index
The `game_index.json` file contains metadata for all available games:
- Game ID and name
- Configuration file path
- Game type and version
- Enable/disable status
- Special features

## UI Components

### Menu Integration
Add game selection to the main menu:

```c
typedef struct {
    int game_id;
    char* name;
    char* emoji;
    GameType type;
} GameMenuItem;

void populate_games_menu() {
    // Load game_index.json
    // Create menu items for each enabled game
    // Apply theme colors to menu
}
```

### In-Game UI
Each game configuration includes UI settings:
- Background colors
- Text colors
- HUD layout
- Control mappings

Example for Wheelie Lynch:
```c
void render_wheelie_lynch_hud() {
    Theme* theme = get_current_theme();
    GameConfig* config = get_game_config("wheelie_lynch");
    
    // Use theme->game_specific->wheelie_lynch colors
    render_speed(config->ui_config->speedometer_color);
    render_position(config->ui_config->position_indicator_color);
}
```

## Control Mapping

### Input Handling
Each game defines control mappings in JSON:

```json
{
  "controls": {
    "move_left": "D-pad left or left key",
    "move_right": "D-pad right or right key"
  }
}
```

Implement input handling:
```c
void handle_input(GameConfig* config, InputEvent event) {
    // Map physical inputs to game actions
    // Based on config->controls
}
```

## Asset Loading

### Asset Directory Structure
```
games/ui/assets/
├── icons/          # Game icons and emojis
├── sprites/        # Game sprites
├── backgrounds/    # Background images
└── fonts/          # Custom fonts
```

### Loading Assets
```c
void load_game_assets(const char* game_name) {
    char asset_path[256];
    snprintf(asset_path, sizeof(asset_path), "games/ui/assets/%s/", game_name);
    // Load sprites, icons, etc.
}
```

## Rendering Pipeline

### Game Rendering Flow
1. Load game configuration
2. Apply theme
3. Initialize game state
4. Render loop:
   - Clear screen (background color from theme)
   - Render game elements
   - Render HUD
   - Apply effects/animations

### Example Render Loop
```c
void game_render_loop(GameConfig* config, Theme* theme) {
    while (game_running) {
        clear_screen(theme->global->primary_bg);
        
        // Render game-specific content
        switch(config->type) {
            case GAME_PUZZLE:
                render_puzzle_game(config, theme);
                break;
            case GAME_ARCADE:
                render_arcade_game(config, theme);
                break;
            case GAME_RACING:
                render_racing_game(config, theme);
                break;
        }
        
        render_ui_overlay(config, theme);
        swap_buffers();
    }
}
```

## Platform-Specific Notes

### Libretro Integration
For libretro builds, use RetroArch's rendering API:
```c
void libretro_render_game(GameConfig* config) {
    // Use video_cb for rendering
    // Use input_poll_cb for controls
}
```

### GameCube/Wii Integration
For GX builds, use the existing GUI framework:
```c
void gx_render_game(GameConfig* config) {
    // Use GX graphics API
    // Map controls to GameCube/Wii controller
}
```

### SDL Integration
For SDL builds:
```c
void sdl_render_game(GameConfig* config, SDL_Renderer* renderer) {
    // Use SDL2 rendering functions
    // Handle SDL events for input
}
```

## Testing

### Validation Checklist
- [ ] All JSON configs parse correctly
- [ ] Theme colors display properly
- [ ] Controls map to correct actions
- [ ] Game logic works as expected
- [ ] UI scales correctly on different resolutions
- [ ] Performance is acceptable (60 FPS target)

### Test Each Game
```bash
# Validate JSON configs
python3 -m json.tool games/configs/hangman.json
python3 -m json.tool games/ui/themes/bleu_kongo_classic.json

# Test game loading
./test_game_loader hangman
./test_game_loader minesweeper
./test_game_loader atari_breakout
./test_game_loader wheelie_lynch
```

## Future Enhancements
- Additional themes (light mode, high contrast)
- Custom asset packs
- Savegame system
- High score tracking
- Multiplayer support
- Additional mini-games
