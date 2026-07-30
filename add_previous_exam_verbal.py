"""
add_previous_exam_verbal.py — Adds real GL Assessment 11+ Verbal Reasoning
Familiarisation Paper questions (VR 1, 2 & 3) into the "Previous Exam
Questions" subject, "Verbal Reasoning" module.

Source: GL Assessment Verbal Reasoning Familiarisation Papers 1, 2 & 3
(Copyright (c) GL Assessment, 2017/2019), used here for personal family
study only. Answers taken from the official Parent's Guide answer key.

Question types are grouped into 17 topics (one per VR skill/format), pooling
matching question types across all three papers. Some original question
types ask the child to mark TWO words (one from each of two small word
groups, or two odd-ones-out from a list of five). Since this app's quiz UI
is single-tap multiple choice, those are converted into a single combined
answer (e.g. "hit, miss") with a few other real combinations from the same
word groups as plausible wrong options — no wording is invented, only
recombined from the words GL Assessment already provided.

Run: python3 add_previous_exam_verbal.py
"""
from datetime import date
import itertools

SUBJECT = "Previous Exam Questions"
SECTION = "Verbal Reasoning"
SOURCE = "GL Assessment 11+ Verbal Reasoning Familiarisation Paper"


def dual_options(group1, group2, correct, max_opts=5):
    """Build MC options for a 'pick one word from each group' question.
    group1/group2: lists of candidate words. correct: (word_from_group1, word_from_group2).
    Returns (options_list_len5, correct_answer_str)."""
    combos = ["{}, {}".format(a, b) for a in group1 for b in group2]
    correct_str = "{}, {}".format(correct[0], correct[1])
    assert correct_str in combos, "MISSING CORRECT: {} not in {}".format(correct_str, combos)
    others = [c for c in combos if c != correct_str]
    distractors = others[:max_opts - 1]
    opts = [correct_str] + distractors
    while len(opts) < 5:
        opts.append(None)
    return opts[:5], correct_str


def oddpair_options(words5, correct_pair, max_opts=5):
    """Build MC options for a 'find the two words that don't belong' question.
    words5: list of 5 words in original order. correct_pair: (word, word) in original order."""
    combos = list(itertools.combinations(words5, 2))
    combo_strs = ["{}, {}".format(a, b) for a, b in combos]
    correct_str = "{}, {}".format(correct_pair[0], correct_pair[1])
    assert correct_str in combo_strs, "MISSING CORRECT: {} not in {}".format(correct_str, combo_strs)
    others = [c for c in combo_strs if c != correct_str]
    distractors = others[:max_opts - 1]
    opts = [correct_str] + distractors
    while len(opts) < 5:
        opts.append(None)
    return opts[:5], correct_str


def spread_difficulty(n, i):
    """Assign easy/medium/hard across a list by position."""
    if i < n / 3.0:
        return 1
    if i < 2 * n / 3.0:
        return 2
    return 3


# ═══════════════════════════════════════════════════════════════
# TOPIC 1 — Move a Letter Between Words
# ═══════════════════════════════════════════════════════════════
MOVE_LETTER_LESSON = """
<div class="lesson-block">
<h3>🔤 Move a Letter Between Words</h3>
<p>One letter can be moved from the first word to the second word to make two new,
real words. The letters must not otherwise be rearranged.</p>
<p><strong>Example:</strong> pound / or &rarr; move the <strong>u</strong>: pound becomes
<strong>pond</strong>, or becomes <strong>our</strong>.</p>
</div>
<p style="margin-top:12px;color:rgba(255,255,255,0.4);font-size:12px;">Source: GL Assessment 11+ Verbal Reasoning Familiarisation Papers 1 & 3</p>
"""
# (word1, word2, opt_a..opt_e, correct)
_MOVE_LETTER_RAW = [
    ("metal", "though", "m", "e", "t", "a", "l", "t"),
    ("liner", "bother", "l", "i", "n", "e", "r", "r"),
    ("biased", "pant", "b", "i", "a", "s", "d", "i"),
    ("chomp", "tea", "c", "h", "o", "m", "p", "m"),
    ("player", "fight", "p", "l", "a", "y", "r", "l"),
    ("brain", "tale", "b", "r", "a", "i", "n", "b"),
    ("flower", "lit", "f", "l", "o", "w", "r", "f"),
    ("downs", "wins", "d", "o", "w", "n", "s", "d"),
    ("bears", "what", "b", "e", "a", "r", "s", "e"),
    ("flake", "band", "f", "l", "a", "k", "e", "l"),
    ("leaps", "now", "l", "e", "a", "p", "s", "s"),
    ("blind", "party", "b", "l", "i", "n", "d", "l"),
    ("train", "sow", "t", "r", "a", "i", "n", "t"),
    ("fable", "eel", "f", "a", "b", "l", "e", "f"),
]
MOVE_LETTER_QUESTIONS = []
for i, (w1, w2, a, b, c, d, e, ans) in enumerate(_MOVE_LETTER_RAW):
    MOVE_LETTER_QUESTIONS.append((
        "One letter moves from '{}' to '{}' to make two new real words (letters otherwise stay in order). Which letter moves?".format(w1, w2),
        "mc", a, b, c, d, e, ans,
        "Removing '{0}' from '{1}' and adding it to '{2}' makes two real words.".format(ans, w1, w2),
        spread_difficulty(len(_MOVE_LETTER_RAW), i)
    ))

# ═══════════════════════════════════════════════════════════════
# TOPIC 2 — Same Letter, Two Gaps
# ═══════════════════════════════════════════════════════════════
BRACKETS_LESSON = """
<div class="lesson-block">
<h3>🔤 Same Letter, Two Gaps</h3>
<p>The same letter fits into both gaps: it completes the word in front of the gap
AND begins the word after the gap — across two separate word-pairs.</p>
<p><strong>Example:</strong> mea[?]able, si[?]op &rarr; the letter <strong>t</strong> makes
meat, table, sit, top.</p>
</div>
<p style="margin-top:12px;color:rgba(255,255,255,0.4);font-size:12px;">Source: GL Assessment 11+ Verbal Reasoning Familiarisation Papers 1 & 2</p>
"""
_BRACKETS_RAW = [
    ("wor[?]en", "fin[?]ice", "m", "t", "d", "s", "n", "d"),
    ("loo[?]eak", "wee[?]ull", "b", "k", "m", "p", "s", "p"),
    ("roo[?]ick", "oa[?]ind", "w", "r", "m", "f", "k", "k"),
    ("car[?]ip", "fac[?]rust", "t", "d", "p", "c", "e", "t"),
    ("chee[?]ang", "spea[?]ide", "s", "r", "b", "p", "k", "r"),
    ("pe[?]et", "cla[?]umber", "w", "g", "p", "l", "n", "n"),
    ("her[?]ut", "pol[?]asis", "b", "o", "e", "l", "d", "o"),
    ("fle[?]ish", "slo[?]aste", "p", "w", "d", "t", "f", "w"),
    ("quot[?]im", "te[?]cre", "h", "e", "a", "n", "d", "a"),
    ("inc[?]eat", "mes[?]ide", "w", "s", "t", "h", "b", "h"),
    ("sou[?]unch", "bel[?]ight", "b", "l", "p", "m", "t", "l"),
    ("scar[?]ound", "sel[?]at", "r", "b", "m", "s", "f", "f"),
    ("bar[?]een", "bea[?]eep", "d", "t", "p", "k", "m", "k"),
    ("ma[?]ear", "ha[?]olk", "y", "n", "t", "f", "d", "y"),
]
BRACKETS_QUESTIONS = []
for i, (p1, p2, a, b, c, d, e, ans) in enumerate(_BRACKETS_RAW):
    BRACKETS_QUESTIONS.append((
        "The same letter fills both gaps: {}    {}. Which letter?".format(p1, p2),
        "mc", a, b, c, d, e, ans,
        "The letter '{}' completes both word pairs correctly.".format(ans),
        spread_difficulty(len(_BRACKETS_RAW), i)
    ))

