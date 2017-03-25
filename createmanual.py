
# coding: utf-8
from random import choice, randint
import re
import getpass
import os

user = str(getpass.getuser())
cwd = os.getcwd()

raw_windows = open("ulogme-master/data/windows.txt").read().decode('ascii', errors="replace")
raw_keyfreq = open("ulogme-master/data/keyfreq.txt").read().decode('ascii', errors="replace")

raw_windows = raw_windows.split('\n')
raw_keyfreq = raw_keyfreq.split('\n')

windows = []
keyfreq = []

# windows opened
for line in raw_windows:
    line = line[11:]
    windows.append(line)

# keys pressed
for line in raw_keyfreq:
    line = line[18:]
    keyfreq.append(line)

instructions = []
current_window = 0

# create an array with a random sets of instructions
while (current_window < len(windows)):
    current_window_number = randint(4, 12)

    set_of_instructions = []

    for line in range(current_window_number):
        if ((current_window + line) < len(windows)):
            set_of_instructions.append(windows[current_window + line])
            if (randint(1,10) > 5):
                set_of_instructions.append(choice(keyfreq))

    instructions.append(set_of_instructions)
    current_window = current_window + current_window_number



# build the html element to append
first_part = '''
<!-- Page -->
<div id="title" style="page-break-before: always">
 <h2>Instructions for Part
'''

second_part = 0

third_part = '''
</h2> <div id="line-instructions"></div>
</div>

<div id="instruction">
  <h4>Please Perform the following tasks:</h4>
'''

fourth_part = []

fourth_part_first = '''
<ol>
<li>Press the power button on your Digital Computer.</li>
<li>Wait until the screen loads.</li>
</ol>
'''

fifth_part = '''
</div>
<div class="footer">
  <p class="left">Page
'''

sixth_part = 3

sevent_part = '''
</p>
  <p class="right">User User Manual</p>
</div>
'''

for line in instructions:
    ol = '<ol>'
    for element in line:
        if len(element) < 2:
            if str(element) == '0':
                li = '<li> Look at your screen for ' + str(randint(1,200)) + ' seconds</li>'
            else:
                li = '<li> Press ' + str(element) + ' keys from your keyboard</li>'
        else:
            li = '<li> Open and use ' + str(element) + '</li>'
        ol = ol + li
    ol = ol + '</ol>'
    fourth_part.append(ol)

all_elements = first_part + str(second_part) +third_part + fourth_part_first + fifth_part + str(sixth_part) + sevent_part

for element in fourth_part:
    second_part = second_part + 1
    sixth_part = sixth_part + 1
    all_elements = all_elements + (first_part + str(second_part) + third_part + element + fifth_part + str(sixth_part) + sevent_part)

index = ''

for i in range(second_part):
    index = index + '<li>Instructions for Part ' + str(i) + '.....................................................................' + str(3+i) + '</li>'

from weasyprint import HTML, CSS

text = '''

<!-- Cover -->
<div id="cover" style="page-break-before: always">
  <h1>User Manual</h1>
  <h5>A comprehensive guide ''' + user + '''</h5>
  <p>Version 1.0.8 </p>

  <div id="copyright">
    <h4>Copyrights</h4>
    <p>
      Copyrights laws in your country may prohibit the use of your recorded instructions or copyrighted keystrokes with keystokes in the memory RAM, for anything other than private enjoyment. Also be aware that certain countries may ban the use of certain applications or the type of certains keystrokes in a certain pattern. This is uncertain in some cases. Penalties may include the prision or even death penalty.
    </p>
    <p>
      Get faster instructions, reduce errors, and save paper.
  For more information on User User Manuale and e-file,
  see Free Software Options for your User Manual in
  these instructions or go to userusermanual.com.
    </p>
  </div>

</div>

<div class="footer">
  <p>The 'Software Start Guide' and 'Quick Reference Guide' are not provided at the end of this manual.</p>
</div>

<!-- Check list -->
<div id="title" style="page-break-before: always">
  <h2>Item Check List</h2> <div id="line"></div>
  <p>
    Before starting, check that all the following items have been included with your package. If anything is missing, contact your dealer.
  </p>
</div>

<div id="images">
  <div class="icons">
    <img class="icon" src="./imgs/computer.png" />
    <p> Computer x1 </p>
  </div>

  <div class="icons">
    <img class="icon" src="./imgs/user.png" />
    <p> User ''' + user +'''</p>
  </div>
</div>

<ul>
  <li>If you purchased another user, check that his computer is included.</li>
  <li>
    Be careful not to lose any of the above items.
  </li>
</ul>

<div id="warning">
  <h4>Software Instruction Manual</h4>
  <p>The software Instruction Manuals are included in the CD-ROM as PDF Files. See the last page for instructions to look up manuals in the Software Instruction Manual. </p>
</div>

<div class="footer">
  <p class="left">Page 1</p>
  <p class="right">User User Manual</p>
</div>

<!-- Index -->
<div id="title" style="page-break-before: always">
 <h2>Index to Features</h2> <div id="line"></div>
</div>

<div id="index">
  <ul>
'''+ index + '''
  </ul>
</div>

<div class="footer">
  <p class="left">Page 2</p>
  <p class="right">User User Manual</p>
</div>
''' + all_elements

css = '''
#cover{
  margin-top: 200px;
  max-width: 400px;
  border-left: 12px solid #aaaaaa;
  padding: 40px;
}

#title h2{
  display: inline-block;
}

#line{
  width:350px;
  height: 10px;
  background: #aaaaaa;
  margin: 0px 0px 2px 10px;
  display: inline-block;
}

#line-instructions{
  width:280px;
  height: 10px;
  background: #aaaaaa;
  margin: 0px 0px 2px 10px;
  display: inline-block;
}

#images{
  margin: 50px;
}

#warning{
  margin: 100px 20px 20px 20px;
  border: 1px solid black;
  padding: 10px;
}

#index{
  padding: 10px 0px 0px 0px;
}

#instruction{
  margin: 70px 0px 0px 10px;
}

#copyright{
  margin: 150px 0px 0px 0px;
}

.footer{
  border-top: 1px solid black;
  position: absolute;
  bottom: 10px;
}

.footer p{
  font-size: 10px;
}

.right{
  position: relative;
  padding-left: 380px;
  display: inline-block;
}

.left{
  position: relative;
  padding-left: 20px;
  display: inline-block;
}

.icons{
  display: inline-block;
  text-align: center;
}

.icon{

}
'''

# create the document
HTML(string=text, base_url='file://' + cwd + '/imgs').write_pdf(user+'manual.pdf', stylesheets=[CSS(string=css)])
