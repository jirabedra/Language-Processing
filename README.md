# Language-Processing
Language processing models and algorithms based on Jurafsky and Martin Speech And Language Processing
Sections will briefly cover some of the most relevant topics/algorithms I found on such book. They will be mainly implenented in **Python**.

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
