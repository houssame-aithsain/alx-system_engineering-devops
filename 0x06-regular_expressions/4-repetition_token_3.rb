#!/usr/bin/env ruby
# The goal of this task is to extract "hbtn" from the string

puts ARGV[0].scan(/hbt*n/).join
