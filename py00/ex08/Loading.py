import os


def ft_tqdm(lst: range) -> None:
    """
    docstring
    """
    size = len(lst)
    width = os.get_terminal_size().columns
    bar_width = width - 40
    for i, x in enumerate(lst, start=1):
        progress = i * 100 // size
        bar_progress = i * bar_width // size
        percentage = f"{progress:>3}"
        bar = f"{'=' * bar_progress:<{bar_width}}"
        print(f"\r{percentage}%|{bar}| {i}/{size}", end="", flush=True)
        yield i
