# FileRenameByContent
Python program for manipulating original filename and appending descriptor based on content.

## About
I have remotely marked university essays in Classics for years now. Typically, the students submit their work to an online application which can track drafts and perform anti-plagiarism checks with Turnitin. As a marker, I access this application and perform a bulk download of their essays just after the due date. Students, however, are notoriously fickle with their naming conventions, and the application itself appends a lot of administrative detail to the filename.

In order to maintain my sanity, as well as streamline the uploading of marked essays (which works best if files are alphabetical by last name), I have in the past manually changed each filename to "Lastname, Firstname (id#xxxxxxxx)". In addition to this, Classics essays tend to offer a minimum of two questions that students may choose to answer (sometimes up to 5). I have found I can more consistently grade the assignments (and make adjustments) if I mark all of one topic before marking another, and so I append a discriptor to the filename indicating topic.

With 50+ students in some classes, this takes a looooong time!

So for instance, a file that is downloaded as: 
```
Eddard Stark (id15045696)_20611216_assignsubmission_file_15041196 Magic and Witchcraft Classical.World.Essay 
```
becomes:
```
Stark, Eddard (id15045696) - Spell
```

FileRenameByContent is a cute little script which does just that (in most instances - see below).

## Usage

Firstly, open the main program file ```FileRenameByContent-1.0.py``` and edit the function ```def topicCheck(textSplit):``` as desired to correspond with expected topics.

When the .zip file of essays is downloaded simply drag and drop into the following folder:

```
...\FileRenameByContent\rename\files_to_rename
```
From terminal, navigate to the ```FileRenameByContent``` directory. Enter ```python FileRenameByContent-1.0.py``` and let the magic happen.

All that remains is to copy these files to a suitable folder for marking.

### Notes on use

In order to deduce the topic of the essay, the program searches the first 200 words for some given keywords. So far, this results in a positive identification about 90% of the time (care must be take when supplying the keywords). If the program cannot find the keyword, or if more than one keyword is returned, the program appends ```-UNSURE``` to the resulting filename. These files still require manual checking, but since the instances are fairly rare, and the rest of the filename is nicely formatted, this is not too much of a problem.

At the moment, only ```.docx``` is supported. If the program is unable to identify the file, it appends ```-UNSUPPORTED FILETYPE``` to the output.

## Problems

At the time of writing, there are still problems with students whose middle name has been included. I know the solution to this, and will have it sorted shortly.

## Future

It would be nice to turn this into a GUI app, that allows you to choose which folder needs to be renamed, and allows you to create a new folder in an appropriate place for the output.

Add support for other filetypes, especially .pdf and .odt.

## Author

Stefan Pedersen - September 2017