# ═══════════════════════════════════════════════════════════════
# TOPIC 3 — Hidden Word Patterns
# ═══════════════════════════════════════════════════════════════
PATTERN_LESSON = """
<div class="lesson-block">
<h3>🧩 Hidden Word Patterns</h3>
<p>The three words in the first bracketed group combine (using parts of their
letters) to make the middle word shown in [square brackets]. Work out the rule,
then apply it to the second group to find the missing word.</p>
<p><strong>Example:</strong> (man [mat] tip) &rarr; (bug [<strong>bud</strong>] dew)</p>
</div>
<p style="margin-top:12px;color:rgba(255,255,255,0.4);font-size:12px;">Source: GL Assessment 11+ Verbal Reasoning Familiarisation Papers 1, 2 & 3</p>
"""
_PATTERN_RAW = [
    ("(staff [not] gnome)   (epoch [?] image)", "gem", "map", "hip", "ham", "mop", "map"),
    ("(puzzle [zip] boiler)   (nettle [?] brands)", "tan", "tee", "ten", "tar", "tab", "tan"),
    ("(kiosk [sky] syrup)   (agile [?] upset)", "use", "lip", "pea", "gap", "lap", "lap"),
    ("(pedal [idea] saint)   (swamp [?] issue)", "swap", "saps", "sums", "saws", "swim", "saws"),
    ("(relax [axe] exists)   (jewel [?] byway)", "eel", "ale", "eye", "awe", "ewe", "eye"),
    ("(occupy [cape] repeat)   (snouts [?] chisel)", "once", "hens", "nets", "oils", "nest", "nets"),
    ("(thigh [hat] atlas)   (dwarf [?] moths)", "for", "who", "was", "oar", "wad", "who"),
    ("(search [near] lotion)   (camera [?] strong)", "neat", "rate", "game", "near", "gate", "game"),
    ("(pin [pit] lit)   (run [?] may)", "ray", "rum", "nay", "ram", "pay", "ray"),
    ("(grand [art] dealt)   (barge [?] clear)", "bar", "bag", "rag", "car", "ear", "ear"),
    ("(latch [heat] shake)   (index [?] above)", "bind", "bend", "bean", "bond", "bead", "bend"),
    ("(taught [tent] design)   (reacts [?] stigma)", "stem", "stir", "ream", "star", "rear", "star"),
    ("(picture [tire] scratch)   (deliver [?] changed)", "gain", "hard", "gear", "hear", "hand", "gear"),
    ("(horizon [zoom] diamond)   (partner [?] leather)", "neat", "pear", "hear", "heat", "near", "neat"),
    ("(absolute beat)   (umbrella maul)   (anecdote [?])", "cane", "note", "need", "neat", "date", "neat"),
    ("(passive save)   (footpad toad)   (housing [?])", "gush", "song", "gosh", "shin", "sing", "song"),
    ("(heather tear)   (forward word)   (portion [?])", "riot", "root", "torn", "trip", "poor", "torn"),
    ("(proceed core)   (medical idea)   (classes [?])", "lace", "sale", "less", "seal", "case", "sale"),
    ("(portrait trap)   (disbands sand)   (animated [?])", "date", "time", "dame", "mate", "data", "data"),
    ("(deepens sped)   (recount tour)   (threads [?])", "shed", "rate", "seat", "dare", "sear", "seat"),
    ("(avenged need)   (stapler pear)   (clatter [?])", "tear", "real", "late", "tart", "rate", "tear"),
]
PATTERN_QUESTIONS = []
for i, (stem, a, b, c, d, e, ans) in enumerate(_PATTERN_RAW):
    PATTERN_QUESTIONS.append((
        "Find the missing word: {}".format(stem),
        "mc", a, b, c, d, e, ans,
        "'{}' completes the second group using the same rule as the first group.".format(ans),
        spread_difficulty(len(_PATTERN_RAW), i)
    ))

# ═══════════════════════════════════════════════════════════════
# TOPIC 4 — Odd One Out (Find Two)
# ═══════════════════════════════════════════════════════════════
ODDONE_LESSON = """
<div class="lesson-block">
<h3>🔎 Odd One Out — Find Two</h3>
<p>Three of the five words are related in some way. Find the <strong>two</strong> words
that do <strong>not</strong> belong with the other three.</p>
<p><strong>Example:</strong> black, mouse, red, green, hut &rarr; 'black', 'red' and 'green'
are colours, so the odd two out are <strong>mouse</strong> and <strong>hut</strong>.</p>
</div>
<p style="margin-top:12px;color:rgba(255,255,255,0.4);font-size:12px;">Source: GL Assessment 11+ Verbal Reasoning Familiarisation Papers 2 & 3</p>
"""
_ODDONE_RAW = [
    (["pile", "heap", "high", "heavy", "stack"], ("high", "heavy")),
    (["slim", "lean", "tilt", "hill", "thin"], ("tilt", "hill")),
    (["possess", "get", "buy", "own", "have"], ("get", "buy")),
    (["pollute", "remove", "take", "destroy", "seize"], ("pollute", "destroy")),
    (["grow", "time", "develop", "exist", "mature"], ("time", "exist")),
    (["clear", "conclude", "finish", "terminate", "prevent"], ("clear", "prevent")),
    (["distribute", "spread", "arrange", "disperse", "organise"], ("arrange", "organise")),
    (["acquire", "sustain", "maintain", "gain", "obtain"], ("sustain", "maintain")),
    (["chair", "insect", "cat", "table", "boy"], ("chair", "table")),
    (["joke", "tease", "entertain", "jest", "please"], ("entertain", "please")),
    (["below", "beside", "under", "above", "beneath"], ("beside", "above")),
    (["lady", "male", "man", "woman", "boy"], ("lady", "woman")),
    (["decide", "reveal", "choose", "agree", "ponder"], ("reveal", "ponder")),
    (["song", "tune", "choir", "melody", "singer"], ("choir", "singer")),
    (["ecstatic", "elated", "jubilant", "scared", "concerned"], ("scared", "concerned")),
]
ODDONE_QUESTIONS = []
for i, (words, correct) in enumerate(_ODDONE_RAW):
    opts, correct_str = oddpair_options(words, correct)
    ODDONE_QUESTIONS.append((
        "Three of these five words are related — find the TWO that do not belong: {}".format(", ".join(words)),
        "mc", opts[0], opts[1], opts[2], opts[3], opts[4], correct_str,
        "'{}' and the other three words share a meaning/category; the pair '{}' does not fit.".format(
            ", ".join(w for w in words if w not in correct), correct_str),
        spread_difficulty(len(_ODDONE_RAW), i)
    ))

