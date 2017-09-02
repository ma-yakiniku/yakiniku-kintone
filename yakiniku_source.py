import io
from PIL import Image
import pykintone
import pykintone.structure_field as sf
from yakiniku import Yakiniku


class YakinikuSource:
    def __init__(self, domain, app, token):
        self.app = pykintone.app(domain, app, token)

    def push(self, image):
        image.save('temp.png')
        yakiniku = Yakiniku()
        yakiniku.image = [sf.File.upload('temp.png', self.app)]
        self.app.create(yakiniku)

    def pull(self):
        yakinikus = self.app.select("limit 1").models(Yakiniku)
        if len(yakinikus) <= 0:
            return None

        yakiniku = yakinikus[0]
        bytes = yakiniku.image.download(self.app)
        return Image.open(io.BytesIO(bytes))
