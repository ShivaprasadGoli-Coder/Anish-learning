"""
add_previous_exam_english.py — Adds real GL Assessment 11+ Familiarisation
Paper questions (English 1 & English 2) into a new "Previous Exam Questions"
subject, "English" module/section.

Source: GL Assessment English Familiarisation Papers 1 & 2 (Copyright (c) GL
Assessment, 2017/2019), used here for personal family study only. Answers
taken from the official Parent's Guide answer key.

Creates 8 new topics (4 per paper) and inserts their questions.
Safe to re-run: skips topics/questions that already exist.

Run: python3 add_previous_exam_english.py
"""
from datetime import date

SUBJECT = "Previous Exam Questions"
SECTION = "English"
SOURCE = "GL Assessment 11+ English Familiarisation Paper"

# Each question tuple: (text, type, a, b, c, d, e, answer, explanation, difficulty)
# e is None for standard 4-option questions.

# ─────────────────────────────────────────────────────────────
# PAPER 1 — Reading Comprehension: The Swiss Family Robinson
# ─────────────────────────────────────────────────────────────
SWISS_FAMILY_LESSON = """
<div class="lesson-block">
<h3>📖 Passage: The Swiss Family Robinson (by Johann David Wyss)</h3>
<p><em>This story is told by a father who has been shipwrecked on an island along with his wife and sons, Jack and Fritz, and their pet dogs. They have spent the winter safely in Falconhurst, which is the home that they built. The weather has recently improved, and it is time to find out what effect the winter storms have had on their tree house and tents.</em></p>
<p>The winds at length were lulled, the sun shot his brilliant rays through the clouds, the rain ceased to fall &ndash; spring had come. No prisoners set free could have felt more joy than we did as we stepped out from our winter home. We refreshed our eyes with the pleasant greenery around us, and our ears with the merry songs of a thousand happy birds, and drank in the pure air of spring.</p>
<p>Our tree house was our first care: filled with leaves and broken and torn by the wind, it looked indeed dilapidated. We worked hard, and in a few days it was again habitable. I was anxious to visit the tent, for I feared that much of our precious stores might have suffered. The damage done to Falconhurst was nothing compared to the scene that awaited us. The tent was blown to the ground, the canvas torn to rags, and the provisions soaked. We immediately spread the things that we hoped to preserve in the sun to dry.</p>
<p>The irreparable damage we had suffered made me resolve to find some safer and more stable winter-quarters before the arrival of the next rainy season. Fritz proposed that we should hollow out a cave in the rock. The difficulties such a task would present appeared almost insurmountable, yet I was determined to make the attempt. We might not, I thought, cut out a cavern of sufficient size to serve as a room, but we might at least make a cellar for the more valuable and perishable of our stores.</p>
<p>Some days afterwards we left Falconhurst with the cart laden with a cargo of spades, hammers, chisels, pickaxes and crowbars, and began the work. On the smooth face of the rock I drew out in chalk the size of the proposed entrance, and then, with minds bent on success, we battered away.</p>
<p>Six days of hard and incessant toil made little impression; I do not think that the hole would have been a satisfactory shelter for even our smallest dog. But we still did not despair, and were soon rewarded by coming to a softer and more yielding substance; our work progressed, and our minds were relieved.</p>
<p>On the tenth day, as our persevering blows were falling heavily, Jack, who was working hard with a hammer and crowbar, shouted: &lsquo;Gone, father! Fritz, my bar has gone through the mountain! It went right through the rock; I heard it crash down inside. Oh, do come and see!&rsquo;</p>
<p>We sprang to his side, and I thrust the handle of my hammer into the hole. I could turn it in any direction I chose. Fritz handed me a long pole; I tried the depth with that. Nothing could I feel. A thin wall, then, was all that stood between us and a great cavern.</p>
<p>With a shout of joy, we battered vigorously at the rock; piece by piece fell, and soon the hole was large enough for us to enter. Fritz and I enlarged the opening, while Jack, springing on his horse, thundered away to Falconhurst to bear the great and astonishing news to his mother.</p>
<p>He soon returned, quickly followed by the rest of our party in the cart. All were in the highest state of excitement.</p>
<p>Jack had stowed in the cart all the candles he could find, and we now, lighting these, entered. I led the way. Silently we marched &ndash; my wife, the boys, and even the dogs seeming overawed with the grandeur and beauty of the scene. We were in a cave of diamonds &ndash; a vast chamber of glittering crystal. The candles reflected on the walls a golden light, bright as the stars, while great crystal pillars rose from the floor like mighty trees, mingling their branches which sparkled and glittered with all the colours of the rainbow.</p>
<p>The floor of this magnificent palace was formed of hard, dry sand, so dry that I saw at once that we might safely make our home inside it.</p>
</div>
<p style="margin-top:12px;color:rgba(255,255,255,0.4);font-size:12px;">Source: GL Assessment English Familiarisation Paper 1 (2017)</p>
"""