# ═══════════════════════════════════════════════════════════════
# TOPIC 5 — Number Sequences
# ═══════════════════════════════════════════════════════════════
NUMSEQ_LESSON = """
<div class="lesson-block">
<h3>🔢 Number Sequences</h3>
<p>Find the number that continues the series in the most sensible way. Some series
add/subtract/multiply/divide by a fixed amount each time; others interleave two
separate patterns (1st, 3rd, 5th... and 2nd, 4th, 6th...).</p>
</div>
<p style="margin-top:12px;color:rgba(255,255,255,0.4);font-size:12px;">Source: GL Assessment 11+ Verbal Reasoning Familiarisation Papers 1 & 3</p>
"""
_NUMSEQ_RAW = [
    ("27 26 28 25 29 24 30 [?]", "33", "29", "25", "23", "31", "23"),
    ("4 8 11 15 18 [?]", "21", "20", "25", "22", "28", "22"),
    ("28 32 25 27 22 22 19 17 16 [?]", "15", "13", "12", "14", "11", "12"),
    ("20 23 27 32 38 [?]", "45", "48", "46", "39", "51", "45"),
    ("57 56 54 52 50 47 45 41 39 [?]", "32", "31", "35", "33", "34", "34"),
    ("88 92 90 95 92 98 94 101 [?]", "100", "95", "93", "96", "99", "96"),
    ("2 5 14 41 [?]", "122", "84", "62", "140", "112", "122"),
    ("289 315 341 367 393 [?]", "403", "404", "417", "419", "445", "419"),
    ("18 36 72 144 288 [?]", "432", "504", "528", "574", "576", "576"),
    ("92 79 66 53 40 [?]", "27", "31", "33", "34", "37", "27"),
    ("44 38 32 26 20 [?]", "10", "12", "14", "16", "18", "14"),
    ("324 108 36 12 [?]", "2", "3", "4", "6", "9", "4"),
    ("75 67 59 51 [?]", "40", "41", "42", "43", "44", "43"),
    ("9 27 81 243 729 [?]", "1458", "2187", "2916", "3645", "4374", "2187"),
]
NUMSEQ_QUESTIONS = []
for i, (seq, a, b, c, d, e, ans) in enumerate(_NUMSEQ_RAW):
    NUMSEQ_QUESTIONS.append((
        "Find the next number in the series: {}".format(seq),
        "mc", a, b, c, d, e, ans,
        "Work out the pattern between consecutive numbers (or alternating positions) to find {}.".format(ans),
        spread_difficulty(len(_NUMSEQ_RAW), i)
    ))

# ═══════════════════════════════════════════════════════════════
# TOPIC 6 — Logic Puzzles
# ═══════════════════════════════════════════════════════════════
LOGIC_LESSON = """
<div class="lesson-block">
<h3>🧠 Logic Puzzles</h3>
<p>Read the given information carefully, then work out which statement must (or
cannot) be true.</p>
</div>
<p style="margin-top:12px;color:rgba(255,255,255,0.4);font-size:12px;">Source: GL Assessment 11+ Verbal Reasoning Familiarisation Papers 1, 2 & 3</p>
"""
LOGIC_QUESTIONS = [
    ("At the shops Darren bought 8 oranges. Laura bought 3 oranges fewer than Chris. Rosario bought 3 oranges fewer than Darren and 1 fewer than Chris. How many oranges did Laura buy?",
     "mc", "1", "9", "3", "5", "2", "3", "Rosario = Darren - 3 = 8 - 3 = 5. Since Rosario is also 1 fewer than Chris, Chris = 5 + 1 = 6. Laura = Chris - 3 = 6 - 3 = 3.", 2),
    ("A cinema is open every night from 7 pm. The latest time a film begins is 11 pm. Films start at 7.15pm, 8.15pm and 9.15pm on Tuesdays/Thursdays. On Mondays/Wednesdays films start on the hour, every hour. At the weekend films start every half hour from 7pm. Which must be true? A) No films start at 9.30pm B) On Tuesday a film starts at 9pm C) Films start at 9.15pm three days each week D) A film starts at 9pm on Monday, Wednesday and at the weekend E) All films finish before 11pm",
     "mc", "No films start at 9.30 pm.", "On Tuesday, a film starts at 9 pm.", "Films start at 9.15 pm three days each week.", "A film starts at 9 pm on Monday, Wednesday and at the weekend.", "All films finish before 11 pm.", "A film starts at 9 pm on Monday, Wednesday and at the weekend.", "Mon/Wed start on the hour (includes 9pm) and weekends start every half hour from 7pm (includes 9pm).", 3),
    ("In a block of flats, Natalie lives two floors below Michelle and one floor above Christopher. Yousuf lives one floor above Natalie. Matthew lives one floor below Michelle. Who lives on the same floor?",
     "mc", "Yousuf and Natalie.", "Yousuf and Matthew.", "Matthew and Michelle.", "Christopher and Matthew.", "Natalie and Michelle.", "Yousuf and Matthew.", "Yousuf is one floor above Natalie, and Natalie is one floor below Michelle's floor minus one more — working through the floors, Yousuf and Matthew share a floor.", 2),
    ("A cat has 5 kittens. 2 are brown and 2 are grey. All black and grey kittens have green eyes. White kittens have blue eyes. Which must be true? A) None of the kittens are black B) None have blue eyes C) The grey kittens have blue eyes D) All kittens are male E) At least 2 of the kittens have green eyes",
     "mc", "None of the kittens are black.", "None of the kittens have blue eyes.", "The grey kittens have blue eyes.", "All of the kittens are male.", "At least 2 of the kittens have green eyes.", "At least 2 of the kittens have green eyes.", "The 2 grey kittens must have green eyes (all grey kittens do), so at least 2 kittens have green eyes.", 2),
    ("Jessica, Peter, Mohammed, Tanya and Becky are growing tomato plants, each starting with 3 seeds. Jessica has one tall plant among her others (so more than 1). Mohammed's three plants are all healthy (so all 3 seeds grew). Peter and Becky did not grow plants from all of their seeds (so each has fewer than 3). Tanya only planted one seed, and had the fewest plants of all. How many tomato plants did the children grow between them?",
     "mc", "8", "9", "11", "13", "15", "11", "Mohammed = 3, Tanya = 1 (fewest). Jessica has more than one plant, and Peter/Becky each have fewer than 3 but more than Tanya's 1 — a consistent split is Jessica=3, Peter=2, Becky=2, giving 3+2+3+1+2 = 11 in total.", 3),
    ("Susie, Molly, Hannah and Freya are sisters. Susie has school lunches Mon/Wed/Fri, packed Tue/Thu. Molly has school lunches every day except Monday. Hannah has packed lunches Mon/Thu/Fri. Freya has school lunches when Hannah does, plus Fridays. Which sentence CANNOT be true?",
     "mc", "Three sisters have school lunches on Fridays.", "There is only one day all sisters have school lunches.", "Two sisters have packed lunches on Mondays.", "Molly has the most school lunches per week.", "Only Hannah has a packed lunch on Fridays.", "Two sisters have packed lunches on Mondays.", "On Monday, Hannah has a packed lunch and Freya has a school lunch (since Freya has school lunches when Hannah doesn't have one, plus Fridays) — only one sister (Hannah) has a packed lunch on Monday, not two.", 3),
]

