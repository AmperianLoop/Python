<hr>

<h1>ytCCRemovingTags</h1>
<p>The Python script ytCCRemovingTags.py takes a file with tags and removes them all. Further editing is usually required since the auto generated sub titles do not have many punctuations.</p>

<h2>Manually obtain YouTube's auto generated sub titles.</h2>

1. Open the Network tab by right clicking on the page and selecting inspect element, a new window should pop up. click on the Network tab.

2. On the YouTube video player menu, click on the CC icon to activate the auto generated sub titles. This fetching of the sub title data is shown in the network tab as a file name timedtext?... Right click on the timedtext link and select to open in new tab.

3. Select all the text, ctrl + a, copy, ctrl + c, and paste, ctrl + v, to the file named ytAutoCC.txt which should be located in the same folder and level as the removingTagsFromYTautoCC.py

[![How to Get YT Auto GeneratedCC](https://github.com/valestro/Python/blob/master/PythonAllImagesGH/howToGetYTCCxml.gif?raw=true)](https://www.youtube.com/watch?v=r3nK-y1_5rI&feature=youtu.be)

<h2>Obtain YouTube's auto generated sub titles automatically using youtube-dl</h2>

<pre>youtube-dl --write-sub --write-auto-sub --sub-format "ttml" --sub-lang es --skip-download https://www.youtube.com/watch?v=fkPjFfhigcA</pre>

<hr>
STEPS FOR CREATING A DJANGO PROJECT
anImage
edit / run
1. Create the main folder and sub-folder by running the command

<pre>django-admin startproject WebsiteName</pre>
In autoDjango.py

<pre># Creating the Django Project
os.system(r'django-admin startproject ' + WebsiteName)  # This is like typing in the terminal
time.sleep(2)                                # Give time to create the Django project folders.
os.chdir(WebsiteName)                        # Desktop/WebsiteName</pre>


2. Create the homepage app of your project in the main folder by running the command

<pre>python manage.py startapp Home_App_Name<pre>
In autoDjango.py

<pre># Creating the Home App inside Desktop/WebsiteName/
os.system(r'python manage.py startapp ' + Home_App_Name)  # Makes the folders for your Home_App_Name.
time.sleep(1)  # In case cpu is slow.<pre>


3. Install the Home_App_Name and rest_framework to the file WebsiteName/WebsiteName/settings.py by typing the name under INSTALLED_APPS. Also, at the end of the file add the path to the static and media folders.

<pre>INSTALLED_APPS = [
        'Home_App_Name',
        'rest_framework',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]
    ...
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')  
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')</pre> 
In autoDjango.py

<pre># Install Home_App_Name, rest_framework , and declare MEDIA_URL by reading and writing to settings.py.
settings_dot_py = os.path.join(desktop, WebsiteName, WebsiteName, r'settings.py')
    with open(settings_dot_py, 'r') as f:
    contents = f.readlines()
    contents.insert(125, "STATIC_ROOT = os.path.join(BASE_DIR, 'static')"
                         '\n' "MEDIA_URL = '/media/'" '\n'
                         "MEDIA_ROOT = os.path.join(BASE_DIR, 'media')")
    contents.insert(33, "    '" + Home_App_Name + "'," '\n'
                                                       "    'rest_framework'," '\n')
    with open(settings_dot_py, 'w') as f2:
        contents = "".join(contents)  # Turn array to string.
        f2.write(contents)</pre>

4. The basic project is built. Now going to enhance with custom files by overriding the models.py, urls.py (urlsSuper.py), urls.py (sub), views.py, admin.py, forms.py, serializers.py with the files in the folder autoDjangoDep. Also the same for static, templates, and media.

In autoDjango.py

<pre># Copying the files from autoDjangoDep folder located on desktop.
... See below for code ...</pre>


5. Before running the python manage.py runserver command, "sync" the models (classes) from the models.py to tables in MySqlite3 by running the commands

<pre>python manage.py makemigrations</pre>
and

<pre>python manage.py migrate</pre>

Also create a super user by running the command

<pre>python manage.py createsuperuser</pre>


6. Should all be working now.

<pre># Automates the starting process of creating a project with Django, need a desktop and a folder named autoDjangoDep.
import os                                   # Navigate the file system.
from os.path import expanduser              # For cross operating system compatibility.
from shutil import copyfile, copytree       # Makes copying files simpler.
import time                                 # Time to sleep when building django project folders on slower computers.


home = expanduser("~")                      # Python automatically converts ~ to %HOMEPATH% on Windows.
desktop = os.path.join(home, 'Desktop')     # Note: Linux may not have a desktop, change accordingly.

os.chdir(desktop)                           # The below folder should also be located at the desktop
autoDjangoDep = os.path.join(desktop, 'autoDjangoDep')  # Desktop/autoDjangoDep/

# https://stackoverflow.com/questions/24520329/python-reference-a-file-in-the-same-directory-as-the-running-file?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
# autoDjangoDep = os.path.join(os.path.dirname(__file__),"autoDjangoDep")

# Variables used below
# WebsiteName = ''                          # WebsiteName/
# Home_App_Name = ''                        # WebsiteName/Home_App_Name/
# home_app_path = ''                        # Desktop/WebsiteName/Home_App_Name/

# Get user input for the name of the Django project, e.i. VCWeb.
WebsiteName = input('Enter your website Main folder name (which is also the main sub-folder hub name): ')

# Creating the Django Project
os.system(r'django-admin startproject ' + WebsiteName)      # This is like typing in the terminal
time.sleep(2)                                               # Give time to create the django project folders.
os.chdir(WebsiteName)                                       # Desktop/WebsiteName

# Get user input for the name of the Home App, e.i. VApp.
Home_App_Name = input('Enter your homepage apps name: ')

# Creating the Home App inside Desktop/WebsiteName/
os.system(r'python manage.py startapp ' + Home_App_Name)    # Makes the folders for your Home_App_Name.
time.sleep(1)  # In case cpu is slow.

# Desktop/WebsiteName/Home_App_Name/
home_app_path = os.path.join(desktop, WebsiteName, Home_App_Name)  # Used later as dst3.

# Install Home_App_Name, rest_framework , and declare MEDIA_URL by reading and writing to the settings.py file.
settings_dot_py = os.path.join(desktop, WebsiteName, WebsiteName, r'settings.py')  # Not sure I need the raw string.
with open(settings_dot_py, 'r') as f:
    contents = f.readlines()
    contents.insert(125, "STATIC_ROOT = os.path.join(BASE_DIR, 'static')"
                         '\n' "MEDIA_URL = '/media/'" '\n'
                         "MEDIA_ROOT = os.path.join(BASE_DIR, 'media')")

    contents.insert(33, "    '" + Home_App_Name + "'," '\n'
                                                       "    'rest_framework'," '\n')

    with open(settings_dot_py, 'w') as f2:
        contents = "".join(contents)  # Turn array to string.
        f2.write(contents)


# Copying the files from autoDjangoDep folder located on desktop.
# Defining variables of the file paths as sources and destinations to make a source to destination=src_dst dictionary.
# Then will loop through the keys and values of this dictionary to copy the files with the copyfile() function.
src3 = os.path.join(autoDjangoDep, 'models.py')  # autoDjangoDep/models.py
dst3 = os.path.join(home_app_path, 'models.py')  # WebsiteName/Home_App_Name/models.py
src6 = os.path.join(autoDjangoDep, 'urlsSuper.py')
dst6 = os.path.join(desktop, WebsiteName, WebsiteName, 'urls.py')
src7 = os.path.join(autoDjangoDep, 'urls.py')
dst7 = os.path.join(desktop, WebsiteName, Home_App_Name, 'urls.py')
src8 = os.path.join(autoDjangoDep, 'views.py')
dst8 = os.path.join(desktop, WebsiteName, Home_App_Name, 'views.py')
src9 = os.path.join(autoDjangoDep, 'admin.py')
dst9 = os.path.join(desktop, WebsiteName, Home_App_Name, 'admin.py')
src10 = os.path.join(autoDjangoDep, 'forms.py')
dst10 = os.path.join(desktop, WebsiteName, Home_App_Name, 'forms.py')
src11 = os.path.join(autoDjangoDep, 'serializers.py')
dst11 = os.path.join(desktop, WebsiteName, Home_App_Name, 'serializers.py')

src_dst = {src3: dst3,
           src6: dst6,
           src7: dst7,
           src8: dst8,
           src9: dst9,
           src10: dst10,
           src11: dst11}

# Looping through the keys and values of of src_dst to copy the files with the copyfile() function. Also Replace holder.
for s, d in src_dst.items():
    copyfile(s, d)

    with open(d, 'r')as f:  # f = file, c = contents
        c = f.readlines()  # a list

        with open(d, 'w')as f2:
            c = ''.join(c)
            c2 = c.replace("*Home_App_Name*", Home_App_Name)
            f2.write(c2)


# Copying folders
src4 = os.path.join(autoDjangoDep, 'static')
dst4 = os.path.join(home_app_path, 'static')
src5 = os.path.join(autoDjangoDep, 'templates')  # Here are all the html files.
dst5 = os.path.join(home_app_path, 'templates', Home_App_Name)  # WebsiteName/Home_App_Name/templates/Home_App_Name/
src13 = os.path.join(autoDjangoDep, 'media')
dst13 = os.path.join(desktop, WebsiteName, 'media')

copytree(src4, dst4)
copytree(src5, dst5)
copytree(src13, dst13)

#  Changing dirs
os.chdir(home_app_path)                 # WebsiteName/Home_App_Name/
os.chdir('templates')                   # WebsiteName/Home_App_Name/templates/
os.chdir(Home_App_Name)                 # WebsiteName/Home_App_Name/templates/Home_App_Name/

# Need to check if a folder. For now make sure no folder in dst5. Should not be any I think, Django convention.
for filename in os.listdir(dst5):       # dst5 = WebsiteName/Home_App_Name/templates/Home_App_Name/

    with open(filename, 'r')as f:  # f = file, c = contents
        c = f.readlines()  # a list

        with open(filename, 'w')as f2:
            c = ''.join(c)
            c2 = c.replace("*Home_App_Name*", Home_App_Name)
            f2.write(c2)</pre>
<hr>


<hr>
<hr>