SWISS_FAMILY_QUESTIONS = [
("At what time of year is the passage set?", "mc", "winter", "spring", "rainy season", "mid-summer", "autumn", "spring", "'The winds at length were lulled... spring had come' tells us directly.", 1),
("The father compares himself and his family to prisoners set free. Why? (lines 2–3)", "mc", "They had been held hostage by pirates.", "They had been trapped in their cave.", "They had been trapped in their house due to stormy weather.", "They had been caught in heavy rain which had finally stopped.", "They had been unfairly accused of crimes but the accusations had been dropped.", "They had been trapped in their house due to stormy weather.", "They had been shut in Falconhurst by the winter storms all season.", 2),
("'The winds at length were lulled' (line 1). What is another way of saying 'lulled'?", "mc", "rhythmic", "weakened", "welcomed", "rocked", "calmed", "calmed", "'Lulled' means soothed or calmed down.", 1),
("Why might the author have decided to include water references in the first paragraph? (lines 1–5)", "mc", "The heavy rain had recently stopped.", "Rain was still falling heavily.", "Water makes the setting seem more peaceful.", "The family hadn't had a drink for a long time.", "The family have found themselves on an island surrounded by water.", "The heavy rain had recently stopped.", "The passage marks the end of winter storms and the arrival of spring.", 2),
("How many adjectives can you count in the sentence beginning “We refreshed our eyes…”? (lines 3–5)", "mc", "1", "2", "3", "4", "5", "4", "'pleasant', 'merry', 'happy', 'pure' are the adjectives.", 2),
("'in a few days it [the tree-house] was again habitable' (line 7). What does this mean?", "mc", "The family soon got used to the damage to the tree-house.", "The tree-house was rapidly transformed into a luxury home.", "The family were soon able to live in the tree-house again.", "The tree-house was destroyed again within a few days.", "The tree-house quickly dried out by itself.", "The family were soon able to live in the tree-house again.", "'Habitable' means able to be lived in.", 2),
("Where had the family kept their supplies over the winter?", "mc", "in a cellar", "in their tree-house", "in their tent", "in a cave", "outside, in barrels", "in their tent", "'The tent was blown to the ground... and the provisions soaked.'", 1),
("How did the family attempt to rescue their supplies?", "mc", "They shook all of the water off them.", "They fetched new materials to mend them.", "They took them to the tree-house instead of the tent.", "They made a fire to dry them out.", "They placed them out in the sun to dry.", "They placed them out in the sun to dry.", "'We immediately spread the things that we hoped to preserve in the sun to dry.'", 2),
("The father considered the damage inflicted on their property 'irreparable'. (line 12) What does this word suggest he thought about the damage?", "mc", "It would be easy to repair the damage.", "The damage was likely to be repeated.", "The damage could be repaired but it would be difficult.", "It would be impossible to repair all of the damage.", "The father had never seen damage like it before.", "It would be impossible to repair all of the damage.", "'Irreparable' means unable to be repaired.", 2),
("What is meant by 'quarters' (line 13)?", "mc", "sections", "lodgings", "storerooms", "stables", "beds", "lodgings", "'Winter-quarters' here means a place to live.", 1),
("What do we know about the climate on the island?", "mc", "The island is protected from heavy winds.", "There is a rainy season.", "The climate is very consistent.", "Despite being warm, there is not much sun.", "It rains all the time.", "There is a rainy season.", "The father wants shelter 'before the arrival of the next rainy season.'", 2),
("Based on the passage, what was the main goal of hollowing out a cave in the rock?", "mc", "to provide a look-out point to watch for enemies", "to provide a space for their animals", "to test how much water had got into the rock", "to provide an extra room in case they had visitors", "to provide accommodation for the winter season", "to provide accommodation for the winter season", "They wanted 'safer and more stable winter-quarters' before the rains.", 2),
("If they only managed to carve out a smaller cave, what did the father hope to use it as?", "mc", "a shelter for emergencies", "a house for their dog", "a playroom for the children", "a storage space for supplies", "a shelter for rain showers", "a storage space for supplies", "'We might at least make a cellar for... our stores.'", 2),
("How easy did the father think it would be to carve out a cave?", "mc", "very easy", "easy as long as they set their minds to it", "quite difficult, with no guarantee of success", "so difficult it was nearly impossible", "completely impossible", "so difficult it was nearly impossible", "'The difficulties... appeared almost insurmountable.'", 2),
("'with minds bent on success' (lines 20–21). What does this imply about their attitude to the work?", "mc", "They were indifferent as to whether they succeeded.", "They wanted to succeed but struggled to believe they could.", "They were absolutely determined to see it through.", "They were so confident they felt they had already succeeded.", "They worked cautiously because there was a high chance they wouldn't succeed.", "They were absolutely determined to see it through.", "'Minds bent on success' shows total determination.", 3),
("'incessant toil' (line 22). What does the word 'incessant' say about the work they were doing?", "mc", "The work they were doing was very difficult.", "They kept working without a break.", "They worked hard but it was having no effect.", "They worked on and off, taking frequent breaks.", "The work was uninspiring and monotonous.", "They kept working without a break.", "'Incessant' means continuous, without stopping.", 2),
("What would be another word for 'impression' on line 22?", "mc", "impact", "dent", "consequence", "trouble", "achievement", "impact", "'Made little impression' means had little effect/impact.", 1),
("Why did the family feel 'relieved' after they had started their work? (line 25)", "mc", "They knew they couldn't get any further and could stop working.", "They had finally begun to make progress.", "Somebody rewarded them for their six days of work.", "They realised they could fit their dog in the hole.", "They had learned from the experience so it hadn't been a complete waste of time.", "They had finally begun to make progress.", "They reached 'softer and more yielding substance' and progress resumed.", 2),
("What type of word is 'persevering' on line 26?", "mc", "noun", "verb", "adjective", "adverb", "preposition", "adjective", "'Persevering blows' — 'persevering' describes the blows.", 1),
("What type of words are the following? heavily (line 26), hard (line 27), vigorously (line 33), quickly (line 37), safely (line 46)", "mc", "nouns", "verbs", "adjectives", "adverbs", "prepositions", "adverbs", "They all describe how an action was done.", 1),
("What was the reaction when Jack lost his crowbar?", "mc", "Jack's father was angry because Jack had lost one of their tools.", "Jack was embarrassed because he looked incompetent.", "Jack was excited because of what it implied about the rock.", "Jack and his father were relieved because it meant they could stop work.", "Jack and his father were nervous because they didn't know what to expect.", "Jack was excited because of what it implied about the rock.", "Jack shouted excitedly — the crowbar going through meant a cavern was near.", 2),
("'we battered vigorously at the rock' (line 33). Which of the following words is closest in meaning to 'vigorously'?", "mc", "painfully", "rebelliously", "energetically", "carefully", "powerlessly", "energetically", "'Vigorously' means with great energy and force.", 1),
("What did Jack do while Fritz and his father enlarged the opening of the cave?", "mc", "Jack went for a ride on his horse to celebrate the work was over.", "Jack went to inform his mother.", "Jack shouted loudly.", "Jack went to collect more tools.", "Jack had a rest so that he could take over next.", "Jack went to inform his mother.", "'Jack, springing on his horse, thundered away to Falconhurst to bear the... news to his mother.'", 2),
("What type of words are the following? resolve (line 12), sprang (line 30), thrust (line 30), enlarged (line 34), thundered (line 35)", "mc", "nouns", "verbs", "adjectives", "adverbs", "prepositions", "verbs", "They are all action words.", 1),
("What was the family's reaction to the cave?", "mc", "They thought it was so beautiful they couldn't possibly make a home inside.", "They were excited but fearful about what was inside.", "They couldn't see much because it was so dark.", "The cave was as they had expected and they immediately felt at-home.", "They were overwhelmed at the dazzling appearance.", "They were overwhelmed at the dazzling appearance.", "'We were in a cave of diamonds... glittered with all the colours of the rainbow.'", 3),
("What other word is used interchangeably with 'diamonds' in the description of the cave? (lines 41–44)", "mc", "gold", "rainbow", "silver", "stars", "crystal", "crystal", "'A vast chamber of glittering crystal... great crystal pillars.'", 1),
("Inside the cave, 'crystal pillars rose from the floor like mighty trees' (line 43). This is an example of…", "mc", "a metaphor", "personification", "exaggeration", "a simile", "alliteration", "a simile", "It uses 'like' to compare the pillars to trees.", 3),
("Why was the cave considered suitable as a home?", "mc", "because it resembled the family's previous home", "because it was high and hidden from animals", "because the crystal made it brighter inside", "because the hard, dry sand would protect against damp", "because it was warm inside", "because the hard, dry sand would protect against damp", "'So dry that I saw at once that we might safely make our home inside it.'", 3),
]

