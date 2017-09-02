from PIL import Image

from yakiniku_service import YakinikuService

service = YakinikuService("7nkse", "app 61 token", "app 64 token")

# Client PC
# upload pillow original image
service.original().push(Image.open("sample.png"))
# get pillow marker image
image = service.marker().pull()

# Server
# get pillow origina image
image = service.original().pull()
# upload pillow marker image
service.marker().push(Image.open("sample.png"))
