class Person:
    def __init__(self ,name:str,id:int,address:str,phone:int):
        self.name:name
        self.id=id
        self.address=address
        self.phone=phone

    def __str__(self):
        details = f' -\nNAME: {self.name}\nADDRESS: {self.address}\n' \
                  f'PHONE: {self.phone}\nEMAIL: {self.email}\n'
        return details