# ─────────────────────────────────────────────────────────────
# PAPER 1 — Spelling Exercise
# ─────────────────────────────────────────────────────────────
SPELLING1_LESSON = """
<div class="lesson-block">
<h3>✏️ Spelling Exercise</h3>
<p>In the real exam, each sentence has one word (out of an underlined A/B/C/D
section) that is spelled incorrectly, or has no mistake at all (marked N).
Here, each question asks you to spot the misspelled word directly &mdash;
same skill, adapted to a tap-the-answer format.</p>
</div>
<p style="margin-top:12px;color:rgba(255,255,255,0.4);font-size:12px;">Source: GL Assessment English Familiarisation Paper 1 (2017)</p>
"""

SPELLING1_QUESTIONS = [
("Which word is spelled incorrectly? “The local county's superior players dominated the tennis tornament.”", "mc", "county's", "superior", "dominated", "tornament", None, "tornament", "Correct spelling: 'tournament'.", 1),
("Which word is spelled incorrectly? “I recieved an elaborate invitation to an exclusive party next week.”", "mc", "recieved", "elaborate", "exclusive", "party", None, "recieved", "Correct spelling: 'received' (i before e except after c).", 1),
("Which word is spelled incorrectly? “The telephone company persued the customers that did not pay.”", "mc", "telephone", "persued", "customers", "pay", None, "persued", "Correct spelling: 'pursued'.", 1),
("Which word is spelled incorrectly? “Oli asked his mum for permision to attend the charity concert.”", "mc", "asked", "permision", "attend", "charity", None, "permision", "Correct spelling: 'permission'.", 1),
("Is there a spelling mistake in this sentence? “Julia regretted postponing her annual expedition to Norway.”", "mc", "regretted", "postponing", "annual", "No mistake — all words are spelled correctly", None, "No mistake — all words are spelled correctly", "Every word in this sentence is spelled correctly.", 2),
("Which word is spelled incorrectly? “Attendance at the secret meeting was compulsery and critical.”", "mc", "Attendance", "secret", "compulsery", "critical", None, "compulsery", "Correct spelling: 'compulsory'.", 2),
("Which word is spelled incorrectly? “Ezra's adorable new puppy was obedient but also enthusiastic and playfull.”", "mc", "adorable", "obedient", "enthusiastic", "playfull", None, "playfull", "Correct spelling: 'playful' (one L).", 1),
("Which word is spelled incorrectly? “Sam enjoyed climing mountains and spending time in the countryside.”", "mc", "enjoyed", "climing", "spending", "countryside", None, "climing", "Correct spelling: 'climbing' (don't forget the silent B).", 1),
("Which word is spelled incorrectly? “Consistant hard work has contributed to significant improvements.”", "mc", "Consistant", "contributed", "significant", "improvements", None, "Consistant", "Correct spelling: 'consistent'.", 2),
]

# ─────────────────────────────────────────────────────────────
# PAPER 1 — Punctuation Exercise: Hippos
# ─────────────────────────────────────────────────────────────
HIPPOS_LESSON = """
<div class="lesson-block">
<h3>❗ Punctuation Exercise: Hippos</h3>
<p><em>Original passage:</em></p>
<p>Mention the word hippo and you will probably think of a cute but robust animal. But how accurate is this? Hippos look like they have tough skin when, in fact, their skin is highly sensitive and susceptible to burn in the sun. Hippo sweat even has special properties to protect the skin from the sun's harmful rays. The same fluid, red in colour, also moisturises and serves as an antibiotic. Imagine using hippo sweat as a cosmetic or a medicine! It's true that hippos are omnivores, but don't let yourself be fooled: they are not gentle creatures and can be quite dangerous, especially given the speed they can run (up to 30 kilometres per hour). Hippos typically do their running at night whilst hunting for food. During the day, they stay in the water.</p>
<p>In the real exam, each line has an underlined A/B/C/D section and you find which one has a punctuation mistake, or mark N for no mistake. Here, each question asks you to diagnose the error directly.</p>
</div>
<p style="margin-top:12px;color:rgba(255,255,255,0.4);font-size:12px;">Source: GL Assessment English Familiarisation Paper 1 (2017)</p>
"""

