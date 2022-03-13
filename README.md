Spambayes Core
==============

Background
----------

This is a pruned down version of "spambayes", containing only the core parts.
Most importantly, it includes the classifier and tokenizer.  Code has been
converted to run with Python 3.  I have not done extensive testing and so the
code conversion may have introduced bugs.

The initial code was taken from Skip's github repo:

    <https://github.com/smontanaro/spambayes>

See LICENSE.txt for the copyright and license terms.


Training
--------

Create a corpus by putting ham (non-spam) and spam messages into mbox
files.  The number of messsages in each file does not have to the be the
same.

Example script for training database:

    #!/bin/sh
    set -e
    SPAMBAYES=$HOME/src/spambayes-core
    BAYESCUSTOMIZE=$(pwd)/bayescustomize.ini
    export BAYESCUSTOMIZE
    python3 $SPAMBAYES/utils/tte.py -R \
            -o Categorization:ham_cutoff:0.05 \
            -o Categorization:spam_cutoff:0.80 \
            -g Corpus/ham.mbox  -s Corpus/spam.mbox -p db.pkl
    python3 $SPAMBAYES/utils/hammie2cdb.py -p db.pkl wordprobs.cdb
    rm -f db.pkl


The resulting database is "wordprobs.cdb" and is in the "CDB" format.

You can check the word probabilties by dumping the database:

    $HOME/src/spambayes-core/utils/dump_cdb.py wordprobs.cdb |less


Classifying
-----------

Once the database has been created, it can be used to classify incoming
email as spam.  For best performance, this should be done by a
background daemon process.   To use the database, code like below can be
used:

    # Assumes that BAYESCUSTOMIZE envvar is set.
    from spambayes.cdb_classifier import CdbClassifier
    from spambayes.tokenizer import tokenize
    from spambayes.Options import options
    _BAYES = CdbClassifier(open(DB_FILE, 'rb'))

    def check_spam(msg):
        # msg is a email.message.Message object
        prob = _BAYES.spamprob(tokenize(msg))
        if prob < options['Categorization', 'ham_cutoff']:
            status = 'OK'
        elif prob > options['Categorization', 'spam_cutoff']:
            status = 'SPAM'
        else:
            status = 'UNSURE'
        return status, prob
