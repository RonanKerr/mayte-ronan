class Address:

    def __init__(self, line1, line2, city, postcode):
        self.line1 = line1
        self.line2 = line2
        self.city = city
        self.postcode = postcode

    def __repr__(self):
        return f'    {self.line1}\n    {self.line2}\n    {self.city}\n    {self.postcode}'


