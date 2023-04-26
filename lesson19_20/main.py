# Задача#
# У многих на рабочем столе есть папка, которая называется как-то вроде "Разобрать".
# Как правило, разобрать эту папку руки никогда так и не доходят.
#
# Мы с вами напишем скрипт, который разберет эту папку. В конечном итоге вы сможете настроить
# эту программу под себя и она будет выполнять индивидуальный сценарий, соответствующий вашим
# нуждам. Для этого наше приложение будет проверять расширение файла (последние символы в имени
# файла, как правило, после точки) и, в зависимости от расширения, принимать решение, к
# какой категории отнести этот файл.
#
# Скрипт принимает один аргумент при запуске — это имя папки, в которой он будет проводить
# сортировку. Допустим файл с программой называется sort.py, тогда, чтобы отсортировать
# папку /user/Desktop/Хлам, надо запустить скрипт командой python sort.py /user/Desktop/Хлам
#
# Для того чтобы успешно справится с этим заданием, вы должны вынести логику обработки папки
# в отдельную функцию.
# Чтобы скрипт мог пройти на любую глубину вложенности, функция обработки папок должна
# рекурсивно вызывать сама себя, когда ей встречаются вложенные папки.
# Скрипт должен проходить по указанной во время вызова папке и сортировать все файлы по группам:
#
# изображения ('JPEG', 'PNG', 'JPG', 'SVG');
# видео файлы ('AVI', 'MP4', 'MOV', 'MKV');
# документы ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX');
# музыка ('MP3', 'OGG', 'WAV', 'AMR');
# архивы ('ZIP', 'GZ', 'TAR');
# неизвестные расширения.
# Вы можете расширить и дополнить этот список, если хотите.
#
# В результатах работы должны быть:
#
# Список файлов в каждой категории (музыка, видео, фото и пр.)
# Перечень всех известных скрипту расширений, которые встречаются в целевой папке.
# Перечень всех расширений, которые скрипту неизвестны.
# После необходимо добавить функции, которые будут отвечать за обработку каждого типа файлов.
#
# Кроме того, все файлы и папки нужно переименовать, удалив из названия все потенциально
# приводящие к проблемам символы. Для этого надо применить к именам файлов функцию normalize.
# Следует помнить, что переименовать файлы нужно так, чтобы не изменить расширения файлов.
#
# Функция normalize:
#
# Проводит транслитерацию кириллического алфавита на латинский.  борщ -> borcsh
# Заменяет все символы кроме латинских букв, цифр на '_'.
# Требования к функции normalize:
#
# принимает на вход строку и возвращает строку;
# проводит транслитерацию кириллических символов на латиницу;
# заменяет все символы, кроме букв латинского алфавита и цифр, на символ '_';
# транслитерация может не соответствовать стандарту, но быть читабельной;
# большие буквы остаются большими, а меленькие — маленькими после транслитерации.
# Условия для обработки:#
# изображения переносим в папку images
# документы переносим в папку documents
# аудио файлы переносим в audio
# видео файлы в video
# архивы распаковываются и их содержимое переносится в папку archives
# Критерии приёма задания#
# все файлы и папки переименовываются при помощи функции normalize.
# расширения файлов не изменяются после переименования.
# пустые папки удаляются
# скрипт игнорирует папки archives, video, audio, documents, images;
# распакованное содержимое архива переносится в папку archives в подпапку, названную
# точно так же, как и архив, но без расширения в конце;
# файлы, расширения которых неизвестны, остаются без изменений.
from pathlib import Path
import shutil
import sys
from normalize import normalize  # борщ -> borsch
import file_parser as parser

def handler_files(filename: Path, target_folder: Path):
    # Створюємо папку
    target_folder.mkdir(exist_ok=True, parents=True)
    # Замінюємо шлях до файлу + перетворюємо кирилицю на литиницю
    filename.replace(target_folder / normalize(filename.name))


def handler_archive(filename: Path, target_folder: Path):
    # Створюємо папку
    target_folder.mkdir(exist_ok=True, parents=True)
    # розпаковуємо архів
    # Беремо суфікс у файла і забираємо replace(filename.suffix, '')
    folder_for_file = target_folder / normalize(filename.name.replace(filename.suffix, ''))

    # створюємо папку для архіву з іменем файла
    folder_for_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(str(filename.resolve()), str(folder_for_file.resolve()))
    except shutil.ReadError:
        print(f'Це не архів!: {filename.name}')
        folder_for_file.rmdir()
        return None
    filename.unlink()


def handler_folders(folder: Path):
    try:
        folder.rmdir()
    except OSError:
        print(f'Не вдалось видалити папку')


def main(folder: Path):
    parser.scan(folder)

    for file in parser.JPEG_IMAGES:
        handler_files(file, folder / 'images' / 'JPEG')
    for file in parser.JPG_IMAGES:
        handler_files(file, folder / 'images' / 'JPG')
    for file in parser.PNG_IMAGES:
        handler_files(file, folder / 'images' / 'PNG')
    for file in parser.SVG_IMAGES:
        handler_files(file, folder / 'images' / 'SVG')

    for file in parser.TXT_DOCUMENTS:
        handler_files(file, folder / 'documents' / 'TXT')
    for file in parser.DOC_DOCUMENTS:
        handler_files(file, folder / 'documents' / 'DOC')
    for file in parser.DOCX_DOCUMENTS:
        handler_files(file, folder / 'documents' / 'DOCX')
    for file in parser.PPTX_DOCUMENTS:
        handler_files(file, folder / 'documents' / 'PPTX')
    for file in parser.PDF_DOCUMENTS:
        handler_files(file, folder / 'documents' / 'PDF')
    for file in parser.XLSX_DOCUMENTS:
        handler_files(file, folder / 'documents' / 'XLSX')

    for file in parser.OTHER:
        handler_files(file, folder / 'OTHERS')

    for file in parser.ARCHIVES:
        handler_archive(file, folder / 'archives')

    for folder in parser.FOLDERS[::-1]:
        handler_folders(folder)


if __name__ == "__main__":
    folder_for_scan = Path(input('Input path: '))
    print(f'Start in folder {folder_for_scan}')
    main(folder_for_scan.resolve())




