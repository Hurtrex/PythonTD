from abc import ABC, abstractmethod

class IList(ABC):

    @abstractmethod
    def add(self, element):         # ajouter à la fin
        pass

    @abstractmethod
    def add_at(self, index, element): # ajouter à une position
        pass

    @abstractmethod
    def get(self, index):           # obtenir un élément
        pass

    @abstractmethod
    def remove(self, index):        # supprimer à une position
        pass

    @abstractmethod
    def size(self):                 # taille de la liste
        pass

    @abstractmethod
    def is_empty(self):             # liste vide ?
        pass

    @abstractmethod
    def contains(self, element):    # élément présent ?
        pass

    @abstractmethod
    def clear(self):                # vider la liste
        pass