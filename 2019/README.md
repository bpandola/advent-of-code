Day 1: The Tyranny of the Rocket Equation
-----------------------------------------

I did this one a day late.  It was pretty simple and I got the answers after
a few code iterations.  I also created my Part 1/Part 2 code structure with
`asserts` that has worked pretty well for me.  

Initially I imported `math` and used the `floor` method, but after reading the
subreddit, I learned something new: Python has an integer division operator,
`//`, that returns the floored value, which is a nice shortcut.

Day 2: 1202 Program Alarm
-------------------------

This was my first real attempt.  I was ready to go at 9pm, got my input and
got started.  There was a lot of reading on this one, but in the end it was
a very simple program and I manage to get one of my best ranks for both parts.
(It was also at this point that I realized just how good and crazy fast these
competitive programmers are.  I was so stoked to finish the first part in less
than 20 minutes, only to find out that 1300 people had gotten there before me...)

```
     --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
  2   00:18:20   1362      0   00:22:48    831      0
```

Day 3: Crossed Wires
--------------------

This one definitely upped the complexity and made me realize how quickly I
gravitate right toward the most brute-force implementation, which worked 
fine for Part 1 but failed miserably for Part 2.  I was basically just 
storing the line segments with their start/end points and then I had 
another function that checked if two lines intersected, but with the twist 
in Part 2 (counting the steps) I had to rewrite everything.  I really 
struggled, for hours, making a *lot* of dumb mistakes in the process, 
e.g. only adding the start/end points of a line instead of all points.  
I significantly cleaned this one up after the fact, using `max` and `min` 
instead of `for` loops, as well as using `sets` with the `&` operator, 
which I discovered reading through the top solutions in the subreddit.

```
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
  3   00:53:18   1885      0   03:42:54   4346      0
```

Day 4: Secure Container
-----------------------

This one was right up my alley, as I've actually had to write code at work
to come up with a password that adheres to various constraints.  I got right 
to it.  My excitement at getting the answer to Part 1 in just about 10 minutes 
was quickly diminished when I realized that was only good enough for Rank 1436.  
It also became abundantly clear to me, after watching Jonathan Paulson's livestream
of today's puzzle, that using an IDE with a debugger and clicking around with
a mouse the way I do will *never* be anywhere near as fast as someone using vim, 
no mouse, and debugging with print statements--even if our approach is exactly
the same.  I was happy to get a respectable sub-1000 rank for Part 2--and even
happier to have jumped ahead of hundreds of people who beat me to the answer
for Part 1.  (Looking at the solutions on the subreddit is such an eye-opener.
It's incredible how diverse they are!  Even how different the various Python
solutions are, some using regex, some using practically incoherent one-liners,
etc.)

```
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
  4   00:10:42   1436      0   00:16:17    801      0
```

Day 5: Sunny with a Chance of Asteroids
---------------------------------------

The return of `intcode` and the assumption that it will be a recurring theme in
this year's Advent of Code seems to be receiving mixed reviews on the subreddit.
Personally, I think it's pretty cool because it sort of mimics real-world coding
where you have to take some existing program and modify it to satisfy new 
requirements.  I made some dumb mistakes today (a recurring theme, it seems), but
I got pretty decent times/ranks all things considered.

```
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
  5   00:55:50   1634      0   01:23:12   1690      0
```

Day 6: Universal Orbit Map
--------------------------

This was the first one where we had to translate the puzzle input into a real
data structure.  I knew I needed a graph, but had to resort to the internet to
figure out how to model one in Python.   I struggled a bit with this puzzle, 
and even had to resort to doodling the graph out on paper and hand-counting 
the answer to some of the example inputs to make sure I fully understood the 
orbital relationships.  Part 2 marks the first time I had to kinda cheat: I
give myself credit for knowing that I needed a recursive path-finding 
algorithm, but I just couldn't quite figure out the implementation on my own.
The internet is such an amazing thing, though, as I was able to find the
exact function I needed, written in Python, in about two seconds.  (I was 
really down on myself for having to "cheat" until checking the subreddit and
discovering that tons of people simply imported a graph library, `networkx`, 
and had the solutions to both parts in barely 5 lines of code...)

```
     --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
  6   01:08:06   2993      0   01:36:56   2800      0
```

Day 7: Amplification Circuit
----------------------------

I rolled my own permutations code, only to find out later that it's in the
Python standard library (`itertools.permutations`).  That was fine, though, 
as I did set a goal for myself to rely very little on imports and googling
things.  I knew what I had to do for Part 1, and it didn't take me too long
to modify my existing `intcode` implementation as needed.  I had to re-read
Part 2 over and over before I finally got what it was saying.  I feel like
my game programming experience with update loops came in handy here, and 
while my solution wasn't quite as elegant as some of the others I saw later
that used `yield` or created a full-blown virtual machine, it was good 
enough to score my best finishes yet. 

```
     --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
  7   00:33:09   1212      0   01:14:19    712      0
```

Day 8: Space Image Format
-------------------------

