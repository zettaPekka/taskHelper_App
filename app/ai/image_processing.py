import base64


def encode_image(image_file):
    return base64.b64encode(image_file).decode('utf-8')