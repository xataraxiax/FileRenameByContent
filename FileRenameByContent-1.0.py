import os
import docx #python-docx needs to be installed via pip (give details?)

#split filename from extension
file_name, f_ext = os.path.splitext('Helen Leggatt (id10073324)_20612219_assignsubmission_file_LEGGATT Assignment One Classical.docx')

#split filename at spaces
fname = file_name.split()

#the first and last names are by default split. now to isolate the id number
id = fname[2]
id = id[id.find("(id"):id.find(")")+1]

#test read of docx file
def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    
    return '\n'.join(fullText)

textComplete = getText('testdata\original\Adam Stock (id15041196)_20611216_assignsubmission_file_15041196 Magic and Witchcraft Classical.World.Essay.docx')
textSplit = textComplete.split()

#check for keywords in first 400 words
#append the first instance of keywords in range to list(topic), or None if none found
#remove(filter) None types from list
#if the remaining list contains exactly one element, return that element(topic[0])
#otherwise return "UNSURE" to prompt manual evaluation of topic
def topicCheck(textSplit):    
    topic = []
    topic.append(next(("Spell" for i in xrange(400) if (textSplit[i] == "spell" or textSplit[i] == "invoke")), None))
    topic.append(next(("Language" for i in xrange(400) if (textSplit[i] == "language")), None))
    topic = filter(None, topic)
    if len(topic) == 1:
        return topic[0]
    else:
        return "UNSURE"

topic = topicCheck(textSplit)

#print last, first, id, topic, extension
print fname[1]+',', fname[0], id + ' - ' + topic + f_ext
