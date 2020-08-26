import unittest


from final_class import Unsubclassable


class UnsubclassableTests(unittest.TestCase):

    """Tests for Unsubclassable."""

    def test_initialization(self):
        d = Unsubclassable()
        d.x = 4
        self.assertEqual(d.x, 4)
        with self.assertRaises(TypeError):
            class B(Unsubclassable):
                pass
            B()

    def test_deep_inheritance(self):
        d = Unsubclassable()
        d.x = 4
        self.assertEqual(d.x, 4)
        with self.assertRaises(TypeError):
            class B(Unsubclassable):
                pass
            class C(B):
                pass
            C()

    def test_custom_initializer(self):
        d = Unsubclassable()
        d.x = 4
        self.assertEqual(d.x, 4)
        with self.assertRaises(TypeError):
            class Point(Unsubclassable):
                def __init__(self, x, y, z):
                    self.x, self.y, self.z = x, y, z
            Point(1, 2, 3)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_error_raised_immediately(self):
        d = Unsubclassable()
        d.x = 4
        self.assertEqual(d.x, 4)
        with self.assertRaises(TypeError):
            class Point(Unsubclassable):
                def __init__(self, x, y, z):
                    self.x, self.y, self.z = x, y, z


# To test the Bonus part of this exercise, comment out the following line
# @unittest.expectedFailure
class FinalClassTests(unittest.TestCase):

    """Tests for final_class."""

    def test_empty_class(self):
        from final_class import final_class
        @final_class
        class A:
            pass
        a = A()
        a.x = 4
        self.assertEqual(a.x, 4)
        with self.assertRaises(TypeError):
            class B(A):
                pass

    def test_multiple_inheritance(self):
        from final_class import final_class
        @final_class
        class A:
            pass
        class B:
            pass
        with self.assertRaises(TypeError):
            class C(A, B):
                pass
        with self.assertRaises(TypeError):
            class D(B, A):
                pass
        a = A()
        a.x = 4
        self.assertEqual(a.x, 4)

    def test_final_class_inheriting_from_other_classes(self):
        from final_class import final_class
        @final_class
        class A(object):
            pass
        @final_class
        class B(int):
            pass
        with self.assertRaises(TypeError):
            class C(A):
                pass
        with self.assertRaises(TypeError):
            class D(B):
                pass
        a = A()
        a.x = 4
        self.assertEqual(a.x, 4)
        b = B()
        self.assertEqual(b, 0)


# To test the Bonus part of this exercise, comment out the following line
# @unittest.expectedFailure
class UnsubclassableTypeTests(unittest.TestCase):

    """Tests for UnsubclassableType."""

    def test_empty_class(self):
        from final_class import UnsubclassableType
        class A(metaclass=UnsubclassableType):
            pass
        a = A()
        a.x = 4
        self.assertEqual(a.x, 4)
        with self.assertRaises(TypeError):
            class B(A):
                pass

    def test_multiple_inheritance(self):
        from final_class import UnsubclassableType
        class A(metaclass=UnsubclassableType):
            pass
        class B:
            pass
        with self.assertRaises(TypeError):
            class C(A, B):
                pass
        with self.assertRaises(TypeError):
            class D(B, A):
                pass
        a = A()
        a.x = 4
        self.assertEqual(a.x, 4)

    def test_inheritance_with_metaclass(self):
        from final_class import UnsubclassableType
        class A:
            pass
        class B(A, metaclass=UnsubclassableType):
            pass
        with self.assertRaises(TypeError):
            class C(B):
                pass
        with self.assertRaises(TypeError):
            class D(B, A):
                pass
        with self.assertRaises(TypeError):
            class E(A, B):
                pass
        a = A()
        a.x = 4
        self.assertEqual(a.x, 4)


if __name__ == "__main__":
    unittest.main(verbosity=2)
