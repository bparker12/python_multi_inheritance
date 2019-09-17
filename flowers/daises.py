from .flowers import Flowers
from .organic import Organic

class Daises(Organic, Flowers):

    def __init__(self):
        Organic.__init__(self)
        Flowers.__init__(self, 4)
