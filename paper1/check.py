import subprocess
import sys
import os
import os.path


def execute(command):
    output=subprocess.check_output(command, stderr=sys.stdout, shell=True).decode("utf-8").splitlines()
    return output

def shell(command):
    try:
        output = subprocess.check_output(command, shell=True, stderr=sys.stdout)
        lines = output.decode("utf-8").splitlines()

    except Exception as e:
        lines = str(e)

    return lines

# print (execute("ls | fgrep Makefile"))

def banner(msg=""):
    name = sys._getframe(1).f_code.co_name
    print ()
    print (name.strip(), msg)
    print (79 * "=")

def wordcount(content):
    banner()
    wc = [0,0,0]
    wc[0] = execute('wc -w ' + content)[0].strip().split()[0]
    wc[1] = execute('ps2ascii report.pdf | wc -w')[0].strip()
    wc[2] = execute('wc -w report.bib')[0].strip().split()[0]

    print ('wc', wc[0], content)
    print ('wc', wc[1], 'report.pdf')
    print ('wc', wc[2], 'report.bib')

def find(filename, c, erroron=True):
    banner(c)
    counter = 1
    found = False
    with open(filename, "r") as f:
        for line in f:
            counter += 1
            if c in line:
                found = True
                print (counter, ": ", line, sep="")
    print ("passed:", erroron != found)
        
def floats(filename):
    banner()
            
    counter = {
        'begin{figure}' : 0,
        'begin{table}' : 0,
        'includegraphics' : 0,
        'label{' : 0,
        'ref{' : 0,
    }
    
    linecounter = 1
    found = False
    with open(filename, 'r') as f:
        content = f.readlines()
        
    for line in content:
        linecounter += 1
        for c in counter:
                
            if c in line:
                counter[c] += 1
                print (linecounter, ": ", line.strip("\n"), sep="")

    # rename
    found = {
        'figures' : counter['begin{figure}'],
        'tables' : counter['begin{table}'],
        'includegraphics' : counter['includegraphics'],
        'labels' : counter['label{'],
        'refs': counter['ref{']
    }
    found['floats']=found['figures'] + found['tables']

    print()
    for entry in found:
        print (entry, found[entry])
    print()
    
    print ( found['figures'] + found['tables'] >= found['refs'], ': ref check passed: (refs >= figures + tables)')
    print (found['figures'] + found['tables'] >= found['labels'], ': label check passed: (refs >= figures + tables)')
    print (found['figures'] >= found['includegraphics'], ': include graphics passed: (figures >= includegraphics)')

    print()
    print('Label/ref check')
    linecounter = 0
    top = max(found['figures'],found['tables'], found['includegraphics'])
    passing = True
    for line in content:
        linecounter += 1
        for i in range(1,top+1):
            if "igure {i}".format(i=i) in line:
                print (linecounter, ": ", line, sep='')
                passing = False
            if "able {i}".format(i=i) in line:
                print (linecounter, ": ", line, sep='')
                passing = False
    if passing:
            msg = ''
    else:
        msg = '-> labels or refs used wrong'
    print('passed:', passing, msg)

                
def yamlcheck(filename):
    banner()
    os.system('yamllint ../README.yml')


def bibtex(filename):
    banner()
    print()
    print ('label errors')
    print()
    with open("{filename}.bib".format(filename=filename), 'r') as f:
        content = f.readlines()
    counter = 0
    for line in content:
        counter += 1
        if "@" in line:
            if '@String' in line or '@Comment' in line:
                continue
            if not ',' in line:
                print (counter, ": you forgot the , after a bibtex label ")
                return

            label = line.split("{")[1].strip()[:-1]
            if '_' in label:
                print (counter, ": ", label, ": do not use _ in labels:", sep = '')
            if ' ' in label:
                print (counter, ": ", label, ": do not use ' ' (spaces) in labels:", sep='')
    print()
    print('bibtex errors')
    print()
    output = shell('bibtex {filename}'.format(filename=filename))
    print ('\n'.join(output[3:]))

def bibtex_empty_fields(filename)               
    banner()
    print()
    print('entries in general should not be empty in bibtex')
    print()
    find(filename + ".bib", '""')
    

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def ascii(filename):
    banner()
    with open("{filename}".format(filename=filename), 'r') as f:
        content = f.readlines()
    # print (ord('"'))
    counter = 0
    for line in content:
        counter += 1
        for c in line:
            if not is_ascii(c):
                print ("non ascii found", ord(c))
    
if os.path.isfile('content.tex'):
    filename = 'content.tex'
else:
    filename = 'report.tex'    
                
wordcount(filename)
find(filename, '"')
find(filename, 'footnote')
yamlcheck('../README.yml')
find("report.tex", "input{format/i523}", erroron=False)
floats(filename)
bibtex('report')
bibtex_empty_fields('report')                
ascii(filename)
