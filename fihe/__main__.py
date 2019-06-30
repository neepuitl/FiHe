from .remove_duplication import duplicates, remove_duplicates
import argparse
import os


def rm(p_args):
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


def ls(p_args):
    rootdir = str(p_args.root_dir)
    if not os.path.isdir(rootdir):
        print("Please input the correct root directory!")
        return
    file_duplicates = duplicates(rootdir)
    for key, value in file_duplicates.items():
        print("** Duplicated files, Count: {0}, SHA1 value: {1} **".format(len(value), key))
        for i, fn in enumerate(value):
            print("No: {0}, Path: {1}".format(i + 1, fn))


parser = argparse.ArgumentParser(description="File Helper")
sub_parsers = parser.add_subparsers()
ls_parser = sub_parsers.add_parser(name="ls", help="list duplicates")
ls_parser.add_argument("--root-dir",
                    type=str,
                    help="the root directory that is needed to show duplicates.")
ls_parser.set_defaults(func=ls)
dedu_parser = sub_parsers.add_parser(name="rm", help="remove duplicates")
dedu_parser.add_argument("--root-dir",
                    type=str,
                    help="the root directory that is needed to remove duplicates.")
dedu_parser.add_argument("--target-dir",
                    type=str,
                    help="the target directory that all duplicates are moved into.")
dedu_parser.set_defaults(func=rm)


def main():
    p_args = parser.parse_args()
    if hasattr(p_args, "func"):
        p_args.func(p_args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
