import pyttsx3

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

path = input("Enter the path to the file: ")
read_file_contents(read_text_from_file(path))
     