HIPPOS_QUESTIONS = [
("What is wrong with this sentence? “Mention the word hippo and you will probably think of a cute but robust animal”", "mc", "A comma is missing after 'hippo'", "An apostrophe is missing", "The sentence needs a question mark", "The sentence is missing its closing full stop", None, "The sentence is missing its closing full stop", "The sentence should end with a full stop.", 1),
("What is wrong with this sentence? “But how accurate is this.”", "mc", "This should end with a question mark, not a full stop", "A comma is needed after 'But'", "An apostrophe is missing from 'this'", "No mistake — correctly punctuated", None, "This should end with a question mark, not a full stop", "It's a question, so it needs a question mark: 'But how accurate is this?'", 1),
("Is there a punctuation mistake here? “Hippos look like they have tough skin when, in fact, their skin is highly sensitive and susceptible to burn in the sun.”", "mc", "A comma is missing before 'when'", "The apostrophe in 'their' is misused", "A semicolon is needed instead of the comma after 'skin'", "No mistake — correctly punctuated", None, "No mistake — correctly punctuated", "This sentence is correctly punctuated as it stands.", 2),
("What is wrong with this sentence? “Hippo sweat even has special properties to protect the skin from the suns harmful rays.”", "mc", "'Suns' needs an apostrophe: sun's harmful rays", "A comma is needed after 'properties'", "'Harmful' should be capitalised", "No mistake — correctly punctuated", None, "'Suns' needs an apostrophe: sun's harmful rays", "'Suns' is possessive here (the rays belonging to the sun), so it needs an apostrophe.", 2),
("What is wrong with this sentence? “The same fluid, red in colour also moisturises and serves as an antibiotic.”", "mc", "A comma is missing after 'colour'", "An apostrophe is missing from 'fluid'", "The exclamation mark is missing", "No mistake — correctly punctuated", None, "A comma is missing after 'colour'", "The phrase 'red in colour' needs a comma on both sides.", 3),
("What is wrong with this sentence? “Its true that hippos are omnivores.”", "mc", "'Its' should be 'It's' (short for 'it is')", "A comma is needed after 'true'", "The full stop should be a question mark", "No mistake — correctly punctuated", None, "'Its' should be 'It's' (short for 'it is')", "'It's' is the contraction of 'it is'; 'its' (no apostrophe) shows possession.", 1),
("What is wrong with this sentence? “...but don't let yourself be fooled they are not gentle creatures and can be quite dangerous...”", "mc", "A semicolon or colon is missing after 'fooled'", "'Yourself' should be 'yourselves'", "A question mark is needed at the end", "No mistake — correctly punctuated", None, "A semicolon or colon is missing after 'fooled'", "Two separate ideas are joined with no punctuation — a colon or semicolon is needed after 'fooled'.", 3),
("What is wrong with this sentence? “...especially given the speed they can run (up to 30 kilometres per hour.”", "mc", "The opening bracket is missing", "The closing bracket ')' is missing", "A comma is needed instead of the bracket", "No mistake — correctly punctuated", None, "The closing bracket ')' is missing", "The bracket that opened before '(up to 30 kilometres' is never closed.", 1),
("Is there a punctuation mistake here? “Hippos typically do their running at night whilst hunting for food. During the day, they stay in the water.”", "mc", "A comma is missing after 'night'", "'Their' should be 'there'", "The full stop after 'food' should be a comma", "No mistake — correctly punctuated", None, "No mistake — correctly punctuated", "This is correctly punctuated as it stands.", 2),
]

# ─────────────────────────────────────────────────────────────
# PAPER 1 — Cloze Passage: Performance Time
# ─────────────────────────────────────────────────────────────
PERFORMANCE_LESSON = """
<div class="lesson-block">
<h3>🎭 Cloze Passage: Performance Time</h3>
<p>Choose the best word or group of words to complete each numbered gap so the passage makes sense and is written in correct English.</p>
<p><em>Waiting in the wings, the students' nerves soared as they listened to the ___(1)___ whispers from the audience. All of ___(2)___ friends and family had come to see them perform in the end-of-year show. But what they were about to see was not what you ___(3)___ a normal show. Whilst the curtain was still down, Jamie and Farooq heaved the three boxes into the centre of the stage. One of the boxes ___(4)___ slightly so they hastily slammed it shut. The noise from the audience was getting ___(5)___. &ldquo;Who ___(6)___ their goggles?&rdquo; asked their teacher in an urgent whisper. Sara rushed forward to grab them and almost tripped on the ropes ___(7)___ three of the students were harnessed. ___(8)___ the teacher nodded, the three students rose into the air and the curtain lifted.</em></p>
</div>
<p style="margin-top:12px;color:rgba(255,255,255,0.4);font-size:12px;">Source: GL Assessment English Familiarisation Paper 1 (2017)</p>
"""

PERFORMANCE_QUESTIONS = [
("Waiting in the wings, the students' nerves soared as they listened to the ___ whispers from the audience.", "mc", "excitement", "excite", "exciting", "excited", "excites", "excited", "'Excited whispers' describes the whispers full of excitement.", 1),
("All of ___ friends and family had come to see them perform in the end-of-year show.", "mc", "there", "they're", "their", "those", "them", "their", "Possessive 'their' (belonging to the students) is needed.", 1),
("But what they were about to see was not what you ___ a normal show.", "mc", "considered", "would consider", "are considering", "considering", "wouldn't consider", "would consider", "'Would consider' fits the conditional sense of the sentence.", 2),
("One of the boxes ___ slightly so they hastily slammed it shut.", "mc", "will open", "was opened", "would open", "won't open", "had opened", "had opened", "Past perfect 'had opened' fits the sequence of past events.", 3),
("The noise from the audience was getting ___.", "mc", "louder", "loud", "loudest", "increased", "increasing", "louder", "The comparative 'louder' fits after 'getting'.", 1),
("“Who ___ their goggles?” asked their teacher in an urgent whisper.", "mc", "has missed", "misses", "is missing", "will miss", "does miss", "is missing", "Present continuous 'is missing' fits someone currently lacking their goggles.", 2),
("Sara rushed forward to grab them and almost tripped on the ropes ___ three of the students were harnessed.", "mc", "next to", "to which", "onto", "in between", "from", "to which", "'To which' correctly links back to 'the ropes'.", 3),
("___ the teacher nodded, the three students rose into the air and the curtain lifted.", "mc", "As", "Because", "Although", "Before", "Even as", "As", "'As' shows the two actions happening at the same time.", 2),
]

