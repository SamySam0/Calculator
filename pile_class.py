from onClick_Events import *

class Pile:
  def __init__(self):
    self.pile = [] # on crée une liste vide lors de la création de l'objet.
  
  
  def push(self, element_a_empiler):
    '''
    Empile un élément sur la pile.
    :param element_a_empiler: ce qu'on veut
    ''' 
    self.pile.append(element_a_empiler)
    return self
   
  def __len__(self):
    return len(self.pile)

  def size (self):
    '''
    :returns: un entier correspondant au nombre d'éléments sur la pile.
    '''
    # c'est à vous !
    return len(self.pile)

  def pop(self):
    '''
   Renvoie l'élément sur le haut de la pile et l'enlève de la pile.
    :returns: dernier élément empilé 
    :raises: renvoi une erreur si la pile est vide !
    '''
    assert len(self.pile) > 0
    elast = self.pile[-1]
    del self.pile[-1]
    return elast

  def is_empty(self):
    '''
    :returns: un booléen True si la pile est vide 
    '''
    return len(self.pile) == 0

