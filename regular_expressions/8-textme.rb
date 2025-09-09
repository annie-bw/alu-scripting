#!/usr/bin/env ruby

# Regex pattern to match the "from", "to", and "flags" fields in the log
pattern = /\[from:(\+?\d+)\]\s*\[to:(\+?\d+)\]\s*\[flags:([-\d:]+)\]/

ARGF.each_line do |line|
  # Try to match the pattern
  if match = line.match(pattern)
    sender, receiver, flags = match.captures
    # Print in the requested format
    puts "#{sender},#{receiver},#{flags}"
  end
end
