from XYRobot import XYRobot
import unittest

class TestXYRobot(unittest.TestCase):

    # Permet que l'instance de XYRobot soit initialisée avant l'exécution de chaque méthode de test
    def setUp(self):
        self.r = XYRobot("TEST", 100, 150)

    def test_print_xyr(self):
        self.assertEqual(f"{self.r}", "TEST@(100,150) angle: 0.0")
        
    def test_nom_xyr(self):
        self.assertEqual(self.r.nom(), "TEST")

    def test_x_xyr(self):
        self.assertEqual(self.r.x(), 100)

    def test_y_xyr(self):
        self.assertEqual(self.r.y(), 150)

    def test_position(self):
        self.assertEqual(self.r.position(), (100, 150))
    
    def test_move_forward(self):
        self.r.move_forward(50)
        self.assertEqual(self.r.position(), (150, 150))

    def test_move_backward(self):
        self.r.move_backward(30)
        self.assertEqual(self.r.position(), (70, 150))

    def test_move_up(self):
        self.r.turn_right()
        self.r.move_forward(50)
        self.assertEqual(self.r.angle(), 90)
        self.assertEqual(self.r.position(), (100, 200))

    def test_move_down(self):
        self.r.turn_left()
        self.r.move_forward(50)
        self.assertEqual(self.r.angle(), 270)
        self.assertEqual(self.r.position(), (100, 100))

    def test_historique(self):
        self.r.move_forward(10)
        self.assertEqual(self.r.history(), [["forward", 10]])
        self.r.turn_left()
        self.assertEqual(self.r.history(), [["forward", 10], ["left"]])

    def test_undo(self):
        self.r.move_forward(10)
        self.r.unplay()
        self.assertEqual(self.r.position(), (100, 150))

if __name__ == "__main__":
    unittest.main(verbosity=2)