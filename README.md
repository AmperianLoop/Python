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
<p>1. Create the main folder and sub-folder by running the command</p>
<pre class="prettyprint lang-py prettyprinted" style="line-height: 1.42857;"><span class="pln">django</span><span class="pun">-</span><span class="pln">admin startproject </span><span class="typ">WebsiteName</span></pre><p><i style="color: rgba(0, 133, 255, 0.89);">In autoDjango.py</i>
</p>
<pre class="prettyprint lang-py prettyprinted" id="speakMess318" style="line-height: 1.42857; font-weight: bold;"><span class="com"># Creating the Django Project</span><span class="pln">
os</span><span class="pun">.</span><span class="pln">system</span><span class="pun">(</span><span class="pln">r</span><span class="str">'django-admin startproject '</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="typ">WebsiteName</span><span class="pun">)</span><span class="pln">  </span><span class="com"># This is like typing in the terminal</span><span class="pln">
time</span><span class="pun">.</span><span class="pln">sleep</span><span class="pun">(</span><span class="lit">2</span><span class="pun">)</span><span class="pln">                                </span><span class="com"># Give time to create the Django project folders.</span><span class="pln">
os</span><span class="pun">.</span><span class="pln">chdir</span><span class="pun">(</span><span class="typ">WebsiteName</span><span class="pun">)</span><span class="pln">                        </span><span class="com"># Desktop/WebsiteName</span></pre><p>
</p>
<p>2. Create the homepage app of your project in the main folder by running the command
</p>
<pre class="prettyprint lang-py prettyprinted" style="line-height: 1.42857;"><span class="pln">python manage</span><span class="pun">.</span><span class="pln">py startapp </span><span class="typ">Home_App_Name</span></pre>
<p><i style="color: rgba(0, 133, 255, 0.89);">In autoDjango.py</i>
</p>
<pre class="prettyprint lang-py prettyprinted" id="speakMess318" style="line-height: 1.42857; font-weight: bold;"><span class="com"># Creating the Home App inside Desktop/WebsiteName/</span><span class="pln">
os</span><span class="pun">.</span><span class="pln">system</span><span class="pun">(</span><span class="pln">r</span><span class="str">'python manage.py startapp '</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="typ">Home_App_Name</span><span class="pun">)</span><span class="pln">  </span><span class="com"># Makes the folders for your Home_App_Name.</span><span class="pln">
time</span><span class="pun">.</span><span class="pln">sleep</span><span class="pun">(</span><span class="lit">1</span><span class="pun">)</span><span class="pln">  </span><span class="com"># In case cpu is slow.</span></pre><p>
</p>
<p>3. Install the Home_App_Name and rest_framework to the file <i>WebsiteName/WebsiteName/settings.py</i> by typing the name under INSTALLED_APPS. Also, at the end of the file add the path to the static and media folders.</p>
<pre class="prettyprint lang-py prettyprinted" style="line-height: 1.42857;"><span class="pln">INSTALLED_APPS </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[</span><span class="pln">
        </span><span class="str">'Home_App_Name'</span><span class="pun">,</span><span class="pln">
        </span><span class="str">'rest_framework'</span><span class="pun">,</span><span class="pln">
        </span><span class="str">'django.contrib.admin'</span><span class="pun">,</span><span class="pln">
        </span><span class="str">'django.contrib.auth'</span><span class="pun">,</span><span class="pln">
        </span><span class="str">'django.contrib.contenttypes'</span><span class="pun">,</span><span class="pln">
        </span><span class="str">'django.contrib.sessions'</span><span class="pun">,</span><span class="pln">
        </span><span class="str">'django.contrib.messages'</span><span class="pun">,</span><span class="pln">
        </span><span class="str">'django.contrib.staticfiles'</span><span class="pun">,</span><span class="pln">
    </span><span class="pun">]</span><span class="pln">
    </span><span class="pun">...</span><span class="pln">
    STATIC_URL </span><span class="pun">=</span><span class="pln"> </span><span class="str">'/static/'</span><span class="pln">
    STATIC_ROOT </span><span class="pun">=</span><span class="pln"> os</span><span class="pun">.</span><span class="pln">path</span><span class="pun">.</span><span class="pln">join</span><span class="pun">(</span><span class="pln">BASE_DIR</span><span class="pun">,</span><span class="pln"> </span><span class="str">'static'</span><span class="pun">)</span><span class="pln">  
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media') 
</span></pre><p><i style="color: rgba(0, 133, 255, 0.89);">In autoDjango.py</i>
</p>
<pre class="prettyprint lang-py prettyprinted" style="line-height: 1.42857;"><span class="com"># Install Home_App_Name, rest_framework , and declare MEDIA_URL by reading and writing to settings.py.</span><span class="pln">
settings_dot_py </span><span class="pun">=</span><span class="pln"> os</span><span class="pun">.</span><span class="pln">path</span><span class="pun">.</span><span class="pln">join</span><span class="pun">(</span><span class="pln">desktop</span><span class="pun">,</span><span class="pln"> </span><span class="typ">WebsiteName</span><span class="pun">,</span><span class="pln"> </span><span class="typ">WebsiteName</span><span class="pun">,</span><span class="pln"> r</span><span class="str">'settings.py'</span><span class="pun">)</span><span class="pln">
    </span><span class="kwd">with</span><span class="pln"> open</span><span class="pun">(</span><span class="pln">settings_dot_py</span><span class="pun">,</span><span class="pln"> </span><span class="str">'r'</span><span class="pun">)</span><span class="pln"> </span><span class="kwd">as</span><span class="pln"> f</span><span class="pun">:</span><span class="pln">
    contents </span><span class="pun">=</span><span class="pln"> f</span><span class="pun">.</span><span class="pln">readlines</span><span class="pun">()</span><span class="pln">
    contents</span><span class="pun">.</span><span class="pln">insert</span><span class="pun">(</span><span class="lit">125</span><span class="pun">,</span><span class="pln"> </span><span class="str">"STATIC_ROOT = os.path.join(BASE_DIR, 'static')"</span><span class="pln">
                         </span><span class="str">'\n'</span><span class="pln"> </span><span class="str">"MEDIA_URL = '/media/'"</span><span class="pln"> </span><span class="str">'\n'</span><span class="pln">
                         </span><span class="str">"MEDIA_ROOT = os.path.join(BASE_DIR, 'media')"</span><span class="pun">)</span><span class="pln">
    contents</span><span class="pun">.</span><span class="pln">insert</span><span class="pun">(</span><span class="lit">33</span><span class="pun">,</span><span class="pln"> </span><span class="str">"    '"</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="typ">Home_App_Name</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="str">"',"</span><span class="pln"> </span><span class="str">'\n'</span><span class="pln">
                                                       </span><span class="str">"    'rest_framework',"</span><span class="pln"> </span><span class="str">'\n'</span><span class="pun">)</span><span class="pln">
    </span><span class="kwd">with</span><span class="pln"> open</span><span class="pun">(</span><span class="pln">settings_dot_py</span><span class="pun">,</span><span class="pln"> </span><span class="str">'w'</span><span class="pun">)</span><span class="pln"> </span><span class="kwd">as</span><span class="pln"> f2</span><span class="pun">:</span><span class="pln">
        contents </span><span class="pun">=</span><span class="pln"> </span><span class="str">""</span><span class="pun">.</span><span class="pln">join</span><span class="pun">(</span><span class="pln">contents</span><span class="pun">)</span><span class="pln">  </span><span class="com"># Turn array to string.</span><span class="pln">
        f2</span><span class="pun">.</span><span class="pln">write</span><span class="pun">(</span><span class="pln">contents</span><span class="pun">)</span></pre><div><span class="pun">
