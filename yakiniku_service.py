from yakiniku_source import YakinikuSource


class YakinikuService:
    def __init__(self, domain, originalToken, markerToken):
        self.domain = domain
        self.originalToken = originalToken
        self.markerToken = markerToken

    def original(self):
        return YakinikuSource(self.domain, "61", self.originalToken)

    def marker(self):
        return YakinikuSource(self.domain, "64", self.markerToken)
