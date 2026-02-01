from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivy.metrics import dp

class CalculatorApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style = "Dark"
        layout = MDBoxLayout(orientation="vertical", spacing=15, padding=20)
        
        title = MDLabel(text="BUSINESS CALC", halign="center", font_style="H4", size_hint_y=None, height=dp(60))
        layout.add_widget(title)
        
        self.solution = MDTextField(
            text="0", halign="right", font_size=50, readonly=True,
            multiline=False, size_hint_y=None, height=dp(120), mode="fill"
        )
        layout.add_widget(self.solution)
        
        grid = MDGridLayout(cols=4, spacing=15)
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["C", "0", ".", "+"],
            ["="]
        ]
        
        for row in buttons:
            for label in row:
                btn = MDRoundFlatButton(
                    text=label, font_size=36, size_hint=(1, 1), padding=(dp(0), dp(25))
                )
                btn.bind(on_press=self.on_button_press)
                if label == "=":
                    btn.size_hint_x = 4
                grid.add_widget(btn)

        layout.add_widget(grid)
        return layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text
        if button_text == "C":
            self.solution.text = "0"
        elif button_text == "=":
            try:
                if current == "Error": current = "0"
                self.solution.text = str(eval(current))
            except Exception:
                self.solution.text = "Error"
        else:
            if current == "0" or current == "Error":
                self.solution.text = button_text
            else:
                self.solution.text += button_text

if __name__ == "__main__":
    CalculatorApp().run() 
