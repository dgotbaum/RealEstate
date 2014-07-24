class Tract:
    def __init__(self, key, value, borough, neighborhood ):
        self.brgh = borough
        self.nbrhd = neighborhood
        self.val = value
        self.key = key.split("_")[1]
        self.block = int(self.key.split(".")[1])
        self.tract = int(self.key.split(".")[0])



