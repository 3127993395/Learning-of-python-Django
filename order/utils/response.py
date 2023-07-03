class BaseResponse(object):
    def __init__(self, status=False, detail=None, data=None):
        self.status = status
        self.detail = detail
        self.data = data

    @property
    def dict(self):
        return self.__dict__
