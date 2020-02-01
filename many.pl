#!/usr/bin/env perl

use strict;
use warnings;

sub main {
    foreach $name (@_) {
        system("python3 csv.py $name");
    }
    return 0;
}

exit(main(@ARGV));
