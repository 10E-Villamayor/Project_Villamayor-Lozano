from pyscript import display, document # pyright: ignore[reportMissingImports]

class Classmate:
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject

    def introduce(self):
        display(
            f"Hi My name is {self.name}. "
            f"I am from {self.section}. "
            f"My favorite subject is {self.favorite_subject}.",
            target="output"
        )


c1 = Classmate("Angela", "10 - Emerald", "English")
c2 = Classmate("Ashley", "10 - Emerald", "Filipino")
c3 = Classmate("Erich", "10 - Emerald", "Science")
c4 = Classmate("Keisha", "10 - Emerald", "PE")
c5 = Classmate("Lia", "10 - Emerald", "Math")

classmates_list = [c1, c2, c3, c4, c5]


for classmate in classmates_list:
    classmate.introduce()


def add_classmate(event):
    name = document.getElementById("name").value
    section = document.getElementById("section").value
    favorite_subject = document.getElementById("favorite_subject").value

    new_classmate = Classmate(name, section, favorite_subject)
    classmates_list.append(new_classmate)

    display(
        f"Hi My name is {name}. I am from {section}. My favorite subject is {favorite_subject}.",
        target="output"
    )