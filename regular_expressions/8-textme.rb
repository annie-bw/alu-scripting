#!/usr/bin/env ruby

pattern = /From:\s*(\+?\d+)\s*To:\s*(\+?\d+)\s*FLAGS:\s*([\w,]+)/

ARGF.each_line do |line|
  if match = line.match(pattern)
    sender, receiver, flags = match.captures
    puts "#{sender},#{receiver},#{flags}"
  end
end
