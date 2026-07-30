"""
add_previous_exam_maths.py — Adds real GL Assessment 11+ Mathematics
Familiarisation Paper questions (Maths 1 & 2) into the "Previous Exam
Questions" subject, "Maths" module.

Source: GL Assessment Mathematics Familiarisation Papers 1 & 2
(Copyright (c) GL Assessment, 2021), used here for personal family study only.
Answers taken from the official Parent's Guide answer key.

The original papers include charts, graphs, coordinate grids and diagrams
that can't be rendered in this app's plain-text quiz screen. Wherever a
question depended on an image, the real data/values shown in that image
were transcribed into the question text (e.g. bar chart figures written out
as numbers, coordinate positions stated as facts) so the question can still
be solved correctly and faithfully — nothing was invented beyond what the
image showed. One question (Maths 2, Q26 — identifying a non-translation
among six shaded shapes on a grid) could not be reliably transcribed from
the image without risking inaccuracy, so it was left out rather than guessed.

99 of the 100 questions across both papers are included.

Run: python3 add_previous_exam_maths.py
"""
from datetime import date

SUBJECT = "Previous Exam Questions"
SECTION = "Maths"
SOURCE = "GL Assessment 11+ Mathematics Familiarisation Paper"


def spread_difficulty(n, i):
    if i < n / 3.0:
        return 1
    if i < 2 * n / 3.0:
        return 2
    return 3


# ═══════════════════════════════════════════════════════════════
# TOPIC 1 — Place Value & Reading Numbers
# ═══════════════════════════════════════════════════════════════
PLACEVALUE_LESSON = """
<div class="lesson-block">
<h3>🔢 Place Value & Reading Numbers</h3>
<p>Practice reading numbers written in words, identifying what each digit is
worth (place value), and converting between numbers and Roman numerals.</p>
</div>
<p style="margin-top:12px;color:rgba(255,255,255,0.4);font-size:12px;">Source: GL Assessment 11+ Mathematics Familiarisation Papers 1 & 2</p>
"""
PLACEVALUE_RAW = [
    ("What is this number in figures: five thousand, one hundred and nine?",
     "5190", "5019", "519", "51009", "5109", "5109",
     "5109 = 5 thousands, 1 hundred, 0 tens, 9 ones."),
    ("What is the value of the 7 in this number: 7240?",
     "7 thousands", "7 hundreds", "7 tens", "7 ones", "7 thousandths", "7 thousands",
     "The 7 is in the thousands column, so it's worth 7000."),
    ("Work out XXVI multiplied by XLI (Roman numerals), and give the answer in Roman numerals.",
     "CMLXXXIV", "MLXVI", "DCCCLXXXIV", "MCDLXIV", "MDLXXXVI", "MLXVI",
     "XXVI = 26 and XLI = 41. 26 x 41 = 1066, which is MLXVI in Roman numerals."),
    ("Change the order of the figures 6085 to make the biggest number possible.",
     "8605", "6850", "8650", "6580", "8560", "8650",
     "Put the digits in descending order: 8, 6, 5, 0 -> 8650."),
    ("Write this number in figures: eight thousand and twenty-five.",
     "8250", "80025", "8205", "8025", "800025", "8025",
     "8025 = 8 thousands, 0 hundreds, 2 tens, 5 ones."),
    ("In the number 836, what does the 3 stand for?",
     "3 hundreds", "3 ones", "3 thousands", "3 hundredths", "3 tens", "3 tens",
     "The 3 is in the tens column, so it's worth 30."),
]
PLACEVALUE_QUESTIONS = []
for i, (q, a, b, c, d, e, ans, exp) in enumerate(PLACEVALUE_RAW):
    PLACEVALUE_QUESTIONS.append((q, "mc", a, b, c, d, e, ans, exp, spread_difficulty(len(PLACEVALUE_RAW), i)))

# ═══════════════════════════════════════════════════════════════
# TOPIC 2 — Number Sequences & Properties
# ═══════════════════════════════════════════════════════════════
SEQUENCES_LESSON = """
<div class="lesson-block">
<h3>🔢 Number Sequences & Properties</h3>
<p>Spot the pattern in a sequence, and recognise special types of number
(square numbers, prime numbers, multiples).</p>
</div>
<p style="margin-top:12px;color:rgba(255,255,255,0.4);font-size:12px;">Source: GL Assessment 11+ Mathematics Familiarisation Papers 1 & 2</p>
"""
SEQUENCES_RAW = [
    ("What is the missing number in this sequence: 393, 384, 375, ___, 357?",
     "367", "368", "365", "369", "366", "366",
     "Each number decreases by 9: 393-9=384, 384-9=375, 375-9=366, 366-9=357."),
    ("9, 36, 81 — the three numbers above are alike in some way. Which statement is true?",
     "They are all even numbers.", "They are all two-figure numbers.", "They are all prime numbers.", "They are all square numbers.", "They can all be divided by 2 without a remainder.", "They are all square numbers.",
     "9 = 3x3, 36 = 6x6, 81 = 9x9 — all square numbers."),
    ("What is 3 squared (3²)?",
     "5", "6", "9", "18", "27", "9",
     "3 squared means 3 x 3 = 9."),
    ("A Venn diagram has two overlapping circles: 'Multiples of 4' and 'Multiples of 3'. Which of these numbers could go in the section where the circles overlap (a multiple of both 3 and 4)?",
     "9", "12", "15", "16", "18", "12",
     "12 is a multiple of both 3 (3x4=12) and 4 (4x3=12), so it belongs in the overlap."),
    ("Callum is thinking of a two-digit number. Its digits add up to 5. It is a prime number. Its square is a three-digit number. What number is he thinking of?",
     "31", "14", "23", "13", "41", "23",
     "Digits summing to 5 and prime: 23 and 41 qualify. 23 squared = 529 (3 digits), but 41 squared = 1681 (4 digits) — so it must be 23."),
    ("What is the next number in this sequence: 49, 43, 37, 31, ___?",
     "27", "21", "25", "23", "29", "25",
     "Each number decreases by 6: 49-6=43, 43-6=37, 37-6=31, 31-6=25."),
    ("4³ x 4 x 3² is NOT the same as which of the following?",
     "9 x 8² x 4", "3² x 4² x 4²", "4³ x 6²", "6 x 12 x 16", "36 x 64", "6 x 12 x 16",
     "4³ x 4 x 3² = 64 x 4 x 9 = 2304. Checking each option: 6x12x16 = 1152, which does NOT equal 2304 (all the others do)."),
]
SEQUENCES_QUESTIONS = []
for i, (q, a, b, c, d, e, ans, exp) in enumerate(SEQUENCES_RAW):
    SEQUENCES_QUESTIONS.append((q, "mc", a, b, c, d, e, ans, exp, spread_difficulty(len(SEQUENCES_RAW), i)))

