import argparse
import shutil
from pathlib import Path


def copy_file(file_path, output_folder):
    extension = file_path.suffix.lower()

    if extension:
        folder_name = extension[1:]
    else:
        folder_name = "no_extension"

    destination_folder = output_folder / folder_name
    destination_folder.mkdir(parents=True, exist_ok=True)

    destination_file = destination_folder / file_path.name

    try:
        shutil.copy2(file_path, destination_file)
        print(f"Скопійовано: {file_path} -> {destination_file}")
    except OSError as error:
        print(f"Помилка копіювання {file_path}: {error}")


def read_directory(source_folder, output_folder):
    try:
        for item in source_folder.iterdir():
            if item.resolve() == output_folder.resolve():
                continue

            if item.is_dir():
                read_directory(item, output_folder)
            elif item.is_file():
                copy_file(item, output_folder)

    except OSError as error:
        print(f"Помилка читання директорії {source_folder}: {error}")


def main():
    parser = argparse.ArgumentParser(
        description="Рекурсивне копіювання файлів за розширеннями"
    )

    parser.add_argument("source", help="Шлях до вихідної директорії")
    parser.add_argument(
        "destination",
        nargs="?",
        default="dist",
        help="Шлях до директорії призначення (за замовчуванням dist)"
    )

    args = parser.parse_args()

    source_folder = Path(args.source).resolve()
    output_folder = Path(args.destination).resolve()

    if not source_folder.is_dir():
        print("Помилка: вихідна директорія не існує.")
        return

    if source_folder == output_folder:
        print("Помилка: директорії джерела та призначення мають бути різними.")
        return

    try:
        output_folder.mkdir(parents=True, exist_ok=True)
    except OSError as error:
        print(f"Не вдалося створити директорію призначення: {error}")
        return

    read_directory(source_folder, output_folder)

    print("Копіювання завершено.")


if __name__ == "__main__":
    main()
