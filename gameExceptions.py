from colorama import Fore


class BoardException(Exception):
    pass


class BoardOutException(BoardException):
    def __str__(self):
        return Fore.RED+"Shooting out of board. Try again."+Fore.RESET


class BoardAlreadyFiredException(BoardException):
    def __str__(self):
        return Fore.RED+"Already shot this cell. Try again."+Fore.RESET


class BoardPlayerWinsException(BoardException):
    def __init__(self):
        print(Fore.LIGHTGREEN_EX+"╔", "="*15, "╗", sep="")
        print("║  Player win!  ║")
        print("╚", "=" * 15, "╝"+Fore.RESET, sep="")
        exit()


class BoardAiWinsException(BoardException):
    def __init__(self):
        print(Fore.LIGHTBLUE_EX+"╔", "="*11, "╗", sep="")
        print("║  AI win!  ║")
        print("╚", "=" * 11, "╝"+Fore.RESET, sep="")
        exit()

