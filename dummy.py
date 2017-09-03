import os
from time import sleep

from PIL import Image

from yakiniku_service_factory import create

service = create()


def upload(index):
    name = os.path.join("samples", str(index) + ".jpg")

    if not os.path.exists(name):
        return None

    return Image.open(name)


index = 1
image = None
while True:
    result = upload(index)

    if result is not None:
        index += 1
        image = result

    service.original().push(image)
    print(index - 1, image)

    sleep(10)
