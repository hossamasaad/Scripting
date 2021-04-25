# dirLatex
A directory-tree generator script in LaTeX format

## What is this?
A python script generates the code to represent a directory tree in LaTeX

## Example ?!
    > python dirLatex.py /Users/hossam/workplace
    \dirLatex {%
    .1 {workspace} .
      .2 {csv_file.csv} .
      .2 {dirLatex.py} .
      .2 {dirLatexwdw.y.py} .
      .2 {flowers.csv} .
      .2 {hossam.txt} .
      .2 {main.py} .
      .2 {Module.py} .
      .2 {Test} .
        .3 {1} .
          .4 {hi.txt} .
      .2 {__pycache__} .
        .3 {Module.cpython-39.pyc} .
    }


## Windows or Linux ?
I have tested the script on Windows and Linux and it worked properly in both of them

## How can I use it?
### Requirements!
There are no requirements, just Python (https://www.python.org/downloads/)

### Download!
Direct Download (https://raw.githubusercontent.com/hossamasaad/dirLatex/main/dirLatex.py)

### Finaly Run it!!!
    > python <script path>/dirLatex.py <directory path>
