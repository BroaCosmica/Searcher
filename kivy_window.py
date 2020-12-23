from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class MyApp(App):
    def build(self):
        layout = FloatLayout()

        self.btn_search = Button(
            text="Search",
            font_size=30,
            size_hint=(0.4, 0.2),
            pos_hint={"center_x": 0.5, "center_y": 0.4}
        )
        self.txtinput = TextInput(
            hint_text="Type a word or more.",
            font_size=40,
            size_hint=(0.7, 0.11),
            pos_hint={"center_x": 0.5, "center_y": 0.65},
            multiline=False
        )

        layout.add_widget(self.btn_search)
        layout.add_widget(self.txtinput)

        self.btn_search.bind(on_press=(self.researcher))

        return layout

    def researcher(self, *args):
        text = self.txtinput.text
        MyApp().stop()
        return text

# if __name__ == "__main__":
#     MyApp().run()
