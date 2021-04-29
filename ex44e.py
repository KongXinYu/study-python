# 组合
# 继承很有用，但是还有一种能实现相同效果的方法，就是使用其他类和模块，而不是依赖于隐式继承。
# 如果你看看使用继承的三种方法，其中两种都涉及编写新代码来替换或更改函数功能。
# 这很容易通过调用模块中的函数来复制。

class Other(object):

    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")

class Child(object):
    def __init__(self):
        self.other = Other()
    
    def implicit(self):
        self.other.implicit()

    def override(self):
        print("CHILD override()")
    
    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")

son = Child()

son.implicit()
son.override()
son.altered()
