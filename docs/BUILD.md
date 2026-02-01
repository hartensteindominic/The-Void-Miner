# Building The Void Miner

This guide explains how to build The Void Miner from source.

## Prerequisites

Before building, ensure you have:

- Python 3.8 or higher installed
- pip package manager
- git (for cloning the repository)

## Build Methods

### Method 1: Using Build Scripts (Recommended)

The easiest way to build the project is using the provided build scripts.

#### Linux/macOS

```bash
./build.sh
```

This script will:
1. Create a virtual environment
2. Install all dependencies
3. Install the package in development mode

#### Windows

```cmd
build.bat
```

This script performs the same steps as the Linux/macOS version.

### Method 2: Manual Build

If you prefer to build manually or need more control:

1. **Create Virtual Environment**
   ```bash
   python -m venv venv
   ```

2. **Activate Virtual Environment**
   
   Linux/macOS:
   ```bash
   source venv/bin/activate
   ```
   
   Windows:
   ```cmd
   venv\Scripts\activate.bat
   ```

3. **Upgrade pip**
   ```bash
   pip install --upgrade pip
   ```

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Install Package**
   
   Development mode (recommended for development):
   ```bash
   pip install -e .
   ```
   
   Or regular installation:
   ```bash
   pip install .
   ```

## Verifying the Build

After building, verify the installation:

```bash
void-miner --version  # Check if command is available
python -m void_miner  # Alternative way to run
```

## Troubleshooting

### pygame Installation Issues

If you encounter issues installing pygame:

1. **Linux**: Install SDL dependencies
   ```bash
   sudo apt-get install python3-dev libsdl2-dev libsdl2-image-dev \
                        libsdl2-mixer-dev libsdl2-ttf-dev
   ```

2. **macOS**: Install via Homebrew
   ```bash
   brew install sdl2 sdl2_image sdl2_mixer sdl2_ttf
   ```

3. **Windows**: pygame should install without issues via pip

### Virtual Environment Issues

If virtual environment activation fails:

- **Linux/macOS**: Ensure the script has execute permissions
  ```bash
  chmod +x build.sh
  ```

- **Windows**: Run Command Prompt as Administrator

### Python Version Issues

Ensure you're using Python 3.8 or higher:
```bash
python --version
```

If multiple Python versions are installed, you may need to use `python3` instead of `python`.

## Building for Distribution

To create a distributable package:

```bash
python setup.py sdist bdist_wheel
```

This creates distribution files in the `dist/` directory.

## Clean Build

To clean build artifacts:

```bash
rm -rf build/ dist/ *.egg-info
```

Or on Windows:
```cmd
rmdir /s /q build dist
del /s /q *.egg-info
```

## Next Steps

After building, see the main README.md for instructions on running the game.
