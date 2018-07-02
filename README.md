# bannepy

nostalgic banner program.

## Overview
 you can print banner text from command line.  
 when need to banner text for your programs(logging etc...) then you can use class.  
 (see sample_bannepy.py)

## Description
**banne.py**  
banner program  

*command line parameter*

* pixel char  
bright=" "  
dark=#

* style  
style=bold,italic,bottomline,linethrough,kerning

* margin for space of char and line.  
margin=1,1

* word count for line  
wrap=12

* other option  
 change backslash for yen, use symbol  
option=yen,symbol

*parameter for class use only*

 * custom font  
pybanner.set_config("font", FONT_OBJECT)
 * font width  
pybanner.set_config("font.width", int)  

---  
**sample_bannepy.py**  
usage sample  

---  
**aa2h.py**  
dot art to hex  
 * example  
python3 aa2h.py ../dot_sample.txt  

## Requirement

## Usage
```
python3 banne.py ABC123
   #   ####   ###    #    ###   ### 
  # #  #   # #   #  ##   #   # #   #
 #   # #   # #       #      #      #
 #   # ####  #       #     #    ### 
 ##### #   # #       #    #        #
 #   # #   # #   #   #   #     #   #
 #   # ####   ###   ###  #####  ### 

python3 banne.py "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz:;<=>?@#$'()*+,./[\]^_\`{|}~%&" -w12 -s=kerning.bottomline
  ###   #   ###   ###     #  #####  ###  #####  ###   ###    #   #### 
 #   # ##  #   # #   #   ##  #     #   #     # #   # #   #  # #  #   #
 #  ##  #     #      #  # #  #     #        #  #   # #   # #   # #   #
 # # #  #    #    ###  #  #  ####  ####    #    ###   #### #   # #### 
 ##  #  #   #        # #####     # #   #  #    #   #     # ##### #   #
 #   #  #  #     #   #    #  #   # #   #  #    #   # #   # #   # #   #
  ###  ### #####  ###     #   ###   ###   #     ###   ###  #   # #### 
######################################################################
omitted below...

echo 'Hello! banne.py' | python3 banne.py

python3 banne.py
input your text.
```

## Install

## Contribution

## Licence
there is licensed under the Apache License, Version2.0
(see ./LICENSE.txt)

## Author
Nobuo Tateishi(https://github.com/nob0tate14)
