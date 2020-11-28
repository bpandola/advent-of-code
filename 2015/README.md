


Day 13: Knights of the Dinner Table
-----------------------------------

I started working on this one, thinking it was pretty easy, but also fully aware
that there was combination/permutation here that could take up some time.  Per
usual, I decided to brute-force it for Part 1.  I got the sample data working
pretty quickly, although admittedly I went to lift the combination generator 
from a previous AoC day and when I found it on Day 9 I realized I could just
use most of the rest of that code too (with some minor modifications for 
a round table where the path returns back to where it started).  Anyway, it
ran a bit longer than I would have liked (so I'm probably screwed for Part 2)
but it worked.  (I do wonder where I would have ended up if I had not re-used
my previous code.)

So... for Part 2 we have to add ourself to the seating arrangement and I'm
guessing that with these exponential things that adding one more person to 
the table is likely to make this thing unworkable in any reasonable time
frame.  Let's see...

Aaaaand that's a nope.

Because the table is round, there's actually a *lot* of duplication in the
seating arrangements (e.g.  1->2->3 == 2->3->1 == 3->1->2) so I think I need
to figure out a way to pare the combinations down before attempting to calculate
the optimal seating arrangement.

Bleh.  Whatever.  Long story short, I went down this ridiculous rabbit hole of
trying to "de-dupe" the permutations and I think it just made things take longer.
I finally caved and went to Reddit, only to find everyone saying that there was 
no trick, that they just brute-forced it.  Furthermore, everyone seemed to realize
that this puzzle was "isomorphic" to Day 9 and also re-used their previous code.
Longer story even shorter, I was calculating all the possible seating arrangements 
and then looping through them at the end to find the max and all I had to do was 
just check if my current seating arrangement was greater than the max--if so, save 
the value; if not, disregard.  Once I did that, both Part 1 and Part 2 finished 
in just a few seconds.

I had forgotten how frustrated I get with these things.  I'm always *right*
there, but just can't get it right.