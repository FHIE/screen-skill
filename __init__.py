from mycroft import MycroftSkill, intent_file_handler


class Screen(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('screen.intent')
    def handle_screen(self, message):
        self.speak_dialog('screen')


def create_skill():
    return Screen()

