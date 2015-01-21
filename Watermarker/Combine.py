{\rtf1\ansi\ansicpg1252\cocoartf1343\cocoasubrtf160
{\fonttbl\f0\fnil\fcharset0 Menlo-Bold;\f1\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red180\green36\blue25;\red46\green174\blue187;\red47\green180\blue29;
}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural

\f0\b\fs22 \cf2 \CocoaLigature0 #Import the required modules
\f1\b0 \cf0 \

\f0\b \cf3 import
\f1\b0 \cf0  os, shutil, fnmatch, Image, ImageEnhance\
\

\f0\b \cf2 #Ask for pictures folder and move to it
\f1\b0 \cf0 \
picsFolder = raw_input(
\f0\b \cf4 "Where are your pictures? "
\f1\b0 \cf0 )\
os.chdir(picsFolder)\
\

\f0\b \cf2 #Create a Backup directory
\f1\b0 \cf0 \
os.mkdir ( 
\f0\b \cf4 'Backup'
\f1\b0 \cf0  )\
\

\f0\b \cf2 #Copy pictures to a Backup directory
\f1\b0 \cf0 \

\f0\b \cf3 for
\f1\b0 \cf0  filename 
\f0\b \cf3 in
\f1\b0 \cf0  fnmatch.filter(os.listdir(picsFolder),
\f0\b \cf4 '*.jpg'
\f1\b0 \cf0 ):\
    shutil.copy2(filename, 
\f0\b \cf4 "Backup/%s"
\f1\b0 \cf0  % filename)\
\

\f0\b \cf2 #Ask for desired largest side size in pixels
\f1\b0 \cf0 \
px = raw_input(
\f0\b \cf4 "Which is the desired largest side size in pixels? "
\f1\b0 \cf0 )\
px = int(px)\
\
\

\f0\b \cf2 #----------------------------------------------------------------------------
\f1\b0 \cf0 \

\f0\b \cf2 #Image processing    
\f1\b0 \cf0 \

\f0\b \cf3 for
\f1\b0 \cf0  file 
\f0\b \cf3 in
\f1\b0 \cf0  fnmatch.filter(os.listdir(picsFolder),
\f0\b \cf4 '*.jpg'
\f1\b0 \cf0 ):\
    
\f0\b \cf3 print
\f1\b0 \cf0  
\f0\b \cf4 "Resizing image "
\f1\b0 \cf0  + file\
\

\f0\b \cf2 # Open the image
\f1\b0 \cf0 \
    img = Image.open(file)\
\

\f0\b \cf2 #Get actual image size and convert it to float
\f1\b0 \cf0 \
    width, height = img.size\
    width = float(width)\
    height = float(height)\
\

\f0\b \cf2 #Resize landscape images
\f1\b0 \cf0 \
    
\f0\b \cf3 if
\f1\b0 \cf0  width > height:\
        resizeFactor = width/int(px*2)\
        img = img.resize((int(width/resizeFactor),int(height/resizeFactor)))\
        width, height = img.size\
        img = img.resize((int(width/2),int(height/2)), Image.ANTIALIAS)\
\

\f0\b \cf2 #Resize portrait images
\f1\b0 \cf0 \
    
\f0\b \cf3 if
\f1\b0 \cf0  width<height:\
        resizeFactor = height/int(px*2)\
        img = img.resize((int(width/resizeFactor),int(height/resizeFactor)))\
        width, height = img.size\
        img = img.resize((int(width/2),int(height/2)), Image.ANTIALIAS)\
\

\f0\b \cf2 #Resize square images
\f1\b0 \cf0 \
    
\f0\b \cf3 if
\f1\b0 \cf0  width==height:\
        img = img.resize((int(px*2),int(px*2)))\
        width, height = img.size\
        img = img.resize((int(px),int(px)), Image.ANTIALIAS)\
\

\f0\b \cf2 #Save resized image
\f1\b0 \cf0 \
    img.save(file)\
\

\f0\b \cf2 #Create a Resized directory
\f1\b0 \cf0 \
os.mkdir ( 
\f0\b \cf4 'Resized'
\f1\b0 \cf0  )\

\f0\b \cf2 #Copy pictures to a Resized directory
\f1\b0 \cf0 \

\f0\b \cf3 for
\f1\b0 \cf0  filename 
\f0\b \cf3 in
\f1\b0 \cf0  fnmatch.filter(os.listdir(picsFolder),
\f0\b \cf4 '*.jpg'
\f1\b0 \cf0 ):\
    shutil.copy2(filename, 
\f0\b \cf4 "Resized/%s"
\f1\b0 \cf0  % filename)\
\
\

\f0\b \cf2 #----------------------------------------------------------------------------    
\f1\b0 \cf0 \

\f0\b \cf2 #Add mark
\f1\b0 \cf0 \
\

\f0\b \cf2 #Create a marked directory
\f1\b0 \cf0 \
os.mkdir ( 
\f0\b \cf4 'Watermarked'
\f1\b0 \cf0  )\
\

\f0\b \cf2 #Ask for mark file
\f1\b0 \cf0 \
markFile = raw_input(
\f0\b \cf4 "Where is your mark file? "
\f1\b0 \cf0 )\
\

\f0\b \cf2 #Getting the sizes of the base image and the mark
\f1\b0 \cf0 \
imgmark = Image.open(markFile)\
markWidth, markHeight = imgmark.size\

\f0\b \cf3 for
\f1\b0 \cf0  filename 
\f0\b \cf3 in
\f1\b0 \cf0  fnmatch.filter(os.listdir(picsFolder),
\f0\b \cf4 '*.jpg'
\f1\b0 \cf0 ):\
\

\f0\b \cf2 # Open the image
\f1\b0 \cf0 \
    img = Image.open(file)\
\

\f0\b \cf2 #Get actual image size and convert it to float
\f1\b0 \cf0 \
    width, height = img.size\
\
    baseim = Image.open(file)\
    logoim = Image.open(markFile) 
\f0\b \cf2 #transparent image
\f1\b0 \cf0 \
    baseim.paste(logoim,(int(width)-int(markWidth)-20,int(height)-int(markHeight)-10),logoim)\

\f0\b \cf2 #Recover EXIF data
\f1\b0 \cf0 \
    os.system(
\f0\b \cf4 "jhead -te Backup/*jpg *.jpg"
\f1\b0 \cf0 )\

\f0\b \cf3 for
\f1\b0 \cf0  filename 
\f0\b \cf3 in
\f1\b0 \cf0  fnmatch.filter(os.listdir(picsFolder),
\f0\b \cf4 '*.jpg'
\f1\b0 \cf0 ):\
    shutil.move(filename, 
\f0\b \cf4 "Watermarked/%s"
\f1\b0 \cf0  % filename)\
\
}