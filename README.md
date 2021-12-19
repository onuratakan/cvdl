# CVDL

## What is CVDL?
CV Description Language is the first part of a project aiming to create an open source format for description of Curriculum Vitae(CV) and Resume documents. 

## High Level Project Roadmap
First step of the project includes design and implementation of CVDL language and compiler, which is going to be constituting the back-end of the system and allow anyone to easily transcribe the contents of theirs CV's into CVDL.

Next step of the project includes rendering this data into a PDF file, essentially creating the CV itself. At first, we will be generating Latex files with a select few public templates, later we will be developing our own themes and PDF rendering engine.

Once project moves into PDF rendering phase after Latex Generation phase, we will also design CVTL(CV Theme Language), defining views and themes over the CV's. An analogy at this point could be made with HTML/CSS, where CVDL is HTML and CVTL is CSS.

## Motivations for CVDL
Our motivation is to allow everyone to take control of their CV documents without relying on paid subscriptions to CV Builders. We want to empower people to design their own themes, publish them, allow others to use them. We also want people to be able to separate their concerns about the content of their CV's from the design.

## Contributions
We are very much open to every kind of help. From the design of the CVDL grammar to the rendering engine, anything you would like to help will delight us. Please reach out to me at alpkeles99@gmail.com about any ideas, or just drop some issues or pull requests. 