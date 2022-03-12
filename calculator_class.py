from pile_class import *

#J'utilise à la fois les piles/objets et le basique.
#Maintenant je vais dormir et demain j'en fais une application. Bonne nuit.

#J'utilise à la fois les piles/objets et le basique.
#Maintenant je vais dormir et demain j'en fais une application. Bonne nuit.

class Calculator:
  '''
  La super calculatrice deluxe version limité collector chez votre marchand de journaux
  '''
  def __init__(self, liste):
    self.calculation = Pile()
    self.calculation.pile = liste

  def inverse(self, caractere):
    '''
    Inverse le sens d'une parenthese ou d'un crochet
    Entree : un caractere "(", ")", "[" ou "]"
    Sortie : caractere de sens oppose a celui d'entree
    '''
    assert caractere in ["(",")","[","]"]
    if caractere == "(":
      return ")"
    elif caractere == "[":
      return "]"
    elif caractere == ")":
      return "("
    elif caractere == "]":
      return "["

  def inversement(self, liste_donnee):
    '''
    Inverse l'ordre des elements d'une pile/liste
    Entre : liste/pile a inverser
    Sortie : liste/pile inversee
    '''
    self.liste_entrante, self.liste_entrante.pile = Pile(), liste_donnee
    self.liste_inversee = Pile()
    while len(self.liste_entrante.pile) > 0:
      self.liste_inversee.push(self.liste_entrante.pop())
    return self.liste_inversee.pile

  def isolation_parentheses(self):
    '''
    Isole les parentheses/crochets d'une liste
    Entree : une liste / pile
    Sortie : pile composee seulement des parentheses/crochets de la pile/liste d'entree
    '''
    self.only_parentheses = Pile()
    for i in self.calculation.pile:
      if i in ["(", ")", "[", "]"]:
        self.only_parentheses.push(i)
    return self.only_parentheses.pile


  def verification_parentheses(self):
    '''
    Verifie si les parentheses sont dans un ordre propice a un calcul
    Entree : une pile / liste de calcul
    Sortie : {pass} si ordre syntaxiquement correct OU raise une exeption si non correcte
    '''
    self.L = Pile()
    self.only_parentheses2, self.only_parentheses2.pile = Pile(), self.inversement(self.isolation_parentheses())
    if self.only_parentheses2.size() > 0:
      self.L.push(self.inverse(self.only_parentheses2.pile[0]))
      for n in range(1, self.only_parentheses2.size()):
        if (self.L.size() == 0) or (self.only_parentheses2.pile[n] != self.L.pile[-1]):
          self.L.push(self.inverse(self.only_parentheses2.pile[n]))          
        else:
          self.L.pop()
    if self.L.size() == 0: 
      pass #Continue si size() = 0
    else : raise ValueError('Attention mec ! Les parenthèses ne sont pas bien rangées !') #Emet une exception si != 0


  def calculer(self):
    '''
    Fonction d'une calculatrice a partir d'une pile / liste
    Entree : Une pile/liste a calculer
    Sortie : Le resultat mon pote !
    '''
    self.verification_parentheses()
    return eval("".join(self.calculation.pile))