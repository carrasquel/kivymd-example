from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar


class ConverterApp(MDApp):

    def flip(self):

        self.ctof = not self.ctof

        self.converted_label.text = ""
        self._input.text = ""

        if self.ctof:
            self.toolbar.text = "Convertio (Celsius to Fahrenheit)"
            self._input.hint_text = "Enter temperature in Celsius"
        else:
            self.toolbar.text = "Convertio (Fahrenheit to Celsius)"
            self._input.hint_text = "Enter temperature in Fahrenheit"

    def convert(self, args):

        if self.ctof:
            celsius = float(self._input.text)

            fahrenheit = celsius * (9 / 5) + 32

            self.converted_label.text = str(round(fahrenheit, 2))

            self.label.text = "In Fahrenheit is:"
        else:
            fahrenheit = float(self._input.text)

            celsius = (fahrenheit - 32) * (5 / 9)

            self.converted_label.text = str(round(celsius, 2))

            self.label.text = "In Celsius is:"

    def build(self):
        self.ctof = True
        self.theme_cls.primary_palette = "Indigo"
        screen = MDScreen()
        
        # toolbar
        self.toolbar = MDToolbar(title="Convertio (Celsius to Fahrenheit)")
        self.toolbar.pos_hint = {"top": 1}
        self.toolbar.right_action_items = [["rotate-3d-variant", lambda x: self.flip()]]
        screen.add_widget(self.toolbar)

        # logo
        
        screen.add_widget(Image(source="logo.png", pos_hint={"center_x": 0.5, "center_y": 0.7}))

        # input

        self._input = MDTextField(
            hint_text="Enter temperature in Celsius",
            halign="center",
            size_hint=(0.8, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            font_size=22
        )
        screen.add_widget(self._input)

        # labels

        self.label = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.35},
            theme_text_color="Secondary"
        )

        self.converted_label = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.3},
            theme_text_color="Primary",
            font_style="H5"
        )

        screen.add_widget(self.label)
        screen.add_widget(self.converted_label)

        # convert button

        screen.add_widget(MDFillRoundFlatButton(
            text="CONVERT",
            font_size=17,
            pos_hint={"center_x": 0.5, "center_y": 0.15},
            on_press=self.convert
        ))

        return screen


if __name__ == '__main__':
    
    ConverterApp().run()
