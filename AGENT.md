# AGENT.md

Entry for make.fun competition `u-kiencx-sorry-i-heard-that-wrong-1858c729`
("Sorry, I Heard That Wrong"): the funniest one-line apology a smart speaker
gives after mishearing its owner, max 140 characters.

The line: "Sorry, you said 'call Mom,' I heard 'call a mob.' They arrive at
six. I have already apologised to them." (104 characters.)

How it was built: read the kit RULES and requirements first, drafted three
candidate lines out loud and weighed them against the judge's criteria
(on-subject apology, humour with the punch at the end, freshness, device
voice, tightness). The winner was chosen because the mishearing is concrete
("Mom" -> "mob"), the consequence is absurd, and the punch lands last: the
speaker apologises to the mob it just summoned, which is exactly the device's
voice. The obvious misheard-song-title and Alexa-orders-something jokes were
rejected as un-fresh. `main.py` (stdlib only) writes the line to
`$MAKEFUN_OUTPUT_DIR/entry.txt`, one line, no trailing newline, and asserts
the 1-140 character gate before writing.
