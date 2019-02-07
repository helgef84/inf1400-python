class Parent():
    def test(self):
        print("test")

class Brother():
    def testB(self):
        print("test brother")

class child(Parent, Brother):
    def test2(self):
        print("test2")



parent = Parent()
child = child()

parent.test()
child.test()
child.test2()
child.testB()