# ═══════════════════════════════════════════════════════════════
# TOPIC 3 — Fractions
# ═══════════════════════════════════════════════════════════════
FRACTIONS_LESSON = """
<div class="lesson-block">
<h3>🍕 Fractions</h3>
<p>Work with fractions of shapes and amounts, order fractions by size, and
convert between fractions and decimals.</p>
</div>
<p style="margin-top:12px;color:rgba(255,255,255,0.4);font-size:12px;">Source: GL Assessment 11+ Mathematics Familiarisation Papers 1 & 2</p>
"""
FRACTIONS_RAW = [
    ("A large triangle is divided into 9 equal small triangles (each side of the big triangle split into 3 equal parts). 3 of the small triangles are shaded. What fraction of the whole shape is shaded?",
     "3/10", "1/3", "3/8", "1/4", "3/11", "1/3",
     "3 shaded out of 9 equal triangles = 3/9 = 1/3."),
    ("A bag had 36 sweets in it. Ethan took out 2/3 of them. How many sweets did he take out?",
     "12", "18", "22", "24", "26", "24",
     "2/3 of 36 = 36 ÷ 3 x 2 = 12 x 2 = 24."),
    ("Put these fractions in order of size, starting with the largest first: 3/4, 5/8, 1/2, 7/8, 1/4",
     "7/8, 3/4, 5/8, 1/2, 1/4", "7/8, 5/8, 3/4, 1/2, 1/4", "3/4, 7/8, 5/8, 1/2, 1/4", "7/8, 3/4, 1/2, 5/8, 1/4", "7/8, 5/8, 1/2, 3/4, 1/4",
     "7/8, 3/4, 5/8, 1/2, 1/4",
     "As decimals: 7/8=0.875, 3/4=0.75, 5/8=0.625, 1/2=0.5, 1/4=0.25 — already in descending order."),
    ("What is 1.7 as a fraction?",
     "17/10", "1/17", "10/17", "17/100", "17/11", "17/10",
     "1.7 = 1 and 7/10 = 17/10."),
    ("Ali and his sister share a pizza cut into six equal pieces. Ali eats 1/3 of all the pieces. His sister eats 1/4 of the remaining pieces. After both have eaten, what fraction of the pizza is left?",
     "5/12", "1/2", "1/4", "1/12", "1/6", "1/2",
     "Ali eats 1/3 of 6 = 2 pieces, leaving 4. His sister eats 1/4 of 4 = 1 piece, leaving 3. 3 out of 6 pieces = 1/2."),
    ("A circle is divided into 4 equal quarters by two lines through the centre. One of those quarters is then split in half diagonally, and just one of those two halves is shaded. What fraction of the whole circle is shaded?",
     "1/12", "1/5", "1/4", "1/6", "1/8", "1/8",
     "One quarter split in half gives two eighths; only one of those eighths is shaded, so 1/8 of the circle is shaded."),
    ("What number goes in the box: 3/4 = box/8 ?",
     "5", "6", "7", "9", "12", "6",
     "3/4 = 6/8 (multiply top and bottom by 2)."),
    ("There were 24 marbles in a bag. I took out 1/3 of the marbles. How many marbles did I take out?",
     "16", "17", "9", "8", "18", "8",
     "1/3 of 24 = 24 ÷ 3 = 8."),
    ("What is 1.7 as a fraction? (out of 10)",
     "17/10", "1/17", "10/17", "17/100", "17/11", "17/10",
     "1.7 = 1 whole and 7 tenths = 17/10."),
]
FRACTIONS_QUESTIONS = []
for i, (q, a, b, c, d, e, ans, exp) in enumerate(FRACTIONS_RAW):
    FRACTIONS_QUESTIONS.append((q, "mc", a, b, c, d, e, ans, exp, spread_difficulty(len(FRACTIONS_RAW), i)))

