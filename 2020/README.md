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
and somehow screwing up a dead simple problem.  He probably does.  It
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

## Day 3: Toboggan Trajectory

Fun, straightforward little puzzle today involving the usual ascii map
of `#`s and `.`s to indicate obstacles and open space.  I made a couple
dumb mistakes, but thankfully they blew up at runtime.  Once my program
actually worked, I got both solutions correct on the first try.  Just 
under 10 minutes for Part 1 and exactly 15 minutes total for both parts,
which left me ranked >2000th place.  Man these coders are fast!

## Day 4: Passport Processing

This was fun, but a little grindy translating all the constraints for the 
passport data fields into code.  I got a respectable sub-1000 rank for Part 1,
but a bunch of people caught up to and passed me while I slowly typed out
Part 2.  I cleaned things up a bit, as there is some speculation on the
boards that a future problem may call back to this one.

## Day 5: Binary Boarding

I knew what I had to do here and got to it, but I had an off-by-one
error in my logic that tripped me up.  Worse, the PyCharm debugger
just completely went haywire on me, and I could not figure out why.
I had to restart the entire application for it to start working again,
but I'd lost so much time by that point I just kinda threw in the 
towel and hacked my way through the rest of it.

Premature Generalization is a thing.  I stacked two `while True` loops
on top of each other to parse each sequence of characters when I really
should have just hardcoded the 7 and 3.  Worse, I missed the critical
insight.  I thought about using bit shifting to clean up my divide-by-twos,
but if only I'd continued on that train of thought I might've realized
that the whole number could simply be parsed as a string of bits!

Remarkable difference between my initial working code and my cleaned
up version.  It's really cool with a lot of these puzzles to see just
how little code is required when you fully understand the problem set
and are able to really boil the solution down to only what is necessary.

This was an ingenious puzzle.  Kudos to the AoC creator on this one.

## Day 6: Custom Customs

Of course my fastest, most accurate attempt so far would be on a day
when I couldn't start at 9pm...  Maybe the lack of pressure is what
allowed me to not make any dumb mistakes.  Whatever the cause, I was
able to just get to work, banging out about 15 lines of code in less
than ten minutes, with both answers correct on the first try.  Feels good, 
man.

## Day 7: Handy Haversacks

I was waiting for one of these puzzles... It took me 20 minutes just
to get the input parsed and another 15 to get an answer for Part 1, 
but I got it right on the first try without resorting to google or 
looking at any code from previous AoC puzzles.

Took me another 20 minutes to get the Part 2 sample input to work, 
but again I had the right answer on the first try.  1 hour total
for both parts, 3000+ ranking.  Not great, and my code was pret-ty
ug-ly, but I managed to futz my way through some sort of recursive
graph traversal using only my limited brain power and the PyCharm
debugger.

I gotta bone up on DFS and BFS algorithms!!!

Another great puzzle, though.  I love how creative this guy is.

## Day 8: Handheld Halting

I love these VM type puzzles!  One dumb mistake on Part 1, but
I made up a *lot* of time on Part 2 and almost cracked the Top
1000.

I took a lot of time cleaning this one up, as there's the possibility
this might come back repeatedly (like `intcode`) last year.  If it
doesn't, this will likely end up as my most over-engineered solution, 
by far!

Great day!  Enjoyed the puzzle and the refactoring.