#!/usr/bin/env ruby
# The goal of this task is to extract a 10 digit phone number from the string

puts ARGV[0].scan(/^\d{10}$/).join
