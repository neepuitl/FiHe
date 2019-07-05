from .remove_duplication import duplicates, remove_duplicates
from .image_to_string import image_to_base64
import argparse
import os


def drm(p_args):
    rootdir = str(p_args.root_dir)
    if not os.path.isdir(rootdir):
        print("Please input the correct root directory!")
        return
    target_dir = str(p_args.target_dir)
    if not os.path.isdir(target_dir):
        print("Please input the correct target directory!")
        return
    file_duplicates = duplicates(rootdir)
    remove_duplicates(file_duplicates, target_dir)


def dls(p_args):
    rootdir = str(p_args.root_dir)
    if not os.path.isdir(rootdir):
        print("Please input the correct root directory!")
        return
    file_duplicates = duplicates(rootdir)
    for key, value in file_duplicates.items():
        print("** Duplicated files, Count: {0}, SHA1 value: {1} **".format(len(value), key))
        for i, fn in enumerate(value):
            print("No: {0}, Path: {1}".format(i + 1, fn))


def its(p_args):
    filepath = str(p_args.file_path)
    if os.path.isfile(filepath):
        print(image_to_base64(filepath))
    else:
        print("File {0} is not found!".format(filepath))


parser = argparse.ArgumentParser(description="File Helper")

sub_parsers = parser.add_subparsers()
ls_parser = sub_parsers.add_parser(name="dls", help="list duplicates")
ls_parser.add_argument("--root-dir",
                    type=str,
                    help="the root directory that is needed to show duplicates.")
ls_parser.set_defaults(func=dls)

dedu_parser = sub_parsers.add_parser(name="drm", help="remove duplicates")
dedu_parser.add_argument("--root-dir",
                    type=str,
                    help="the root directory that is needed to remove duplicates.")
dedu_parser.add_argument("--target-dir",
                    type=str,
                    help="the target directory that all duplicates are moved into.")
dedu_parser.set_defaults(func=drm)

its_parser = sub_parsers.add_parser(name="its", help="image to ecoding string (base64)")
its_parser.add_argument("--file-path",
                    type=str,
                    help="image path.")
its_parser.set_defaults(func=its)


def main():
    p_args = parser.parse_args()
    if hasattr(p_args, "func"):
        p_args.func(p_args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
