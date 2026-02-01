"""
Main entry point for The Void Miner game
"""

import sys
from void_miner.core.game import Game


def main():
    """Main entry point"""
    try:
        game = Game()
        game.run()
    except Exception as e:
        print(f"Error running game: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
