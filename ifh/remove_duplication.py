import hashlib
import os
import pprint


def calcsha1(filepath: str) -> str:
    sha1 = hashlib.sha1()
    with open(filepath, "rb") as f:
        while True:
            content = f.read(8096)
            if not content:
                break
            else:
                sha1.update(content)
    return sha1.hexdigest()


def dfs(rootdir: str) -> list:
    file_sha1s: list = []
    files_or_dirs = os.listdir(rootdir)
    for file_or_dir in files_or_dirs:
        file_or_dir_path = os.path.join(rootdir, file_or_dir)
        if os.path.isdir(file_or_dir_path) and not file_or_dir.startswith("."):
            file_sha1s.extend(
                dfs(file_or_dir_path)
            )
        elif os.path.isfile(file_or_dir_path) and not file_or_dir.startswith("."):
            file_sha1s.append({
                "path": file_or_dir_path,
                "sha1": calcsha1(file_or_dir_path)
            })
    return file_sha1s


def duplicates(rootdir: str) -> dict:
    file_sha1s = dfs(rootdir)
    file_duplicates = {}
    for fs in file_sha1s:
        if fs["sha1"] not in file_duplicates.keys():
            file_duplicates[fs["sha1"]] = []
        file_duplicates[fs["sha1"]].append(fs["path"])
    should_be_removed = []
    for key in file_duplicates.keys():
        if len(file_duplicates[key]) == 1:
            should_be_removed.append(key)
    for key in should_be_removed:
        file_duplicates.pop(key)
    return file_duplicates


def copy_file(source_file: str, target_dir: str) -> None:
    if os.path.isfile(source_file) and os.path.isdir(target_dir):
        target_file = os.path.join(
            target_dir, os.path.basename(source_file)
        )
        open(target_file, "wb").write(open(source_file, "rb").read())
        os.remove(source_file)
        print("{0} has been moved in {1}".format(
            source_file, target_file
        ))

def remove_duplicates(file_duplicates: dict, target_dir: str) -> None:
    for _, value in file_duplicates.items():
        print("# original file: {0}".format(value[0]))
        for filepath in value[1:]:
            copy_file(filepath, target_dir)
