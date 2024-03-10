#-------------------------------------------------------------------------------------------------------#
import toga
from toga.style import Pack
from toga.style.pack import COLUMN

from healthapp.app import HealthApp
from healthapp.style import create_border
#-------------------------------------------------------------------------------------------------------#

class Cognition():
    # Images would be imported into this class for the cognitive analysis, planning to add to the choice box
    # putting the image the user makes this decision based on inside of the 'choice_box' 

    def __init__(self, app: HealthApp):  
        self.app = app

        # Create the main container
        main_container = toga.Box(style=Pack(direction=COLUMN, background_color="#e0965e"))

        # Main box for the initial content
        header_box = toga.Box(style=Pack(padding=20)) # for label
        main_box = toga.Box(style=Pack(padding=20)) # for cognitive choices
        choice_box = toga.Box(style=Pack(padding=20)) # for choice of the correct cognitive analysis
        footer_box = toga.Box(style=Pack(padding=5)) # for submit + back buttons

        # button for behavioural analysis
        c_label = toga.Label("Select the next image in the sequence: ", style=Pack(font_size=15, padding=(0, 10)))

        submit_button = toga.Button('Submit', on_press=self.c_class_handler, style=Pack(background_color="#fbf5cc", padding=(-3)))
        submit_box = create_border(submit_button, inner_color="#fbf5cc")

        back_button = toga.Button('Back', on_press=self.back_handler, style=Pack(background_color="#fbf5cc", padding=(-3)))
        back_box = create_border(back_button, inner_color="#fbf5cc")

        for button in [submit_box, back_box]:
            if button != back_box or button != submit_box:
                choice_box.add(button) # add the choice image button to the choice_box
                                       # assuming thats how the cognitive analysis will be done
                
            else: # add the submit and back buttons to the footer_box
                footer_box.add(button) 

        # add boxes to the main container
        for box in [header_box, main_box, choice_box, footer_box]:
            main_container.add(box)

        # set the main container as the content of the main window
        self.app.update_content(main_container)

    def c_class_handler(self, widget):
        #add logic
        print("Cognitive button pressed!")

    def back_handler(self, widget):
        print("Back button pressed!")
        self.app.show_menu()