import base64
import os

def image_to_base64(filepath: str) -> str:
    with open(filepath, 'rb') as f:
        ctx = base64.b64encode(f.read())
    return str(ctx)[2: -1]
