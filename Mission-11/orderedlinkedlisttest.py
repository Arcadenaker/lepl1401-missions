import unittest
from orderedlinkedlist import OrderedLinkedList
from coureur    import Coureur
from temps      import Temps
from resultat   import Resultat

coureurs = [Coureur("Alfred", 24),
            Coureur("Bernard", 27),
            Coureur("Claude", 19),
            Coureur("Daniel", 31),
            Coureur("Emile", 25),
            Coureur("Fred", 28),
            Coureur("Gerard", 25)]

class OrderedLinkedListTest(unittest.TestCase):
    def test_init(self):
        r1 = Resultat(coureurs[0], Temps())
        r2 = Resultat(coureurs[1], Temps())
        r3 = Resultat(coureurs[2], Temps())
        oll = OrderedLinkedList([r1, r2, r3])
        self.assertEqual(oll.size(), 3, "La méthode init de OrderedLinkedList ne fonctionne pas correctement")
        self.assertNotEqual(oll.search(coureurs[0]), -1, "L'initialisation du premier coureur ne s'est pas fait correctement")
        self.assertNotEqual(oll.search(coureurs[1]), -1, "L'initialisation du deuxième coureur ne s'est pas fait correctement")
        self.assertNotEqual(oll.search(coureurs[2]), -1, "L'initialisation du troisième coureur ne s'est pas fait correctement")

    def test_size(self):
        r1 = Resultat(coureurs[0], Temps())
        r2 = Resultat(coureurs[1], Temps())
        oll = OrderedLinkedList([r1, r2])
        self.assertEqual(oll.size(), 2, "La méthode size de OrderedLinkedList ne retourne pas la bonne taille")

    def test_add(self):
        r1 = Resultat(coureurs[0], Temps())
        r2 = Resultat(coureurs[1], Temps())
        r3 = Resultat(coureurs[2], Temps())
        oll = OrderedLinkedList([r1, r2])
        oll.add(r3)
        self.assertEqual(oll.size(), 3, "La méthode add de OrderedLinkedList n'ajoute pas correctement un résultat")

    def test_search(self):
        r1 = Resultat(coureurs[0], Temps(0,20,6))
        r2 = Resultat(coureurs[1], Temps(1,4,32))
        r3 = Resultat(coureurs[2], Temps(0,24,10))
        oll = OrderedLinkedList([r1, r2, r3])
        self.assertEqual(oll.search(coureurs[0]), 1, "La méthode search de OrderedLinkedList ne retourne pas la bonne position pour le coureur 0")
        self.assertEqual(oll.search(coureurs[1]), 3, "La méthode search de OrderedLinkedList ne retourne pas la bonne position pour le coureur 1")
        self.assertEqual(oll.search(coureurs[2]), 2, "La méthode search de OrderedLinkedList ne retourne pas la bonne position pour le coureur 2")

    def test_get_node(self):
        r1 = Resultat(coureurs[0], Temps())
        r2 = Resultat(coureurs[1], Temps())
        r3 = Resultat(coureurs[2], Temps())
        oll = OrderedLinkedList([r1, r2, r3])
        node = oll.get_node(coureurs[1])
        self.assertEqual(node, r2, "La méthode get_node de OrderedLinkedList ne retourne pas le bon résultat")

    def test_remove(self):
        r1 = Resultat(coureurs[0], Temps())
        r2 = Resultat(coureurs[1], Temps())
        r3 = Resultat(coureurs[2], Temps())
        oll = OrderedLinkedList([r1, r2, r3])
        oll.remove(coureurs[0])
        self.assertEqual(oll.size(), 2, "La méthode remove de OrderedLinkedList ne retire pas correctement le résultat")
        self.assertEqual(oll.search(coureurs[0]), -1, "La méthode remove ne supprime pas correctement le premier coureur")
        oll.remove(coureurs[1])
        self.assertEqual(oll.size(), 1, "La méthode remove de OrderedLinkedList ne retire pas correctement le résultat")
        self.assertEqual(oll.search(coureurs[1]), -1, "La méthode remove ne supprime pas correctement le deuxième coureur")
        oll.remove(coureurs[2])
        self.assertEqual(oll.size(), 0, "La méthode remove de OrderedLinkedList ne retire pas correctement le résultat")
        self.assertEqual(oll.search(coureurs[2]), -1, "La méthode remove ne supprime pas correctement le deuxième coureur")

if __name__ == '__main__':
    unittest.main(verbosity=2)