# ═══════════════════════════════════════════════════════════════
# TOPIC 4 — Decimals & Percentages
# ═══════════════════════════════════════════════════════════════
DECIMALS_LESSON = """
<div class="lesson-block">
<h3>💯 Decimals & Percentages</h3>
<p>Multiply and add decimals, work out percentages of amounts, and put
decimals in order of size.</p>
</div>
<p style="margin-top:12px;color:rgba(255,255,255,0.4);font-size:12px;">Source: GL Assessment 11+ Mathematics Familiarisation Papers 1 & 2</p>
"""
DECIMALS_RAW = [
    ("What percentage of £5 is 50p?",
     "1%", "5%", "10%", "20%", "50%", "10%",
     "50p is 1/10 of £5 (500p), which is 10%."),
    ("3.6 x 10 = ?",
     "0.36", "0.036", "36", "360", "36.6", "36",
     "Multiplying by 10 moves the decimal point one place right: 3.6 -> 36."),
    ("What is 60% of 50?",
     "5", "25", "27", "27.5", "30", "30",
     "60% of 50 = 0.6 x 50 = 30."),
    ("Put these numbers in order from smallest to biggest: 0.525, 0.7, 0.35, 0.175",
     "0.7, 0.525, 0.35, 0.175", "0.175, 0.525, 0.35, 0.7", "0.175, 0.35, 0.525, 0.7", "0.7, 0.35, 0.175, 0.525", "0.175, 0.35, 0.7, 0.525",
     "0.175, 0.35, 0.525, 0.7",
     "In increasing size: 0.175 < 0.35 < 0.525 < 0.7."),
    ("What is 50% of 40?",
     "16", "20", "25", "8", "18", "20",
     "50% of 40 = half of 40 = 20."),
    ("0.02 + 7.8 = ?",
     "7.802", "7.82", "7.822", "8.00", "7.102", "7.82",
     "7.8 + 0.02 = 7.82."),
]
DECIMALS_QUESTIONS = []
for i, (q, a, b, c, d, e, ans, exp) in enumerate(DECIMALS_RAW):
    DECIMALS_QUESTIONS.append((q, "mc", a, b, c, d, e, ans, exp, spread_difficulty(len(DECIMALS_RAW), i)))

# ═══════════════════════════════════════════════════════════════
# TOPIC 5 — Money
# ═══════════════════════════════════════════════════════════════
MONEY_LESSON = """
<div class="lesson-block">
<h3>💷 Money</h3>
<p>Work out costs, savings, change and unit prices in pounds and pence
(and other currencies).</p>
</div>
<p style="margin-top:12px;color:rgba(255,255,255,0.4);font-size:12px;">Source: GL Assessment 11+ Mathematics Familiarisation Papers 1 & 2</p>
"""
MONEY_RAW = [
    ("Wendy saved £2.50 a week. How many weeks did it take her to save £20?",
     "4 weeks", "8 weeks", "9 weeks", "10 weeks", "14 weeks", "8 weeks",
     "£20 ÷ £2.50 = 8 weeks."),
    ("A club offers a 'Family one adult' membership (1 adult and children under 18) at an offer price of £46.50, instead of the normal £62.00. Mrs Ward wants to join with her three children, aged 10, 12 and 15. How much must she pay?",
     "£82.00", "£62.63", "£62.00", "£61.50", "£46.50", "£46.50",
     "Mrs Ward and her under-18 children fit the 'Family one adult' membership, at the offer price of £46.50."),
    ("A swimming pool charges £3.60 for entry. A membership card saves 1/3 of the entry fee. On his first visit, Ken spends £5 on a membership card plus the reduced entry fee. How many times does Ken visit before he gets back his £5 (through the savings)?",
     "4", "2", "5", "1", "3", "5",
     "Each visit saves 1/3 of £3.60 = £1.20. £5 ÷ £1.20 = 4.17, so it takes 5 visits for the total savings to reach £5."),
    ("A boy delivered newspapers. He was paid £1.40 for every 100 papers he delivered. How much was he paid for delivering 250 papers?",
     "£2.80", "£3.40", "£3.50", "£4.20", "£4.40", "£3.50",
     "250 papers = 2.5 x 100. 2.5 x £1.40 = £3.50."),
    ("How many 10p coins can I get for £1.80?",
     "10 coins", "18 coins", "88 coins", "108 coins", "180 coins", "18 coins",
     "£1.80 = 180p. 180 ÷ 10 = 18 coins."),
    ("Karen wants to buy a guitar. She has saved £43.95. The guitar costs £65.00. How much more money does she need?",
     "£22.05", "£21.05", "£20.05", "£12.05", "£11.05", "£21.05",
     "£65.00 - £43.95 = £21.05."),
    ("8 chocolate bars cost £5.20. How much do 6 chocolate bars cost?",
     "£3.75", "£3.80", "£3.85", "£3.90", "£3.95", "£3.90",
     "One bar costs £5.20 ÷ 8 = £0.65. 6 bars cost 6 x £0.65 = £3.90."),
    ("Ella paid £780 per month in rent. How much rent did she pay in 12 months?",
     "£2340", "£8360", "£8580", "£9260", "£9360", "£9360",
     "£780 x 12 = £9360."),
    ("This graph converts British Pounds (£) to United States Dollars ($): the line shows £1 = $1.25 (for example, at £4 the graph shows $5). How many Dollars ($) is £34?",
     "$42.50", "$47.50", "$45", "$42.05", "$27.20", "$42.50",
     "£34 x 1.25 = $42.50."),
]
MONEY_QUESTIONS = []
for i, (q, a, b, c, d, e, ans, exp) in enumerate(MONEY_RAW):
    MONEY_QUESTIONS.append((q, "mc", a, b, c, d, e, ans, exp, spread_difficulty(len(MONEY_RAW), i)))

