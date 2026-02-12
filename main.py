import json
from playsound3 import playsound

def main():
    print("Starting...")
    filepath = "./codex.json"
    #Load codex
    codex = loadCodex(filepath)

    textString = "This, is a test text string."
    morseConversion = translateTextToMorse(codex, textString)
    print(morseConversion)
    textConversion = translateMorseToText(codex, morseConversion)
    print(textConversion)

    sound = playsound("morseCode.mp3", block=False)
    sound.stop()

def loadCodex(filepath):
    return loadFile(filepath)

def translateTextToMorse(codex, input):
    print("Translating from text to morse code....")
    translation = []
    input = input.upper()
    lookup = codex["language"]["english"]
    for char in input:
       translation.append(lookup[char])
       translation.append(" ")
    return ''.join(translation)

def translateMorseToText(codex, input):
    print("Translating from morse code to text....")
    translation = []
    lookup = codex["language"]["english"]
    codes = input.split(" ")
    for code in codes:   
        translation.append(list(lookup.keys())[list(lookup.values()).index(code)])
    return ''.join(translation)

def loadFile(filepath):
    print(f"Loading file from path: {filepath}") 
    with open(filepath) as file:
        return json.load(file)


if __name__=="__main__":
    main()