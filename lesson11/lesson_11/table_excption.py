class Table_excption(Exception):
    def __init__(self,msg):
        super().__init__(msg)
class Occupied_seats(Exception):
    def __init__(self,msg):
        super().__init__(msg)

