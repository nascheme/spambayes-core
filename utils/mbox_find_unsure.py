#!/usr/bin/env python3
#
# Dump messages that Spambayes is unsure about to stdout.

import sys
import mailbox
from spambayes.mboxutils import get_message
from spambayes.cdb_classifier import CdbClassifier
from spambayes.tokenizer import tokenize

DB_FILE = sys.argv[1]

_bayes = CdbClassifier(DB_FILE)


def classify(msg):
    return _bayes.spamprob(tokenize(msg))


def main():
    unsure = 0
    for fn in sys.argv[2:]:
        mbox = mailbox.mbox(fn, get_message)
        for msg in mbox:
            p = classify(msg)
            if 0.1 < p < 0.7:
                unsure += 1
                sys.stdout.buffer.write(msg.as_bytes(unixfrom=True))
    sys.stderr.write('unsure %d\n' % unsure)


if __name__ == '__main__':
    main()
