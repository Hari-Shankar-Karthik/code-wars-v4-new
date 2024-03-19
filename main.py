from engine.main import Game
import scriptred, scriptblue, hari_script

if __name__ == "__main__":
    G = Game((40, 40), hari_script, hari_script)
    G.run_game()