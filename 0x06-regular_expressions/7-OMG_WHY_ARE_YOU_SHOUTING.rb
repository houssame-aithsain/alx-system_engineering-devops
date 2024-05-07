#!/usr/bin/env ruby
# The goal of this task is to extract only capital letters from the string

puts ARGV[0].scan(/[A-Z]/).join