# ─────────────────────────────────────────────────────────────
# PAPER 2 — Reading Comprehension: The Secret Garden
# ─────────────────────────────────────────────────────────────
SECRET_GARDEN_LESSON = """
<div class="lesson-block">
<h3>📖 Passage: The Secret Garden (by Frances Hodgson Burnett)</h3>
<p><em>While walking in the garden Mary watched a robin and, after following it, discovered a key on the ground.</em></p>
<p>She looked at the key quite a long time. She turned it over and over, and thought about it. All she thought about the key was that if it was the key to the closed garden, and she could find out where the door was, she could perhaps open it and see what was inside the walls, and what had happened to the old rose-trees. It was because it had been shut up so long that she wanted to see it. It seemed as if it must be different from other places and that something strange must have happened to it during ten years. Besides that, if she liked it she could go into it every day and shut the door behind her, and she could make up some play of her own and play it quite alone, because nobody would ever know where she was, but would think the door was still locked and the key buried in the earth. The thought of that pleased her very much.</p>
<p>Living in a house with a hundred mysteriously closed rooms and having nothing whatever to do to amuse herself, had set her inactive brain to working and was actually awakening her imagination.</p>
<p>She put the key in her pocket and walked up and down her path. No one but herself ever seemed to come there, so she could walk slowly and look at the wall, or, rather, at the ivy growing on it. The ivy was the baffling thing. Howsoever carefully she looked she could see nothing but thickly growing, glossy, dark green leaves. She was very much disappointed as she paced the path and looked over it at the tree-tops inside. It seemed so silly, she said to herself, to be near it and not be able to get in. She took the key in her pocket when she went back to the house, and she made up her mind that she would always carry it with her when she went out, so that if she ever should find the hidden door she would be ready.</p>
<p>The skipping-rope was a wonderful thing. The sun was shining and a little wind was blowing &ndash; not a rough wind, but one which came in delightful little gusts and brought a fresh scent of newly turned earth with it.</p>
<p>Mary skipped round all the gardens and round the orchard, resting every few minutes. At length she went to her own special path and made up her mind to try if she could skip the whole length of it. It was a good long skip and she began slowly, but before she had gone half-way down the path she was so hot and breathless that she was obliged to stop. She did not mind much, because she had already counted up to thirty. She stopped with a little laugh of pleasure, and there, lo and behold, was the robin swaying on a long branch of ivy. He had followed her and he greeted her with a chirp. As Mary had skipped toward him she felt something heavy in her pocket strike against her at each jump, and when she saw the robin she laughed again.</p>
<p>&lsquo;You showed me where the key was yesterday,&rsquo; she said. &lsquo;You ought to show me the door today; but I don't believe you know!&rsquo;</p>
<p>The robin flew from his swinging spray of ivy on to the top of the wall and he opened his beak and sang a loud, lovely trill, merely to show off. Nothing in the world is quite as adorably lovely as a robin when he shows off &ndash; and they are nearly always doing it.</p>
<p>One of the nice little gusts of wind rushed down the path, and it was a stronger one than the rest. It was strong enough to wave the branches of the trees, and it was more than strong enough to sway the trailing sprays of untrimmed ivy hanging from the wall. Mary had stepped close to the robin, and suddenly the gust of wind swung aside some loose ivy trails, and more suddenly still she jumped toward it and caught it in her hand. This she did because she had seen something under it &ndash; a round knob which had been covered by the leaves hanging over it. It was the knob of a door.</p>
<p>She put her hands under the leaves and began to pull and push them aside. Thick as the ivy hung, it nearly all was a loose and swinging curtain, though some had crept over wood and iron. Mary's heart began to thump and her hands to shake a little in her delight and excitement. The robin kept singing and twittering away and tilting his head on one side, as if he were as excited as she was. What was this under her hands which was square and made of iron and which her fingers found a hole in?</p>
<p>It was the lock of the door which had been closed ten years and she put her hand in her pocket, drew out the key and found it fitted the keyhole. She put the key in and turned it. It took two hands to do it, but it did turn.</p>
<p>And then she took a long breath and looked behind her up the long path to see if anyone was coming. No one was coming. No one ever did come, it seemed, and she took another long breath, because she could not help it, and she held back the swinging curtain of ivy and pushed back the door which opened slowly &ndash; slowly.</p>
<p>Then she slipped through it, and shut it behind her, and stood with her back against it, looking about her and breathing quite fast with excitement, and wonder, and delight.</p>
<p>She was standing inside the secret garden.</p>
</div>
<p style="margin-top:12px;color:rgba(255,255,255,0.4);font-size:12px;">Source: GL Assessment English Familiarisation Paper 2 (2017)</p>
"""

