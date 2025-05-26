from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.button import Button


class CalculatorApp(App):
    def build(self):
        self.operand1 = TextInput(hint_text="Enter first number", multiline=False, input_filter='float', font_size=48)
        self.operand2 = TextInput(hint_text="Enter second number", multiline=False, input_filter='float', font_size=48)

        self.toggle_add = ToggleButton(text="+", group="operation", font_size=32)
        self.toggle_sub = ToggleButton(text="-", group="operation", font_size=32)
        self.toggle_mul = ToggleButton(text="×", group="operation", font_size=32)
        self.toggle_div = ToggleButton(text="÷", group="operation", font_size=32)

        self.calc_button = Button(text="CALCULATE", font_size=30, size_hint=(1, 0.5))
        self.calc_button.bind(on_press=self.calculate)

        self.result_label = Label(text="Result will appear here", font_size=32, size_hint=(1, 0.5))

        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        layout.add_widget(self.operand1)
        layout.add_widget(self.operand2)

        toggles = BoxLayout(spacing=10)
        toggles.add_widget(self.toggle_add)
        toggles.add_widget(self.toggle_sub)
        toggles.add_widget(self.toggle_mul)
        toggles.add_widget(self.toggle_div)
        layout.add_widget(toggles)

        layout.add_widget(self.calc_button)
        layout.add_widget(self.result_label)

        return layout

    def calculate(self, instance):
        try:
            num1 = float(self.operand1.text)
            num2 = float(self.operand2.text)

            if self.toggle_add.state == 'down':
                result = num1 + num2
            elif self.toggle_sub.state == 'down':
                result = num1 - num2
            elif self.toggle_mul.state == 'down':
                result = num1 * num2
            elif self.toggle_div.state == 'down':
                if num2 != 0:
                    result = num1 / num2
                else:
                    self.result_label.text = "Error: Division by 0"
                    return
            else:
                self.result_label.text = "Select an operation"
                return

            self.result_label.text = f"{result}"
        except ValueError:
            self.result_label.text = "Invalid input"


if __name__ == '__main__':
    CalculatorApp().run()
