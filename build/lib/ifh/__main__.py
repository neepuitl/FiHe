from .remove_duplication import duplicates, remove_duplicates
import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument("--root-dir",
                    type=str,
                    help="the root directory that is needed to remove duplicates.")
parser.add_argument("--target-dir",
                    type=str,
                    help="the target directory that all duplicates are moved into.")
p_args = parser.parse_args()


def main():
    rootdir = str(p_args.root_dir)
    if not os.path.isdir(rootdir):
        print("Please input the correct root directory!")
        return
    target_dir = str(p_args.target_dir)
    if not os.path.isdir(rootdir):
        os.makedirs(target_dir)
    file_duplicates = duplicates(rootdir)
    remove_duplicates(file_duplicates, target_dir)


if __name__ == "__main__":
    main()
