Ping Pong Game

A simple two-player Ping Pong game built with Python's Turtle module. Enjoy fast-paced gameplay where each player controls a paddle to bounce the ball and score points!

Description

This classic Ping Pong game features:
- Two-player gameplay
- Custom paddle controls
- Real-time score tracking
- Smooth ball and paddle movement

The game uses Python's built-in Turtle graphics library to render the game window, paddles, ball, and score.

Requirements

- Python 3.x** (Tested with Python 3.13)
- The **turtle** module (included with Python)
  
 Installation

1. Clone or Download the Repository :

   ```bash
   git clone https://github.com/yourusername/ping-pong-game.git
   ```

   Or simply download the ZIP file and extract it.

2. Navigate to the Game Directory :

   ```bash
   cd ping-pong-game
   ```

3. Run the Game :

   ```bash
   python ping_pong.py
   ```

How to Play

- Left Paddle Controls :  
  - `W` key: Move paddle up
  - `S` key: Move paddle down

- **Right Paddle Controls:**  
  - `Up Arrow` key: Move paddle **up**
  - `Down Arrow` key: Move paddle **down**

- **Objective:**  
  Prevent the ball from passing your paddle. Each time the ball passes the opponent's paddle, you score a point. The score is displayed at the top of the window.

## Troubleshooting

- **Error:** `_tkinter.TclError: invalid command name ".!canvas"`  
  **Cause:** This error may occur if the game window is closed manually during gameplay.  
  **Solution:** The game loop is designed to handle window closures gracefully and will print "Game closed gracefully." in the console.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Author

- [Mohamed Eid] (https://github.com/mohamedammareid)

## Acknowledgments

- Python Turtle documentation
- Various online tutorials and community contributions for Python game development
```