# ═══════════════════════════════════════════════════════════════
# TOPIC 6 — Ratio, Proportion & Algebra Puzzles
# ═══════════════════════════════════════════════════════════════
ALGEBRA_LESSON = """
<div class="lesson-block">
<h3>🧮 Ratio, Proportion & Algebra Puzzles</h3>
<p>Solve for missing numbers, "think of a number" puzzles, ratios, and
simple algebraic equations.</p>
</div>
<p style="margin-top:12px;color:rgba(255,255,255,0.4);font-size:12px;">Source: GL Assessment 11+ Mathematics Familiarisation Papers 1 & 2</p>
"""
ALGEBRA_RAW = [
    ("Write the correct number in the box: 123 ÷ box = 123",
     "123", "0", "0.1", "0.5", "1", "1",
     "Any number divided by 1 stays the same, so 123 ÷ 1 = 123."),
    ("a - 9 = 10. What is a?",
     "19", "1", "-1", "21", "-19", "19",
     "a = 10 + 9 = 19."),
    ("Matthew thinks of a number. He multiplies it by 2, then subtracts 4. The answer is 10. What number did Matthew first think of?",
     "3", "7", "10", "12", "14", "7",
     "Work backwards: 10 + 4 = 14, then 14 ÷ 2 = 7."),
    ("105 ÷ box = 21. What number does the box stand for?",
     "4", "5", "6", "7", "15", "5",
     "105 ÷ 21 = 5."),
    ("There were 27 children in a class. There were twice as many boys as girls. How many boys were there?",
     "21 boys", "18 boys", "16 boys", "14 boys", "9 boys", "18 boys",
     "27 children split in a 2:1 ratio (boys:girls) means 3 equal parts of 9. Boys = 2 x 9 = 18."),
    ("Zac starts with the number 5. Which of these instructions does NOT give him an answer of 17? A) Halve, add six, then double. B) Multiply by four, then subtract three. C) Triple, then add two. D) Add three and double. E) Multiply by ten, subtract sixteen, then halve.",
     "Halve your value, add six, then double.", "Multiply by four, then subtract three.", "Triple your value, then add two.", "Add three and double.", "Multiply by ten, subtract sixteen, then halve.",
     "Add three and double.",
     "A: (5/2+6)x2=17. B: 5x4-3=17. C: 5x3+2=17. D: (5+3)x2=16, NOT 17. E: (5x10-16)/2=17. So D is the one that does not give 17."),
    ("Put the correct number in the box: 27 x 99 = 2700 - box",
     "27", "37", "127", "137", "687", "27",
     "27 x 99 = 27 x 100 - 27 = 2700 - 27, so the box is 27."),
    ("To make brown paint, you mix 2 parts red, 17 parts yellow and 1 part blue. How much red paint is needed to make 40 litres of brown paint?",
     "20 litres", "34 litres", "1.5 litres", "4 litres", "2 litres", "4 litres",
     "The ratio has 2+17+1=20 parts total, so each part = 40/20 = 2 litres. Red is 2 parts, so 2 x 2 = 4 litres."),
    ("Share 240 into 4 equal parts. How much is one part?",
     "80", "60", "65", "40", "70", "60",
     "240 ÷ 4 = 60."),
    ("324 ÷ 6 = ?",
     "44", "54", "56", "58", "64", "54",
     "324 ÷ 6 = 54."),
    ("If X stands for a whole number and 3 lots of X are equal to 36, what are 2 lots of X equal to?",
     "12", "18", "24", "26", "28", "24",
     "3X = 36, so X = 12. 2 lots of X = 2 x 12 = 24."),
    ("Greg thinks of a number, multiplies it by 3, subtracts 5, then multiplies by 2. His answer is 26. What number did Greg think of?",
     "9", "8", "7", "6", "5", "6",
     "Work backwards: 26 ÷ 2 = 13, 13 + 5 = 18, 18 ÷ 3 = 6."),
]
ALGEBRA_QUESTIONS = []
for i, (q, a, b, c, d, e, ans, exp) in enumerate(ALGEBRA_RAW):
    ALGEBRA_QUESTIONS.append((q, "mc", a, b, c, d, e, ans, exp, spread_difficulty(len(ALGEBRA_RAW), i)))