SECRET_GARDEN_QUESTIONS = [
("For how many years had the secret garden been locked?", "mc", "seven", "eight", "nine", "ten", "eleven", "ten", "'It was the lock of the door which had been closed ten years.'", 1),
("Which of the following facts do we know about the secret garden from the passage?", "mc", "It receives a lot of sunlight.", "There is lots of space for playing.", "There is a pond.", "There are trees inside.", "There is a gardener.", "There are trees inside.", "Mary '...looked over it at the tree-tops inside.'", 2),
("What word best describes Mary as she 'turned it [the key] over and over'?", "mc", "regretful", "frustrated", "pensive", "frightened", "ecstatic", "pensive", "'She turned it over and over, and thought about it' — thoughtful/pensive.", 2),
("What made Mary especially keen to see the secret garden?", "mc", "It had been inaccessible for so long.", "People had been saying how beautiful it was inside.", "She could see a bit of it through the wall and it looked very tempting.", "She was bored of playing in the rest of the garden.", "Her parents had encouraged her to play outside.", "It had been inaccessible for so long.", "'It was because it had been shut up so long that she wanted to see it.'", 1),
("Mary was keen to keep the garden a secret even if she found the entrance. Why?", "mc", "Mary didn't like spending time with other people.", "People had warned her that she shouldn't go into the garden.", "Mary wanted to play by herself.", "Mary found it thrilling to keep secrets.", "Mary had promised a friend that she would keep it a secret.", "Mary wanted to play by herself.", "'She could make up some play of her own and play it quite alone.'", 2),
("What did Mary plan to do in the secret garden?", "mc", "play with her skipping rope", "invite her friends over to play", "tend to the plants", "read her books", "play her own games", "play her own games", "'She could make up some play of her own and play it quite alone.'", 2),
("According to the first paragraph, where had the key been hidden? (line 9)", "mc", "on the wall", "next to a flower pot", "in the earth", "in a bird's nest", "on the window-sill", "in the earth", "'The key buried in the earth.'", 1),
("According to the passage, what accounted for Mary's particularly strong imagination?", "mc", "Mary had been brought up with no toys.", "Mary had always been a very creative child.", "Mary's school encouraged imaginative activities.", "Mary had nothing to entertain her at home.", "Mary's parents had instilled in Mary a love of imaginative games.", "Mary had nothing to entertain her at home.", "'Having nothing whatever to do to amuse herself... was actually awakening her imagination.'", 2),
("According to the passage, what impression do we get of the house in which Mary lived?", "mc", "It was an inviting place.", "The house contained many secrets.", "The house was an old, dilapidated building.", "The people who lived there were very posh.", "All the neighbours were in awe of the house.", "The house contained many secrets.", "'A house with a hundred mysteriously closed rooms.'", 2),
("Why was it particularly hard to see if there was a door to the garden?", "mc", "The garden walls were covered in thick ivy.", "The garden was so large it was hard to get all the way around it.", "There were trees obscuring the garden walls.", "Mary only ever looked for the door after dark, when no one was around.", "The house towered over the garden so the walls were in shadow.", "The garden walls were covered in thick ivy.", "'She could see nothing but thickly growing, glossy, dark green leaves.'", 1),
("Why did Mary decide to keep the key on her at all times?", "mc", "She didn't trust anyone else to keep it safe.", "She had nowhere to store it in her house.", "She wanted to be able to open the door whenever she found it.", "She often lost things, even if they were important.", "It might get lost amongst the other keys.", "She wanted to be able to open the door whenever she found it.", "'So that if she ever should find the hidden door she would be ready.'", 2),
("What best describes the wind that blew along the path?", "mc", "gentle gust", "strong wind", "stiff breeze", "gale-force", "high wind", "gentle gust", "'Not a rough wind, but one which came in delightful little gusts.'", 1),
("What else did Mary skip around other than the gardens?", "mc", "the old rose trees", "the summerhouse", "the stables", "the orchard", "the boating lake", "the orchard", "'Mary skipped round all the gardens and round the orchard.'", 1),
("What challenge did Mary set herself as she played in the gardens?", "mc", "Mary decided to run from one side to the other.", "Mary wanted to skip all the way down the path.", "Mary aimed to do more than thirty skips.", "Mary aimed to exercise for thirty minutes without getting out of breath.", "Mary wanted to run up and down the path to find her friend, the robin.", "Mary wanted to skip all the way down the path.", "'She made up her mind to try if she could skip the whole length of it.'", 2),
("What happened just before Mary's discovery of the key AND the hidden door?", "mc", "Mary came across the robin.", "Mary played with her skipping rope.", "The winds increased.", "Mary felt breathless.", "Mary started laughing.", "Mary came across the robin.", "The robin led her to both discoveries in the passage.", 2),
("Which of the following quotations from the passage suggests that the gardens in which Mary played were neglected?", "mc", "“thickly growing, glossy, dark green leaves” (line 17)", "“fresh scent of newly turned earth” (line 25)", "“skipped round all the gardens and round the orchard” (line 26)", "“the robin swaying on a long branch of ivy” (line 31)", "“trailing sprays of untrimmed ivy” (line 42)", "“trailing sprays of untrimmed ivy” (line 42)", "'Untrimmed' shows the garden has not been cared for.", 3),
("What was the significance of the wind in the story?", "mc", "The wind filled the silence.", "The wind stopped Mary doing what she wanted to do.", "The wind brushed aside the earth to uncover the key.", "The wind propelled the robin to Mary.", "The wind blew the ivy to reveal the doorknob.", "The wind blew the ivy to reveal the doorknob.", "'The gust of wind swung aside some loose ivy trails' revealing the knob.", 2),
("What metaphor is used when describing the ivy?", "mc", "It is a curtain.", "It is thick.", "It is untrimmed hair.", "It is like a swing.", "It is glossy.", "It is a curtain.", "'The swinging curtain of ivy' is a metaphor.", 2),
("What suggests that the robin was as excited as Mary at finding the door to the garden?", "mc", "The robin was silent as Mary uncovered the door.", "The robin flew around frantically.", "The robin made lots of noise.", "The robin started pecking at the doorknob.", "The robin came and sat on Mary's shoulder.", "The robin made lots of noise.", "'The robin kept singing and twittering away... as if he were as excited as she was.'", 2),
("Why is “no one” repeated in line 57?", "mc", "The author couldn't think of anything else to write.", "Repetition can build suspense.", "Mary's actions were repetitive.", "Mary was feeling lonely at that moment.", "It reflects Mary's muddled thoughts.", "Repetition can build suspense.", "The repetition builds tension before Mary enters the garden.", 3),
("Why is there an emphasis on Mary's breathing in the last seven lines of the passage?", "mc", "Mary had been skipping a lot and was out of breath.", "The key was very hard to turn so Mary had to breathe deeply to give her strength.", "Mary was being dramatic so she was exaggerating her breathing.", "Mary was breathless with excitement and anticipation.", "Mary was inhaling deeply before calling to her friends.", "Mary was breathless with excitement and anticipation.", "'Breathing quite fast with excitement, and wonder, and delight.'", 2),
("What type of words are the following? mysteriously (line 11), carefully (line 16), thickly (line 17), adorably (line 39)", "mc", "nouns", "verbs", "adjectives", "adverbs", "prepositions", "adverbs", "They all describe how something is/was done.", 1),
("Which of these words is an adjective?", "mc", "swaying (line 31)", "trailing (line 42)", "singing (line 50)", "tilting (line 50)", "standing (line 62)", "trailing (line 42)", "'Trailing sprays' — 'trailing' describes the sprays.", 3),
]

# ─────────────────────────────────────────────────────────────
# PAPER 2 — Punctuation Exercise
# ─────────────────────────────────────────────────────────────
PUNCT2_LESSON = """
<div class="lesson-block">
<h3>❗ Punctuation Exercise</h3>
<p>Each question below is based on a real GL Assessment sentence with a
punctuation error hidden in it. Work out what's wrong — or whether nothing
is wrong at all.</p>
</div>
<p style="margin-top:12px;color:rgba(255,255,255,0.4);font-size:12px;">Source: GL Assessment English Familiarisation Paper 2 (2017)</p>
"""

