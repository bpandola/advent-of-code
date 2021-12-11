# Advent of Code 2021

I was going to practice, but didn't.

I was on vacation for the first 7 days, so I caught up on those first without
the time pressure, which was nice.


## Day 1: Sonar Sweep

It's Day 1.  Simple list of numbers.  Got Part 1 on the first try.  On Part 2, 
a silly off-by-one error on the array indexing caused my test case to fail.
Fixed that and got the right answer for Part 2.  Whole thing took me about 5 minutes.

I watched J. Paulson's video after I got my answers, and it's amazing how much
faster he is at even these super easy early puzzles.

## Day 2: Dive!

I spent too much time trying to figure out the best way to multiply values in
a tuple before just giving up and doing the multiplication in my calculation
method.  My code worked on the first try for both parts, which is always satisfying,
even with the really simple puzzles.

And again, I watched J. Paulson's video after I got my answers, and it literally took 
him less than two minutes to complete the whole thing.  Unbelievable.

## Day 3: Binary Diagnostic

I loved this puzzle, especially the second part.  It's quintessential AOC, where 
you have to tease apart the criteria, and then you get a fun twist on things in
Part 2.  Anyway, Part 1 was straightforward, save for the fact that I originally
was trying to append to an array by writing `array[index] = value`.  Oops.  Once
I corrected that and looked up how to convert a string of 1s and 0s to a number in
Python (`int(value, 2)`) I had the answer.

Part 2 was a fun additional complication added on to the original puzzle.  I 
actually wrote out my algorithm in a notebook by hand, which I think I might 
do going forward if I'm not going for speed.  I usually just start typing and
then continually running the code at each stage to verify my assumptions, but
it was a good feeling to do it all on paper and have the code work on the first
try.  My streak of no wrong answers continues!

I love the binary stuff and thinking about bits--I used an XOR too--even though
you didn't really have to understand bits at a low level to get the answer.

## Day 4: Giant Squid

This was a good one.  I spent a bit of time thinking about how to represent
the bingo board in code.  I knew I needed a class with various methods for 
`.score()`, `.has_a_bingo()`, etc.  My original thoughts had me storing
multiple hash maps of grid-positions-to-numbers and numbers-to-grid-positions,
but then I realized I could just take the raw grid data and generate all the
winning combinations and use set operations with the currently drawn numbers
to easily determine if a board had a bingo, and that ended up working quite
well.

It took me a bit of time to get everything coded up--I doubt I would
have been a contender--but everything worked on the first try, which was
very satisfying.  Nice little twist on Part 2, but my code was architected 
in such a way that I had the answer in just a couple more minutes time.

Still no wrong answers!

## Day 5: Hydrothermal Venture

Well, I did fine on Part 1 and then got totally tripped up on Part 2 
trying to plot a diagonal line.  So embarrassing.  My line drawing code
was terribly off the mark, and it took way too long to figure out.
Unfortunately, once I did figure it out, I got the right answer for
the sample input but got my first wrong answer for my puzzle input.
Thankfully it took me only a couple of minutes to see that my diagonal
line drawing code was off-by-one and not rendering the final point.

I'm starting to remember the aggravation and self-loathing I felt last
year when making dumb mistakes or struggling with an implementation. 

And it's only on Day 5...

## Day 6: Lanternfish

Oh, I love Advent of Code.  This was the classic Part 1 is an easy simulation
for `x` number of ticks and Part 2 is just simulate it for a few more ticks
and watch your naive implementation bring your CPU to its knees and never 
complete...

I actually had a hunch that it would go like this and thought about doing 
something a bit more clever for Part 1 in anticipation of Part 2, but I
ended up just going the naive, brute force way for Part 1.

Part 2 was as expected, and I immediately came up with the idea to only simulate
each fish with a different age and just keep track of their counts.  This took
only a few minutes to implement, and it was blazingly fast for both parts.

I loved this puzzle, and I was very pleased with my solution.