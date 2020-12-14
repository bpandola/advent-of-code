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

## Day 9: Encoding Error

Cool puzzle.  Took me ten minutes for each part, which was **way too slow**!

## Day 10: Adapter Array

The degree of difficulty definitely got ratcheted up today.   Part 1 was
a fantastic example of an overly-complicated problem description masking
a dead simple solution.  I'm coding up this `while` loop with an embedded 
`for` loop, and painstakingly testing parts of the input that fall within
this `0-3` range, all so I could put values into an array I named `order`.

So... yeah... the smart people literally just called `sort` on the input
for Part 1.  This was by far my most naive brute force attempt for Part
1, which is saying something!

Part 2 was interesting because it was immediately clear that a brute 
force attempt would not be workable.  I quickly came up with what I 
thought was a clever solution (just keeping track of the parts of the
chain that had multiple possible combinations), but it took me a while
to implement a (messy) working version of it.  It performed exactly
as I'd hoped, though, taking just milliseconds to return an answer in
the 10s of trillions.

Everyone on reddit is saying this is just a DP (Dynamic Programming)
problem or easily solvable with memoized recursion, but I don't see
anyone else using my technique.  I don't know if I just totally lucked
out, or if I came up with something novel.

Regardless, it worked!  And, to quote the great George Costanza: "It didn't 
really take very long either."

## Day 11: Seating System

Today was a fun cellular automaton puzzle (involving occupied and unoccupied 
seats in a ferry terminal waiting area because the author does a great job
of fitting each puzzle into an overarching and coherent narrative, which 
is pretty creative, I must say).  

Anyway, I tend to work on these 2D puzzles by translating the input into 
a dictionary that maps coords (x,y) to whatever value is at that location.
It's not fast, but it does have some nice properties, depending on the 
problem space, that help speed up the coding time.

I tried to be clever by using a defaultdict and then not bothering to 
check grid boundaries, but I dropped that in my cleaned up version in 
favor of just catching KeyError exceptions for boundary testing, which 
seemed to work a bit better.

I felt like I was fast on Part 1, but it took me almost 30 minutes.
I got the right answer on the first try, which is always nice.  And I 
made up some time on Part 2, which is even nicer.

Decent showing tonight, but then of course I go check the subreddit
for a reality check.  It's really amazing how bright, clever, and
fast these top guys/gals are.  It also never ceases to amaze me just
how many ways you can tackle these problems.  Most of the
pros just treated the grid as an array of strings, which is way faster
than using dictionaries, of course.  Other people used grid "helper"
libraries.  That's fine, I guess; but I always try to do the whole
thing on my own from scratch, only using standard libraries when
absolutely necessary.  Maybe I should reconsider...

Regardless, I enjoyed this one!  And, as always, I learned a thing or
two along the way (as well as after the fact).

## Day 12: Rain Risk

I like the puzzles that involve something moving around a 2D grid.  I
always seemed to do better than usual on them, which I attribute to all the
game development stuff I did as a kid.  There have been lots of AoC
puzzles like this, so I grabbed some code from a previous year/day, 
but in the end it wasn't all that helpful.

I drew a complete blank on how to rotate the direction the ship was
facing in Part 1, so I ended up just creating these huge look-up tables
and putting the values in manually.  It worked, but it was pretty sad.

Part 2 was an interesting twist.  Originally, I was doing extra work to
keep the waypoint relative to the ship (because that's what the problem 
said to do), but I later realized that it made no difference in the 
calculations.  I got stumped again on the rotational bit and had to 
look up the equation, but once I had it plugged in I had the answer.

Checking the sub-reddit was illuminating, as always.  Apparently everyone
but me knows that using complex numbers simplifies rotational equations.
It's a neat trick--although I wish I understood a bit better how it actually
works--and I used it in my cleaned up version.

## Day 13: Shuttle Search

Gah... it's so frustrating to know exactly what to do (for Part 1), code it 
up with no mistakes and submit the answer, only to wind up in 2800th place.

I got the logic right for Part 2, and was able to get the right answer for
the sample input pretty quickly, but I knew there was no way it was going
to be able to compute the answer for the real input.  I came up with a
couple of obvious speed-ups and let it run, but again it was clear that
it was never gonna get there.

The puzzle text contained the line `surely the actual earliest timestamp will be larger than 100000000000000!`,
which I took as a generous hint to us simpletons who just try to brute force
all the answers.  Given that, I set my starting index to that number and let'er 
run again.  In the meantime, I was opening Chrome tabs on Least Common Multiple 
and Greatest Common Denominator, etc.  I just knew there had to be some sort of 
esoteric key to this thing, but it was 1:30 AM and I had to throw in the towel
and admit defeat for the first time this AoC.  I left my code running overnight
in the hopes I might wake to an answer.

...

Sixteen hours later and my naive code is still chugging away, my laptop fan
is at max rpm, and I don't think I'm anywhere near a solution.

I checked the subreddit for a hint and everyone is mentioning the 
[Chinese Remainder Theorem](https://en.wikipedia.org/wiki/Chinese_remainder_theorem).
I'm not great at reading math notation, but I sort of got the gist of it and
saw how it would be applicable to our problem.  I found a Chinese Remainder
Theorem calculator on the internet, but it wasn't working with my puzzle
input.  After going over the wikipedia page several more times, interspersed
with staring out the window at the falling snow for long periods of time, I 
finally managed to figure out a way to translate my puzzle input into the 
inputs needed for the calculator and--voila!--I had an answer!  And it was 
correct!

Interestingly, my naive approach was not even halfway to the answer after
almost 20 hours.  I set about trying to come up with some code based on 
the math notation on the wikipedia page, but... I gave up.  A simple
google search pointed straight at a remarkably simple 
[Python implementation](https://rosettacode.org/wiki/Chinese_remainder_theorem#Python) 
that I was able to just drop right into my code.  

I had been going down the LCM/GCD/Multiplicative Inverse path, but there was 
no chance I was going to independently derive the Chinese Remainder Theorem.
There were a few people on reddit that seemed to have solved it without
using the Chinese Remainder Theorem, so I guess I'm still a bit annoyed that
I couldn't figure it out on my own.

(I love the comments on reddit that say things like, "I knew immediately that 
it was Chinese Remainder Theory" 🙄)

## Day 14: Docking Data

This was a really fun puzzle.  I liked that it involved bitmasking, but in a 
way that made it impossible (I think) to solve with actual bitmasking.  I was
able to code up solutions to both parts and run them correctly on the first
try.  I got stuck on Part 2 trying to get my combinations to work properly 
and ended up having to resort to using `set()` to remove the duplicates.  I 
feel like I shouldn't have had to do that, but it did the trick and I got 
pretty decent rankings (for me) on both parts.