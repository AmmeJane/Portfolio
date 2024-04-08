#making executable
import sys
from cx_Freeze import setup, Executable
import sys

executables = [Executable("THEREALGAME.py")]

setup(
    name="pythonGame",
    options={"build_exe": {"packages":["pygame"],
                       "include_files":[
                           "store.py",
                           "ship.py",
                           "settings.py",
                           "scoreboard.py",
                           "rewards.py",
                           "gameFunctions.py",
                           "fireball.py",
                           "fire.py",
                           "buttons.py",
                           "blocks.py",
                           "endGame.py",
                           "userInstructions.py",
                           "images/",
                           "LeaderboardFile.txt",
                           "CurrencyFile.txt",]}},
    executables = executables

)
#in cmd prompt made of folder dict write python setup.py build