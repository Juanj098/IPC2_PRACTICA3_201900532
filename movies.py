class Movies:

    def __init__(self,id,name,genre) -> None:
        self.id = id
        self.name = name
        self.genre = genre

    def edit(self,Nid,Nname,Ngenre):
        self.id = Nid
        self.name = Nname
        self.genre = Ngenre

    def __str__(self) -> str:
        return f'ID:{self.id}, Name:{self.name}, Genre:{self.genre}'