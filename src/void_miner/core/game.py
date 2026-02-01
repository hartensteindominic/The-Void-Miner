"""
Main game class for The Void Miner
"""

import pygame
import sys


class Game:
    """Main game class that manages the game loop and state"""
    
    def __init__(self, width=800, height=600, fps=60):
        """
        Initialize the game
        
        Args:
            width: Screen width in pixels
            height: Screen height in pixels
            fps: Target frames per second
        """
        pygame.init()
        self.width = width
        self.height = height
        self.fps = fps
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("The Void Miner")
        self.clock = pygame.time.Clock()
        self.running = False
        
    def handle_events(self):
        """Handle pygame events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
    
    def update(self, dt):
        """
        Update game state
        
        Args:
            dt: Delta time since last frame in seconds
        """
        pass
    
    def render(self):
        """Render the game"""
        self.screen.fill((0, 0, 0))  # Clear screen with black
        
        # Draw title text
        font = pygame.font.Font(None, 74)
        text = font.render("The Void Miner", True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.width // 2, self.height // 2 - 50))
        self.screen.blit(text, text_rect)
        
        # Draw instructions
        font_small = pygame.font.Font(None, 36)
        instructions = font_small.render("Press ESC to exit", True, (200, 200, 200))
        inst_rect = instructions.get_rect(center=(self.width // 2, self.height // 2 + 50))
        self.screen.blit(instructions, inst_rect)
        
        pygame.display.flip()
    
    def run(self):
        """Main game loop"""
        self.running = True
        print("Starting The Void Miner...")
        print("Press ESC to exit")
        
        while self.running:
            dt = self.clock.tick(self.fps) / 1000.0  # Convert to seconds
            
            self.handle_events()
            self.update(dt)
            self.render()
        
        pygame.quit()
        print("Game closed successfully")
