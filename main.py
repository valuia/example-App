# for kivymd and md locals
from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRectangleFlatIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen


class StudyApp(MDApp):
    def __init__(self):
        super().__init__()

        # locals layouts
        self.positive = True
        self.screen = None
        self.layout = None
        self.screen_manager = None
        self.main_layout = None

        self.i = 0

    def build(self):
        self.screen = MDScreen()
        self.screen.md_bg_color = (1, 0.2, 0.6, 0.5)

        self.main_layout = MDBoxLayout(orientation="vertical", spacing=5,
                                       padding=5)  # main_layout for the main windows widgets.

        self.header = MDLabel(text=f"clicked :{self.i}", pos_hint={"center_x": 0.5}, halign="center", font_style="H3")

        btn = MDRectangleFlatIconButton(icon="emoticon-happy", text="Click Me!", pos_hint={"center_x": 0.5},
                                        on_release=self.Update_Lbl, size_hint=(1,0.25), icon_size=50)

        self.main_layout.add_widget(self.header)
        self.main_layout.add_widget(btn)

        self.screen.add_widget(self.main_layout)

        return self.screen

    def Update_Lbl(self, instance):

        # Example usage:


        if self.positive == True:
            self.i = self.i + 1
            self.header.text = f"clicked :{self.i}"
        elif self.positive == False:
            self.i = self.i - 1
            self.header.text = f"clicked :{self.i}"
        if self.i <= 0:
            toast(text="Kuch Kam Nhi Hai Kya?", duration=3)

            self.positive = True
        if self.i == 10:
            toast(text="Padai Kr LE!", duration=3)
            instance.icon = "emoticon-happy"
        if self.i == 20:
            toast(text="OOO Tere Ko hi bol rha Hu .", duration=3)
            instance.icon="emoticon-angry"
        if self.i == 30:
            toast(text="BSDK Salla Button Dabaya Ja Rha Hai!", duration=3)
            instance.icon = "ghost"
        if self.i == 40:
            toast(text="Pagal Khopdi", duration=3)
            instance.icon = "emoticon-angry"
        if self.i > 50:
            toast(text="khayega Kya Kopta", duration=3)
            instance.icon = "emoticon-happy"

            self.positive = False



if __name__ == '__main__':
    StudyApp().run()