This one was fun, particularly the visual aspect of Part 2, and I was able
to do it fairly quickly.  This was the first puzzle that I solved entirely
in the main method without creating any subroutines.  I did clean things up
a bit after solving it, especially after seeing some clever array slicing on
the subreddit and thinking it far more clever and Pythonic than my implementation.
I was *really* close to cracking the top 1000 for Part 1 and did crack it for
Part 2, so I was pretty happy about that.  (If I could just stop making stupid
mistakes, I might actually have a chance at a 3-digit rank one of these days.)

```
     --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
  8   00:14:20   1030      0   00:27:01    884      0
```

Day 9: Sensor Boost
-------------------

I'm loving the `intcode` puzzles and I've done a pretty good job cleaning up
my existing code each step of the way, but I got tripped up again today, which
was pretty frustrating.  It's kind of brilliant that Part 1 actually generated
output that told me exactly what I was doing wrong (`203`, relative parameter
mode for input operation) but actually fixing it took me about 90 minutes... 
Part 2 was supposed to be a freebie, but I had my virtual machine single-stepping 
in a `while` loop, which turned out to be horrendously slow. Changing it to
only halt when it needs input or has generated output not only makes more sense, 
but resulted in about a 1000x speed-up.  Apparently our `intcode` computer is 
now complete, so I'll clean this up one final time to make sure it's absolutely 
ready the next time it's needed.

```
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
  9   01:45:51   2103      0   01:47:30   2069      0
```


Day 10: Monitoring Station
--------------------------

My initial attempt was trying to do a full-blown raycaster, but despite my
conceptual knowledge of the topic, I was really struggling with the math and 
not getting very far on an actual implementation.  Of course, this ended up
being a perfect example of overcomplicating things as a result of having some
esoteric knowledge, and it eventually occurred to me that the puzzle creator
would not expect people to write a full-blown raycaster on Day 10, if ever.
I tried to simplify things with some basic `y = mx + b` slope stuff, but my
code started getting really ugly trying to handle negative/positive slopes
as well as the vertical/horizontal line edge cases.  Eventually I made the 
decision--far too late in retrospect--to call it a night and sleep on it.  
This was the first day I had to give up without an answer, which didn't feel
great.

The next day I checked the stats and could at least take solace in the fact
that this problem had by far the lowest completion rate to date for Part 1
and more than 2500 still stuck working on Part 2.  The leaderboard still
managed to devise a solution to both parts in under an hour, but it clearly
was tougher to solve even for them. 

Anyway, I did finally figure out a pretty clean and readable solution to
Part 1, but Part 2 (predictably) had me even more stumped.  I don't remember
where I got the hint--I only know that I didn't come up with it on my own--but
I saw a mention of the `atan2` function and once I looked it up, I immediately 
knew what I had to do.  I still struggled a bit trying to figure out how to 
shift the angles returned from the `atan2` function to properly simulate a 
laser sweeping around in a clockwise direction.  I had to bust out the ol'
pen and paper, where I drew a grid with nine points on it, (0, 0) in the center,
and all the straight and diagonal lines labeled `-1/4π`, `3/4π`, etc.  I 
was just staring at it, hoping for the answer to come to me, but in the end
I just wrote an `if` statement to handle each quadrant and adjust the angle
manually.  As to the actual formulas needed for each adjustment, I pretty much 
just guessed and checked until I got it right.

This was a tough one, but fun and very satisfying to finally complete!

```
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 10   12:11:32   7236      0   18:07:46   6833      0
```

Day 11: Space Police
--------------------

Another `intcode` problem, which I enjoy.  This was easily my best translation
of the text of the puzzle into an actual game plan.  And despite making my usual
amount of *really* stupid mistakes, I was able to debug them all quite quickly, 
getting the answer to Part 1 in just under 30 minutes.  Part 2 was a fun little
visualization, which I also managed to figure out faster than I could actually
code the implementation.  This was by far my best rank for getting both stars,
and I was quite pleased with myself.  This was also the first time where I
could really sense how much of a time penalty it is to be constantly switching
from keyboard to mouse and futzing around in an IDE when compared to those
on the leaderboard who use a simple editor and never take their hands off their
keyboard...

```
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 11   00:29:18    779      0   00:39:44    756      0
```

Day 12: The N-Body Problem
--------------------------

I think this is the first puzzle where I actually wrote a class for some OOP-y
goodness.  Part 1 was pretty straightforward, but once again I ended up with a
*really* stupid bug due to copy/pasting the x/y/z stuff, and it took way too 
long to figure out.  (The whole time I was thinking _I know this is going to 
be something dumb_.  And it was!)

Part 2 was painful.  Brute force didn't seem to work at all.  I ran the simulation
for 30 million steps, which took a long time, and was nowhere near an answer as
far as I could tell.  I just couldn't see any way to fast forward the simulation,
so I tried to optimize my loop, but it was just too slow and Python was not 
helping.  I started thinking maybe I needed to do some matrix multiplication, 
but I was just grasping at that point.  I read the entire Wikipedia article on 
the `N-Body Problem`, which was interesting, but also useless.  At some point I
got the idea to show the output for a few steps and look for a pattern.  Sure 
enough, on the sample input, an obvious pattern emerged and I was able to code
up a solution that worked perfectly on the sample data, but--of course!--didn't
work at all on my actual puzzle input.  In fact, I couldn't find any pattern
at all using my puzzle input, and so I was forced to throw in the towel a 
second time, deciding to sleep on it at 4am...