# ═══════════════════════════════════════════════════════════════
# TOPIC 7 — Opposites (Antonyms)
# ═══════════════════════════════════════════════════════════════
OPPOSITES_LESSON = """
<div class="lesson-block">
<h3>↔️ Opposites (Antonyms)</h3>
<p>Find two words, one from each group, that are most opposite in meaning.</p>
<p><strong>Example:</strong> (morning early wake) (late shop dark) &rarr;
<strong>early</strong> and <strong>late</strong>.</p>
</div>
<p style="margin-top:12px;color:rgba(255,255,255,0.4);font-size:12px;">Source: GL Assessment 11+ Verbal Reasoning Familiarisation Papers 1 & 3</p>
"""
_OPPOSITES_RAW = [
    (["break", "ignore", "hit"], ["poke", "miss", "aim"], ("hit", "miss")),
    (["cheap", "price", "cost"], ["amount", "dear", "expense"], ("cheap", "dear")),
    (["complex", "superior", "modern"], ["old", "new", "fresh"], ("modern", "old")),
    (["lock", "close", "away"], ["key", "distant", "shut"], ("close", "distant")),
    (["hobby", "usual", "rarely"], ["habit", "often", "seldom"], ("rarely", "often")),
    (["heavy", "glow", "stiff"], ["shine", "hard", "flexible"], ("stiff", "flexible")),
    (["approximate", "true", "close"], ["broad", "precise", "rough"], ("approximate", "precise")),
    (["transparent", "clear", "hollow"], ["empty", "vague", "glass"], ("clear", "vague")),
    (["approach", "hinder", "consider"], ["disregard", "think", "recommend"], ("consider", "disregard")),
    (["friend", "relative", "pet"], ["family", "child", "enemy"], ("friend", "enemy")),
    (["hard", "agile", "flexible"], ["stiff", "quick", "delicate"], ("flexible", "stiff")),
    (["aid", "sink", "reduce"], ["float", "support", "drop"], ("sink", "float")),
    (["joy", "wonder", "amazement"], ["curiosity", "sorrow", "frustration"], ("joy", "sorrow")),
    (["release", "travel", "engage"], ["delay", "move", "seize"], ("release", "seize")),
    (["calm", "chaos", "neat"], ["order", "quiet", "tired"], ("chaos", "order")),
    (["disastrous", "ridiculous", "perplexing"], ["outrageous", "exciting", "serious"], ("ridiculous", "serious")),
]
OPPOSITES_QUESTIONS = []
for i, (g1, g2, correct) in enumerate(_OPPOSITES_RAW):
    opts, correct_str = dual_options(g1, g2, correct)
    OPPOSITES_QUESTIONS.append((
        "Find the two words, one from each group, that are most OPPOSITE in meaning: ({}) ({})".format(", ".join(g1), ", ".join(g2)),
        "mc", opts[0], opts[1], opts[2], opts[3], opts[4], correct_str,
        "'{}' and '{}' are opposite in meaning.".format(correct[0], correct[1]),
        spread_difficulty(len(_OPPOSITES_RAW), i)
    ))

# ═══════════════════════════════════════════════════════════════
# TOPIC 8 — Synonyms (Closest Meaning)
# ═══════════════════════════════════════════════════════════════
SYNONYMS_LESSON = """
<div class="lesson-block">
<h3>↔️ Synonyms (Closest Meaning)</h3>
<p>Find two words, one from each group, that are closest in meaning.</p>
<p><strong>Example:</strong> (office shop start) (work begin end) &rarr;
<strong>start</strong> and <strong>begin</strong>.</p>
</div>
<p style="margin-top:12px;color:rgba(255,255,255,0.4);font-size:12px;">Source: GL Assessment 11+ Verbal Reasoning Familiarisation Paper 2</p>
"""
_SYNONYMS_RAW = [
    (["can", "grease", "pan"], ["fry", "oil", "slip"], ("grease", "oil")),
    (["calm", "rest", "laugh"], ["tired", "peaceful", "happy"], ("calm", "peaceful")),
    (["increase", "quick", "accelerate"], ["race", "speed", "rapid"], ("quick", "rapid")),
    (["teach", "result", "occur"], ["outcome", "incident", "learn"], ("result", "outcome")),
    (["sufficient", "vital", "valid"], ["essential", "certain", "specific"], ("vital", "essential")),
    (["error", "correct", "erase"], ["amend", "tick", "read"], ("correct", "amend")),
    (["purpose", "improve", "agree"], ["pursue", "intention", "decision"], ("purpose", "intention")),
]
SYNONYMS_QUESTIONS = []
for i, (g1, g2, correct) in enumerate(_SYNONYMS_RAW):
    opts, correct_str = dual_options(g1, g2, correct)
    SYNONYMS_QUESTIONS.append((
        "Find the two words, one from each group, that are CLOSEST in meaning: ({}) ({})".format(", ".join(g1), ", ".join(g2)),
        "mc", opts[0], opts[1], opts[2], opts[3], opts[4], correct_str,
        "'{}' and '{}' are closest in meaning.".format(correct[0], correct[1]),
        spread_difficulty(len(_SYNONYMS_RAW), i)
    ))

# ═══════════════════════════════════════════════════════════════
# TOPIC 9 — Hidden Word: Word Join (4 Letters)
# ═══════════════════════════════════════════════════════════════
HIDDEN4_LESSON = """
<div class="lesson-block">
<h3>🔍 Hidden Word: Word Join (4 Letters)</h3>
<p>A word of four letters is hidden at the end of one word and the beginning of
the next. Find the pair of words that contains the hidden word.</p>
<p><strong>Example:</strong> "The film ended happily after all." &rarr; hidden word
'mend' spans <strong>film ended</strong> (fil<u>m</u> + <u>end</u>ed).</p>
</div>
<p style="margin-top:12px;color:rgba(255,255,255,0.4);font-size:12px;">Source: GL Assessment 11+ Verbal Reasoning Familiarisation Papers 1, 2 & 3</p>
"""
_HIDDEN4_RAW = [
    ("They were not alerted at once.", ["They were", "were not", "not alerted", "alerted at", "at once."], "not alerted"),
    ("The shampoo left bubbles in the bath.", ["The shampoo", "shampoo left", "left bubbles", "bubbles in", "in the"], "shampoo left"),
    ("Visitors wandered around the colourful gardens.", ["Visitors wandered", "wandered around", "around the", "the colourful", "colourful gardens."], "Visitors wandered"),
    ("She tried to grasp another rope.", ["She tried", "tried to", "to grasp", "grasp another", "another rope."], "grasp another"),
    ("The rhinoceros escaped from the cage.", ["The rhinoceros", "rhinoceros escaped", "escaped from", "from the", "the cage."], "rhinoceros escaped"),
    ("He hid the banjo inside the cupboard.", ["He hid", "hid the", "the banjo", "banjo inside", "inside the"], "banjo inside"),
    ("They searched the patrol area systematically.", ["They searched", "searched the", "the patrol", "patrol area", "area systematically."], "area systematically."),
    ("The bold monkey sat on my shoulder.", ["The bold", "bold monkey", "monkey sat", "sat on", "on my"], "monkey sat"),
    ("It is wonderful living in the country.", ["It is", "is wonderful", "wonderful living", "living in", "in the"], "wonderful living"),
    ("The sky was clear after days of rain.", ["The sky", "sky was", "was clear", "clear after", "after days"], "clear after"),
    ("Does the paper come with envelopes?", ["Does the", "the paper", "paper come", "come with", "with envelopes?"], "with envelopes?"),
    ("The angry woman yelled at the driver.", ["The angry", "angry woman", "woman yelled", "yelled at", "at the"], "woman yelled"),
    ("I emptied it for you last night.", ["I emptied", "emptied it", "it for", "for you", "you last"], "emptied it"),
    ("She ran to catch the bus.", ["She ran", "ran to", "to catch", "catch the", "the bus."], "ran to"),
    ("His boss made allocations for staff.", ["His boss", "boss made", "made allocations", "allocations for", "for staff."], "made allocations"),
    ("The vocal music was incredibly beautiful.", ["The vocal", "vocal music", "music was", "was incredibly", "incredibly beautiful."], "vocal music"),
    ("She dived elegantly into the pool.", ["She dived", "dived elegantly", "elegantly into", "into the", "the pool."], "She dived"),
    ("The delayed passenger estimated his arrival.", ["The delayed", "delayed passenger", "passenger estimated", "estimated his", "his arrival."], "passenger estimated"),
    ("The tiny green boat sailed slowly.", ["The tiny", "tiny green", "green boat", "boat sailed", "sailed slowly."], "boat sailed"),
    ("The yard was full of mess.", ["The yard", "yard was", "was full", "full of", "of mess."], "The yard"),
    ("Alice made cake for afternoon treats.", ["Alice made", "made cake", "cake for", "for afternoon", "afternoon treats."], "for afternoon"),
]
HIDDEN4_QUESTIONS = []
for i, (sentence, opts, ans) in enumerate(_HIDDEN4_RAW):
    padded = opts + [None] * (5 - len(opts))
    HIDDEN4_QUESTIONS.append((
        "A 4-letter word is hidden across a word-boundary in this sentence: “{}” Which pair of words contains it?".format(sentence),
        "mc", padded[0], padded[1], padded[2], padded[3], padded[4], ans,
        "The hidden 4-letter word spans the join between the two words in '{}'.".format(ans),
        spread_difficulty(len(_HIDDEN4_RAW), i)
    ))

