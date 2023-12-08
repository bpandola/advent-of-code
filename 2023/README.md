# Advent of Code 2023

## Day 1: Trebuchet?!

Simple character-by-character analysis of lines of input for Day 1, Part 1.
Using my incredible knowledge of Python, I put both `string.isdigit()` and 
negative slicing (`array[-1]`) to work.  Checked my code against the sample
input and got the right answer on the first try for my puzzle input!

I say this a lot, but I just love the twists this guy puts on the Part 2s.
This time we had to track single characters that were digits as well as
any words (e.g. `one`) that indicated a digit.  My initial thought was to 
analyze the string in two passes.  The first pass would get the index of
any words that indicated digits, the second pass would get all the single
characters that were digits, and then I'd have to find some way to combine
the indices from the first and second passes into the correct order, so I 
could grab the first and last digits.  I busied myself trying to figure out 
a custom array-like data structure that would allow me to insert indices 
randomly but wind up with the correct order...

As usual, I was totally overcomplicating things.  I figured there was 
probably a more elegant solution that could just do everything in one
pass (spoiler alert: there was!), but I decided to do two separate loops:
I got the first digit starting from the left side, then I got the last 
digit by getting the first digit walking the string in reverse.  I had
to correct an off-by-one error and a string slicing issue after my code
failed with the sample input, but once that was fixed I got the right
answer for my puzzle input on the first try.

After cleaning up my code, I checked the subreddit.  Lots of people
seemed to have had trouble with Part 2 because they were trying to regex 
or `string.replace` and got tripped up by some of the inputs that had
overlapping words, like `eightwo3` and `xtwone3four`.  I guess I just
got lucky that my naive, ham-fisted approach avoided this pitfall. 🙃

I humbled myself, as usual, by watching Jonathan Paulson's solution on
YouTube.  He just used `.startswith()`!  So simple, so elegant, avoids
the overlapping words issue, and can get the answer in one pass.  Why
didn't I think of that?!

I also saw that George Hotz tackled the Day 1 problem on one of his
tinygrad livestreams.  I was amused to see him make some silly mistakes,
though he is way smarter than I am in general.  Also, he was throwing
the problem at ChatGPT, and it was pretty damn impressive how close it
got, even if the code it wrote didn't actually work without human tweaks.
In some cases, George and the LLM were naming their variables exactly the
same as I had named mine, which was cool to see.

Fun first day!