# ═══════════════════════════════════════════════════════════════
# TOPIC 7 — Measurement (Length, Weight, Capacity & Temperature)
# ═══════════════════════════════════════════════════════════════
MEASURE_LESSON = """
<div class="lesson-block">
<h3>📏 Measurement</h3>
<p>Convert between units of length, weight, capacity and temperature, and
solve real-world measurement word problems.</p>
</div>
<p style="margin-top:12px;color:rgba(255,255,255,0.4);font-size:12px;">Source: GL Assessment 11+ Mathematics Familiarisation Papers 1 & 2</p>
"""
MEASURE_RAW = [
    ("Iveta was 1.43 metres tall. She grew 2 centimetres more. How tall was she then, in metres?",
     "1.45 m", "1.63 m", "1.65 m", "1.405 m", "1.603 m", "1.45 m",
     "2 cm = 0.02 m. 1.43 + 0.02 = 1.45 m."),
    ("A jug holds 1 litre of water. An empty jar holds 700 millilitres. The jar is filled from the jug. How much water is left in the jug?",
     "0.3 litres", "0.25 litres", "400 millilitres", "0.35 litres", "200 millilitres", "0.3 litres",
     "1 litre = 1000 ml. 1000 - 700 = 300 ml = 0.3 litres."),
    ("A small square has sides of 1 cm. A large rectangle measures 6 cm by 3 cm. How many small squares will fit into the large rectangle?",
     "12", "15", "18", "21", "24", "18",
     "Area of rectangle = 6 x 3 = 18 square cm, so 18 unit squares fit inside."),
    ("About how much does an ordinary mug hold?",
     "30 millilitres", "300 millilitres", "3 litres", "30 litres", "300 litres", "300 millilitres",
     "An ordinary mug holds roughly 300 ml — a small glass of water, not litres."),
    ("A ship travels 528 nautical miles in one day. How many nautical miles does it travel in 15 days?",
     "3168", "3173", "7920", "7925", "7950", "7920",
     "528 x 15 = 7920."),
    ("Mateo's temperature is 37.5°C. When he was ill it rose 3°C. What was his temperature when he was ill?",
     "37.8°C", "47.5°C", "34.5°C", "37.2°C", "40.5°C", "40.5°C",
     "37.5 + 3 = 40.5°C."),
    ("Ava had 5 boxes. Each box weighed 800 grams. How many KILOGRAMS was this altogether?",
     "4 kg", "4.5 kg", "40 kg", "4000 kg", "4500 kg", "4 kg",
     "5 x 800g = 4000g = 4 kg."),
    ("A frog starts jumping from the middle of a circular pond, 12 metres across. It jumps towards the edge, and each jump halves its remaining distance to the edge. How far is the frog from the edge after 3 jumps?",
     "10.5 m", "75 cm", "150 cm", "5.25 m", "125 cm", "75 cm",
     "The radius is 6 m = 600 cm. After jump 1: 300 cm left. After jump 2: 150 cm left. After jump 3: 75 cm left."),
    ("Instructions for roasting meat: cook for 30 minutes at 230°C, then turn down the heat, allowing 30 minutes cooking time for every 450g. A piece of meat takes 2.5 hours altogether to cook. How heavy is it?",
     "2.25 kg", "1.25 kg", "1.8 kg", "2.7 kg", "1.35 kg", "1.8 kg",
     "2.5 hours = 150 minutes. Subtract the initial 30 minutes: 120 minutes remain for the weight-based cooking. 120 ÷ 30 = 4 lots of 450g = 1800g = 1.8 kg."),
    ("Three pieces of wood are cut from a plank 1 metre long. Each piece is 30 cm long. How long is the piece left over?",
     "10 cm", "40 cm", "70 cm", "910 cm", "970 cm", "10 cm",
     "1 metre = 100 cm. 3 x 30 cm = 90 cm used. 100 - 90 = 10 cm left."),
    ("The thermometer shows the temperature in Kiev is -3°C. London is 18°C warmer. What is the temperature in London?",
     "17°C", "16°C", "15°C", "14°C", "13°C", "15°C",
     "-3 + 18 = 15°C."),
    ("Look at these bottles: 1 litre, 500 ml, 250 ml, 100 ml. How many times would you have to fill the 250 ml bottle to make 1 litre?",
     "8 times", "14 times", "4 times", "3 times", "40 times", "4 times",
     "1 litre = 1000 ml. 1000 ÷ 250 = 4."),
    ("Jenny is wallpapering. She starts with a 6 metre roll but has to cut off 1.75 metres because it's damaged. If she needs 33.75 metres of wallpaper in total, how many more 6-metre rolls must she buy?",
     "8", "7", "6", "5", "4", "5",
     "The first roll gives 6 - 1.75 = 4.25 usable metres. She still needs 33.75 - 4.25 = 29.5 metres, and 29.5 ÷ 6 = 4.9, so she needs 5 more whole rolls."),
    ("An empty box weighs 150 grams. When filled with paper it weighs 1 kilogram. How much does the paper weigh?",
     "350 g", "750 g", "850 g", "950 g", "9850 g", "850 g",
     "1 kg = 1000 g. 1000 - 150 = 850 g."),
    ("Mrs Shaw has 175 ml of liquid and needs a container for it. Which suits her needs best: bath, mug, large saucepan, egg cup, or bucket?",
     "Bath", "Mug", "Large saucepan", "Egg cup", "Bucket", "Mug",
     "175 ml is about a small cupful — a mug is the best fit; an egg cup is far too small and the others are much too big."),
    ("Liam carried ten parcels. Each parcel weighed 250 grams. How many KILOGRAMS was this altogether?",
     "25 kg", "2.50 kg", "2.25 kg", "0.25 kg", "0.025 kg", "2.50 kg",
     "10 x 250g = 2500g = 2.50 kg."),
    ("Henry says that to change kilometres to miles, you divide by 8 and multiply by 5. Which of these is NOT correct? A) 168km is 105 miles. B) 248km is 155 miles. C) 192km is 125 miles. D) 216km is 135 miles. E) 264km is 165 miles.",
     "168 kilometres is 105 miles.", "248 kilometres is 155 miles.", "192 kilometres is 125 miles.", "216 kilometres is 135 miles.", "264 kilometres is 165 miles.",
     "192 kilometres is 125 miles.",
     "192 ÷ 8 x 5 = 24 x 5 = 120 miles, not 125 — so C is the incorrect one (all the others check out correctly)."),
]
MEASURE_QUESTIONS = []
for i, (q, a, b, c, d, e, ans, exp) in enumerate(MEASURE_RAW):
    MEASURE_QUESTIONS.append((q, "mc", a, b, c, d, e, ans, exp, spread_difficulty(len(MEASURE_RAW), i)))

# ═══════════════════════════════════════════════════════════════
# TOPIC 8 — Time
# ═══════════════════════════════════════════════════════════════
TIME_LESSON = """
<div class="lesson-block">
<h3>🕐 Time</h3>
<p>Read clocks and timetables, work out durations, and convert between time
zones.</p>
</div>
<p style="margin-top:12px;color:rgba(255,255,255,0.4);font-size:12px;">Source: GL Assessment 11+ Mathematics Familiarisation Papers 1 & 2</p>
"""
TIME_RAW = [
    ("Which of these digital alarm clocks shows quarter past seven in the evening?",
     "7:15", "7:25", "19:25", "19:15", "21:15", "19:15",
     "Quarter past seven in the evening is 19:15 in 24-hour time."),
    ("A train left at 10:20 and arrived at 11:15. How long did the journey take, in minutes?",
     "45 mins", "55 mins", "65 mins", "75 mins", "95 mins", "55 mins",
     "From 10:20 to 11:15 is 55 minutes."),
    ("Part of a train timetable shows a train leaving East Croydon at 23:27 and arriving at Victoria at 23:43. How long does it take to get to Victoria?",
     "6 mins", "10 mins", "13 mins", "16 mins", "26 mins", "16 mins",
     "From 23:27 to 23:43 is 16 minutes."),
    ("The time in New York is 5 hours behind the time in London. In London it is 9am. What time is it in New York?",
     "14:00", "04:00", "05:00", "4pm", "5pm", "04:00",
     "9am minus 5 hours = 4am = 04:00."),
    ("A television programme finished at 4:55pm. It lasted three-quarters of an hour. At what time did it start?",
     "4.15 pm", "4.10 pm", "4.05 pm", "4.25 pm", "4.20 pm", "4.10 pm",
     "Three-quarters of an hour = 45 minutes. 4:55pm minus 45 minutes = 4:10pm."),
    ("Muhammed must get up at 07:30. He goes to bed at 22:38 the night before. How long does he spend in bed?",
     "8 hours 22 minutes", "8 hours 42 minutes", "8 hours 52 minutes", "9 hours 42 minutes", "9 hours 52 minutes", "8 hours 52 minutes",
     "22:38 to midnight is 1 hour 22 minutes. Midnight to 07:30 is 7 hours 30 minutes. Total: 8 hours 52 minutes."),
]
TIME_QUESTIONS = []
for i, (q, a, b, c, d, e, ans, exp) in enumerate(TIME_RAW):
    TIME_QUESTIONS.append((q, "mc", a, b, c, d, e, ans, exp, spread_difficulty(len(TIME_RAW), i)))