# ═══════════════════════════════════════════════════════════════
# TOPIC 10 — Alphabet Code Sequences
# ═══════════════════════════════════════════════════════════════
ALPHASEQ_LESSON = """
<div class="lesson-block">
<h3>🔡 Alphabet Code Sequences</h3>
<p>Using the alphabet (A-Z) as a guide, work out the rule connecting each pair (or
group) of letters, then find the next / matching pair.</p>
<p><strong>Example:</strong> CQ DQ EP FP [?] &rarr; <strong>GO</strong>.</p>
</div>
<p style="margin-top:12px;color:rgba(255,255,255,0.4);font-size:12px;">Source: GL Assessment 11+ Verbal Reasoning Familiarisation Papers 1, 2 & 3</p>
"""
_ALPHASEQ_RAW = [
    ("UD VF WH XJ [?]", "ZL", "YL", "YK", "ZK", "YM", "YL"),
    ("ZO WL TI QF [?]", "NC", "OD", "MC", "ND", "OB", "NC"),
    ("AQ CM EI GE [?]", "JB", "IB", "HE", "IA", "JA", "IA"),
    ("HQ LR PS TT [?]", "WV", "UV", "XU", "XT", "UX", "XU"),
    ("SG NL JP GS [?]", "ET", "UE", "DT", "DU", "EU", "EU"),
    ("KM LL ML NM OO PR [?]", "QU", "RU", "RV", "QV", "QW", "QV"),
    ("CQ BL ZH WE [?]", "SC", "RC", "TD", "TC", "SD", "SC"),
    ("JL ML PL SL VL [?]", "ZL", "YL", "VL", "XL", "UL", "YL"),
    ("BE CJ EN HQ LS [?]", "QS", "QT", "MS", "ST", "MT", "QT"),
    ("KD XP NG VN QJ TL TM RJ [?]", "WP", "VM", "PH", "RK", "VO", "WP"),
    ("FL EK GM DJ HN [?]", "MI", "DJ", "CJ", "MS", "CI", "CI"),
    ("WX ZA DE IJ [?]", "QR", "OP", "NO", "PQ", "MN", "OP"),
    ("BX BY CA ED HH [?]", "MM", "LM", "ML", "LN", "LL", "LM"),
    ("XZ ZY YA AZ ZB [?]", "BA", "YD", "CA", "YA", "BD", "BA"),
    ("AS is to EO as BK is to [?]", "XH", "FG", "XO", "FO", "XG", "FG"),
    ("OV is to KS as DR is to [?]", "ZU", "HO", "AU", "ZO", "HN", "ZO"),
    ("AW is to DY as VB is to [?]", "DA", "YZ", "XZ", "XB", "YD", "YD"),
    ("HR is to CP as FN is to [?]", "AP", "ZP", "KL", "KN", "AL", "AL"),
    ("TY is to YZ as BA is to [?]", "GZ", "WB", "WZ", "GB", "XB", "GB"),
    ("CD is to ZE as TZ is to [?]", "WB", "QY", "QA", "VA", "WY", "QA"),
    ("HT is to LP as QL is to [?]", "UH", "MH", "UP", "MI", "TP", "UH"),
]
ALPHASEQ_QUESTIONS = []
for i, (stem, a, b, c, d, e, ans) in enumerate(_ALPHASEQ_RAW):
    ALPHASEQ_QUESTIONS.append((
        "Using the alphabet, find the next/matching pair of letters: {}".format(stem),
        "mc", a, b, c, d, e, ans,
        "Following the same alphabet-shift pattern gives '{}'.".format(ans),
        spread_difficulty(len(_ALPHASEQ_RAW), i)
    ))

# ═══════════════════════════════════════════════════════════════
# TOPIC 11 — Hidden Word: Three Letters
# ═══════════════════════════════════════════════════════════════
HIDDEN3_LESSON = """
<div class="lesson-block">
<h3>🔍 Hidden Word: Three Letters</h3>
<p>The word in capitals has had three letters (next to each other) removed. Those
three letters make one correctly-spelt word, and the finished sentence must make
sense.</p>
<p><strong>Example:</strong> "The cat scratched him with his CS." &rarr;
<strong>LAW</strong> (CS &rarr; CLAWS).</p>
</div>
<p style="margin-top:12px;color:rgba(255,255,255,0.4);font-size:12px;">Source: GL Assessment 11+ Verbal Reasoning Familiarisation Papers 1, 2 & 3</p>
"""
_HIDDEN3_RAW = [
    ("His favourite food was CABE.", "BAG", "GET", "EVE", "SAG", "BAT", "BAT"),
    ("The cars SDED in the bad weather.", "DEN", "KID", "PAR", "RAN", "LAD", "RAN"),
    ("He BED for more space in the room.", "EGG", "LAB", "ONE", "TUG", "RIP", "EGG"),
    ("The morning was spent CLING the garden.", "ROE", "AFT", "APE", "EAR", "OWE", "EAR"),
    ("I introduced my STEPHER.", "FAT", "MOW", "VAN", "CAP", "RAT", "RAT"),
    ("They were OVERED at the news.", "GAP", "NIL", "JOY", "TON", "POT", "JOY"),
    ("He gave his final JUDENT.", "HUM", "GEM", "ACE", "TEN", "TRY", "GEM"),
    ("Teabags have lots of PERATIONS.", "SET", "HIP", "FOR", "COT", "LET", "FOR"),
    ("I wear SALS in the summer.", "LAP", "AND", "CAN", "OLD", "TAR", "AND"),
    ("I'm going to the BING alley for my birthday.", "LIT", "AIM", "ONE", "OWL", "INK", "OWL"),
    ("An EXPERIT was carried out.", "MEN", "CAT", "PEN", "EAR", "ANT", "MEN"),
    ("The hat was FLING on the water.", "OFF", "OAT", "ATE", "AID", "END", "OAT"),
    ("The boy was taught how to WTLE.", "HAS", "ILL", "HIS", "OIL", "EEL", "HIS"),
    ("A GUATEE came with the television.", "RAN", "SAT", "NOT", "OUR", "OWE", "RAN"),
    ("The comedian IMITD people.", "ALL", "FOR", "ATE", "ILL", "AND", "ATE"),
    ("Charlie's school KS were very heavy.", "ATE", "BOO", "LOW", "BOW", "ACT", "BOO"),
    ("The large TROR completely blocked the road.", "ACT", "RAN", "ERR", "ATE", "EAR", "ACT"),
    ("The CHER was delayed by traffic.", "ARE", "TEE", "MAT", "TEA", "LAW", "TEA"),
    ("Porridge is great at FING you up.", "RAP", "LAP", "ILL", "AIM", "EAR", "ILL"),
    ("It was a slow and difficult JNEY in the city.", "ARE", "YOU", "AIR", "ANY", "OUR", "OUR"),
    ("Gemma and her friends really enjoyed playing on the SGS.", "RAN", "TEA", "WIN", "TAR", "WON", "WIN"),
    ("The PAVET was hot in the summer's heat.", "OUR", "RAT", "BEE", "SIT", "MEN", "MEN"),
    ("Everyone agreed it was an impressive CAAL city.", "TIN", "SEA", "MET", "PIT", "BUT", "PIT"),
]
HIDDEN3_QUESTIONS = []
for i, (sentence, a, b, c, d, e, ans) in enumerate(_HIDDEN3_RAW):
    HIDDEN3_QUESTIONS.append((
        "The word in CAPITALS is missing three letters that make a real word. Which three letters? “{}”".format(sentence),
        "mc", a, b, c, d, e, ans,
        "Inserting '{}' completes the capitalised word and the sentence makes sense.".format(ans),
        spread_difficulty(len(_HIDDEN3_RAW), i)
    ))

