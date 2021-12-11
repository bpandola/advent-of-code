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
