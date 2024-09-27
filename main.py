import pyttsx3

def add_to_file(path):
    open_file = open(path, "a")
    info = input("Enter what you would like to write: ")
    open_file.write(info)
    open_file.close()

def read_text_from_file(file_path):
    file = open(file_path, 'r')
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return None
  
def read_file_contents(file_content):
        engine = pyttsx3.init()
        engine.say(file_content)
        engine.runAndWait()

def Main():        
    choice = input("Would you like to write in the file: ")
    if(choice.lower() == 'yes'):
        path = input("Enter the path to the file: ")
        print(add_to_file(path))
        read_text_from_file(path)

print(Main())        