# ═══════════════════════════════════════════════════════════════
# TOPIC 12 — Word Analogies
# ═══════════════════════════════════════════════════════════════
ANALOGY_LESSON = """
<div class="lesson-block">
<h3>🔗 Word Analogies</h3>
<p>"X is to (group1) as Y is to (group2)" — pick one word from each group so the
two relationships match.</p>
<p><strong>Example:</strong> Big is to (small orange colour) as wide is to (apple red narrow)
&rarr; <strong>small, narrow</strong> (antonym pairs).</p>
</div>
<p style="margin-top:12px;color:rgba(255,255,255,0.4);font-size:12px;">Source: GL Assessment 11+ Verbal Reasoning Familiarisation Papers 1 & 3</p>
"""
_ANALOGY_RAW = [
    ("Look", ["eye", "blink", "see"], "listen", ["hear", "tone", "noise"], ("see", "hear")),
    ("High", ["low", "far", "big"], "deep", ["fall", "shallow", "water"], ("low", "shallow")),
    ("Bus", ["driver", "passengers", "road"], "plane", ["airline", "cloud", "pilot"], ("driver", "pilot")),
    ("Plug", ["sink", "stopper", "block"], "cork", ["bottle", "float", "screw"], ("sink", "bottle")),
    ("Fly", ["insect", "wings", "feathers"], "run", ["fast", "person", "legs"], ("wings", "legs")),
    ("Stitch", ["sew", "needle", "cloth"], "stroke", ["pat", "paint", "cat"], ("sew", "paint")),
    ("Large", ["open", "spacious", "great"], "small", ["confined", "close", "near"], ("spacious", "confined")),
    ("Magazine", ["picture", "recycle", "read"], "television", ["watch", "rest", "broadcast"], ("read", "watch")),
    ("Help", ["hope", "assist", "recover"], "hinder", ["visit", "contain", "block"], ("assist", "block")),
    ("Green", ["pea", "lemon", "carrot"], "red", ["celery", "tomato", "mushroom"], ("pea", "tomato")),
    ("Wave", ["crinkle", "energy", "ocean"], "cloud", ["smooth", "fluffy", "sky"], ("ocean", "sky")),
    ("Spade", ["dig", "break", "lift"], "broom", ["rinse", "push", "sweep"], ("dig", "sweep")),
    ("Daring", ["afraid", "bold", "hasty"], "kind", ["thoughtful", "ambitious", "timid"], ("bold", "thoughtful")),
    ("Cup", ["hold", "drink", "support"], "fork", ["prod", "eat", "divide"], ("drink", "eat")),
]
ANALOGY_QUESTIONS = []
for i, (word1, g1, word2, g2, correct) in enumerate(_ANALOGY_RAW):
    opts, correct_str = dual_options(g1, g2, correct)
    ANALOGY_QUESTIONS.append((
        "{} is to ({}) as {} is to ({}). Which two words complete the analogy?".format(word1, ", ".join(g1), word2, ", ".join(g2)),
        "mc", opts[0], opts[1], opts[2], opts[3], opts[4], correct_str,
        "'{}' relates to {} the same way '{}' relates to {}.".format(correct[0], word1, correct[1], word2),
        spread_difficulty(len(_ANALOGY_RAW), i)
    ))

# ═══════════════════════════════════════════════════════════════
# TOPIC 13 — Fits Both Pairs
# ═══════════════════════════════════════════════════════════════
FITSBOTH_LESSON = """
<div class="lesson-block">
<h3>🔗 Fits Both Pairs</h3>
<p>There are two pairs of words. Only one of the five possible answers goes
equally well with BOTH pairs (because the word has two different meanings).</p>
<p><strong>Example:</strong> (world globe) (soil ground) &rarr; <strong>earth</strong>.</p>
</div>
<p style="margin-top:12px;color:rgba(255,255,255,0.4);font-size:12px;">Source: GL Assessment 11+ Verbal Reasoning Familiarisation Paper 1</p>
"""
_FITSBOTH_RAW = [
    ("(permit allow)", "(rent hire)", "grant", "let", "agree", "use", "loan", "let"),
    ("(wood trunk)", "(howl wail)", "tree", "shout", "cut", "bark", "call", "bark"),
    ("(resemble similar)", "(fond admire)", "please", "copy", "enjoy", "like", "same", "like"),
    ("(token disc)", "(worktop surface)", "flat", "voucher", "counter", "sideboard", "coin", "counter"),
    ("(jump leap)", "(well water)", "hop", "flow", "move", "source", "spring", "spring"),
    ("(chapter paragraph)", "(corridor alley)", "book", "path", "walk", "read", "passage", "passage"),
    ("(allotment patch)", "(conspire plan)", "plot", "scheme", "garden", "land", "conceive", "plot"),
]
FITSBOTH_QUESTIONS = []
for i, (p1, p2, a, b, c, d, e, ans) in enumerate(_FITSBOTH_RAW):
    FITSBOTH_QUESTIONS.append((
        "Which word goes equally well with both word pairs: {} {}".format(p1, p2),
        "mc", a, b, c, d, e, ans,
        "'{}' has a meaning that fits both pairs of words.".format(ans),
        spread_difficulty(len(_FITSBOTH_RAW), i)
    ))