</span></div><p>4. The basic project is built. Now going to enhance with custom files by overriding the models.py, urls.py (urlsSuper.py), urls.py (sub), views.py, admin.py, forms.py, serializers.py with the files in the folder autoDjangoDep. Also the same for static, templates, and media.</p>
<p><i style="color: rgba(0, 133, 255, 0.89);">In autoDjango.py</i>
</p>
<pre class="prettyprint lang-py prettyprinted" style="line-height: 1.42857;"><span class="com"># Copying the files from autoDjangoDep folder located on desktop.</span><span class="pln">
</span><span class="pln"><font color="#87ceeb">... See below for code ...</font>
</span></pre><p><i>
</i></p>
<p><i>5. </i>Before running the<i> </i><span style="color: rgb(135, 206, 235); background-color: black; font-family: Menlo, Monaco, Consolas, "Courier New", monospace; font-size: 13px;">python manage.py runserver</span> command,<i> "sync" </i>the models (classes) from the models.py to tables in MySqlite3 by running the commands</p>
<pre class="prettyprint lang-py prettyprinted" id="speakMess318" style="line-height: 1.42857; font-weight: bold;"><span class="com">python manage.py makemigrations</span></pre><p>and </p>
<pre class="prettyprint lang-py prettyprinted" id="speakMess318" style="line-height: 1.42857; font-weight: bold;"><span class="com">python manage.py migrate</span></pre><p>Also create a super user by running the command</p>
<pre class="prettyprint lang-py prettyprinted" id="speakMess318" style="line-height: 1.42857; font-weight: bold;"><span class="com">python manage.py createsuperuser</span></pre><p><i>
</i></p>
<p><i>6. </i>Should all be working now.</p>
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
