try:
    from .start_game import start_game
except ImportError:
    print(
        """
        please run this as a MODULE NOT as a script,
        with `python -m src.kuzuki`
    """
    )
    exit(1)


start_game()
