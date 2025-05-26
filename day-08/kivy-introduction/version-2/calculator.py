from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class CalculatorLayout(BoxLayout):
    
    def calculate(self):
        try:
            num1 = float(self.ids.input1.text)
            num2 = float(self.ids.input2.text)

            if self.ids.add.state == 'down':
                result = num1 + num2
            elif self.ids.sub.state == 'down':
                result = num1 - num2
            elif self.ids.mul.state == 'down':
                result = num1 * num2
            elif self.ids.div.state == 'down':
                if num2 != 0:
                    result = num1 / num2
                else:
                    self.ids.result.text = "Error: Division by 0"
                    return
            else:
                self.ids.result.text = "Select an operation"
                return

            self.ids.result.text = f"Result: {result}"
        except ValueError:
            self.ids.result.text = "Invalid input"


class CalculatorApp(App):
    def build(self):
        return CalculatorLayout()


if __name__ == '__main__':
    CalculatorApp().run()
