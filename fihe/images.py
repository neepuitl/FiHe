from PIL import Image
import os
import base64


def get_kb_size(filepath: str) -> float:
    return os.path.getsize(filepath) / 1024


def get_output_filepath(input_filepath: str) -> str:
    directory, suffix = os.path.splitext(input_filepath)
    output_filepath = '{0}-out{1}'.format(directory, suffix)
    return output_filepath


def compress_image(input_filepath: str, 
                   quality: int) -> tuple:
    if not isinstance(quality, int) or quality <=0 or quality > 100:
        print("Quality must be in (0, 100] with integer.")
    output_filepath = get_output_filepath(input_filepath)
    im = Image.open(input_filepath)
    im.save(output_filepath, quality=quality)
    return output_filepath, get_kb_size(output_filepath)

def image_to_base64(filepath: str) -> str:
    with open(filepath, 'rb') as f:
        ctx = base64.b64encode(f.read())
    return str(ctx)[2: -1]
