from pathlib import Path


p = Path('C:/Users/pc/Desktop/заняття/hw_timoha/lesson13')

def parse_folder(path: Path) -> None:
    for el in path.iterdir():
        if el.is_dir():
            print(f'This is folder {el.name}')
        else:
            print(f'This is file {el.name}')


def parse_file(path: Path) -> None:
    for el in path.iterdir():
        if el.is_dir():
            parse_file(el)
        else:
            print(f'This is file: {el.name}')


if __name__ == "__main__":
    parse_folder(p)