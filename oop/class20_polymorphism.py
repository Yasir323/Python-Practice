from abc import ABC, abstractmethod


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


# The following function implements Polymorphism.
# Depending on the object passed it'll behave differently.
def draw(*controls):
    for control in controls:
        control.draw()

ddl = DropDownList()
txtbox = TextBox()
draw(ddl, txtbox)
