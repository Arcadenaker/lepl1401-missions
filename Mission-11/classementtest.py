import unittest
import random
from classement import Classement
from coureur    import Coureur
from classement import Classement
from temps      import Temps
from resultat   import Resultat

coureurs = [ Coureur("Alfred", 24), \
            Coureur("Bernard", 27), \
            Coureur("Claude", 19), \
            Coureur("Daniel", 31),  \
            Coureur("Emile", 25),  \
            Coureur("Fred", 28),  \
            Coureur("Gerard", 25) ]

class ClassementTest(unittest.TestCase):
    def test_init(self):
        c1 = coureurs[0]
        c2 = coureurs[1]
        t = Temps(1,2,3)
        r1 = Resultat(c1, t)
        r2 = Resultat(c2, t)
        cl = Classement([r1, r2])
        self.assertNotEqual(cl.get_position(c1), -1, "Le premier coureur ne s'est pas ajouté dans la liste")
        self.assertNotEqual(cl.get_position(c2), -1, "Le deuxième coureur ne s'est pas ajouté dans la liste")

    def test_size(self):
        c1 = coureurs[2]
        c2 = coureurs[3]
        c3 = coureurs[4]
        t = Temps(1,2,3)
        r1 = Resultat(c1, t)
        r2 = Resultat(c2, t)
        r3 = Resultat(c3, t)
        cl = Classement([r1, r2, r3])
        self.assertEqual(cl.size(), 3, "La méthode size de classement ne retourne pas la bonne taille")

    def test_add(self):
        c1 = coureurs[0]
        c2 = coureurs[1]
        c3 = coureurs[2]
        t = Temps(1,2,3)
        r1 = Resultat(c1, t)
        r2 = Resultat(c2, t)
        r3 = Resultat(c3, t)
        cl = Classement([r1, r2])
        cl.add(r3)
        self.assertEqual(cl.size(), 3, "La méthode add de classement n'ajoute pas correctement un coureur")

    def test_get(self):
        c1 = coureurs[0]
        t = Temps()
        t.add_secondes(random.randint(1000, 5000))
        r1 = Resultat(c1, t)
        cl = Classement([r1])
        self.assertEqual(cl.get(c1), r1, "La méthode get de classement ne retourne pas le bon résultat")

    def test_get_position(self):
        c1 = coureurs[0]
        c2 = coureurs[1]
        r1 = Resultat(c1, Temps(1,10,5))
        r2 = Resultat(c2, Temps(0,21,19))
        cl = Classement([r1, r2])
        self.assertEqual(cl.get_position(c2), 1, "La méthode get_position de classement ne retourne pas la bonne position")

    def test_remove(self):
        c1 = coureurs[0]
        t = Temps(1,2,3)
        r1 = Resultat(c1, t)
        cl = Classement([r1])
        cl.remove(c1)
        self.assertEqual(cl.size(), 0, "La méthode remove de classement ne retire pas correctement le coureur")

if __name__ == '__main__':
    unittest.main(verbosity=2)