PUNCT2_QUESTIONS = [
("What is wrong with this sentence? ‘Why don't you play outside today,' suggested Tom's aunt.", "mc", "The comma should be a question mark (it's a question)", "'Tom's' should be 'Toms'", "A comma is needed after 'suggested'", "No mistake — correctly punctuated", None, "The comma should be a question mark (it's a question)", "'Why don't you play outside today?' is a question, so it needs a question mark inside the quotation marks.", 2),
("What is wrong with this sentence? “Even the best, most expensive detergent, couldn't remove the mud stains.”", "mc", "There should be no comma after 'detergent'", "An apostrophe is missing from 'couldnt'", "A comma is needed after 'Even'", "No mistake — correctly punctuated", None, "There should be no comma after 'detergent'", "The comma wrongly separates the subject from its verb 'couldn't'.", 2),
("Is there a punctuation mistake here? “The recipe had two simple stages: finely chop the ingredients and then blend together.”", "mc", "The colon should be a semicolon", "A comma is needed after 'stages'", "'Finely' should be capitalised", "No mistake — correctly punctuated", None, "No mistake — correctly punctuated", "A colon correctly introduces the explanation of the two stages.", 1),
("What is wrong with this sentence? “Caitlin had carelessly lost Asaf's charger (his brand new one)”", "mc", "A comma is needed after 'carelessly'", "'Asaf's' should not have an apostrophe", "The bracket should be a comma", "The sentence is missing its closing full stop", None, "The sentence is missing its closing full stop", "After the closing bracket, the sentence still needs a full stop.", 1),
("What is wrong with this sentence? ‘I'd book first because the restaurant is so popular especially on Fridays.'", "mc", "A comma is missing before 'especially'", "'I'd' should be 'Id'", "An extra apostrophe is needed in 'Fridays'", "No mistake — correctly punctuated", None, "A comma is missing before 'especially'", "'Especially on Fridays' is an added-on phrase and needs a comma before it.", 3),
("What is wrong with this sentence? “Looking through my parents music collection, I was amazed to see so many CDs!”", "mc", "'Parents' needs an apostrophe: parents' music collection", "The exclamation mark should be a full stop", "A comma is needed after 'Looking'", "No mistake — correctly punctuated", None, "'Parents' needs an apostrophe: parents' music collection", "The music collection belongs to the parents, so it needs a possessive apostrophe: 'parents''.", 2),
("What is wrong with this sentence? “If we hadnt seen the road sign, we would have ended up in Wales.”", "mc", "'Hadnt' needs an apostrophe: hadn't", "'Wales' should not be capitalised", "A comma is needed after 'If'", "No mistake — correctly punctuated", None, "'Hadnt' needs an apostrophe: hadn't", "'Hadn't' is the contraction of 'had not'.", 1),
("What is wrong with this sentence? “We were lucky to win tickets to see The Nutcracker this Winter.”", "mc", "'Winter' should not be capitalised", "'The Nutcracker' should not be capitalised", "A comma is needed after 'tickets'", "No mistake — correctly punctuated", None, "'Winter' should not be capitalised", "Seasons like winter, spring, summer and autumn are not proper nouns.", 3),
]

# ─────────────────────────────────────────────────────────────
# PAPER 2 — Spelling Exercise: A Ghostly Encounter
# ─────────────────────────────────────────────────────────────
GHOSTLY_LESSON = """
<div class="lesson-block">
<h3>👻 Spelling Exercise: A Ghostly Encounter</h3>
<p><em>Original passage:</em></p>
<p>There was something different about the school playground today: not the usual lull before exams or anticipation before sports day. This was a one-off, whatever it was. One thing you couldn't fail to notice on entering the school gates was a sea of hats, as far as the eye could see: not the usual peaked caps but wide-brimmed hats with feathers. There were also helmets (not the bicycle kind) and even some crowns. No-one was wearing modern clothes either; the usual sportswear was nowhere in sight. The vast majority of children wore robes, some adorned with jewels and others very plain. You could say it was an attempt by the school to bring the past to life. In spite of their altered appearance, pupils lined up as normal and Class 5B waited for Mr Holterson to take the register. The only difference on this morning, however, was that pupils answered to the name of their chosen person from history.</p>
<p>&lsquo;Cleopatra! Gandhi! Einstein!&hellip; Einstein?' After a slight delay, a mumbled response emerged from the line of pupils. &lsquo;Wow, Johnny, that's a really good impersonation. You even sound German!' &lsquo;That's because I am Albert Einstein.' &lsquo;Very good, Johnny!' the teacher laughed. But Einstein did not laugh and, instead, started to cough: an old-man's cough that couldn't possibly come from a ten-year-old &ndash; could it? Mr Holterson looked worried for a moment, then shepherded the pupils, or rather the phantoms of the past, inside.</p>
</div>
<p style="margin-top:12px;color:rgba(255,255,255,0.4);font-size:12px;">Source: GL Assessment English Familiarisation Paper 2 (2017)</p>
"""

GHOSTLY_QUESTIONS = [
("Which word is spelled incorrectly? “...not the usual lull before exams or antisipation before sports day.”", "mc", "lull", "exams", "antisipation", "sports", None, "antisipation", "Correct spelling: 'anticipation'.", 1),
("Which word is spelled incorrectly? “...a sea of hats, as far as the eye could see: not the usual peeked caps but wide-brimmed hats with feathers.”", "mc", "hats", "peeked", "wide-brimmed", "feathers", None, "peeked", "Correct spelling: 'peaked' caps (a peaked cap has a brim, not to be confused with 'peeked' meaning glanced).", 2),
("Which word is spelled incorrectly? “...the usual sportswear was knowhere in sight.”", "mc", "modern", "sportswear", "knowhere", "sight", None, "knowhere", "Correct spelling: 'nowhere'.", 1),
("Which word is spelled incorrectly? “The vast majority of children wore robes, some adorned with jewels and others very plane.”", "mc", "majority", "adorned", "jewels", "plane", None, "plane", "Correct spelling: 'plain' (meaning simple), not 'plane' (an aircraft or flat surface).", 2),
("Which word is spelled incorrectly? “...to bring the past to life. In spite of their altered appearence, pupils lined up as normal...”", "mc", "attempt", "altered", "appearence", "normal", None, "appearence", "Correct spelling: 'appearance'.", 2),
("Which word is spelled incorrectly? “The only differance on this morning, however, was that pupils answered to the name of their chosen person from history.”", "mc", "differance", "however", "answered", "chosen", None, "differance", "Correct spelling: 'difference'.", 1),
("Is there a spelling mistake in this sentence? “After a slight delay, a mumbled response emerged from the line of pupils.”", "mc", "slight", "mumbled", "response", "No mistake — all words are spelled correctly", None, "No mistake — all words are spelled correctly", "Every word in this sentence is spelled correctly.", 2),
("Which word is spelled incorrectly? “Wow, Johnny, that's a really good impersonatian. You even sound German!”", "mc", "Johnny", "really", "impersonatian", "German", None, "impersonatian", "Correct spelling: 'impersonation'.", 1),
("Which word is spelled incorrectly? “Mr Holterson looked worried for a moment, then sheperded the pupils, or rather the phantoms of the past, inside.”", "mc", "worried", "sheperded", "phantoms", "past", None, "sheperded", "Correct spelling: 'shepherded'.", 2),
]

