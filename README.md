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

<hr>


<hr>
<hr>
