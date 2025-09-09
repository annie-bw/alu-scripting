#!/usr/bin/env ruby

# This regex captures:
# 1. sender: [from:...] 
# 2. receiver: [to:...]
# 3. flags: [flags:...]
pattern = /\[from:([+\d]+)\].*?\[to:([+\d]+)\].*?\[flags:([-\d:]+)\]/ 

ARGF.each_line do |line|
  # Remove HTML entities like &nbsp; that may appear in logs
  clean_line = line.gsub('&nbsp;', ' ')

  if match = clean_line.match(pattern)
    sender, receiver, flags = match.captures
    # Print exactly in requested format: [SENDER],[RECEIVER],[FLAGS]
    puts "#{sender},#{receiver},#{flags}"
  end
end