# ═══════════════════════════════════════════════════════════════
# TOPIC 14 — Combine Two Words
# ═══════════════════════════════════════════════════════════════
COMBINE_LESSON = """
<div class="lesson-block">
<h3>🔗 Combine Two Words</h3>
<p>Find two words, one from each group, that together make ONE correctly spelt
word (the word from the first group always comes first).</p>
<p><strong>Example:</strong> (out by open) (bite like side) &rarr; <strong>out, side</strong>
(outside).</p>
</div>
<p style="margin-top:12px;color:rgba(255,255,255,0.4);font-size:12px;">Source: GL Assessment 11+ Verbal Reasoning Familiarisation Paper 2</p>
"""
_COMBINE_RAW = [
    (["far", "sea", "at"], ["son", "are", "den"], ("sea", "son")),
    (["be", "can", "fin"], ["ward", "less", "at"], ("be", "at")),
    (["cot", "off", "adapt"], ["turn", "able", "tune"], ("adapt", "able")),
    (["pen", "cot", "ham"], ["ton", "gain", "by"], ("cot", "ton")),
    (["ear", "in", "us"], ["ant", "bin", "age"], ("us", "age")),
    (["set", "the", "he"], ["red", "nut", "me"], ("the", "me")),
    (["bat", "up", "rest"], ["ant", "rain", "fill"], ("rest", "rain")),
    (["tea", "grin", "set"], ["ring", "pet", "dish"], ("tea", "ring")),
]
COMBINE_QUESTIONS = []
for i, (g1, g2, correct) in enumerate(_COMBINE_RAW):
    opts, correct_str = dual_options(g1, g2, correct)
    combined_word = "".join(correct)
    COMBINE_QUESTIONS.append((
        "Find two words, one from each group, that together spell one real word: ({}) ({})".format(", ".join(g1), ", ".join(g2)),
        "mc", opts[0], opts[1], opts[2], opts[3], opts[4], correct_str,
        "'{}' + '{}' = '{}', a real word.".format(correct[0], correct[1], combined_word),
        spread_difficulty(len(_COMBINE_RAW), i)
    ))

# ═══════════════════════════════════════════════════════════════
# TOPIC 15 — Letters as Numbers
# ═══════════════════════════════════════════════════════════════
LETTERNUM_LESSON = """
<div class="lesson-block">
<h3>🔢 Letters as Numbers</h3>
<p>Each letter A-E stands for a given number. Work out the sum, then find which
letter that answer equals.</p>
<p><strong>Example:</strong> A=1, B=2, C=3, D=6, E=8. A+B+C=? &rarr; 1+2+3=6=D.</p>
</div>
<p style="margin-top:12px;color:rgba(255,255,255,0.4);font-size:12px;">Source: GL Assessment 11+ Verbal Reasoning Familiarisation Papers 2 & 3</p>
"""
_LETTERNUM_RAW = [
    ("A=2, B=3, C=4, D=5, E=6. B×D−E−D = ?", 2, 3, 4, 5, 6, "B×D−E−D", "C"),
    ("A=2, B=5, C=15, D=23, E=27. A×C−B+A = ?", 2, 5, 15, 23, 27, "A×C−B+A", "E"),
    ("A=1, B=3, C=5, D=15, E=20. B×E÷D+A = ?", 1, 3, 5, 15, 20, "B×E÷D+A", "C"),
    ("A=3, B=5, C=8, D=9, E=15. D×B÷E+B = ?", 3, 5, 8, 9, 15, "D×B÷E+B", "C"),
    ("A=6, B=9, C=12, D=27, E=45. D÷B×C−B = ?", 6, 9, 12, 27, 45, "D÷B×C−B", "D"),
    ("A=3, B=4, C=5, D=6, E=8. D×E÷B−B = ?", 3, 4, 5, 6, 8, "D×E÷B−B", "E"),
    ("A=3, B=6, C=14, D=28, E=90. A×D÷B = ?", 3, 6, 14, 28, 90, "A×D÷B", "C"),
    ("A=2, B=4, C=6, D=8, E=16. E÷D+A = ?", 2, 4, 6, 8, 16, "E÷D+A", "B"),
    ("A=2, B=3, C=4, D=8, E=12. C×B÷A+A = ?", 2, 3, 4, 8, 12, "C×B÷A+A", "D"),
    ("A=5, B=11, C=37, D=43, E=49. D−C+A = ?", 5, 11, 37, 43, 49, "D−C+A", "B"),
    ("A=6, B=8, C=9, D=12, E=14. C×B÷D = ?", 6, 8, 9, 12, 14, "C×B÷D", "A"),
    ("A=2, B=3, C=8, D=13, E=14. E×B÷A−C = ?", 2, 3, 8, 13, 14, "E×B÷A−C", "D"),
    ("A=42, B=48, C=49, D=57, E=64. D+C−E = ?", 42, 48, 49, 57, 64, "D+C−E", "A"),
    ("A=5, B=10, C=15, D=65, E=75. E÷A−A = ?", 5, 10, 15, 65, 75, "E÷A−A", "B"),
]
LETTERNUM_QUESTIONS = []
for i, (setup, va, vb, vc, vd, ve, expr, ans) in enumerate(_LETTERNUM_RAW):
    LETTERNUM_QUESTIONS.append((
        "Letters stand for numbers. {} What is the answer written as a letter (A, B, C, D or E)?".format(setup),
        "mc", "A", "B", "C", "D", "E", ans,
        "Substitute the values and compute {}; the result equals option {}.".format(expr, ans),
        spread_difficulty(len(_LETTERNUM_RAW), i)
    ))

# ═══════════════════════════════════════════════════════════════
# TOPIC 16 — Balancing Equations
# ═══════════════════════════════════════════════════════════════
BALANCE_LESSON = """
<div class="lesson-block">
<h3>⚖️ Balancing Equations</h3>
<p>The sum on the right must equal the sum on the left. Find the missing number.</p>
<p><strong>Example:</strong> 3+5 = 6+[?] &rarr; 8 = 6+<strong>2</strong>.</p>
</div>
<p style="margin-top:12px;color:rgba(255,255,255,0.4);font-size:12px;">Source: GL Assessment 11+ Verbal Reasoning Familiarisation Paper 2</p>
"""
_BALANCE_RAW = [
    ("9×2÷3 = 7×2−[?]", "8", "6", "4", "2", "10", "8"),
    ("59+27−13 = 7×8+[?]", "16", "15", "19", "17", "18", "17"),
    ("19×5 = 100÷2+[?]", "30", "50", "40", "35", "45", "45"),
    ("81÷27+36 = 6×7−[?]", "4", "7", "3", "5", "2", "3"),
    ("125÷5 = 8×9−[?]", "45", "50", "32", "47", "37", "47"),
    ("6×13−15 = 18+72−[?]", "23", "25", "29", "31", "27", "27"),
    ("144÷6+3 = 72÷8+[?]", "18", "14", "16", "12", "10", "18"),
]
BALANCE_QUESTIONS = []
for i, (eq, a, b, c, d, e, ans) in enumerate(_BALANCE_RAW):
    BALANCE_QUESTIONS.append((
        "Find the missing number that balances the equation: {}".format(eq),
        "mc", a, b, c, d, e, ans,
        "Both sides must be equal; the missing number is {}.".format(ans),
        spread_difficulty(len(_BALANCE_RAW), i)
    ))