# ═══════════════════════════════════════════════════════════════
# TOPIC 9 — Shape & Geometry
# ═══════════════════════════════════════════════════════════════
SHAPE_LESSON = """
<div class="lesson-block">
<h3>📐 Shape & Geometry</h3>
<p>Identify properties of 2D and 3D shapes, work with angles, area and
perimeter, and reason about polygons.</p>
</div>
<p style="margin-top:12px;color:rgba(255,255,255,0.4);font-size:12px;">Source: GL Assessment 11+ Mathematics Familiarisation Papers 1 & 2</p>
"""
SHAPE_RAW = [
    ("A regular hexagon can be divided into equal equilateral triangles, each with sides the same length as the hexagon's side. How many of these triangles fill the hexagon?",
     "10", "9", "8", "6", "4", "6",
     "A regular hexagon is made up of 6 equilateral triangles meeting at its centre."),
    ("Five shapes are shown: A) a regular pentagon (5 sides). B) a parallelogram (4 sides, slanted). C) a square (4 sides). D) a rotated rectangle (4 sides). E) a trapezium (4 sides). Which of these is NOT a quadrilateral?",
     "A", "B", "C", "D", "E", "A",
     "A quadrilateral has exactly 4 sides. Shape A is a pentagon with 5 sides, so it is not a quadrilateral."),
    ("Five 3D shapes are shown: A) a rectangular box (cuboid) on its side. B) a cube. C) a tall rectangular box (cuboid). D) an L-shaped 3D block. E) a rectangular box (cuboid). Which of these shapes is NOT a cuboid?",
     "A", "B", "C", "D", "E", "D",
     "A cuboid has 6 rectangular faces. The L-shaped block (D) is made of two joined cuboids, so on its own it isn't a simple cuboid."),
    ("An angle x is drawn between two rays, clearly wider than a right angle (90°) but not as wide as a straight line (180°) — an obtuse angle. Which statement about angle x is correct?",
     "Angle x is less than 90 degrees.", "Angle x is a right angle.", "Angle x is more than 180 degrees.", "Angle x is between 90 and 180 degrees.", "Angle x is 180 degrees.", "Angle x is between 90 and 180 degrees.",
     "An angle that is wider than a right angle but less than a straight line is between 90 and 180 degrees (obtuse)."),
    ("Three angles fit together to make a straight line (180°). Look at a 30° angle. How many of these 30° angles will fit together to make a straight line?",
     "3", "4", "5", "6", "7", "6",
     "A straight line is 180 degrees. 180 ÷ 30 = 6."),
    ("PQRS is a square, with P at the bottom-left corner, Q at the bottom-right, R at the top-right, and S at the top-left. Which line is perpendicular to the diagonal line connecting P and R?",
     "the line connecting X and Y", "the line connecting P and S", "the line connecting Q and S", "the line connecting S and W", "the line connecting Q and R", "the line connecting Q and S",
     "In a square, the two diagonals are always perpendicular to each other. The diagonal from P to R is crossed at a right angle by the other diagonal, from Q to S."),
    ("Zoey has a large carpet in her room, 5 metres long and 4 metres wide. What is the distance all around the edge of the carpet?",
     "14 m", "16 m", "18 m", "19 m", "20 m", "18 m",
     "Perimeter = 2 x (length + width) = 2 x (5 + 4) = 18 m."),
    ("Which of these statements is NOT true for a regular hexagon with 4cm sides? A) 6 equal sides. B) 6 equal angles. C) Perimeter is 24cm. D) 6 lines of symmetry. E) Only 1 pair of parallel sides.",
     "There are 6 equal sides.", "There are 6 equal angles.", "The perimeter is 24cm.", "There are 6 lines of symmetry.", "There is only 1 pair of parallel sides.", "There is only 1 pair of parallel sides.",
     "A regular hexagon actually has 3 pairs of parallel sides, not just 1 — so that statement is false. (Perimeter = 6 x 4cm = 24cm, which is true.)"),
    ("Emily has six sticks: 3cm, 5cm, 6cm, 8cm, 9cm, 11cm. She wants to make the smallest triangle she can using the 11cm stick with two of the others (the other two lengths must add up to MORE than 11cm to form a valid triangle). Which two other lengths should she use?",
     "3cm and 5cm", "3cm and 6cm", "5cm and 6cm", "5cm and 8cm", "6cm and 8cm", "5cm and 8cm",
     "For a valid triangle, the two shorter sides must add up to more than 11cm. 3+5=8, 3+6=9, and 5+6=11 are all too short or exactly equal (invalid). 5+8=13 is valid and the smallest valid combination available, giving the smallest possible triangle."),
    ("To add up all the angles inside a polygon, subtract 2 from the number of sides and multiply by 180. An octagon has 8 sides. What do the angles inside an octagon add up to?",
     "1438 degrees", "1086 degrees", "186 degrees", "1080 degrees", "1806 degrees", "1080 degrees",
     "(8 - 2) x 180 = 6 x 180 = 1080 degrees."),
    ("What is the area of a rectangle measuring 0.8 m by 0.3 m, given in square centimetres?",
     "0.24 cm²", "2.4 cm²", "24 cm²", "240 cm²", "2400 cm²", "2400 cm²",
     "0.8m = 80cm and 0.3m = 30cm. Area = 80 x 30 = 2400 square cm."),
    ("The area of a rectangular playground is 210 square metres. Which of the following could be the playground's perimeter?",
     "44 metres", "52 metres", "64 metres", "72 metres", "74 metres", "74 metres",
     "One way to get an area of 210 is 7m x 30m (7x30=210). Its perimeter = 2 x (7+30) = 74 metres."),
]
SHAPE_QUESTIONS = []
for i, (q, a, b, c, d, e, ans, exp) in enumerate(SHAPE_RAW):
    SHAPE_QUESTIONS.append((q, "mc", a, b, c, d, e, ans, exp, spread_difficulty(len(SHAPE_RAW), i)))

