# Advent of Code 2020

## Day 1: Report Repair

Oh, man, just by sheer luck I had my input parser already set up for a list 
of numbers and I had the answer in under a minute, but... the site went down!
Well, that's a bummer.  I had the right solution on the first try for both 
parts, so I had that going for me, which is nice. (Yes, I realize this was a 
dead simple Day 1 puzzle, but I gotta get my wins where I can.)

When I finally managed to get back on to the site, I came in around rank 1000
for both parts, although the AoC author later nullified the Day 1 leaderboard 
for obvious reasons.

I know how fast the people on the leaderboard can go and I'm realizing that
even just picking my variables names as `puzzle_input` instead of `p` or 
whatever does matter.  I probably don't have a real shot at getting in the 
Top 100 for any day, but my plan is to do a first pass just to complete the
puzzle, then do a "cleaned up" version, and finally (if it makes sense) I'll
do a "generalized" solution.

## Day 2: Password Philosophy

Uh-oh... I'm insanely frustrated and it's only Day 2.  It's early in the event, 
so the puzzle was easy and I got to work.  I had my input all `split()`-parsed 
into a nice data structure, I ran the basic logic on it and... my answer was 
wrong.  I'm looking at my code and it's so simple I cannot figure out where
a bug could even be hiding.  I step through the parser and make sure things
are as expected, and they are.  I literally stare at it for minutes and 
(stupidly) try my same answer again, knowing there's no way in hell there
was some glitch and it's gonna be right this time.  For the briefest of 
moments, I entertain the notion that I got bad input (hey, the site went 
down Day 1, so anything's possible, right?)  I check my input file again, 
thinking maybe I didn't copy everything... but I did.  I'm totally out of
ideas, but just looking at my input file I happened to notice that it ended
on line 1000.  Then I stepped through my code again and noticed that my
password list was only 995... 

So, yeah, I decided (for some reason) to store the password list in a
hash table with the password as the key and the metadata as the value,
but of course there were duplicate passwords in the input leading to my
winding up with 5 fewer entries... so frustrating.  I sometimes wonder
if the author does that on purpose to trip up someone doing what I did
and someone screwing up a dead simple problem.  He probably does.  It
just sucks when your solution logic is correct but you failed at parsing
the input correctly.  Bleh.

Anyway, once I fixed that, my original logic was fine, but nearly 30
minutes had elapsed and I was well above 4000th place for today.

I cleaned up my code and did a generalized version as well, but it was
hard not to be disappointed.  One thing I notice the people who get on
the leaderboard do--and which would have prevented my stupid mistake--is
just solve the problem as they're parsing the input.  They don't even store
it in an intermediate data structure.  My doing so just added more code in
which a bug could hide.  Lesson learned.