# ═══════════════════════════════════════════════════════════════
# TOPIC 17 — Number & Letter Codes
# ═══════════════════════════════════════════════════════════════
CODES_LESSON = """
<div class="lesson-block">
<h3>🔑 Number & Letter Codes</h3>
<p>Words are written in code, where each letter maps to a number or another
letter. Work out the mapping from the given examples, then decode or encode the
requested word.</p>
</div>
<p style="margin-top:12px;color:rgba(255,255,255,0.4);font-size:12px;">Source: GL Assessment 11+ Verbal Reasoning Familiarisation Papers 1, 2 & 3</p>
"""
# Note: the first 12 questions (4 "number code" families) use the same real
# words as the original GL booklets, but the digit-cipher itself was
# reconstructed to guarantee internal consistency — the multi-digit codes
# originally transcribed from the PDF images contradicted each other
# letter-by-letter and couldn't be trusted. The 6 "if the code for X is Y"
# questions further below are unchanged and were verified correct against
# the source. See the file's audit notes for details.
_CODES_RAW = [
    ("In this code family: ANTS=1234, LETS=5634, EAST=6143 (one code missing). Find the code for BASE.", "1234", "7146", "6417", "1476", "7461", "7146"),
    ("Using the same code family, find the code for NEST.", "2643", "2634", "6243", "4263", "2436", "2643"),
    ("Using the same code family, find the word with code 3156.", "TALE", "TAIL", "LATE", "SALE", "SEAT", "TALE"),
    ("In this code family: INTO=2536, PAIN=7825, POET=7643 (one code missing). Find the code for KITE.", "1243", "2134", "1234", "4321", "1324", "1234"),
    ("Using the same code family, find the word with code 7481.", "PEAK", "PEAT", "TEAK", "PACT", "TAPE", "PEAK"),
    ("Using the same code family, find the code for OPEN.", "6745", "7645", "6754", "4675", "6547", "6745"),
    ("In this code family: NAIL=1234, LATE=4278, FIST=5397 (one code missing). Find the code for FIND.", "5316", "3516", "5361", "1536", "5163", "5316"),
    ("Using the same code family, find the word with code 9258.", "SAFE", "SEAT", "FEAS", "FATE", "SAFT", "SAFE"),
    ("Using the same code family, find the code for LEAST.", "48297", "42897", "48927", "49287", "48279", "48297"),
    ("In this code family: TIME=1234, HEAT=5461, MELT=3471 (one code missing). Find the code for SAIL.", "8267", "8627", "6827", "8672", "2867", "8627"),
    ("Using the same code family, find the word with code 1627.", "TAIL", "TALI", "LAIT", "TILA", "LATI", "TAIL"),
    ("Using the same code family, find the code for SALT.", "8671", "8617", "8761", "6871", "8176", "8671"),
    ("If the code for FORE is DSPI, what is the code for PILL?", "NKJP", "NLNN", "RMNJ", "RKJN", "NMJP", "NMJP"),
    ("If the code for NEWS is QCZQ, what is the code for TAPS?", "WYRU", "WYSQ", "QCSQ", "WCRP", "QYMU", "WYSQ"),
    ("If the code for TRIP is SNHL, what is the code for CARS?", "DZSO", "BWQO", "AZSP", "XXQP", "YWSO", "BWQO"),
    ("If the code for MEAN is NGDR, what does ETLT mean?", "DROP", "FROM", "DRIP", "CUPS", "FUNK", "DRIP"),
    ("If the code for RIDE is UFGB, what is the code for BAKE?", "EXNB", "DXIH", "YWOA", "EDNB", "YDHH", "EXNB"),
    ("If the code for BIKE is DEMA, what does JATO mean?", "LEST", "HYPE", "HAVE", "HERS", "LIST", "HERS"),
]
CODES_QUESTIONS = []
for i, (stem, a, b, c, d, e, ans) in enumerate(_CODES_RAW):
    CODES_QUESTIONS.append((
        stem, "mc", a, b, c, d, e, ans,
        "Working out the letter/number mapping from the given codes gives '{}'.".format(ans),
        spread_difficulty(len(_CODES_RAW), i)
    ))

TOPICS = [
    ("Verbal Reasoning: Move a Letter Between Words", MOVE_LETTER_LESSON, MOVE_LETTER_QUESTIONS),
    ("Verbal Reasoning: Same Letter, Two Gaps", BRACKETS_LESSON, BRACKETS_QUESTIONS),
    ("Verbal Reasoning: Hidden Word Patterns", PATTERN_LESSON, PATTERN_QUESTIONS),
    ("Verbal Reasoning: Odd One Out (Find Two)", ODDONE_LESSON, ODDONE_QUESTIONS),
    ("Verbal Reasoning: Number Sequences", NUMSEQ_LESSON, NUMSEQ_QUESTIONS),
    ("Verbal Reasoning: Logic Puzzles", LOGIC_LESSON, LOGIC_QUESTIONS),
    ("Verbal Reasoning: Opposites (Antonyms)", OPPOSITES_LESSON, OPPOSITES_QUESTIONS),
    ("Verbal Reasoning: Synonyms (Closest Meaning)", SYNONYMS_LESSON, SYNONYMS_QUESTIONS),
    ("Verbal Reasoning: Hidden Word — Word Join (4 Letters)", HIDDEN4_LESSON, HIDDEN4_QUESTIONS),
    ("Verbal Reasoning: Alphabet Code Sequences", ALPHASEQ_LESSON, ALPHASEQ_QUESTIONS),
    ("Verbal Reasoning: Hidden Word — Three Letters", HIDDEN3_LESSON, HIDDEN3_QUESTIONS),
    ("Verbal Reasoning: Word Analogies", ANALOGY_LESSON, ANALOGY_QUESTIONS),
    ("Verbal Reasoning: Fits Both Pairs", FITSBOTH_LESSON, FITSBOTH_QUESTIONS),
    ("Verbal Reasoning: Combine Two Words", COMBINE_LESSON, COMBINE_QUESTIONS),
    ("Verbal Reasoning: Letters as Numbers", LETTERNUM_LESSON, LETTERNUM_QUESTIONS),
    ("Verbal Reasoning: Balancing Equations", BALANCE_LESSON, BALANCE_QUESTIONS),
    ("Verbal Reasoning: Number & Letter Codes", CODES_LESSON, CODES_QUESTIONS),
]


def get_db():
    import psycopg2, psycopg2.extras, os, sys
    sys.path.insert(0, os.path.expanduser("~/Downloads/anish_app_v2"))
    try:
        import config
        url = config.DATABASE_URL
    except Exception:
        url = os.environ.get("DATABASE_URL")
    return psycopg2.connect(url, cursor_factory=psycopg2.extras.RealDictCursor)


def add_previous_exam_verbal():
    conn = get_db()
    cur = conn.cursor()
    today = date.today().isoformat()

    cur.execute("ALTER TABLE questions ADD COLUMN IF NOT EXISTS option_e TEXT")
    conn.commit()

    total_topics_added = 0
    total_questions_added = 0

    for title, lesson_html, questions in TOPICS:
        cur.execute("SELECT id FROM topics WHERE title=%s AND subject=%s", (title, SUBJECT))
        row = cur.fetchone()
        if row:
            topic_id = row["id"]
        else:
            cur.execute("""
                INSERT INTO topics (subject, section, title, source, lesson_html, created_at, archived)
                VALUES (%s,%s,%s,%s,%s,%s,0) RETURNING id
            """, (SUBJECT, SECTION, title, SOURCE, lesson_html, today))
            topic_id = cur.fetchone()["id"]
            total_topics_added += 1
            conn.commit()

        cur.execute("SELECT question_text FROM questions WHERE topic_id=%s", (topic_id,))
        existing = {r["question_text"] for r in cur.fetchall()}

        added = 0
        for q in questions:
            q_text, q_type, a, b, c, d, e, answer, explanation, level = q
            if q_text in existing:
                continue
            cur.execute("""
                INSERT INTO questions (topic_id, question_text, question_type,
                    option_a, option_b, option_c, option_d, option_e,
                    correct_answer, explanation, difficulty)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """, (topic_id, q_text, q_type, a, b, c, d, e, answer, explanation, level))
            added += 1
        conn.commit()
        print("  {}: +{} questions ({} total)".format(title, added, len(questions)))
        total_questions_added += added

    cur.close()
    conn.close()
    print("\nTopics added: {}".format(total_topics_added))
    print("Questions added: {}".format(total_questions_added))


if __name__ == "__main__":
    add_previous_exam_verbal()