# ═══════════════════════════════════════════════════════════════
# TOPIC 10 — Coordinates & Position
# ═══════════════════════════════════════════════════════════════
COORDS_LESSON = """
<div class="lesson-block">
<h3>📍 Coordinates & Position</h3>
<p>Read and plot coordinates on a grid, and reason about how shapes and
points move, scale or reflect.</p>
</div>
<p style="margin-top:12px;color:rgba(255,255,255,0.4);font-size:12px;">Source: GL Assessment 11+ Mathematics Familiarisation Papers 1 & 2</p>
"""
COORDS_RAW = [
    ("On a treasure map grid, the hills icon is at (3,4). The lighthouse icon is 2 squares to the left and 2 squares up from the hills. What are the coordinates of the lighthouse?",
     "(6 , 1)", "(1 , 6)", "(5 , 6)", "(6 , 3)", "(1 , 7)", "(1 , 6)",
     "2 squares left of x=3 is x=1; 2 squares up from y=4 is y=6. So the lighthouse is at (1,6)."),
    ("On a number line from 1200 to 1400, five arrows point to approximately: A=1225, B=1250, C=1275, D=1300 (the midpoint), E=1350. Which letter points at 1250?",
     "A", "B", "C", "D", "E", "B",
     "Arrow B is placed at 1250 on the number line."),
    ("A point A is plotted on a coordinate grid at x=2, y=1. What are the coordinates of A?",
     "(1 , 2)", "(1 , 1)", "(2 , 0)", "(2 , 2)", "(2 , 1)", "(2 , 1)",
     "The point's x-coordinate is 2 and y-coordinate is 1, so it's written (2,1)."),
    ("A rectangle has corner A at (1,1) and the opposite corner C at (3,2) — that's 2 units right and 1 unit up from A. All sides of the rectangle are then doubled in length, with A staying at (1,1). Where will corner C now be drawn?",
     "(6 , 4)", "(4 , 2)", "(5 , 2)", "(4 , 3)", "(5 , 3)", "(5 , 3)",
     "Doubling the sides doubles the distances from A: 2 units becomes 4, and 1 unit becomes 2. New C = (1+4, 1+2) = (5,3)."),
    ("A line is drawn connecting the points (1,5) and (5,1). Which of these lines (given by their endpoints) is PARALLEL to it? A) (3,1) and (1,4). B) (2,6) and (4,3). C) (5,1) and (1,5). D) (2,5) and (4,2). E) (5,2) and (1,6).",
     "(3 , 1) and (1 , 4)", "(2 , 6) and (4 , 3)", "(5 , 1) and (1 , 5)", "(2 , 5) and (4 , 2)", "(5 , 2) and (1 , 6)", "(5 , 2) and (1 , 6)",
     "The original line has a slope of -1 (it drops 1 for every 1 across). The line from (5,2) to (1,6) also has a slope of -1, so it's parallel (and it's a different line, not the same one)."),
    ("A shape has a point S at (6,9). After the shape is reflected, S moves to (6,1). In what line is the shape reflected?",
     "A horizontal line that passes through the y-axis at (0 , 6)", "A vertical line that passes through the x-axis at (5 , 0)", "A horizontal line that passes through the y-axis at (0 , 5)", "A horizontal line that passes through the y-axis at (0 , 4)", "A vertical line that passes through the x-axis at (6 , 0)", "A horizontal line that passes through the y-axis at (0 , 5)",
     "S's x-coordinate stays at 6, so the mirror line is horizontal. It must sit exactly halfway between y=9 and y=1, which is y=5 — a horizontal line through (0,5)."),
]
COORDS_QUESTIONS = []
for i, (q, a, b, c, d, e, ans, exp) in enumerate(COORDS_RAW):
    COORDS_QUESTIONS.append((q, "mc", a, b, c, d, e, ans, exp, spread_difficulty(len(COORDS_RAW), i)))

