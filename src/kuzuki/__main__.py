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

    if isinstance(exc, ImportError):
        # ran it like a script
        print(
            """
            please run this as a MODULE NOT as a script,
            with `python3 -m src.kuzuki`
        """
        )
        exit(1)
    raise exc


start_game()