Nothing came to me in my sleep and I was no closer to anything even resembling
an idea when I looked at things with a fresh pair of eyes the next day.  I did
eventually check the subreddit.  I didn't look at anyone's code or solution
description, but I did see a clue wondering aloud if anything in the simulation
could be disentangled from the other bits in the simulation... and it immediately
hit me that each x/y/z simulation could be done in isolation.  I hate that I
couldn't come up with that on my own--it seems so obvious in hindsight--but the
code to calculate each axis independently of course ended up being extremely
simple (and fast).  Interestingly, despite taking two days to solve the problem, 
this was not my worst rank.  That honor goes to Day 10, which I also had to sleep
on.  Day 10's key was `greatest common denominator` and today's was `least common
multiple`.  Perhaps I should brush up on some basic math concepts...

```
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 12   00:51:59   1703      0   19:13:42   6348      0
```

Day 13: Care Package
--------------------

More `intcode`, more fun.  Getting better at turning my comprehension of the 
puzzle text into an actual working solution coupled with my now-solid `intcode` 
virtual machine resulted in my best finish ever for Part 1. 

I knew *exactly* what to do for Part 2 (I read later that some people had no
idea what `Breakout` is/was), but for the life of me I could not get the paddle
to hit the ball more than once.  On the first hit, the ball would go flying off
to the left, the paddle could never catch up, and it would be Game Over.  I was
so confounded after trying everything I could thing of to no avail, that I just
took the score I got from breaking the first block and multiplied it by the 
remaining blocks, but of course that wasn't correct.  I was totally out of ideas
when I decided to check the subreddit, only to find that nobody else seemed to
be having any issues.  

Then I saw this:

> All my code does is move the paddle horizontally to match the ball's position.  
I was nervous that I might need to anticipate the ball's movement and have  
the paddle one step ahead, but thankfully that wasn't necessary.  

~ #2 on the Leaderboard

Not only was it not necessary, it didn't f*cking work!  My "smart" AI kept causing
the ball to fly two positions away on the first collision and my paddle had no
hope of ever catching up to it.  As far I can tell from reading the subreddit after
the fact, no one else seems to have stumbled upon what tripped me up, which makes
this all the more frustrating.  In any case, I'm very happy with the simplicity of
my cleaned up code and the rudimentary visualization I added for Part 2.

```
     --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 13   00:08:03    703      0   01:41:48   1362      0
```

Day 14: Space Stoichiometry
---------------------------

I spent quite a bit of time parsing the puzzle input for this one into a 
suitable data structure.  Originally I thought it would be a good use for
a `namedtuple` instead of a full-blown class, but in the end I just used a
simple dictionary/array structure.  I understood conceptually what I needed
to do for Part 1, but I totally overcomplicated things by assuming
(incorrectly as it turned out) that there might be multiple recipes for the 
same chemical.  I knew I needed a recursive function to calculate the ore as
I "walked back up the tree", but again I struggled with the implementation 
and wound up with a hideous nested-while loop in addition to recursion.
Further frustration occurred when my solution worked for sample inputs 1, 2,
and 3; but failed for the puzzle input.  I kept tweaking things (for hours)
until I finally got the answer to Part 1 at about ~7am.

Because I'm insane, instead of going to bed I decided to work on Part 2, 
which of course was even more difficult and frustrating.  Although my code
for Part 1 was correct, it was far too slow for the twist (and enormous 
number) in Part 2.  I made some optimizations, but it still ran for 20 minutes
before it produced an answer.  Unbelievably, that answer was correct!

I cleaned this one up big time after the fact, based on some of the 
optimizations discussed in the subreddit.  This was a really cool puzzle
overall--I just wish I'd been clever enough to nail down the algorithm 
in a reasonable amount of time.

```
     --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 14   09:51:11   3080      0   14:46:29   3545      0
```

Day 15: Oxygen System
---------------------

I enjoy and seem to do better with the `intcode` puzzles, and today was no 
exception.  It was a maze, so I got a basic path-finding algorithm working 
using the "right hand rule" in about an hour.  Once I visualized the maze, I
tried to just count the steps by hand for Part 1, but of course I was wrong.
After a bit of pondering, I realized that in order to map the entire maze
I would have to utilize two path-finding routes (a right-hand route followed 
by a left-hand route).  That was a fairly naive, suboptimal method, but it 
worked!

I got Part 2 pretty quickly, complete with a cool visualization, and ended
up with respectable ranks for both parts, despite starting late.  I'm very
pleased with how readable my code was once cleaned up.  This was a fun
puzzle and a good day.

```
     --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 15   03:54:56   1424      0   04:48:10   1379      0
```