# ─────────────────────────────────────────────────────────────
# PAPER 2 — Cloze Passage: Caught Out?
# ─────────────────────────────────────────────────────────────
CAUGHT_OUT_LESSON = """
<div class="lesson-block">
<h3>🏏 Cloze Passage: Caught Out?</h3>
<p>Choose the best word or group of words to complete each numbered gap.</p>
<p><em>Ellie launched the ball into the air and watched it for ___(1)___ split-second before racing to first base. It was summer and that meant rounders: a game which not all pupils enjoyed, ___(2)___ of all the green team because they always seemed to lose. Perhaps the other teams had velcro attached to their hands or super-human vision even in bright sunlight ___(3)___ they never failed to pull off miraculous catches and thunderous strikes of the ball. The green team ___(4)___ their previous round of batting feeling disheartened, having only managed to score three-and-a-half rounders compared to the yellow team's six. What they needed now was a moment ___(5)___ inspiration and maybe &ndash; just maybe &ndash; Ellie could provide that.</em></p>
<p><em>&lsquo;Go, Ellie, go &ndash; YES &ndash; you can do it &ndash; all the way!' The encouragement lifted Ellie's spirits as she sprinted from first to second base, hardly ___(6)___ believe that she might get all the way round. The ball ___(7)___ a long time to finally descend but, when it did, the green team's expressions of excitement turned to horror as they spotted the tallest boy in ___(8)___ year standing directly underneath it, watching, waiting. However, the tension soon gave way to laughter: not cruel, mocking laughter but genuine disbelief. As soon as Ellie reached fourth base, she turned and looked to see what was going on. And there it was: a bird with the ball in its beak. &lsquo;Rounder!' the umpire shouted. When the yellow team protested, the umpire simply smiled and said, &lsquo;Well, the bird's not officially on your team, ___(9)___?'</em></p>
</div>
<p style="margin-top:12px;color:rgba(255,255,255,0.4);font-size:12px;">Source: GL Assessment English Familiarisation Paper 2 (2017)</p>
"""

CAUGHT_OUT_QUESTIONS = [
("Ellie launched the ball into the air and watched it for ___ split-second before racing to first base.", "mc", "the", "an", "this", "a", "that", "a", "'A split-second' is the natural indefinite article choice.", 1),
("It was summer and that meant rounders: a game which not all pupils enjoyed, ___ of all the green team because they always seemed to lose.", "mc", "least", "most", "top", "less", "more", "least", "'Least of all' means 'especially not', matching the losing team's dislike of the game.", 2),
("Perhaps the other teams had velcro attached to their hands or super-human vision even in bright sunlight ___ they never failed to pull off miraculous catches and thunderous strikes of the ball.", "mc", "unless", "because", "whereas", "although", "while", "although", "'Although' introduces the contrast between the excuse and the fact.", 3),
("The green team ___ their previous round of batting feeling disheartened, having only managed to score three-and-a-half rounders compared to the yellow team's six.", "mc", "were finishing", "will finish", "finish", "are finishing", "had finished", "had finished", "Past perfect 'had finished' fits since this happened before the current moment.", 3),
("What they needed now was a moment ___ inspiration and maybe – just maybe – Ellie could provide that.", "mc", "to", "at", "of", "with", "in", "of", "'A moment of inspiration' is the natural phrase.", 1),
("The encouragement lifted Ellie's spirits as she sprinted from first to second base, hardly ___ believe that she might get all the way round.", "mc", "dared", "daring", "to dare", "having dared", "without daring", "daring", "'Hardly daring to believe' is the correct idiomatic phrase.", 2),
("The ball ___ a long time to finally descend but, when it did, the green team's expressions of excitement turned to horror...", "mc", "takes", "is taking", "took", "has taken", "will take", "took", "Simple past 'took' matches the rest of the story's past tense.", 3),
("...as they spotted the tallest boy in ___ year standing directly underneath it, watching, waiting.", "mc", "their", "they're", "there", "them", "his", "their", "Possessive 'their' refers back to the boys/pupils' year group.", 1),
("When the yellow team protested, the umpire simply smiled and said, ‘Well, the bird's not officially on your team, ___?'", "mc", "isn't it", "won't it", "will it", "is it", "could it", "is it", "A question tag matching 'the bird's not... is it?' uses 'is it'.", 2),
]

TOPICS = [
    ("English Practice Paper 1 — Reading Comprehension: The Swiss Family Robinson", SWISS_FAMILY_LESSON, SWISS_FAMILY_QUESTIONS),
    ("English Practice Paper 1 — Spelling Exercise", SPELLING1_LESSON, SPELLING1_QUESTIONS),
    ("English Practice Paper 1 — Punctuation Exercise: Hippos", HIPPOS_LESSON, HIPPOS_QUESTIONS),
    ("English Practice Paper 1 — Cloze Passage: Performance Time", PERFORMANCE_LESSON, PERFORMANCE_QUESTIONS),
    ("English Practice Paper 2 — Reading Comprehension: The Secret Garden", SECRET_GARDEN_LESSON, SECRET_GARDEN_QUESTIONS),
    ("English Practice Paper 2 — Punctuation Exercise", PUNCT2_LESSON, PUNCT2_QUESTIONS),
    ("English Practice Paper 2 — Spelling Exercise: A Ghostly Encounter", GHOSTLY_LESSON, GHOSTLY_QUESTIONS),
    ("English Practice Paper 2 — Cloze Passage: Caught Out?", CAUGHT_OUT_LESSON, CAUGHT_OUT_QUESTIONS),
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


def add_previous_exam_english():
    conn = get_db()
    cur = conn.cursor()
    today = date.today().isoformat()

    # Make sure option_e column exists (safe if already present).
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
        print(f"  {title}: +{added} questions ({len(questions)} total)")
        total_questions_added += added

    cur.close()
    conn.close()
    print(f"\nTopics added: {total_topics_added}")
    print(f"Questions added: {total_questions_added}")


if __name__ == "__main__":
    add_previous_exam_english()
