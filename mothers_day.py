from ucle_jakes_flower_shop import Arrangement

# mother's day incluc=des: daises, babys breath, poppies

class MothersDay(Arrangement):

    def __init__(self):
        super().__init__()

    # Override the `enhance` method to ensure only
    # roses, lillies, and alstroemeria can be added