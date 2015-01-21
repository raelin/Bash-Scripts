#Import the required modules
import os, shutil, fnmatch, Image, ImageEnhance

#Ask for pictures folder and move to it
picsFolder = raw_input("Where are your pictures? ")
os.chdir(picsFolder)

#Create a Backup directory
os.mkdir ( 'Backup' )

#Copy pictures to a Backup directory
for filename in fnmatch.filter(os.listdir(picsFolder),'*.jpg'):
    shutil.copy2(filename, "Backup/%s" % filename)

#Ask for desired largest side size in pixels
px = raw_input("Which is the desired largest side size in pixels? ")
px = int(px)


#----------------------------------------------------------------------------
#Image processing    
for file in fnmatch.filter(os.listdir(picsFolder),'*.jpg'):
    print "Resizing image " + file

# Open the image
    img = Image.open(file)

#Get actual image size and convert it to float
    width, height = img.size
    width = float(width)
    height = float(height)

#Resize landscape images
    if width > height:
        resizeFactor = width/int(px*2)
        img = img.resize((int(width/resizeFactor),int(height/resizeFactor)))
        width, height = img.size
        img = img.resize((int(width/2),int(height/2)), Image.ANTIALIAS)

#Resize portrait images
    if width<height:
        resizeFactor = height/int(px*2)
        img = img.resize((int(width/resizeFactor),int(height/resizeFactor)))
        width, height = img.size
        img = img.resize((int(width/2),int(height/2)), Image.ANTIALIAS)

#Resize square images
    if width==height:
        img = img.resize((int(px*2),int(px*2)))
        width, height = img.size
        img = img.resize((int(px),int(px)), Image.ANTIALIAS)

#Save resized image
    img.save(file)

#Create a Resized directory
os.mkdir ( 'Resized' )
#Copy pictures to a Resized directory
for filename in fnmatch.filter(os.listdir(picsFolder),'*.jpg'):
    shutil.copy2(filename, "Resized/%s" % filename)


#----------------------------------------------------------------------------    
#Add mark

#Create a marked directory
os.mkdir ( 'Watermarked' )

#Ask for mark file
markFile = raw_input("Where is your mark file? ")

#Getting the sizes of the base image and the mark
imgmark = Image.open(markFile)
markWidth, markHeight = imgmark.size
for filename in fnmatch.filter(os.listdir(picsFolder),'*.jpg'):

# Open the image
    img = Image.open(file)

#Get actual image size and convert it to float
    width, height = img.size

    baseim = Image.open(file)
    logoim = Image.open(markFile) #transparent image
    baseim.paste(logoim,(int(width)-int(markWidth)-20,int(height)-int(markHeight)-10),logoim)
#Recover EXIF data
    os.system("jhead -te Backup/*jpg *.jpg")
for filename in fnmatch.filter(os.listdir(picsFolder),'*.jpg'):
    shutil.move(filename, "Watermarked/%s" % filename)

