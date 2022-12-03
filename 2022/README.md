# Advent of Code 2022

I was going to practice before this year's puzzles, but of course I didn't.

I was on vacation for the first x days, so I caught up on those first without
the time pressure, which was nice.

The first day I did live was Day y.

## Day 1: Calorie Counting

Straightforward Day 1, as usual.  I had to kinda get my mind back into thinking 
about parsing inputs again...  I used `max` for Part 1, but then tweaked things
a bit for Part 2 using a sorted array (that worked for both parts).   One minor
mistake in forgetting to use `reverse=True` for the sort, but I did my standard
test asserts before printing my answer, so I caught that before submitting.
Got both parts right on the first try, and hoping to keep that up for as long as 
possible this year!

## Day 2: Rock Paper Scissors

This is exactly the kind of puzzle I love and exactly the kind of puzzle the AOC
creator is so good at devising.  My idea to use lookup tables was the right choice,
I think, but I stupidly mixed up which data in the input was me vs my opponent. 
Then, even more stupidly, I forgot to re-do my lookup tables based on my original
mistake of swapping the input... Anyway, bit of frustration (and it's only the 
second day!), but I'm happy with the cleaned up code.  Already broke my correct
answer streak (how embarrassing!) but I did get Part 2 correct on the first try
once I finally got all my lookup tables properly sorted out.

## Day 3: Rucksack Reorganization

I decided to do this one as fast as I could, not bothering with breaking out methods
or picking descriptive variable names.  I realized pretty quickly that using Python
sets would make this one trivial, and it did.  I got both parts right on the first try
and eventually cleaned things up a bit.  Simple and fun, this one.

