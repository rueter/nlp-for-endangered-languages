# This is a really preliminary script that reads a LIFT XML file, 
# structures that into JSON, and then saves that into a little bit
# formatted markdown file. We could use also simple HTML or LaTeX
# as template. Something like this could be also set up as a GitHub
# Action or regularly running script, so that every time a dictionary
# LIFT file is updated it is exported. 

# this can now be used as
# python lift2md.py
# you have to change line 18,
# and also places where language tags are present

# We don't any need other packages now than ElementTree

import xml.etree.ElementTree as ET

# Here we need a complete path to the LIFT file

tree = ET.parse('Lift.lift')
root = tree.getroot()

# We create an empty list where we will store everything

dictionary = []

# We find all entry-elements

for entry in root.findall(".//entry"):
    
    # Here we find an individual form, and iterate over the text
    # we have to do this, because the text is within individual 
    # <text> elements. 
    
    form = entry.find(".//lexical-unit/form")
    form_text = "".join(form.itertext())
    
    # We pick the values that are called traits in this XML,
    # basically this means if it a stem or suffix
    
    trait_value = entry.find(".//trait").get("value")
    
    # We try to find a pronuncation…
    
    pronunciation = entry.find(".//pronunciation")
    
    # and iterate over that like earlier
    
    if pronunciation:
        
        pronunciation_text = "".join(pronunciation.itertext()).strip()
    
    # but if we don't have it, we just store there an empty value
    
    else:
        
        pronunciation_text = ''
        
    # Replacing en with pt here would pick the Portuguese
        
    translation = entry.find(".//gloss[@lang='en']")
    
    if translation:
    
        translation_text = "".join(translation.itertext()).strip()
    
    else:
        
        translation_text = ''
       
    # Also here the language name would need to be changed
    
    example = entry.find(".//example/form[@lang='ktn']")
    
    if example:
        
        example_text = "".join(example.itertext()).strip()
        
    else:
        
        example_text = ''
        
    # Same here, pt for Portuguese
    
    example_translation = entry.find(".//example/translation/form[@lang='en']")
    
    if example_translation:
        
        example_translation_text = "".join(example_translation.itertext()).strip()
    
    else:
        
        example_translation_text = ''
    
    # Let's say we just want the stems
    
    if trait_value == "stem":
      
        # We create an empty dictionary
    
        item = {} 
        
        # We populate that dictionary with the values we extracted
        # We strip some whitespace as we go
        
        item['form'] = form_text.strip()
        item['pronunciation'] = pronunciation_text.strip()
        item['translation_en'] = translation_text.strip()
        
        item['example'] = example_text.strip()
        item['example_translation'] = example_translation_text.strip()
        
        # Then we append this to the dictionary we created in the beginning of the script
    
        dictionary.append(item)

# Here the dictionary is sorted by the lowercased lemma / form

dictionary = sorted(dictionary, key = lambda i: i['form'].lower())

# We open a new file for the dictionary

file = open("dictionary.md", "w")

# Here goes the title

file.write("# Dictionary\n\n")

# For each entry in the dictionary, we write lines and format them while doing that

for e in dictionary:
    
    if e['translation_en']:
    
        if e['pronunciation']:

            file.write(f"**{e['form']}** \[{e['pronunciation']}\] {e['translation_en']}")

        else: 

            file.write(f"**{e['form']}** {e['translation_en']} ")
            
        # If there is an example we write that to the end of the entry
        # separating it with a colon

        if e['example_translation']:

            file.write(f" : *{e['example']}* {e['example_translation']}\n\n")
        
        else:
            
            file.write('\n\n')

# Here could be some description
# Why not also in the beginning

file.write("Dictionary created by … . Please contact … for questions. Released under … license.")

# Here we close the file

file.close()

# The conversion command is: 
# pandoc dictionary.md -o dictionary.docx
# Other file formats would work as well

