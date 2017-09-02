from pykintone import model
import pykintone.structure_field as sf

class Yakiniku(model.kintoneModel):
    def __init__(self):
        super(Yakiniku, self).__init__()
        self.imageId = None
        self.createdAt = None
        self.image = [sf.File()]
