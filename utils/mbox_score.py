#!/usr/bin/env python3
#
# Score a mailbox file, dump scored messages to stdout.

import sys
import mailbox
from spambayes.mboxutils import get_message
from spambayes.cdb_classifier import CdbClassifier
from spambayes.tokenizer import tokenize
from spambayes.Options import options

DB_FILE = sys.argv[1]

_bayes = CdbClassifier(open(DB_FILE, 'rb'))


def classify(msg):
    prob, ev = _bayes.spamprob(tokenize(msg), evidence=True)
    msg['X-Spambayes'] = '%s %s' % (prob, ev)
    if prob < options['Categorization', 'ham_cutoff']:
        status = 'OK'
    elif prob > options['Categorization', 'spam_cutoff']:
        status = 'SPAM'
    else:
        status = 'UNSURE'
    # Always add the X-Spam-Status header (status and prob score).
    msg['X-Spam-Status'] = '%s %.3f' % (status, prob)


def main():
    for fn in sys.argv[2:]:
        mbox = mailbox.mbox(fn, get_message)
        for msg in mbox:
            classify(msg)
            sys.stdout.buffer.write(msg.as_bytes(unixfrom=True))


if __name__ == '__main__':
    main()
