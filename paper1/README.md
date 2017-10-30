Report format
=============

This directory contains a template that will be used for writing
reports. It is important that you do not modify the template so all
students have the same format template.

To make it simple we split the content and the format into two
different files.

The content is in content.tex which you may edit, The template is in
report.tex, which you are not allowed to edit.

Compiling the report
--------------------

We included a simple Makefile in the directory and if you have LaTeX
properly installed you can use it from commandline to create the
report.pdf:

    make

Please remember that you MUST NOT commit the report.pdf file to the
reporsitory. If we detect thsi we will remove it and do not review
your paper. This is to avoid that students submit papers that actually
do not compile in LaTeX. Make sure you paper always compiles.

This will also generate a simple check on some common issues. The 
log file is located in 

    report-latex.log
    
After the compilation is over.

Editing the report
------------------

Unfortunately, we noticed that some students modified our report template 
uneccesarrily. In orde to allow us to undo these changes easily, we have 
separated the format from the content of the file.

Thus you compile report.tex, but you just change your text in content.tex. 
As in this format content.tex will be included in the report.tex automatically
it is easier to manage.

    
Adding your own packages
------------------------

If you need to add additional usepackages, you need to ask for
approval first. You may not modify the color of hyperlinks or place
the figures in the text. But otherwise there will most likely be no
conflicts. To avoid any issue, check it first and ask for final
approval.

Compiling the Review
--------------------

Once your paper has been reviewed you will find a review.tx, a
issue.tex and a bibtex-error.tex file in your directory. With these
files you can create the review.pdf file with the command

    make review
