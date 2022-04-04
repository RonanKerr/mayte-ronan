from printy import printy

class TitleScreen:
    def __init__(self):
        self.title = \
        '''
████████ ██  ██████     ████████  █████   ██████     ████████  ██████  ███████ 
   ██    ██ ██             ██    ██   ██ ██             ██    ██    ██ ██      
   ██    ██ ██             ██    ███████ ██             ██    ██    ██ █████   
   ██    ██ ██             ██    ██   ██ ██             ██    ██    ██ ██      
   ██    ██  ██████        ██    ██   ██  ██████        ██     ██████  ███████
'''

    def print_title(self):
        printy(self.title, 'rB')
        #print(self.title, 'rB')