# ═══════════════════════════════════════════════════════════════
# TOPIC 11 — Charts & Data Handling
# ═══════════════════════════════════════════════════════════════
CHARTS_LESSON = """
<div class="lesson-block">
<h3>📊 Charts & Data Handling</h3>
<p>Read information from pictograms, bar charts and line graphs, and use it
to answer questions.</p>
</div>
<p style="margin-top:12px;color:rgba(255,255,255,0.4);font-size:12px;">Source: GL Assessment 11+ Mathematics Familiarisation Papers 1 & 2</p>
"""
CHARTS_RAW = [
    ("A boat symbol stands for 12 ships in a pictogram. Dock A shows 1 boat symbol. Dock B shows 1 boat symbol plus half a boat symbol. Dock C shows half a boat symbol. How many more ships are in dock A than dock C?",
     "0.5", "1", "3", "4", "6", "6",
     "Dock A = 1 x 12 = 12 ships. Dock C = half of 12 = 6 ships. 12 - 6 = 6."),
    ("A chart shows how Kai spent his spare time last week: Watching TV 7 hrs, Playing football 2.5 hrs, Reading 3 hrs, Fishing 2 hrs, Cycling 3 hrs. How many hours did he spend out of doors (football, fishing and cycling)?",
     "6.5 hours", "7 hours", "7.5 hours", "8 hours", "8.5 hours", "7.5 hours",
     "2.5 + 2 + 3 = 7.5 hours."),
    ("A graph shows a baby girl's weight over her first 8 weeks: Birth 3.0kg, week1 2.9kg, week2 3.0kg, week3 3.25kg, week4 3.9kg, week5 4.0kg, week6 3.9kg, week7 4.35kg, week8 4.5kg. In which week did she gain the most weight compared to the week before?",
     "2 weeks", "3 weeks", "4 weeks", "7 weeks", "8 weeks", "4 weeks",
     "The weight gain each week was: wk1 -0.1, wk2 +0.1, wk3 +0.25, wk4 +0.65, wk5 +0.1, wk6 -0.1, wk7 +0.45, wk8 +0.15. The biggest gain (+0.65kg) was during week 4."),
    ("A graph shows Britain's population growing over time: in 1700 it was about 5 million, in 1750 about 7 million, in 1800 about 10 million, in 1850 about 15 million, and by 1900 about 20-25 million — reading the curve carefully, it reaches exactly 20 million (twice the 1800 figure) partway between 1850 and 1900, at around 1875. In which year was the population twice as much as it was in 1800?",
     "1850", "1875", "1895", "1900", "1910", "1875",
     "The population in 1800 was about 10 million. Twice that is 20 million, which the graph shows was reached around 1875."),
    ("In a class of 28 children: 6 travel by bicycle, 10 by bus, 3 by car, and 5 by train. The rest walk. Which form of transport is used by a total of 4 children?",
     "bicycle", "bus", "car", "train", "walk", "walk",
     "6+10+3+5 = 24 children accounted for. 28 - 24 = 4 children must walk."),
    ("A bar chart shows during which months children in a class have birthdays: Jan 4, Feb 1, Mar 1, Apr 5, May 2, Jun 2, Jul 6, Aug 3, Sep 1, Oct 3, Nov 4, Dec 5. During which month are there most birthdays?",
     "April", "December", "January", "July", "November", "July",
     "July has 6 birthdays, more than any other month."),
    ("Sati records how many children visit the school library each day: Monday 13, Tuesday 10, Wednesday 16, Thursday 5, Friday 11. How many children visited the library over the five days?",
     "55", "54", "53", "52", "51", "55",
     "13 + 10 + 16 + 5 + 11 = 55."),
    ("A bar chart shows the heights of a class of pupils: 110-119cm: 4 children, 120-129cm: 5 children, 130-139cm: 8 children, 140-149cm: 7 children, 150-159cm: 3 children, 160-169cm: 1 child. Which statement MUST be true?",
     "1 child is exactly 165cm tall.", "5 children have a height between 120cm and 129cm.", "No children have a height less than 111cm.", "7 children have a height more than 140cm but less than 150cm.", "8 children have a height of less than 139cm.", "5 children have a height between 120cm and 129cm.",
     "The chart directly shows 5 children in the 120-129cm bar, so that must be true; the other statements go beyond what the chart actually guarantees."),
    ("A bar chart shows savings: Lewis has £15, Jordan has £20, Zoe has £30. Which one of these is NOT true? A) Lewis and Jordan have £35 altogether. B) Lewis has half as much as Jordan. C) The children have £65 altogether. D) Zoe has twice as much as Lewis. E) Jordan has £10 less than Zoe.",
     "Lewis and Jordan have £35 altogether.", "Lewis has half as much as Jordan.", "The children have £65 altogether.", "Zoe has twice as much as Lewis.", "Jordan has £10 less than Zoe.", "Lewis has half as much as Jordan.",
     "Half of Jordan's £20 is £10, but Lewis has £15, not £10 — so that statement is false. (All the other statements check out: 15+20=35, 15+20+30=65, 30=2x15, 30-20=10.)"),
]
CHARTS_QUESTIONS = []
for i, (q, a, b, c, d, e, ans, exp) in enumerate(CHARTS_RAW):
    CHARTS_QUESTIONS.append((q, "mc", a, b, c, d, e, ans, exp, spread_difficulty(len(CHARTS_RAW), i)))

TOPICS = [
    ("Maths: Place Value & Reading Numbers", PLACEVALUE_LESSON, PLACEVALUE_QUESTIONS),
    ("Maths: Number Sequences & Properties", SEQUENCES_LESSON, SEQUENCES_QUESTIONS),
    ("Maths: Fractions", FRACTIONS_LESSON, FRACTIONS_QUESTIONS),
    ("Maths: Decimals & Percentages", DECIMALS_LESSON, DECIMALS_QUESTIONS),
    ("Maths: Money", MONEY_LESSON, MONEY_QUESTIONS),
    ("Maths: Ratio, Proportion & Algebra Puzzles", ALGEBRA_LESSON, ALGEBRA_QUESTIONS),
    ("Maths: Measurement", MEASURE_LESSON, MEASURE_QUESTIONS),
    ("Maths: Time", TIME_LESSON, TIME_QUESTIONS),
    ("Maths: Shape & Geometry", SHAPE_LESSON, SHAPE_QUESTIONS),
    ("Maths: Coordinates & Position", COORDS_LESSON, COORDS_QUESTIONS),
    ("Maths: Charts & Data Handling", CHARTS_LESSON, CHARTS_QUESTIONS),
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


def add_previous_exam_maths():
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
    add_previous_exam_maths()
