try:
    from .start_game import start_game
except ImportError as exc:
    if isinstance(exc, ModuleNotFoundError):
        # dependencies are missing
        print(
            """
            please install dependensies first with,
            `pip3 install -r requirements.txt`
            """
        )
        exit(1)

    print(
        """
        please run this as a MODULE NOT as a script,
        with `python3 -m src.kuzuki`
        """
    )
    # BUG: circular import will also print above statement
    exit(1)


start_game()
