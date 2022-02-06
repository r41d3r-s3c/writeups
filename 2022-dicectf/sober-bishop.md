# DiceCTF 2022 - Misc/Sober-Bishop - Writeup

**Writeup by: r41d3r**

## Problem

The only clue given was a single regex line of the flag format, a hyperlink and two text files.

Flag format is dice{[a-z0-9_-]+}

Link given: https://github.com/openssh/openssh-portable/blob/d9dbb5d9a0326e252d3c7bc13beb9c2434f59409/sshkey.c#L1180

File 1: flag:
```
+----[THIS IS]----+
|          o  o+++|
|         + . .=*E|
|        B . . oo=|
|       = . .  .+ |
|        S        |
|                 |
|                 |
|                 |
|                 |
+---[THE FLAG]----+
```

File 2: hash:
```
+----[THIS IS]----+
|     .E=.        |
|      o..        |
|     o ..        |
|    o o.         |
|     O .S        |
|    o B          |
|     o o         |
|  ... B          |
|  +=.= .         |
+---[md5(FLAG)]---+
```

## Solution

First, I read through the file in the hyperlink, but it didn't immediately make sense to me.

I wasn't really sure where to start with this challenge, so first step was google.  Checking out a few searches on randomart, and that led me to 2 pages that helped me get going:

**Description of Randomart creation**
https://pthree.org/2013/05/30/openssh-keys-and-the-drunken-bishop/

**App that creates the randomart for the text you submit**
https://www.jfurness.uk/the-drunken-bishop-algorithm/

Randomart is created by what's called a Drunken Bishop walk, so the Sober Bishop play on words of the challenge title was neat.  After reading the article from pthree.org, I thought it wouldn't be too difficult to write a python script to create a calculated string that compares a string's randomart to the original randomart.

Playing with the code and knowing that it begins with `dice{`, I was able to see that there were only 2 options after, '5' and 'u', and then about 30 second characters.  This significantly decreased the calculation time.

Here is a sample of the output and the full script is included in the repository:

**Sample Output**
```
dice{5_
Testing:  1 possibles
Testing:  31 possibles
Testing:  526 possibles
Testing:  5466 possibles
Testing:  35060 possibles
Testing:  113520 possibles
Testing:  140804 possibles
dice{5_dzran0} : ['Same', 153] Possible Answer
dice{5_dzrid2} : ['Same', 153] Possible Answer
dice{5_n25an0} : ['Same', 153] Possible Answer
dice{5_zr4an0} : ['Same', 153] Possible Answer
```

After skimming through the output a few times I noticed one was clearly a word vs. nonsense.  Including a couple others for comparison.

**Sample with answer**
```
dice{unr4l0od} : ['Same', 153] Possible Answer
dice{unr4nd0m} : ['Same', 153] Possible Answer
dice{unr4nplp} : ['Same', 153] Possible Answer
dice{unr4nppl} : ['Same', 153] Possible Answer
dice{unr4n0el} : ['Same', 153] Possible Answer
dice{unr4n0md} : ['Same', 153] Possible Answer
```

This one, `dice{unr4nd0m}`, jumped out to me and trying that as the flag completed the challenge.  I started working on an md5 comparison while the possibles were being calculated but didn't finish before trying the proper flag.

The script named sober-bishop.py is included in the repository.
