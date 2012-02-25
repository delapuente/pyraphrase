#-*- encoding:utf-8 -*-
'''
This Python module can be used as a command line utility or as a library. As a
command line utility, it accepts two sentences and prints a list of guessed
periphrasis.

As library, the get_periphrasis() method is available. See its documentation
for further details.

IMPLEMENTATION DETAILS:
The algorithm is inspired by Callison-Burch thesis [1] where the main idea
is to identify pairs of common words inside both sentences and to assume that
the text between them should be the same but expressed in different ways.

    I.e.:
    Sentence 1: I am looking for the key
    Sentence 2: I am in the search of the key

    periphrasis: (looking for, in the search of)

Another equivalent approach is to see the differences between the sentences.
To do this, the Python difflib package is used. This module uses the
difflib.Differ class to compare both sentences and determine their differences.

    I.e:
    Sentence 1: I am looking for the key
    Sentence 2: I am in the search of the key

    Difference:
      I
      am
    - looking
    - for
    + in
    + the
    + search
    + of
      the
      key

The output is a representation of what operations are needed to transform
sentence 1 into sentence 2 (remove 'looking for'; and add 'in the search
of'). Those lines starting by + and - characters are the differences that can be
considered the periphrasis.

Some notes about the implementation of the algorithm described in [2] are
commented in the Python API documentation [3].

[1] http://www.cs.jhu.edu/~ccb/publications/callison-burch-thesis.pdf

[2] Paul E. Black, "Ratcliff/Obershelp pattern recognition", in Dictionary
of Algorithms and Data Structures [online], Paul E. Black, ed., U.S.
National Institute of Standards and Technology. 17 December 2004.
(accessed TODAY)
Available from: http://www.nist.gov/dads/HTML/ratcliffObershelp.html

[3] http://docs.python.org/library/difflib.html#difflib.Differ

@author Salvador de la Puente González
'''
import re
import sys
import difflib

def get_paraphrases(sentence_a, sentence_b):
    '''
    get_paraphrases() returns a tuple with the list of pairs of periphrasis
    shared among the sentences, the longest common subsequence and some
    statistics (token sets and lcsr or longest commont subsequence ratio which
    is the percentage of the common part among the sentences.)

    See the module documentation for further details.
    '''

    wordset_a = sentence_a.split()
    wordset_b = sentence_b.split()
    delta = difflib.Differ().compare(wordset_a, wordset_b)

    result = []
    h = {u'+':[], u'-':[]}
    equal, context = [], []
    ignoring = True
    for line in delta:
        current_char = line[0].strip()
        word = line[1:].strip()
        if not current_char:
            if not ignoring:
                if result:
                    result[-1] += [context]
                result += [[h[u'+'], h[u'-'], context]]
                h = {u'+':[], u'-':[]}
                context = []

                ignoring = True

            equal += [word]
            context += [word]
            continue

        else:
            ignoring = False

        if current_char in h:
            h[current_char] += [word]

    if result:
        result[-1] += [context]
    if not ignoring:
        result += [(h[u'+'], h[u'-'], context, [])]

    # Compute statistics
    stats = {
        'sets':(wordset_a, wordset_b),
        'lcsr':(float(len(equal))/len(wordset_a),
                           float(len(equal))/len(wordset_b))
    }
    return result, equal, stats
