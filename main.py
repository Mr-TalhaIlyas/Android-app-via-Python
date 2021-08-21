from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

# right_action_items: [["dots-vertical", lambda x: app.callback()]] #for tool bar


class NN(MDApp):
    data = {
        'Python': 'language-python',
        'PHP': 'language-php',
        'C++': 'language-cpp',
        'Android': 'android',
    }

    def action(self):
        name_list = ['Talha', 'Abbas', 'Shujaat', 'Mobeen', 'Sharzil', 'Zeeshan', 'Amjad', 'Mehtab', 'Umraiz']
        nick_name = ['Yanders...!', 'Khan', 'Malik Sab', 'Panda G', 'Khan Sab', 'Zayu', 'Amjad bhai', 'Mehtab bhai',
                     'Umraiz bhai']

        label = self.root.ids.show
        try:
            idx = name_list.index(self.root.in_class.text)
            if idx == 0:
                label.text = f'{nick_name[idx]}'
            if idx != 0 and idx <= 5:
                label.text = f'Your nick name is {nick_name[idx]}'
            if idx > 5:
                label.text = f'No nick name for {nick_name[idx]} yet!'
        except ValueError:
            self.dialog = MDDialog(title='Name error',
                                   text="Name not found in database", size_hint=(0.8, 1),
                                   buttons=[MDFlatButton(text='Close', on_release=self.close_dialog),
                                            MDFlatButton(text='More', on_release=self.more_info)]
                                   )
            self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def more_info(self, obj):
        self.dialog2 = MDDialog(title='More Info',
                                text="Your name was not entered by the author in the database.You can try entring your name statring with captial letter!",
                                buttons=[MDFlatButton(text='Close', on_release=self.close_dialog2)]
                                )
        self.dialog2.open()

    def close_dialog2(self, obj):
        self.dialog2.dismiss()
        self.dialog.dismiss()

    def toolbar_dialogue(self):
        self.toolbar_dialogue = MDDialog(title='Home Address',
                               text='Visit: https://github.com/Mr-TalhaIlyas', size_hint=(0.8, 1),
                               buttons=[MDFlatButton(text='Close', on_release=self.toolbar_close)]
                               )
        self.toolbar_dialogue.open()
    def toolbar_close(self, obj):
        self.toolbar_dialogue.dismiss()

    def callback(self, instance):

        if instance.icon == 'language-python':
            label = self.root.ids.show
            label.text = "python Dont press these buttons yet"
        if instance.icon == 'language-php':
            label = self.root.ids.show
            label.text = "php Dont press these buttons yet"
        if instance.icon == 'language-cpp':
            label = self.root.ids.show
            label.text = "c++ Dont press these buttons yet"
        if instance.icon == 'android':
            label = self.root.ids.show
            label.text = "android Dont press these buttons yet"

    def build(self):
        return Builder.load_file('nickname.kv')


if __name__ in ('__main__', '__android__'):
    NN().run()
