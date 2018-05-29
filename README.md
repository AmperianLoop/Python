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
