import shutil

            
# just for beauty and decoration


def print_welcome():
    width = shutil.get_terminal_size(fallback=(80, 20)).columns

    title = "<=: WELCOME TO MESSAGE LOG :=>"
    line = "_" * len(title)

    print("\n" + title.center(width))
    print(line.center(width) + "\n")


def print_messaging_banner():
    width = shutil.get_terminal_size(fallback=(80, 20)).columns

    title = "<=: Welcome to the messaging world :=>"
    underline = "_" * len(title)

    print("\n" + title.center(width))
    print(underline.center(width) + "\n")