#!/usr/bin/env ruby
# The goal of this task is to extract "hbtn" from the string

puts ARGV[0].scan(/hb{0,1}tn/).join
