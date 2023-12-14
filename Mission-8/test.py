import mission8 as m8

def test_Duree_init():
    chanson = m8.Duree(1,8,4)
    assert chanson.secondes == 4, "Erreur dans le test pour initier Duree (secondes)"
    assert chanson.minutes == 8, "Erreur dans le test pour initier Duree (minutes)"
    assert chanson.heures == 1, "Erreur dans le test pour initier Duree (heures)"

def test_Duree_to_secondes():
    chanson = m8.Duree(3,5,58)
    assert chanson.to_secondes() == 11158, "Erreur dans le test to_secondes() (Class Duree)"

def test_Duree_delta():
    chanson1 = m8.Duree(2,4,55)
    chanson2 = m8.Duree(1,24,5)
    assert chanson1.delta(chanson2) == 2450, "Erreur dans le test delta() (Class Duree)"

def test_Duree_apres():
    chanson1 = m8.Duree(2,4,55)
    chanson2 = m8.Duree(3,41,21)
    assert chanson1.apres(chanson2) == False, "Erreur dans le test apres() (Class Duree)"

def test_Duree_ajouter():
    chanson1 = m8.Duree(2,4,61)
    chanson2 = m8.Duree(1,65,95)
    chanson1.ajouter(chanson2)
    assert chanson1.secondes == 36, "Erreur dans le test ajouter() 1 (Class Duree)"
    assert chanson1.minutes == 11, "Erreur dans le test ajouter() 2 (Class Duree)"
    assert chanson1.heures == 4, "Erreur dans le test ajouter() 3 (Class Duree)"

def test_Duree_print():
    chanson1 = m8.Duree(2,4,40)
    assert f"{chanson1}" == "02:04:40", "Erreur dans le test pour print Duree (Class Duree)"

def test_Chanson_init():
    chanson = m8.Chanson("Titre", "Michel Jackson", m8.Duree(1,8,4))
    assert chanson.titre == "Titre", "Erreur dans le test pour initier Chanson (titre)"
    assert chanson.autheur == "Michel Jackson", "Erreur dans le test pour initier Chanson (autheur)"
    assert chanson.duree.secondes == 4, "Erreur dans le test pour initier Chanson (secondes)"
    assert chanson.duree.minutes == 8, "Erreur dans le test pour initier Chanson (minutes)"
    assert chanson.duree.heures == 1, "Erreur dans le test pour initier Chanson (heures)"

def test_Chanson_print():
    chanson1 = m8.Chanson("Titre", "Père Castor", m8.Duree(10,54,32))
    assert f"{chanson1}" == "Titre - Père Castor - 10:54:32", "Erreur dans le test pour print Chanson (Class Chanson)"

def test_Album_class():
    album = m8.Album(24)
    album.add(m8.Chanson("Père Castor", "Michel Jackson", m8.Duree(0,5,4)))
    album.add(m8.Chanson("Père", "Michel Jack", m8.Duree(0,9,5)))
    assert f"{album}" == "Album 24 (2 chansons, 00:14:09)\n01: Père Castor - Michel Jackson - 00:05:04\n02: Père - Michel Jack - 00:09:05"

test_Duree_init()
test_Duree_to_secondes()
test_Duree_delta()
test_Duree_apres()
test_Duree_ajouter()

test_Chanson_init()
test_Chanson_print()

test_Album_class()
print("[Tests effectués avec succès]")