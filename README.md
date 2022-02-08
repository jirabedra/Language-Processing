# Language-Processing
Language processing models and algorithms based on Jurafsky and Martin Speech And Language Processing
Sections will briefly cover some of the most relevant topics/algorithms I found on such book. They will be mainly implenented in **Python**.

## Regular expressions

Regular expressions (regexes or regexps) are an easy application of language processing. Most of us programmers are familiar with them (despite not being our cup of tea...). Regexes are formulas or conditions that match text or strings. There are some standards for writing regexes; in this case I will use the JavaScript standard.   

The regex atom is the character or string of characters. For example hi is, in fact, a regex. hi will only match any substring within a string which contains an h followed by an i.   

The range operator - matches characters within certain range. For example, a-z matches any lowercase letter.  

[Screenshot]https://github.com/jirabedra/Language-Processing/edit/main/Pictures/01_sampleRegex.png?raw=true

The [ and ] operators act like the logical disjunction, a.k.a boolean OR operator. It matches any of the conditions inside the brackets.  Regex disjunction can also be noted with a vertical slash |. For instance, if we were to match any character t or character i within a string, we could either define [it] or i | t. 

There are a couple more operators I found to be useful when matching simple regexes. The negation operator ^ matches any string that does not contain any of its arguments. For example, ^a will match any character different to a lowercase a.  

Finally, I would like to mention the Kleene operators * and + (Kleene star and plus). Kleene * matches zero or more occurences of its preceding symbol. Kleene + matches one or more. Let us look at some examples:



Regexes can get tricky, and pretty nasty, when they are compound conditions. For the sake of brevity, we will not cover such examples in this guide.  

## Finite State Automata
We will try to build three equivalent models that let us represent **Finite State Automata (FSA)**. FSAs can be used in text search. This will be the most basic use case for NLP.  

FSA is a particular case of a Turing Machine. The machine will read the given input and determine whether it belongs to a regular expression from a regular language or not. Naturally, FSAs, in particular DFSAs (see above) are very restricted. Complex languages like English or Polish are not that easily defined. Such languages have, not only a complex syntax (what symbols and combination of symbols are legal in the lenguage), but semantics (what is the meaning of each symbol and how do such meaning interact) should be taken into consideration.   

A simple use case of FSAs I thought could be easy to work around with are mathematical expressions. We will see these later on. Let us proceed and define the simplest FSAs: **Deterministic FSAs**.

### Deterministic Finite State Automata (DFSA)
In order to define a general FSA, we have to define:
A finite set of N states        <img src="https://render.githubusercontent.com/render/math?math={\color{white}Q = q_0 , q_1 , ... , q_{N-1}}">   
A finite alphabet of symbols <img src="https://render.githubusercontent.com/render/math?math={\color{white} \Sigma}">   
A start state <img src="https://render.githubusercontent.com/render/math?math={\color{white} q_0}">   
A set of final states <img src="https://render.githubusercontent.com/render/math?math={\color{white} F \subseteq Q}">  
A transition function between states <img src="https://render.githubusercontent.com/render/math?math={\color{white} \delta \subset Q X \Sigma \to Q}"> so that, given a certain state q and an input symbol/action i, it returns a new state q'. We will model this function with a lookup table for general Deterministic Turing Machines, while we will model this with a tape and symbols for defining the **D-Recognize(tape, machine)** algorithm.

#### D-Recognize Algorithm
The D-Recognize algorithm takes an input tape and a given FSA. The machine **accepts** the string contained in the tape if its legal within the defined formal language (formal lenguages will be covered later within this text). It **rejects** the string otherwise. In such case, we say that the string is **illegal**.  
The model we will define in Python can be found in dfsa.py in the **Code** folder. The application can be used in the following way:  

The program must be fed with two different .csv files. The first one describes the transitions. It fills a lookup table which be used to construct the machine. The second file represents the tape, and it should contain a string. The program will print either **accepted** or **rejected**, according to the inputs given.  
**Note:** as a **deterministic** FSA, given any state q, there should exists only one symbol i such that a pair (q,i,q') exists; else the machine will not be successfully constructed. 

Within this repository, implementations for these models can be found inside the **Code** folder. 
