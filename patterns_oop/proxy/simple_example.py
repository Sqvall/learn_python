class Image:
    def __init__(self, filename):
        self.filename = filename

    def load_image_from_disk(self):
        print("loading " + self.filename)

    def display_image(self):
        print("display " + self.filename)


class Proxy:
    def __init__(self, subject):
        self._subject = subject
        self._proxy_state = None


class ProxyImage(Proxy):
    def display_image(self):
        if self._proxy_state is None:
            self._subject.load_image_from_disk()
            self._proxy_state = 1
        print("display " + self._subject.filename)


proxy_image1 = ProxyImage(Image("HiRes_10Mb_Photo1"))
proxy_image2 = ProxyImage(Image("HiRes_10Mb_Photo2"))

proxy_image1.display_image()  # loading necessary
proxy_image1.display_image()  # loading unnecessary
print()
proxy_image2.display_image()  # loading necessary
proxy_image2.display_image()  # loading unnecessary
print()
proxy_image1.display_image()  # loading unnecessary
