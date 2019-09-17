class Arrangement:

    def __init__(self):
        self.flowers = list()

    def enhance(self, flower):
        self.flowers.append(flower)


class MothersDay(Arrangement):

    def __init__(self):
        super().__init__()

    def enhance(self, flower):
        if flower.Organic == True:
            super().enhance(flower.name)
            for flower in self.flowers:
                 print(f'{flower}s are in valentines day arrangements.')
        else:
            print(f'Please only add organic flowers to this arrangement, {flower.name} is not organic')



class ValentinesDay(Arrangement):
    def __init__(self):
        super().__init__()

    def enhance(self, flower):
        if flower.Organic == False:
            super().enhance(flower.name)
            for flower in self.flowers:
                 print(f'{flower}s are in valentines day arrangements.')
        else:
            print(f'Please only add non-organic flowers to this arrangement, {flower.name} is organic')

class Flower():

    def __init__(self, stem):
        self.stem_length = stem
        self.name = self.__class__.__name__

class Organic():

    def __init__(self, blah=True):
        self.Organic = blah


class Lilly(Flower,Organic):
    def __init__(self):
        Flower.__init__(self, 7)
        Organic.__init__(self, False)

class Rose(Flower, Organic):
    def __init__(self):
        Flower.__init__(self, 7)
        Organic.__init__(self, False)
        self.color = ["red", "pink", "blue"]

class Alstroemeria(Flower, Organic):

    def __init__(self):
        Organic.__init__(self, False)
        Flower.__init__(self, 7)

class Daisy(Organic, Flower):

    def __init__(self):
        Organic.__init__(self)
        Flower.__init__(self, 4)

class Baby_breath(Flower, Organic):

    def __init__(self):
        Organic.__init__(self)
        Flower.__init__(self, 4)


class Poppy(Flower, Organic):

    def __init__(self):
        Organic.__init__(self)
        Flower.__init__(self, 4)


mothers_day = MothersDay()
valentines = ValentinesDay()

breath = Baby_breath()
daisyflower = Daisy()
popflower = Poppy()
red_rose = Rose()
lils = Lilly()

mothers_day.enhance(daisyflower)
mothers_day.enhance(breath)
mothers_day.enhance(popflower)
mothers_day.enhance(red_rose)

valentines.enhance(daisyflower)
valentines.enhance(red_rose)
valentines.enhance(lils)

if __name__ == "__main__":
    for_beth = ValentinesDay()
    red_rose = Rose()
    poppy = Poppy()

    for_beth.flowers.append(red_rose)