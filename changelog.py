#!/usr/bin/python

"""
Sample :

* Tue May 17 2016 Siteshwar Vashisht <svashisht@redhat.com> - 4.3.42-5
- Do not set terminate_immediately and interrupt_immediately while expanding tilda
  Resolves: #1336800
"""

import datetime
import sys

if (len(sys.argv) < 4):
    print "Usage: python changelog.py <release_number> <release_message> <related_bug_string>"
    print 'For e.g.: python changelog.py 4.3.42-5 "Do not set terminate_immediately and interrupt_immediately while expanding tilda" "Resolves: #1336800"'
    print "\nwill produce : \n"
    print '* Thu Jun 23 2016 Siteshwar Vashisht <svashisht@redhat.com> - 4.3.42-5'
    print '- Do not set terminate_immediately and interrupt_immediately while expanding tilda'
    print '  Resolves: #1336800'
    sys.exit(1)

today = datetime.date.today()
release_number = sys.argv[1]
release_message = sys.argv[2]
related_bug = sys.argv[3]
print "* {} {} <{}> - {}".format(today.strftime("%a %b %d %Y"), "Siteshwar Vashisht", "svashisht@redhat.com", release_number)
print "- {}".format(release_message)
print "  {}".format(related_bug)
