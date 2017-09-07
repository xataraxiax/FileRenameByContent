import os
import docx #python-docx needs to be installed via pip (give details?)

"""
Solving people with more than two names still required
I'm sure we can tidy this up too
"""
#establish working directory
directory = './testdata/test/'
files = os.listdir(directory)

for f in files:
    #split filename from extension, save as separate variables
    #needs to take the string from reading in directory
    file_name, f_ext = os.path.splitext(f)

    #split filename at spaces
    fname = file_name.split()

    #the first and last names are by default split. now to isolate the id number
    #unfortunately, this will not work, as there are triple-barrel names
    #eg. 'Brienne of Tarth'. I need to count indexes until I find the ID, then
    #use the last of those as the lastname, and concatenate however many preceeding
    #as first name. eg. 'Tarth, Brienne of'
    id = fname[2]
    id = id[id.find("(id"):id.find(")")+1]

    #test read of docx file
    def getText(filename):
        doc = docx.Document(filename)
        fullText = []
        for para in doc.paragraphs:
            fullText.append(para.text)        
        return '\n'.join(fullText)

    textComplete = getText(directory + f)
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
    #not sure why it ended up a tuple, but .join sorts it back to string
    #look into this
    newname = "".join((fname[1]+', ', fname[0] + ' ', id + ' - ' + topic + f_ext))
    os.rename(directory + f, directory + newname)

    print type(newname)
    print newname

    
