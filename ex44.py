class Parent(object):

    # 显式继承（Override Explicitly）
    # 覆盖子类中的函数，从而有效地替换功能。
    def override(self):
        print("PARENT override()")
    # 隐式继承（Implicit Inheritance）
    # 当你在父类而不是子类中定义一个函数时发生的隐式动作
    def implicit(self):
        print("PARENT implicit()")

    def altered(self):
        print("PARENT altered()")

class Child(Parent):
    def override(self):
        print("CHILD override()")

    #在父类的版本运行之前或之后更改行为
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()
print("*"*20)
dad.implicit()
print("-"*20)
son.implicit()
print("*"*20)
dad.override()
print("-"*20)
son.override()
print("*"*20)
dad.altered()
print("-"*20)
son.altered()