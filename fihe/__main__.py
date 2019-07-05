from .remove_duplication import duplicates, remove_duplicates
from .images import image_to_base64, compress_image
import argparse
import os


parser = argparse.ArgumentParser(description="File Helper")
sub_parsers = parser.add_subparsers()

# file operation
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


dedu_parser = sub_parsers.add_parser(name="dedu", help="deduplication")
dedu_sub_parser = dedu_parser.add_subparsers()
ls_parser = dedu_sub_parser.add_parser(name="ls", help="list duplicates")
ls_parser.add_argument("--root-dir",
                    type=str,
                    help="the root directory that is needed to show duplicates.")
ls_parser.set_defaults(func=ls)
rm_parser = dedu_sub_parser.add_parser(name="rm", help="remove duplicates")
rm_parser.add_argument("--root-dir",
                    type=str,
                    help="the root directory that is needed to remove duplicates.")
rm_parser.add_argument("--target-dir",
                    type=str,
                    help="the target directory that all duplicates are moved into.")
rm_parser.set_defaults(func=rm)


# image operation
def its(p_args):
    filepath = str(p_args.file_path)
    if os.path.isfile(filepath):
        print(image_to_base64(filepath))
    else:
        print("File {0} is not found!".format(filepath))


def ci(p_args):
    input_filepath = str(p_args.input)
    if not os.path.isfile(input_filepath):
        print("File {0} is not found!".format(input_filepath))
        return
    quality = int(p_args.quality)
    out, size = compress_image(input_filepath, quality)
    print("File has been compressed in {0} with {1} KB.".format(out, size))


image_parser = sub_parsers.add_parser(name="image", help="image operation")
image_sub_parser = image_parser.add_subparsers()
its_parser = image_sub_parser.add_parser(name="its", help="converting image to a string (base64)")
its_parser.add_argument("--file-path",
                    type=str,
                    help="image path.")
its_parser.set_defaults(func=its)
ci_parser = image_sub_parser.add_parser(name="ci", help="compressing image")
ci_parser.add_argument("--input",
                    type=str,
                    help="image path.")
ci_parser.add_argument("--quality",
                    type=str,
                    default=100,
                    help="compressed image quality in (0, 100], default 100.")                
ci_parser.set_defaults(func=ci)


def main():
    p_args = parser.parse_args()
    if hasattr(p_args, "func"):
        p_args.func(p_args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
