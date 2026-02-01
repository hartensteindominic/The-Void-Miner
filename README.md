# The Void Miner

A space mining adventure game built with Python and Pygame.

## Description

The Void Miner is an indie game where you explore the void of space, mining asteroids and collecting resources. Navigate your spacecraft through asteroid fields, gather precious materials, and upgrade your mining equipment.

## Features

- Space-themed mining gameplay
- Built with Python and Pygame
- Extensible architecture for future development
- Cross-platform support (Windows, macOS, Linux)

## Requirements

- Python 3.8 or higher
- pygame 2.5.0 or higher

## Installation

### Quick Start

1. Clone the repository:
```bash
git clone https://github.com/hartensteindominic/The-Void-Miner.git
cd The-Void-Miner
```

2. Run the build script:

**Linux/macOS:**
```bash
./build.sh
```

**Windows:**
```cmd
build.bat
```

### Manual Installation

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:

**Linux/macOS:**
```bash
source venv/bin/activate
```

**Windows:**
```cmd
venv\Scripts\activate.bat
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install the package:
```bash
pip install -e .
```

## Running the Game

After installation, you can run the game using:

```bash
void-miner
```

Or:

```bash
python -m void_miner
```

## Controls

- **ESC** - Exit the game

## Development

### Project Structure

```
The-Void-Miner/
├── src/
│   └── void_miner/
│       ├── __init__.py
│       ├── __main__.py
│       ├── core/          # Core game engine
│       │   ├── __init__.py
│       │   └── game.py
│       ├── entities/      # Game entities (player, asteroids, etc.)
│       ├── ui/            # User interface components
│       └── utils/         # Utility functions
├── assets/
│   ├── images/           # Game sprites and textures
│   ├── sounds/           # Sound effects and music
│   └── fonts/            # Custom fonts
├── docs/                 # Additional documentation
├── tests/                # Unit tests
├── build.sh              # Linux/macOS build script
├── build.bat             # Windows build script
├── requirements.txt      # Python dependencies
├── setup.py              # Package configuration
└── README.md            # This file
```

### Building from Source

To build the project from source:

1. Follow the installation steps above
2. Make your changes to the source code
3. Test your changes by running the game

### Running Tests

```bash
python -m unittest discover tests/ -v
```

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

Built with Python and Pygame
