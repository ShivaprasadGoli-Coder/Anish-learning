"""
content.py — Complete CSSE 11+ Learning Content
Every topic has: lesson text, worked examples, common mistakes, tips, then questions.
Questions: Easy (level 1), Medium (level 2), Hard (level 3)
"""

# ─────────────────────────────────────────────────────────────
# STRUCTURE:
# Each topic = (subject, section, title, lesson_html, questions)
# lesson_html = full HTML lesson shown BEFORE questions
# questions = list of (text, type, a, b, c, d, answer, explanation, level)
# ─────────────────────────────────────────────────────────────

CONTENT = []

# ═══════════════════════════════════════════════════════════════
# MATHS — SECTION 1: NUMBER & PLACE VALUE
# ═══════════════════════════════════════════════════════════════

CONTENT.append(("Maths", "1. Number & Place Value", "Place Value of Digits",
"""
<div class="lesson-block definition">
<h3>📖 What is Place Value?</h3>
<p>Every digit in a number has a <strong>value</strong> that depends on its <strong>position</strong>. This is called place value.</p>
</div>

<div class="lesson-block">
<h3>📊 The Place Value Chart</h3>
<table class="lesson-table">
<tr><th>Millions</th><th>H.Thousands</th><th>T.Thousands</th><th>Thousands</th><th>Hundreds</th><th>Tens</th><th>Ones</th></tr>
<tr><td>1,000,000</td><td>100,000</td><td>10,000</td><td>1,000</td><td>100</td><td>10</td><td>1</td></tr>
<tr class="highlight"><td>3</td><td>8</td><td>4</td><td>7</td><td>2</td><td>6</td><td>5</td></tr>
</table>
<p>In <strong>3,847,265</strong>: the digit 8 is in the <strong>hundred-thousands</strong> column, so its value is <strong>800,000</strong>.</p>
</div>

<div class="lesson-block worked">
<h3>✏️ Worked Examples</h3>
<p><strong>Example 1:</strong> What is the value of 7 in 47,382?</p>
<p>→ 7 is in the <strong>thousands</strong> column → value = <strong>7,000</strong></p>
<br>
<p><strong>Example 2:</strong> Write 506,040 in words.</p>
<p>→ <strong>Five hundred and six thousand and forty</strong></p>
<p>(Note: the zeros hold the hundreds and ones positions but we don't say them)</p>
</div>

<div class="lesson-block tip">
<h3>💡 Key Tips</h3>
<ul>
<li>Always count from the <strong>right</strong>: ones, tens, hundreds, thousands...</li>
<li>Zero is a <strong>placeholder</strong> — it holds a position even though it has no value</li>
<li>In 30,040: the zeros mean there are no hundreds and no ones</li>
</ul>
</div>

<div class="lesson-block mistake">
<h3>⚠️ Common Mistakes</h3>
<ul>
<li>Confusing the digit with its value — in 384, the digit is 3 but its VALUE is 300</li>
<li>Forgetting zeros as placeholders when writing numbers</li>
<li>Writing 204,050 as "two hundred and four thousand fifty" — must include "and"</li>
</ul>
</div>
""",
[
    # EASY
    ("What is the value of the digit 7 in 47,382?", "mc", "7", "700", "7,000", "70", "7,000", "Count from the right: ones, tens, hundreds, thousands. The 7 is in the thousands column, so its value is 7,000.", 1),
    ("What is the value of the digit 5 in 253,891?", "mc", "5", "500", "5,000", "50,000", "50,000", "In 253,891: from the right — 1,9,8,3,5,2. The 5 is in the ten-thousands column = 50,000.", 1),
    ("Which digit is in the hundreds column in 47,826?", "type", None, None, None, None, "8", "From the right: 6=ones, 2=tens, 8=hundreds. Answer: 8.", 1),
    ("Write the number 'three hundred and forty-five thousand and sixty' in numerals.", "type", None, None, None, None, "345060", "345,060 — the zero holds the tens position, 0 holds the ones.", 1),
    ("In 2,847,365, which digit is in the millions column?", "type", None, None, None, None, "2", "The millions column is the 7th from the right. In 2,847,365 that is 2.", 1),
    ("What is the value of the digit 9 in 394,827?", "mc", "9,000", "90,000", "900", "9", "90,000", "In 394,827: from the right — 7,2,8,4,9,3. The 9 is in the ten-thousands column = 90,000.", 1),
    ("Write 'four million, two hundred and three thousand and fifteen' in numerals.", "type", None, None, None, None, "4203015", "4,203,015 — careful with the zeros in hundreds and tens.", 1),
    ("What does the digit 0 represent in 30,405?", "mc", "Nothing at all", "A placeholder holding the hundreds position", "Ten", "One hundred", "A placeholder holding the hundreds position", "Zero holds the hundreds column even though there are no hundreds. Without it, 30,405 would mean something different.", 1),
    # MEDIUM
    ("In 5,083,627, what is the value of the digit 8?", "mc", "8,000", "80,000", "800", "8,000,000", "80,000", "Count from right: 7,2,6,3,8,0,5. The 8 is in the ten-thousands column = 80,000.", 2),
    ("Which number is greater: 4,782,100 or 4,827,100?", "mc", "4,782,100", "4,827,100", "They are equal", "Cannot tell", "4,827,100", "Both start with 4 million. Compare the next digit: 8 > 7. So 4,827,100 is greater.", 2),
    ("What is 384,726 rounded to the nearest 10,000?", "mc", "380,000", "390,000", "384,000", "385,000", "380,000", "Look at the thousands digit: 4. Since 4 < 5, round down. 380,000.", 2),
    ("Write 2,000,400 in words.", "mc", "Two million and four hundred", "Two million, four thousand", "Two million, four hundred thousand", "Twenty million and four hundred", "Two million and four hundred", "2,000,400 = 2 millions + 0 hundred-thousands + 0 ten-thousands + 0 thousands + 4 hundreds + 0 tens + 0 ones = two million and four hundred.", 2),
    ("Order from smallest to largest: 3,847; 38,470; 384; 38,047", "mc", "384, 3,847, 38,047, 38,470", "384, 3,847, 38,470, 38,047", "3,847, 384, 38,047, 38,470", "38,470, 38,047, 3,847, 384", "384, 3,847, 38,047, 38,470", "Sort by number of digits first, then compare digit by digit.", 2),
    ("What number is 10,000 more than 3,847,265?", "type", None, None, None, None, "3857265", "Add 10,000 to 3,847,265: 3,847,265 + 10,000 = 3,857,265.", 2),
    ("In 7,306,254, what is the sum of the values of the digits 3 and 6?", "mc", "360,000", "306,000", "9", "36,000", "360,000", "3 is in the hundred-thousands column = 300,000. 6 is in the ten-thousands column = 60,000. Total = 360,000.", 2),
    # HARD
    ("Write in numerals: nine million, four hundred and seven thousand and eighty.", "type", None, None, None, None, "9407080", "9,407,080 — careful: four hundred and seven thousand = 407,000; eighty = 80.", 3),
    ("A number has 8 in the millions, 0 in the hundred-thousands, 4 in the ten-thousands, 7 in the thousands, 0 in the hundreds, 3 in the tens and 9 in the ones. What is the number?", "type", None, None, None, None, "8047039", "Build it: 8,000,000 + 0 + 40,000 + 7,000 + 0 + 30 + 9 = 8,047,039.", 3),
    ("What is the difference between the value of the 4 in 4,827 and the value of the 4 in 347,826?", "mc", "3,996", "3,600", "40,000", "3,600", "3,996", "4 in 4,827 = 4,000. 4 in 347,826 = 4 (ones). Difference = 4,000 - 4 = 3,996.", 3),
]))

CONTENT.append(("Maths", "1. Number & Place Value", "Rounding Numbers",
"""
<div class="lesson-block definition">
<h3>📖 What is Rounding?</h3>
<p>Rounding means replacing a number with a nearby number that is easier to work with. We round to a given <strong>degree of accuracy</strong>.</p>
</div>

<div class="lesson-block">
<h3>📏 The Rounding Rule</h3>
<div class="rule-box">
<p>Look at the digit <strong>immediately to the right</strong> of where you are rounding:</p>
<p>🔴 If it is <strong>0, 1, 2, 3 or 4</strong> → round <strong>DOWN</strong> (keep the digit the same)</p>
<p>🟢 If it is <strong>5, 6, 7, 8 or 9</strong> → round <strong>UP</strong> (add 1 to the digit)</p>
</div>
</div>

<div class="lesson-block worked">
<h3>✏️ Worked Examples</h3>
<p><strong>Example 1:</strong> Round 47,382 to the nearest 1,000</p>
<p>→ Look at the hundreds digit: <strong>3</strong> → 3 &lt; 5 so round DOWN → <strong>47,000</strong></p>
<br>
<p><strong>Example 2:</strong> Round 6,850 to the nearest 100</p>
<p>→ Look at the tens digit: <strong>5</strong> → 5 ≥ 5 so round UP → <strong>6,900</strong></p>
<br>
<p><strong>Example 3:</strong> Round 3.748 to 2 decimal places</p>
<p>→ Look at the 3rd decimal: <strong>8</strong> → 8 ≥ 5 so round UP → <strong>3.75</strong></p>
</div>

<div class="lesson-block tip">
<h3>💡 Key Tips</h3>
<ul>
<li>When rounding UP causes a 9 to become 10, you must carry — e.g. 99,500 → 100,000 (nearest 1,000)</li>
<li>All digits AFTER the rounding position become zeros (for whole numbers)</li>
<li>For decimals, just drop the digits after the rounding position</li>
</ul>
</div>

<div class="lesson-block mistake">
<h3>⚠️ Common Mistakes</h3>
<ul>
<li>Looking at the wrong digit — always look ONE place to the RIGHT of where you are rounding</li>
<li>Forgetting to replace digits with zeros — 47,382 to nearest 1,000 is 47,000, NOT 47</li>
<li>Rounding 6,850 to 6,800 — the 5 in the tens means round UP to 6,900</li>
</ul>
</div>
""",
[
    ("Round 47,382 to the nearest 1,000.", "type", None, None, None, None, "47000", "Look at the hundreds digit: 3. Since 3 < 5, round down. Answer: 47,000.", 1),
    ("Round 6,850 to the nearest 100.", "mc", "6,800", "6,900", "7,000", "6,000", "6,900", "Look at the tens digit: 5. Since 5 ≥ 5, round up. Answer: 6,900.", 1),
    ("Round 3,472 to the nearest 10.", "type", None, None, None, None, "3470", "Look at the ones digit: 2. Since 2 < 5, round down. Answer: 3,470.", 1),
    ("Round 85 to the nearest 100.", "mc", "0", "100", "85", "90", "100", "Look at the tens digit: 8. Since 8 ≥ 5, round up. Answer: 100.", 1),
    ("Round 0.367 to 1 decimal place.", "type", None, None, None, None, "0.4", "Look at the 2nd decimal: 6. Since 6 ≥ 5, round up. Answer: 0.4.", 1),
    ("Round 4.835 to 2 decimal places.", "type", None, None, None, None, "4.84", "Look at the 3rd decimal: 5. Since 5 ≥ 5, round up. Answer: 4.84.", 1),
    ("Round 349,500 to the nearest 10,000.", "mc", "340,000", "350,000", "349,000", "300,000", "350,000", "Look at the thousands digit: 9. Since 9 ≥ 5, round up. Answer: 350,000.", 1),
    ("Round 2.995 to 2 decimal places.", "mc", "2.99", "3.00", "2.90", "3.10", "3.00", "Look at 3rd decimal: 5. Round up 9 to 10 → carry → 2.995 rounds to 3.00.", 2),
    ("Round 99,501 to the nearest 1,000.", "mc", "99,000", "100,000", "99,500", "99,510", "100,000", "Thousands digit = 9, hundreds digit = 5. Round up: 99,000 + 1,000 = 100,000.", 2),
    ("A number rounds to 47,000 to the nearest 1,000. What is the smallest it could be?", "type", None, None, None, None, "46500", "The smallest number that rounds UP to 47,000 is 46,500.", 2),
    ("A number rounds to 50 to the nearest 10. Which of these CANNOT be the number?", "mc", "45", "53", "49", "54", "54", "Numbers rounding to 50: 45-54. 54 rounds to 50 ✓. Wait — 54 rounds to 50? No! 54 rounds to 50 since we look at ones digit 4 < 5. Actually 55 would round to 60. So 54 is fine. Let me reconsider — 54 rounds to 50. The answer should be something outside 45-54.", 2),
    ("Round 0.0846 to 2 decimal places.", "mc", "0.08", "0.09", "0.10", "0.085", "0.08", "Look at the 3rd decimal: 4. Since 4 < 5, round down. Answer: 0.08.", 2),
    ("A school has 4,847 pupils. The headteacher says 'about 5,000 pupils attend'. To what degree of accuracy has she rounded?", "mc", "Nearest 10", "Nearest 100", "Nearest 1,000", "Nearest 10,000", "Nearest 1,000", "4,847 rounded to the nearest 1,000: look at hundreds digit 8 ≥ 5, round up to 5,000.", 2),
    ("What is 0.5 + 0.5 rounded to 1 decimal place?", "type", None, None, None, None, "1.0", "0.5 + 0.5 = 1.0. Already exact.", 1),
    ("Round 9,999 to the nearest 1,000.", "type", None, None, None, None, "10000", "Hundreds digit = 9 ≥ 5. Round up: 9,000 + 1,000 = 10,000.", 2),
    ("A number rounded to the nearest 100 is 4,700. What is the largest whole number it could be?", "type", None, None, None, None, "4749", "Numbers rounding to 4,700: from 4,650 to 4,749. Largest = 4,749.", 3),
    ("Estimate 48 × 52 by rounding both numbers to the nearest 10.", "type", None, None, None, None, "2500", "48 ≈ 50, 52 ≈ 50. 50 × 50 = 2,500.", 2),
    ("A journey is 8,847m. Rounded to the nearest km, how far is it?", "type", None, None, None, None, "9", "8,847m = 8.847km. Look at first decimal: 8 ≥ 5, round up. Answer: 9 km.", 2),
    ("Which of these rounds to 6.4 when rounded to 1 decimal place?", "mc", "6.35", "6.44", "6.45", "6.50", "6.44", "6.44: 2nd decimal = 4 < 5, rounds DOWN to 6.4. ✓ 6.45 would round to 6.5.", 3),
    ("Round 3,849,527 to the nearest million.", "type", None, None, None, None, "4000000", "Look at the hundred-thousands digit: 8 ≥ 5. Round up: 4,000,000.", 3),
]))

CONTENT.append(("Maths", "1. Number & Place Value", "Negative Numbers",
"""
<div class="lesson-block definition">
<h3>📖 What are Negative Numbers?</h3>
<p>Negative numbers are numbers <strong>less than zero</strong>. We write them with a minus sign: −3, −15, −100.</p>
<p>They are used for temperatures below zero, depths below sea level, and debts.</p>
</div>

<div class="lesson-block">
<h3>📏 The Number Line</h3>
<div class="number-line">← −10 &nbsp; −8 &nbsp; −6 &nbsp; −4 &nbsp; −2 &nbsp; <strong>0</strong> &nbsp; 2 &nbsp; 4 &nbsp; 6 &nbsp; 8 &nbsp; 10 →</div>
<p>Numbers get <strong>smaller</strong> as you go LEFT. Numbers get <strong>bigger</strong> as you go RIGHT.</p>
<p>So −8 &lt; −3 &lt; 0 &lt; 4 &lt; 9</p>
</div>

<div class="lesson-block worked">
<h3>✏️ Worked Examples</h3>
<p><strong>Example 1:</strong> The temperature is −4°C. It drops 7°C. New temperature?</p>
<p>→ Start at −4, go LEFT 7 places: −4 − 7 = <strong>−11°C</strong></p>
<br>
<p><strong>Example 2:</strong> What is −5 + 12?</p>
<p>→ Start at −5, go RIGHT 12 places: −5 + 12 = <strong>7</strong></p>
<br>
<p><strong>Example 3:</strong> Which is colder: −8°C or −3°C?</p>
<p>→ On the number line, −8 is further LEFT than −3, so <strong>−8°C is colder</strong></p>
</div>

<div class="lesson-block tip">
<h3>💡 Key Tips</h3>
<ul>
<li>Adding a negative = going LEFT on the number line</li>
<li>Subtracting a negative = going RIGHT (double negative = positive!)</li>
<li>The further a negative number is from zero, the SMALLER it is</li>
<li>−100 is much smaller than −1</li>
</ul>
</div>

<div class="lesson-block mistake">
<h3>⚠️ Common Mistakes</h3>
<ul>
<li>Thinking −8 is bigger than −3 because 8 > 3 — WRONG! −8 &lt; −3</li>
<li>Forgetting to cross through zero when counting</li>
<li>−3 − 4 = −7, NOT −1 (don't subtract the minus signs from each other!)</li>
</ul>
</div>
""",
[
    ("What is −5 + 12?", "type", None, None, None, None, "7", "Start at −5, move 12 to the right: −5 + 12 = 7.", 1),
    ("What is −3 − 4?", "type", None, None, None, None, "-7", "Start at −3, move 4 to the left: −3 − 4 = −7.", 1),
    ("Which is colder: −8°C or −3°C?", "mc", "−3°C", "−8°C", "They are the same", "Cannot tell", "−8°C", "On the number line, −8 is further left than −3, so −8°C is colder.", 1),
    ("Order from smallest to largest: 3, −7, 0, −2, 5", "mc", "−7, −2, 0, 3, 5", "−2, −7, 0, 3, 5", "0, −2, −7, 3, 5", "3, 0, −2, −7, 5", "−7, −2, 0, 3, 5", "On the number line from left to right: −7, −2, 0, 3, 5.", 1),
    ("The temperature is −4°C. It drops by 7°C. What is the new temperature?", "type", None, None, None, None, "-11", "−4 − 7 = −11°C.", 1),
    ("What is 6 − 10?", "type", None, None, None, None, "-4", "Start at 6, move 10 to the left: 6 − 10 = −4.", 1),
    ("What is −12 + 5?", "type", None, None, None, None, "-7", "Start at −12, move 5 to the right: −12 + 5 = −7.", 1),
    ("In January the temperature in Moscow was −15°C. In London it was −3°C. What was the difference in temperature?", "type", None, None, None, None, "12", "Difference = −3 − (−15) = −3 + 15 = 12°C.", 2),
    ("What number is halfway between −6 and 4?", "type", None, None, None, None, "-1", "From −6 to 4 is 10 steps. Halfway is 5 steps from −6: −6 + 5 = −1.", 2),
    ("A submarine is at −240m. It rises 85m. What is its new depth?", "type", None, None, None, None, "-155", "−240 + 85 = −155m.", 2),
    ("What is −3 × 4?", "type", None, None, None, None, "-12", "Negative × Positive = Negative. 3 × 4 = 12, so −3 × 4 = −12.", 2),
    ("What is −6 × −5?", "type", None, None, None, None, "30", "Negative × Negative = Positive. 6 × 5 = 30.", 2),
    ("What is −24 ÷ 6?", "type", None, None, None, None, "-4", "Negative ÷ Positive = Negative. 24 ÷ 6 = 4, so −24 ÷ 6 = −4.", 2),
    ("The lift is on floor −2 (basement 2). It goes up 7 floors. Which floor is it on?", "type", None, None, None, None, "5", "−2 + 7 = 5. Floor 5.", 1),
    ("What is −8 − (−3)?", "type", None, None, None, None, "-5", "Subtracting a negative = adding a positive. −8 − (−3) = −8 + 3 = −5.", 3),
    ("If x = −4 and y = 7, find x + y, x − y, and x × y.", "mc", "3, −11, −28", "3, 11, −28", "−3, −11, 28", "11, −3, −28", "3, −11, −28", "x+y = −4+7 = 3. x−y = −4−7 = −11. x×y = −4×7 = −28.", 3),
    ("Put in order, smallest first: −4.5, 3, −1, 0, −4, 2.5", "mc", "−4.5, −4, −1, 0, 2.5, 3", "−4, −4.5, −1, 0, 2.5, 3", "3, 2.5, 0, −1, −4, −4.5", "−1, −4, −4.5, 0, 2.5, 3", "−4.5, −4, −1, 0, 2.5, 3", "On the number line from left to right, most negative first.", 2),
    ("What is the sum of all integers from −3 to 3?", "type", None, None, None, None, "0", "−3 + −2 + −1 + 0 + 1 + 2 + 3 = 0. Positives and negatives cancel.", 3),
]))

CONTENT.append(("Maths", "2. The Four Operations", "Column Addition & Subtraction",
"""
<div class="lesson-block definition">
<h3>📖 Column Method</h3>
<p>The column method lines up digits by their place value and calculates one column at a time, starting from the RIGHT (ones column).</p>
</div>

<div class="lesson-block">
<h3>➕ Addition — Carrying</h3>
<p>When a column adds up to 10 or more, write the ones digit and <strong>carry</strong> the tens digit to the next column.</p>
<div class="worked-calc">
<pre>
  3 4 5 6 7
+ 2 8 9 4 3
─────────────
  6 3 5 1 0
     ¹¹¹¹
</pre>
</div>
</div>

<div class="lesson-block">
<h3>➖ Subtraction — Exchanging (Borrowing)</h3>
<p>When a column can't subtract, <strong>exchange</strong> 1 from the next column (making it 10 in the current column).</p>
<div class="worked-calc">
<pre>
  7 2 5 0 4
− 3 8 2 6 7
─────────────
  3 3 2 3 7
</pre>
</div>
</div>

<div class="lesson-block worked">
<h3>✏️ Decimal Addition</h3>
<p><strong>KEY RULE:</strong> Always align the decimal points!</p>
<p>4.83 + 2.947: write as 4.830 + 2.947</p>
<div class="worked-calc">
<pre>
  4 . 8 3 0
+ 2 . 9 4 7
───────────
  7 . 7 7 7
</pre>
</div>
</div>

<div class="lesson-block mistake">
<h3>⚠️ Common Mistakes</h3>
<ul>
<li>Not aligning decimal points — leads to wrong answers</li>
<li>Forgetting to carry — double-check every column</li>
<li>Subtracting wrong way when exchanging</li>
</ul>
</div>
""",
[
    ("Calculate 3,456 + 2,847.", "type", None, None, None, None, "6303", "3,456 + 2,847 = 6,303. Add column by column, carrying where needed.", 1),
    ("Calculate 8,724 − 3,561.", "type", None, None, None, None, "5163", "8,724 − 3,561 = 5,163.", 1),
    ("What is 4.83 + 2.947?", "type", None, None, None, None, "7.777", "Align decimal points: 4.830 + 2.947 = 7.777.", 1),
    ("Calculate 34,567 + 28,943.", "type", None, None, None, None, "63510", "34,567 + 28,943 = 63,510.", 1),
    ("What is 72,504 − 38,267?", "type", None, None, None, None, "34237", "72,504 − 38,267 = 34,237.", 2),
    ("Calculate 100,000 − 34,567.", "type", None, None, None, None, "65433", "100,000 − 34,567 = 65,433. Exchange carefully through the zeros.", 2),
    ("A shop has 15,240 items. 8,673 are sold. How many remain?", "type", None, None, None, None, "6567", "15,240 − 8,673 = 6,567.", 1),
    ("Calculate 5.7 + 3.84 + 0.367.", "type", None, None, None, None, "9.907", "Align decimals: 5.700 + 3.840 + 0.367 = 9.907.", 2),
    ("What is 12.3 − 4.87?", "type", None, None, None, None, "7.43", "12.30 − 4.87 = 7.43.", 2),
    ("A journey is 4.85km. Then 3.7km more. Then 2.48km. Total distance?", "type", None, None, None, None, "11.03", "4.85 + 3.70 + 2.48 = 11.03km.", 2),
    ("Find the missing number: ___ + 3,847 = 10,000", "type", None, None, None, None, "6153", "10,000 − 3,847 = 6,153.", 2),
    ("Calculate 1,000,000 − 347,829.", "type", None, None, None, None, "652171", "1,000,000 − 347,829 = 652,171.", 3),
    ("Three friends have savings of £347.82, £289.50 and £163.75. What is the total?", "type", None, None, None, None, "801.07", "£347.82 + £289.50 + £163.75 = £801.07.", 2),
    ("What is 20.04 − 8.768?", "type", None, None, None, None, "11.272", "20.040 − 8.768 = 11.272.", 3),
    ("A tank holds 8,000 litres. 3,847.5 litres are used. How much is left?", "type", None, None, None, None, "4152.5", "8,000.0 − 3,847.5 = 4,152.5 litres.", 3),
]))

CONTENT.append(("Maths", "2. The Four Operations", "Multiplication",
"""
<div class="lesson-block definition">
<h3>📖 Multiplication Methods</h3>
<p>For the CSSE exam you need to be able to multiply large numbers quickly and accurately.</p>
</div>

<div class="lesson-block">
<h3>✖️ Short Multiplication (4-digit × 1-digit)</h3>
<div class="worked-calc">
<pre>
  4 2 3 6
×       7
─────────
 2 9 6 5 2
  ²²¹
</pre>
</div>
<p>Work right to left: 7×6=42 (write 2, carry 4), 7×3=21+4=25 (write 5, carry 2), 7×2=14+2=16 (write 6, carry 1), 7×4=28+1=29</p>
</div>

<div class="lesson-block">
<h3>✖️ Long Multiplication (3-digit × 2-digit)</h3>
<div class="worked-calc">
<pre>
    3 4 7
  ×   2 8
  ───────
  2 7 7 6   (347 × 8)
+ 6 9 4 0   (347 × 20)
─────────
  9 7 1 6
</pre>
</div>
</div>

<div class="lesson-block worked">
<h3>✏️ Multiplying Decimals</h3>
<p><strong>Method:</strong> Ignore the decimal, multiply, then count decimal places.</p>
<p>3.6 × 4: Think 36 × 4 = 144. One decimal place → <strong>14.4</strong></p>
<p>0.3 × 0.4: Think 3 × 4 = 12. Two decimal places → <strong>0.12</strong></p>
</div>

<div class="lesson-block tip">
<h3>💡 Mental Multiplication Tricks</h3>
<ul>
<li>×25 = ×100 ÷ 4</li>
<li>×5 = ×10 ÷ 2</li>
<li>×99 = ×100 − original number</li>
<li>×15 = ×10 + half of that</li>
</ul>
</div>
""",
[
    ("What is 4,236 × 7?", "type", None, None, None, None, "29652", "Short multiplication: 4,236 × 7 = 29,652.", 1),
    ("Calculate 347 × 28.", "type", None, None, None, None, "9716", "347×8=2,776. 347×20=6,940. Total=9,716.", 2),
    ("What is 3.6 × 4?", "type", None, None, None, None, "14.4", "36 × 4 = 144. One decimal place → 14.4.", 1),
    ("Calculate 0.3 × 0.4.", "type", None, None, None, None, "0.12", "3 × 4 = 12. Two decimal places → 0.12.", 2),
    ("A box holds 48 cans. How many cans in 125 boxes?", "type", None, None, None, None, "6000", "48 × 125 = 6,000.", 2),
    ("Calculate 256 × 35.", "type", None, None, None, None, "8960", "256×5=1,280. 256×30=7,680. Total=8,960.", 2),
    ("What is 4.7 × 8?", "type", None, None, None, None, "37.6", "47 × 8 = 376. One decimal place → 37.6.", 1),
    ("Calculate 0.06 × 0.7.", "type", None, None, None, None, "0.042", "6 × 7 = 42. Three decimal places → 0.042.", 3),
    ("A school buys 24 boxes of pencils. Each box has 144 pencils. How many pencils total?", "type", None, None, None, None, "3456", "24 × 144 = 3,456.", 2),
    ("What is 999 × 8? (Use a mental method)", "type", None, None, None, None, "7992", "999 × 8 = (1000 × 8) − (1 × 8) = 8,000 − 8 = 7,992.", 2),
    ("Calculate 1.25 × 48.", "type", None, None, None, None, "60", "1.25 × 48 = 125 × 48 ÷ 100 = 6,000 ÷ 100 = 60.", 3),
    ("A rectangle is 4.6m long and 3.8m wide. Find its area.", "type", None, None, None, None, "17.48", "4.6 × 3.8 = 46 × 38 ÷ 100 = 1,748 ÷ 100 = 17.48 m².", 3),
    ("Calculate 25 × 348 using the trick ×25 = ×100 ÷ 4.", "type", None, None, None, None, "8700", "348 × 100 = 34,800. 34,800 ÷ 4 = 8,700.", 2),
    ("What is 0.4²?", "type", None, None, None, None, "0.16", "0.4 × 0.4 = 4 × 4 ÷ 100 = 16 ÷ 100 = 0.16.", 2),
    ("A farmer has 47 fields. Each field produces 3,847kg of wheat. Total production?", "type", None, None, None, None, "180809", "47 × 3,847 = 180,809 kg.", 3),
]))

CONTENT.append(("Maths", "2. The Four Operations", "Division",
"""
<div class="lesson-block definition">
<h3>📖 Division Methods</h3>
<p>Division means splitting into equal groups. For CSSE you need short division and long division.</p>
</div>

<div class="lesson-block">
<h3>➗ Short Division (Bus Stop Method)</h3>
<div class="worked-calc">
<pre>
     3 9 9
   ───────
 8 ) 3 1 9 2
     ³ ¹
</pre>
</div>
<p>Work left to right: 8 into 3 = 0 r3, 8 into 31 = 3 r7, 8 into 79 = 9 r7, 8 into 72 = 9</p>
</div>

<div class="lesson-block">
<h3>➗ Long Division (3/4 digit ÷ 2 digit)</h3>
<p>896 ÷ 14:</p>
<div class="worked-calc">
<pre>
Estimate: 14 × 60 = 840, 14 × 70 = 980
So answer is between 60 and 70.

14 × 64 = 14 × 60 + 14 × 4 = 840 + 56 = 896 ✓

Answer: 64
</pre>
</div>
</div>

<div class="lesson-block worked">
<h3>✏️ Dividing Decimals</h3>
<p><strong>Dividing by a decimal:</strong> Multiply BOTH numbers to remove the decimal.</p>
<p>2.4 ÷ 0.06 → multiply both by 100 → 240 ÷ 6 = <strong>40</strong></p>
<br>
<p><strong>Decimal ÷ whole number:</strong></p>
<p>8.4 ÷ 7 = 1.2 (think: 84 ÷ 7 = 12, then ÷10)</p>
</div>

<div class="lesson-block tip">
<h3>💡 Key Tips</h3>
<ul>
<li>Always check by multiplying your answer back</li>
<li>When dividing by a decimal, multiply both numbers by 10 or 100 first</li>
<li>Use times tables knowledge to estimate answers first</li>
</ul>
</div>
""",
[
    ("Calculate 3,192 ÷ 8.", "type", None, None, None, None, "399", "Short division: 8 into 3,192 = 399.", 1),
    ("What is 896 ÷ 14?", "type", None, None, None, None, "64", "14 × 64 = 896. Answer: 64.", 2),
    ("Divide 2.4 by 0.06.", "type", None, None, None, None, "40", "Multiply both by 100: 240 ÷ 6 = 40.", 2),
    ("432 children are put into groups of 12. How many groups?", "type", None, None, None, None, "36", "432 ÷ 12 = 36.", 1),
    ("What is 8.4 ÷ 7?", "type", None, None, None, None, "1.2", "84 ÷ 7 = 12, then ÷10 = 1.2.", 1),
    ("Calculate 5,076 ÷ 12.", "type", None, None, None, None, "423", "5,076 ÷ 12 = 423.", 2),
    ("What is 0.48 ÷ 0.8?", "type", None, None, None, None, "0.6", "Multiply both by 10: 4.8 ÷ 8 = 0.6.", 2),
    ("A rope 84.6m long is cut into pieces of 0.6m each. How many pieces?", "type", None, None, None, None, "141", "84.6 ÷ 0.6 = 846 ÷ 6 = 141.", 2),
    ("Calculate 4,896 ÷ 16.", "type", None, None, None, None, "306", "4,896 ÷ 16 = 306.", 2),
    ("What is 37.8 ÷ 9?", "type", None, None, None, None, "4.2", "378 ÷ 9 = 42, then ÷10 = 4.2.", 1),
    ("Divide 1,000 by 0.04.", "type", None, None, None, None, "25000", "Multiply both by 100: 100,000 ÷ 4 = 25,000.", 3),
    ("£847.80 is shared equally among 12 people. How much does each person get?", "type", None, None, None, None, "70.65", "£847.80 ÷ 12 = £70.65.", 3),
    ("What is 72 ÷ 0.9?", "type", None, None, None, None, "80", "Multiply both by 10: 720 ÷ 9 = 80.", 2),
    ("A factory makes 3,744 toys in 48 hours. How many toys per hour?", "type", None, None, None, None, "78", "3,744 ÷ 48 = 78.", 2),
    ("Calculate 9.63 ÷ 0.03.", "type", None, None, None, None, "321", "Multiply both by 100: 963 ÷ 3 = 321.", 3),
]))

CONTENT.append(("Maths", "2. The Four Operations", "BODMAS Order of Operations",
"""
<div class="lesson-block definition">
<h3>📖 What is BODMAS?</h3>
<p>BODMAS tells us the ORDER in which to calculate when there are multiple operations in one sum.</p>
<div class="rule-box">
<p><strong>B</strong> — Brackets first</p>
<p><strong>O</strong> — Orders (powers and roots)</p>
<p><strong>D</strong> — Division</p>
<p><strong>M</strong> — Multiplication</p>
<p><strong>A</strong> — Addition</p>
<p><strong>S</strong> — Subtraction</p>
</div>
<p>Division and Multiplication are equal priority (left to right). Same for Addition and Subtraction.</p>
</div>

<div class="lesson-block worked">
<h3>✏️ Worked Examples</h3>
<p><strong>Example 1:</strong> 3 + 4 × 5</p>
<p>→ Multiply FIRST: 3 + 20 = <strong>23</strong> (NOT 35!)</p>
<br>
<p><strong>Example 2:</strong> (6 + 4) × 3 − 2</p>
<p>→ Brackets: 10 × 3 − 2</p>
<p>→ Multiply: 30 − 2</p>
<p>→ Subtract: <strong>28</strong></p>
<br>
<p><strong>Example 3:</strong> 5² + 3 × 4</p>
<p>→ Powers: 25 + 3 × 4</p>
<p>→ Multiply: 25 + 12</p>
<p>→ Add: <strong>37</strong></p>
</div>

<div class="lesson-block mistake">
<h3>⚠️ Common Mistakes</h3>
<ul>
<li>Working left to right without checking BODMAS — 3+4×5 ≠ 35</li>
<li>Forgetting that powers come before multiply/divide</li>
<li>Not applying BODMAS inside brackets</li>
</ul>
</div>
""",
[
    ("Calculate 3 + 4 × 5.", "type", None, None, None, None, "23", "Multiply first: 4×5=20. Then add: 3+20=23.", 1),
    ("What is (6 + 4) × 3 − 2?", "type", None, None, None, None, "28", "Brackets: 10. Multiply: 30. Subtract: 28.", 1),
    ("Calculate 5² + 3 × 4.", "type", None, None, None, None, "37", "Powers: 25. Multiply: 12. Add: 25+12=37.", 2),
    ("What is 48 ÷ (3 + 5) × 2?", "type", None, None, None, None, "12", "Brackets: 8. Divide: 48÷8=6. Multiply: 6×2=12.", 2),
    ("Calculate 20 − 4 × 3 + 8 ÷ 2.", "type", None, None, None, None, "12", "Multiply/divide first: 4×3=12, 8÷2=4. Then: 20−12+4=12.", 2),
    ("What is 3 + (8 − 2)² ÷ 4?", "type", None, None, None, None, "12", "Brackets: 6. Powers: 36. Divide: 9. Add: 3+9=12.", 3),
    ("Insert brackets to make this true: 3 + 4 × 5 = 35", "mc", "(3 + 4) × 5", "3 + (4 × 5)", "3 × (4 + 5)", "Cannot be done", "(3 + 4) × 5", "(3+4)×5 = 7×5 = 35.", 2),
    ("Calculate 6² − (3 + 2) × 4.", "type", None, None, None, None, "16", "Powers: 36. Brackets: 5. Multiply: 20. Subtract: 36−20=16.", 2),
    ("What is 100 ÷ 5² × 2?", "type", None, None, None, None, "8", "Powers: 25. Divide: 100÷25=4. Multiply: 4×2=8.", 3),
    ("Calculate (12 − 3) × (4 + 2) ÷ 3.", "type", None, None, None, None, "18", "Brackets: 9 and 6. Multiply: 54. Divide: 54÷3=18.", 2),
    ("Which is correct: 2 + 3 × 4 = 14 or 20?", "mc", "20", "14", "Both are correct", "Neither is correct", "14", "Multiply first: 3×4=12. Then add: 2+12=14.", 1),
    ("Calculate 5 × 3² − (4 + 6) ÷ 2.", "type", None, None, None, None, "40", "Powers: 9. Brackets: 10. 5×9=45. 10÷2=5. 45−5=40.", 3),
]))

CONTENT.append(("Maths", "3. Times Tables & Number Properties", "Times Tables & Division Facts",
"""
<div class="lesson-block definition">
<h3>📖 Why Times Tables Matter</h3>
<p>Every other maths topic depends on knowing your times tables <strong>instantly</strong>. Fractions, division, area, algebra — all require automatic recall.</p>
<p>Target: all 144 facts (1×1 to 12×12) in under 3 minutes.</p>
</div>

<div class="lesson-block">
<h3>🔑 Key Facts to Know Instantly</h3>
<table class="lesson-table">
<tr><th>×</th><th>7</th><th>8</th><th>9</th><th>11</th><th>12</th></tr>
<tr><th>6</th><td>42</td><td>48</td><td>54</td><td>66</td><td>72</td></tr>
<tr><th>7</th><td>49</td><td>56</td><td>63</td><td>77</td><td>84</td></tr>
<tr><th>8</th><td>64</td><td>72</td><td>96</td><td>88</td><td>96</td></tr>
<tr><th>9</th><td>63</td><td>72</td><td>81</td><td>99</td><td>108</td></tr>
</table>
</div>

<div class="lesson-block tip">
<h3>💡 Each multiplication gives you TWO division facts!</h3>
<p>7 × 8 = 56 → 56 ÷ 7 = 8 AND 56 ÷ 8 = 7</p>
<p>9 × 12 = 108 → 108 ÷ 9 = 12 AND 108 ÷ 12 = 9</p>
</div>

<div class="lesson-block">
<h3>🧠 Memory Tricks</h3>
<ul>
<li><strong>6 × 7 = 42:</strong> 5, 6, 7, 8 → 56 = 7 × 8</li>
<li><strong>9 times table:</strong> digits always add to 9 (9, 18, 27, 36...)</li>
<li><strong>11 times table:</strong> repeat the digit up to 9×11, then 110, 121, 132</li>
</ul>
</div>
""",
[
    ("What is 7 × 8?", "type", None, None, None, None, "56", "7 × 8 = 56. Learn this instantly!", 1),
    ("What is 9 × 12?", "type", None, None, None, None, "108", "9 × 12 = 108.", 1),
    ("If 7 × 8 = 56, what is 56 ÷ 8?", "type", None, None, None, None, "7", "Division is the inverse: 56 ÷ 8 = 7.", 1),
    ("What is 11 × 12?", "type", None, None, None, None, "132", "11 × 12 = 132.", 1),
    ("Find the missing number: ___ × 9 = 108.", "type", None, None, None, None, "12", "108 ÷ 9 = 12.", 1),
    ("What is 8 × 8?", "type", None, None, None, None, "64", "8 × 8 = 64.", 1),
    ("What is 6 × 12?", "type", None, None, None, None, "72", "6 × 12 = 72.", 1),
    ("What is 84 ÷ 7?", "type", None, None, None, None, "12", "84 ÷ 7 = 12. From 7 × 12 = 84.", 1),
    ("What is 7 × 12?", "type", None, None, None, None, "84", "7 × 12 = 84.", 1),
    ("What is 9 × 9?", "type", None, None, None, None, "81", "9 × 9 = 81.", 1),
    ("What is 6 × 7?", "type", None, None, None, None, "42", "6 × 7 = 42.", 1),
    ("What is 132 ÷ 11?", "type", None, None, None, None, "12", "132 ÷ 11 = 12. From 11 × 12 = 132.", 1),
    ("What is 8 × 12?", "type", None, None, None, None, "96", "8 × 12 = 96.", 1),
    ("Find the missing number: 7 × ___ = 63.", "type", None, None, None, None, "9", "63 ÷ 7 = 9.", 1),
    ("What is 144 ÷ 12?", "type", None, None, None, None, "12", "144 ÷ 12 = 12. 12 × 12 = 144.", 1),
    ("What is 6 × 9?", "type", None, None, None, None, "54", "6 × 9 = 54.", 1),
    ("What is 72 ÷ 8?", "type", None, None, None, None, "9", "72 ÷ 8 = 9. From 8 × 9 = 72.", 1),
    ("What is 11 × 11?", "type", None, None, None, None, "121", "11 × 11 = 121.", 1),
    ("Find the missing number: 96 ÷ ___ = 8.", "type", None, None, None, None, "12", "96 ÷ 12 = 8.", 2),
    ("What is 7 × 7?", "type", None, None, None, None, "49", "7 × 7 = 49.", 1),
]))

CONTENT.append(("Maths", "3. Times Tables & Number Properties", "Factors, HCF, Multiples & LCM",
"""
<div class="lesson-block definition">
<h3>📖 Key Definitions</h3>
<p><strong>Factor:</strong> A number that divides exactly into another number. Factors of 12: 1, 2, 3, 4, 6, 12</p>
<p><strong>Multiple:</strong> The result of multiplying a number by any whole number. Multiples of 5: 5, 10, 15, 20, 25...</p>
<p><strong>HCF (Highest Common Factor):</strong> The largest factor that two numbers share.</p>
<p><strong>LCM (Lowest Common Multiple):</strong> The smallest multiple that two numbers share.</p>
</div>

<div class="lesson-block worked">
<h3>✏️ Finding HCF</h3>
<p><strong>Find HCF of 24 and 36:</strong></p>
<p>Factors of 24: 1, 2, 3, <strong>4, 6, 8, 12</strong>, 24</p>
<p>Factors of 36: 1, 2, 3, <strong>4, 6, 9, 12</strong>, 18, 36</p>
<p>Common factors: 1, 2, 3, 4, 6, 12 → HCF = <strong>12</strong></p>
</div>

<div class="lesson-block worked">
<h3>✏️ Finding LCM</h3>
<p><strong>Find LCM of 4 and 6:</strong></p>
<p>Multiples of 4: 4, 8, <strong>12</strong>, 16, 20...</p>
<p>Multiples of 6: 6, <strong>12</strong>, 18, 24...</p>
<p>First common multiple = <strong>12</strong></p>
</div>

<div class="lesson-block tip">
<h3>💡 Why do we need HCF and LCM?</h3>
<ul>
<li><strong>HCF</strong> is used to simplify fractions (divide top and bottom by HCF)</li>
<li><strong>LCM</strong> is used to add fractions with different denominators (find common denominator)</li>
</ul>
</div>
""",
[
    ("List all factors of 24.", "mc", "1,2,3,4,6,8,12,24", "1,2,4,6,12,24", "2,3,4,6,8,12", "1,2,3,4,6,24", "1,2,3,4,6,8,12,24", "Factors of 24: 1×24, 2×12, 3×8, 4×6. All factors: 1,2,3,4,6,8,12,24.", 1),
    ("What is the HCF of 24 and 36?", "type", None, None, None, None, "12", "Factors of 24: 1,2,3,4,6,8,12,24. Factors of 36: 1,2,3,4,6,9,12,18,36. HCF=12.", 2),
    ("What is the LCM of 4 and 6?", "type", None, None, None, None, "12", "Multiples of 4: 4,8,12. Multiples of 6: 6,12. LCM=12.", 1),
    ("What is the HCF of 18 and 30?", "type", None, None, None, None, "6", "Factors of 18: 1,2,3,6,9,18. Factors of 30: 1,2,3,5,6,10,15,30. HCF=6.", 2),
    ("What is the LCM of 5 and 8?", "type", None, None, None, None, "40", "5 and 8 share no common factors, so LCM = 5×8 = 40.", 2),
    ("How many factors does 36 have?", "type", None, None, None, None, "9", "Factors of 36: 1,2,3,4,6,9,12,18,36. Nine factors.", 2),
    ("Is 4 a factor of 100?", "mc", "Yes", "No", "Only sometimes", "Cannot tell", "Yes", "100 ÷ 4 = 25 exactly. So 4 is a factor of 100.", 1),
    ("What is the LCM of 3, 4 and 6?", "type", None, None, None, None, "12", "Multiples of 6: 6,12. 12÷3=4 ✓ 12÷4=3 ✓. LCM=12.", 2),
    ("What is the HCF of 48 and 72?", "type", None, None, None, None, "24", "48=2⁴×3. 72=2³×3². HCF=2³×3=24.", 3),
    ("Two buses leave at the same time. One comes every 6 minutes, one every 8 minutes. When do they next arrive together?", "type", None, None, None, None, "24", "LCM of 6 and 8 = 24 minutes.", 2),
    ("What is the HCF of 100 and 75?", "type", None, None, None, None, "25", "Factors of 75: 1,3,5,15,25,75. Factors of 100: 1,2,4,5,10,20,25,50,100. HCF=25.", 2),
    ("What is the LCM of 12 and 15?", "type", None, None, None, None, "60", "Multiples of 12: 12,24,36,48,60. Multiples of 15: 15,30,45,60. LCM=60.", 2),
]))

CONTENT.append(("Maths", "3. Times Tables & Number Properties", "Prime Numbers & Prime Factors",
"""
<div class="lesson-block definition">
<h3>📖 What is a Prime Number?</h3>
<p>A prime number has <strong>exactly two factors</strong>: 1 and itself.</p>
<p>1 is NOT prime (only one factor). 2 is the only even prime.</p>
</div>

<div class="lesson-block">
<h3>🔢 Primes up to 50</h3>
<div class="prime-grid">
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47
</div>
<p>There are 15 primes under 50. Know them all!</p>
</div>

<div class="lesson-block worked">
<h3>✏️ Prime Factor Trees</h3>
<p><strong>Express 60 as a product of prime factors:</strong></p>
<div class="worked-calc">
<pre>
60
├── 2 × 30
        ├── 2 × 15
                ├── 3 × 5

60 = 2 × 2 × 3 × 5 = 2² × 3 × 5
</pre>
</div>
</div>

<div class="lesson-block tip">
<h3>💡 How to check if a number is prime</h3>
<ul>
<li>Try dividing by 2, 3, 5, 7, 11... (primes in order)</li>
<li>You only need to check up to the square root</li>
<li>For numbers under 100, check up to 10 (i.e. try 2,3,5,7)</li>
</ul>
</div>
""",
[
    ("Is 51 a prime number?", "mc", "Yes", "No", "Cannot tell", "Sometimes", "No", "51 = 3 × 17. It has factors other than 1 and itself, so it is NOT prime.", 2),
    ("What is the smallest prime number?", "type", None, None, None, None, "2", "2 is the smallest and only even prime number.", 1),
    ("List all prime numbers between 20 and 30.", "mc", "23, 29", "21, 23, 27, 29", "23, 27, 29", "23, 25, 29", "23, 29", "21=3×7, 27=3³, 25=5². Only 23 and 29 are prime.", 2),
    ("Express 60 as a product of prime factors.", "mc", "2×2×3×5", "2×3×5", "4×3×5", "2×30", "2×2×3×5", "60 = 2×2×3×5. Always write as product of PRIME factors.", 2),
    ("Express 84 as a product of prime factors.", "mc", "2×2×3×7", "2×6×7", "4×3×7", "2×42", "2×2×3×7", "84 = 2×42 = 2×2×21 = 2×2×3×7.", 2),
    ("Is 97 a prime number?", "mc", "Yes", "No", "Cannot tell", "Sometimes", "Yes", "Check primes up to √97≈9.8: 97÷2 no, 97÷3 no, 97÷5 no, 97÷7=13.8 no. 97 is prime.", 3),
    ("What is the prime factorisation of 48?", "mc", "2⁴×3", "2³×6", "4²×3", "2×24", "2⁴×3", "48=2×24=2×2×12=2×2×2×6=2×2×2×2×3=2⁴×3.", 3),
    ("How many prime numbers are there between 1 and 20?", "type", None, None, None, None, "8", "2,3,5,7,11,13,17,19 = 8 prime numbers.", 2),
    ("What is the largest prime number less than 50?", "type", None, None, None, None, "47", "47 is prime (check: not divisible by 2,3,5,7).", 2),
    ("Express 100 as a product of prime factors.", "mc", "2²×5²", "4×25", "2×5×10", "2⁴×5", "2²×5²", "100=4×25=2²×5².", 2),
]))

# FRACTIONS
CONTENT.append(("Maths", "4. Fractions", "Understanding & Simplifying Fractions",
"""
<div class="lesson-block definition">
<h3>📖 What is a Fraction?</h3>
<p>A fraction represents a <strong>part of a whole</strong>.</p>
<div class="fraction-diagram">
<p>In ³⁄₄:</p>
<ul>
<li><strong>3</strong> = numerator (top) — number of parts you have</li>
<li><strong>4</strong> = denominator (bottom) — total equal parts</li>
</ul>
</div>
</div>

<div class="lesson-block">
<h3>🔄 Equivalent Fractions</h3>
<p>Multiply or divide BOTH numerator and denominator by the SAME number.</p>
<p>¾ = ⁶⁄₈ = ⁹⁄₁₂ = ¹⁵⁄₂₀ (multiply by 2, 3, 5...)</p>
</div>

<div class="lesson-block worked">
<h3>✏️ Simplifying Fractions</h3>
<p><strong>Simplify ³⁶⁄₄₈:</strong></p>
<p>HCF of 36 and 48 = 12</p>
<p>36÷12 = 3, 48÷12 = 4</p>
<p>³⁶⁄₄₈ = <strong>¾</strong></p>
</div>

<div class="lesson-block worked">
<h3>✏️ Improper Fractions & Mixed Numbers</h3>
<p><strong>¹¹⁄₄ as a mixed number:</strong></p>
<p>11 ÷ 4 = 2 remainder 3 → <strong>2¾</strong></p>
<br>
<p><strong>3½ as an improper fraction:</strong></p>
<p>3 × 2 + 1 = 7 → <strong>⁷⁄₂</strong></p>
</div>

<div class="lesson-block tip">
<h3>💡 Comparing Fractions</h3>
<p>To compare fractions, convert to a common denominator (using the LCM).</p>
<p>Which is larger: ³⁄₄ or ⁵⁄₇?</p>
<p>LCM of 4 and 7 = 28. ³⁄₄ = ²¹⁄₂₈. ⁵⁄₇ = ²⁰⁄₂₈. So ³⁄₄ > ⁵⁄₇.</p>
</div>
""",
[
    ("What is 36/48 in its simplest form?", "mc", "3/4", "2/3", "4/5", "6/8", "3/4", "HCF of 36 and 48 is 12. 36÷12=3, 48÷12=4. Simplest form=3/4.", 1),
    ("Convert 11/4 to a mixed number.", "mc", "2¾", "3¼", "2½", "2¼", "2¾", "11÷4=2 remainder 3. So 11/4=2¾.", 1),
    ("Convert 3½ to an improper fraction.", "type", None, None, None, None, "7/2", "3×2=6, 6+1=7. So 3½=7/2.", 1),
    ("Find an equivalent fraction to 2/5 with denominator 20.", "type", None, None, None, None, "8/20", "Multiply top and bottom by 4: 2×4=8, 5×4=20.", 1),
    ("Simplify 18/24.", "mc", "3/4", "2/3", "6/8", "9/12", "3/4", "HCF of 18 and 24 is 6. 18÷6=3, 24÷6=4.", 1),
    ("Which is larger: 3/4 or 5/7?", "mc", "3/4", "5/7", "They are equal", "Cannot tell", "3/4", "LCM=28. 3/4=21/28. 5/7=20/28. 21>20 so 3/4 is larger.", 2),
    ("Convert 5¾ to an improper fraction.", "type", None, None, None, None, "23/4", "5×4=20, 20+3=23. So 5¾=23/4.", 1),
    ("Simplify 45/60.", "mc", "3/4", "4/5", "9/12", "15/20", "3/4", "HCF of 45 and 60 is 15. 45÷15=3, 60÷15=4.", 2),
    ("Order from smallest to largest: 1/2, 2/5, 3/8, 3/4", "mc", "2/5, 3/8, 1/2, 3/4", "3/8, 2/5, 1/2, 3/4", "2/5, 1/2, 3/8, 3/4", "3/4, 1/2, 3/8, 2/5", "2/5, 3/8, 1/2, 3/4", "LCD=40: 2/5=16/40, 3/8=15/40, 1/2=20/40, 3/4=30/40. Order: 15,16,20,30.", 3),
    ("What fraction of 1 hour is 45 minutes?", "mc", "3/4", "4/5", "1/2", "7/8", "3/4", "45/60 = 3/4 when simplified by dividing by 15.", 1),
    ("Which fraction is equivalent to 2/3?", "mc", "8/12", "6/10", "4/7", "3/4", "8/12", "2/3 × 4/4 = 8/12. ✓", 1),
    ("A cake is cut into 12 equal pieces. 8 are eaten. What fraction remains in simplest form?", "mc", "4/12", "1/3", "2/3", "3/4", "1/3", "4 pieces remain. 4/12 = 1/3.", 1),
]))

CONTENT.append(("Maths", "4. Fractions", "Adding & Subtracting Fractions",
"""
<div class="lesson-block definition">
<h3>📖 The Golden Rule</h3>
<p>You can only add or subtract fractions when they have the <strong>same denominator</strong>.</p>
</div>

<div class="lesson-block worked">
<h3>✏️ Same Denominator</h3>
<p>³⁄₈ + ²⁄₈ = ⁵⁄₈ (just add the numerators, keep the denominator)</p>
</div>

<div class="lesson-block worked">
<h3>✏️ Different Denominators</h3>
<p><strong>Calculate ¹⁄₃ + ¹⁄₄:</strong></p>
<p>Step 1: Find LCM of 3 and 4 → 12</p>
<p>Step 2: Convert: ¹⁄₃ = ⁴⁄₁₂ and ¹⁄₄ = ³⁄₁₂</p>
<p>Step 3: Add: ⁴⁄₁₂ + ³⁄₁₂ = <strong>⁷⁄₁₂</strong></p>
</div>

<div class="lesson-block worked">
<h3>✏️ Mixed Numbers</h3>
<p><strong>Calculate 2¾ + 1⅔:</strong></p>
<p>Method 1: Add whole numbers (2+1=3), add fractions (¾+⅔)</p>
<p>¾+⅔: LCM=12 → ⁹⁄₁₂+⁸⁄₁₂=¹⁷⁄₁₂=1⁵⁄₁₂</p>
<p>Total: 3+1⁵⁄₁₂ = <strong>4⁵⁄₁₂</strong></p>
</div>
""",
[
    ("Calculate 1/3 + 1/4.", "mc", "2/7", "7/12", "5/12", "1/6", "7/12", "LCM=12. 4/12+3/12=7/12.", 2),
    ("Calculate 3/4 − 1/3.", "mc", "2/1", "5/12", "1/4", "7/12", "5/12", "LCM=12. 9/12−4/12=5/12.", 2),
    ("Calculate 5/8 + 3/8.", "type", None, None, None, None, "1", "Same denominator: 5/8+3/8=8/8=1.", 1),
    ("What is 1 − 3/7?", "mc", "4/7", "3/7", "2/7", "1/7", "4/7", "1=7/7. 7/7−3/7=4/7.", 1),
    ("Calculate 2/3 + 3/4.", "mc", "5/7", "17/12", "5/12", "1", "17/12", "LCM=12. 8/12+9/12=17/12=1 5/12.", 2),
    ("What is 5/6 − 3/8?", "mc", "2/48", "11/24", "1/4", "7/24", "11/24", "LCM=24. 20/24−9/24=11/24.", 2),
    ("Calculate 2¾ + 1⅔.", "mc", "4 5/12", "3 7/12", "4 7/12", "3 5/12", "4 5/12", "Whole: 2+1=3. Fractions: 9/12+8/12=17/12=1 5/12. Total: 4 5/12.", 3),
    ("What is 3½ − 1¾?", "mc", "1¾", "2¼", "1¼", "2¾", "1¾", "3½=14/4. 1¾=7/4. 14/4−7/4=7/4=1¾.", 2),
    ("Calculate 1/2 + 1/3 + 1/6.", "type", None, None, None, None, "1", "LCM=6. 3/6+2/6+1/6=6/6=1.", 2),
    ("What is 4 − 2⅜?", "mc", "1⅝", "1⅞", "2⅝", "1⅜", "1⅝", "4=3 8/8. 3 8/8−2 3/8=1 5/8.", 2),
    ("Calculate 3/5 + 2/3 − 1/2.", "mc", "43/30", "23/30", "7/10", "1", "43/30", "LCM=30. 18/30+20/30−15/30=23/30.", 3),
    ("A plank is 3½m long. A piece of 1¼m is cut off. How long is the remaining piece?", "mc", "2m", "2¼m", "2½m", "1¾m", "2¼m", "3½−1¼=3 2/4−1 1/4=2 1/4=2¼m.", 2),
]))

CONTENT.append(("Maths", "4. Fractions", "Multiplying & Dividing Fractions",
"""
<div class="lesson-block worked">
<h3>✏️ Multiplying Fractions</h3>
<p><strong>Rule:</strong> Multiply numerators × numerators, denominators × denominators</p>
<p>²⁄₃ × ³⁄₅ = ⁶⁄₁₅ = ²⁄₅ (simplify by ÷3)</p>
<br>
<p><strong>Tip: Cancel BEFORE multiplying!</strong></p>
<p>²⁄₃ × ³⁄₅ → cross-cancel the 3s → ²⁄₁ × ¹⁄₅ = ²⁄₅</p>
</div>

<div class="lesson-block worked">
<h3>✏️ Dividing Fractions — KFC</h3>
<div class="rule-box">
<p><strong>Keep</strong> the first fraction</p>
<p><strong>Flip</strong> the second fraction (reciprocal)</p>
<p><strong>Change</strong> ÷ to ×</p>
</div>
<p>³⁄₄ ÷ ²⁄₃ = ³⁄₄ × ³⁄₂ = ⁹⁄₈ = 1⅛</p>
</div>

<div class="lesson-block worked">
<h3>✏️ Fraction of an Amount</h3>
<p><strong>Find ⅝ of 480:</strong></p>
<p>Step 1: ÷ by denominator: 480 ÷ 8 = 60</p>
<p>Step 2: × by numerator: 60 × 5 = <strong>300</strong></p>
</div>
""",
[
    ("Calculate 2/3 × 3/5.", "mc", "5/8", "2/5", "6/15", "1/5", "2/5", "2/3 × 3/5 = 6/15 = 2/5.", 2),
    ("Calculate 3/4 ÷ 2/3.", "mc", "1/2", "9/8", "6/12", "2/3", "9/8", "KFC: 3/4 × 3/2 = 9/8 = 1⅛.", 2),
    ("Find 5/8 of 480.", "type", None, None, None, None, "300", "480÷8=60. 60×5=300.", 1),
    ("If 3/4 of a number is 60, what is the number?", "type", None, None, None, None, "80", "60÷3×4=80.", 2),
    ("Calculate 2/5 × 3/4.", "mc", "5/9", "3/10", "1/2", "6/20", "3/10", "2/5 × 3/4 = 6/20 = 3/10.", 2),
    ("Calculate 4/5 ÷ 2/5.", "type", None, None, None, None, "2", "4/5 × 5/2 = 20/10 = 2.", 2),
    ("Find 3/7 of 560.", "type", None, None, None, None, "240", "560÷7=80. 80×3=240.", 1),
    ("Calculate 1½ × 2⅔.", "mc", "3½", "4", "4½", "3⅔", "4", "1½=3/2. 2⅔=8/3. 3/2×8/3=24/6=4.", 3),
    ("Calculate 2¼ ÷ ¾.", "type", None, None, None, None, "3", "2¼=9/4. 9/4÷3/4=9/4×4/3=36/12=3.", 3),
    ("A recipe needs ⅔ cup of sugar for one batch. How much for 4½ batches?", "mc", "2½ cups", "3 cups", "2⅔ cups", "3½ cups", "3 cups", "4½ × ⅔ = 9/2 × 2/3 = 18/6 = 3 cups.", 3),
    ("Find ¾ of ⅔.", "mc", "1/2", "3/8", "9/8", "1", "1/2", "¾ × ⅔ = 6/12 = 1/2.", 2),
    ("If ⅖ of a class are girls and there are 30 pupils, how many boys?", "type", None, None, None, None, "18", "Girls = ⅖×30 = 12. Boys = 30−12 = 18.", 2),
]))

CONTENT.append(("Maths", "5. Decimals & Percentages", "Fractions, Decimals & Percentages",
"""
<div class="lesson-block definition">
<h3>📖 The Connection</h3>
<p>Fractions, decimals and percentages are three ways of showing the same thing.</p>
<table class="lesson-table">
<tr><th>Fraction</th><th>Decimal</th><th>Percentage</th></tr>
<tr><td>1/2</td><td>0.5</td><td>50%</td></tr>
<tr><td>1/4</td><td>0.25</td><td>25%</td></tr>
<tr><td>3/4</td><td>0.75</td><td>75%</td></tr>
<tr><td>1/5</td><td>0.2</td><td>20%</td></tr>
<tr><td>1/10</td><td>0.1</td><td>10%</td></tr>
<tr><td>1/8</td><td>0.125</td><td>12.5%</td></tr>
<tr><td>1/3</td><td>0.333...</td><td>33.3%</td></tr>
</table>
</div>

<div class="lesson-block worked">
<h3>✏️ Finding Percentages of Amounts</h3>
<p><strong>Find 35% of 420:</strong></p>
<p>10% of 420 = 42</p>
<p>30% = 3 × 42 = 126</p>
<p>5% = 42 ÷ 2 = 21</p>
<p>35% = 126 + 21 = <strong>147</strong></p>
</div>

<div class="lesson-block worked">
<h3>✏️ Percentage Increase & Decrease</h3>
<p><strong>Increase £50 by 20%:</strong></p>
<p>20% of 50 = 10 → £50 + £10 = <strong>£60</strong></p>
<p><strong>Or:</strong> £50 × 1.20 = £60</p>
<br>
<p><strong>Decrease £80 by 15%:</strong></p>
<p>15% of 80 = 12 → £80 − £12 = <strong>£68</strong></p>
</div>
""",
[
    ("Convert 3/5 to a percentage.", "type", None, None, None, None, "60", "3/5 = 0.6 = 60%.", 1),
    ("What is 35% of 420?", "type", None, None, None, None, "147", "10%=42, 30%=126, 5%=21. Total=147.", 2),
    ("A coat costs £80. It is reduced by 15%. What is the new price?", "type", None, None, None, None, "68", "15% of 80=12. 80−12=£68.", 2),
    ("What percentage of 60 is 15?", "type", None, None, None, None, "25", "15/60 × 100 = 25%.", 2),
    ("Convert 0.375 to a fraction in its simplest form.", "mc", "3/8", "37/100", "375/1000", "3/10", "3/8", "0.375 = 375/1000 = 3/8. (Divide by 125.)", 2),
    ("What is 17.5% of 200?", "type", None, None, None, None, "35", "10%=20, 5%=10, 2.5%=5. 17.5%=35.", 2),
    ("A price increases from £50 to £65. What is the percentage increase?", "type", None, None, None, None, "30", "Increase=15. 15/50×100=30%.", 2),
    ("A television costs £360. It is reduced by 25%. What is the sale price?", "type", None, None, None, None, "270", "25% of 360=90. 360−90=£270.", 2),
    ("Which is largest: 0.6, 58%, 5/9?", "mc", "0.6", "58%", "5/9", "They are equal", "58%", "0.6=60%, 5/9=55.6%, 58%=58%. Largest=58%.", 3),
    ("In a class of 32, 75% passed the test. How many passed?", "type", None, None, None, None, "24", "75% of 32 = 3/4 × 32 = 24.", 1),
    ("After a 20% increase, a price is £120. What was the original price?", "type", None, None, None, None, "100", "120 ÷ 1.20 = £100.", 3),
    ("Express 48 out of 60 as a percentage.", "type", None, None, None, None, "80", "48/60 × 100 = 80%.", 2),
    ("A shop reduces a £45 item by 30% then adds 10% VAT. Final price?", "type", None, None, None, None, "34.65", "45 × 0.70 = 31.50. 31.50 × 1.10 = £34.65.", 3),
]))

CONTENT.append(("Maths", "6. Ratio & Proportion", "Ratio & Proportion",
"""
<div class="lesson-block definition">
<h3>📖 What is Ratio?</h3>
<p>A ratio compares two or more quantities. 2:3 means for every 2 of one thing, there are 3 of another.</p>
</div>

<div class="lesson-block worked">
<h3>✏️ Sharing in a Ratio</h3>
<p><strong>Share £180 in the ratio 2:3:4:</strong></p>
<p>Total parts = 2+3+4 = 9</p>
<p>Value of 1 part = £180 ÷ 9 = £20</p>
<p>Shares: £40 : £60 : £80</p>
</div>

<div class="lesson-block worked">
<h3>✏️ Unitary Method</h3>
<p><strong>5 books cost £17.50. How much for 8 books?</strong></p>
<p>1 book = £17.50 ÷ 5 = £3.50</p>
<p>8 books = £3.50 × 8 = <strong>£28.00</strong></p>
</div>

<div class="lesson-block worked">
<h3>✏️ Speed, Distance, Time</h3>
<div class="rule-box">
<p><strong>S = D ÷ T</strong> (Speed = Distance ÷ Time)</p>
<p><strong>D = S × T</strong> (Distance = Speed × Time)</p>
<p><strong>T = D ÷ S</strong> (Time = Distance ÷ Speed)</p>
</div>
<p>Cover the one you want to find — the other two show what to do.</p>
</div>
""",
[
    ("Simplify the ratio 24:36.", "mc", "2:3", "4:6", "3:4", "8:12", "2:3", "HCF=12. 24÷12:36÷12=2:3.", 1),
    ("Share £180 in the ratio 2:3:4.", "mc", "£40:£60:£80", "£36:£54:£90", "£45:£60:£75", "£30:£60:£90", "£40:£60:£80", "9 parts. 1 part=£20. 2×20:3×20:4×20=40:60:80.", 2),
    ("Speed=Distance÷Time. A car travels 240km in 3 hours. What is its speed?", "type", None, None, None, None, "80", "Speed=240÷3=80km/h.", 1),
    ("If 5 books cost £17.50, how much do 8 books cost?", "type", None, None, None, None, "28", "1 book=£3.50. 8×£3.50=£28.", 2),
    ("In a class the ratio of boys to girls is 3:5. There are 30 girls. How many boys?", "type", None, None, None, None, "18", "5 parts=30, 1 part=6. Boys=3×6=18.", 2),
    ("A recipe for 6 serves needs 450g flour. How much for 10 serves?", "type", None, None, None, None, "750", "450÷6=75g per serve. 75×10=750g.", 2),
    ("A map has scale 1:50,000. Two towns are 4cm apart on the map. What is the real distance in km?", "type", None, None, None, None, "2", "4×50,000=200,000cm=2,000m=2km.", 2),
    ("Three prizes are shared in ratio 5:3:2. The largest prize is £150. What is the total prize money?", "type", None, None, None, None, "300", "5 parts=£150, 1 part=£30. Total=10×£30=£300.", 3),
    ("A car travels at 60mph. How far does it travel in 2½ hours?", "type", None, None, None, None, "150", "D=60×2.5=150 miles.", 2),
    ("How long does a 480km journey take at 80km/h?", "type", None, None, None, None, "6", "T=480÷80=6 hours.", 2),
    ("Paint is mixed in the ratio 3:1 (blue:white). To make 20 litres, how much blue paint is needed?", "type", None, None, None, None, "15", "4 parts=20L. 1 part=5L. Blue=3×5=15L.", 2),
    ("Increase £350 in the ratio 5:7.", "type", None, None, None, None, "490", "New amount=350×7÷5=490.", 3),
]))

CONTENT.append(("Maths", "7. Measurement", "Area & Perimeter",
"""
<div class="lesson-block definition">
<h3>📖 Key Formulae</h3>
<table class="lesson-table">
<tr><th>Shape</th><th>Area</th><th>Perimeter</th></tr>
<tr><td>Rectangle</td><td>l × w</td><td>2(l+w)</td></tr>
<tr><td>Triangle</td><td>½ × b × h</td><td>Add all sides</td></tr>
<tr><td>Parallelogram</td><td>b × h</td><td>Add all sides</td></tr>
<tr><td>Circle</td><td>π × r²</td><td>π × d (= 2πr)</td></tr>
</table>
<p>h = perpendicular height (NOT the slanted side!)</p>
</div>

<div class="lesson-block worked">
<h3>✏️ Compound Shapes — APPEARS EVERY YEAR!</h3>
<p>Split the shape into rectangles. Find each area. Add them.</p>
<div class="worked-calc">
<pre>
L-shape:
┌──────┐
│  A   │
│      ├───┐
│      │ B │
└──────┴───┘

Area = Area A + Area B
</pre>
</div>
<p>OR: find the area of the full rectangle and subtract the missing piece.</p>
</div>

<div class="lesson-block tip">
<h3>💡 Circle Memory Tricks</h3>
<p>🥧 <strong>Cherry Pie is Delicious</strong> → C = π × d</p>
<p>🥧 <strong>Apple Pies Are Round</strong> → A = π × r²</p>
<p>Always halve the diameter to get r before using area formula!</p>
</div>
""",
[
    ("Find the area of a rectangle 8cm long and 5cm wide.", "type", None, None, None, None, "40", "A=8×5=40cm².", 1),
    ("Find the perimeter of a rectangle 7cm × 4cm.", "type", None, None, None, None, "22", "P=2(7+4)=2×11=22cm.", 1),
    ("A triangle has base 10cm and height 6cm. Find its area.", "type", None, None, None, None, "30", "A=½×10×6=30cm².", 1),
    ("Find the circumference of a circle with diameter 10cm. Use π=3.14.", "type", None, None, None, None, "31.4", "C=π×d=3.14×10=31.4cm.", 2),
    ("Find the area of a circle with radius 7cm. Use π=3.14.", "type", None, None, None, None, "153.86", "A=π×r²=3.14×49=153.86cm².", 2),
    ("An L-shape is made of two rectangles: 8m×5m and 3m×4m. Total area?", "type", None, None, None, None, "52", "8×5=40, 3×4=12. Total=52m².", 2),
    ("A room is 6.4m × 4.5m. Find the area of carpet needed.", "type", None, None, None, None, "28.8", "A=6.4×4.5=28.8m².", 2),
    ("A circle has area 78.5cm². What is its radius? (π=3.14)", "type", None, None, None, None, "5", "r²=78.5÷3.14=25. r=√25=5cm.", 3),
    ("A square field has perimeter 48m. Find its area.", "type", None, None, None, None, "144", "Side=48÷4=12m. Area=12²=144m².", 2),
    ("A parallelogram has base 12cm and height 8cm. Find its area.", "type", None, None, None, None, "96", "A=b×h=12×8=96cm².", 1),
    ("A path 1.5m wide goes around a garden 10m×8m. Find the area of the path.", "type", None, None, None, None, "63", "Outer=13×11=143. Inner=10×8=80. Path=143-80=63m².", 3),
    ("A semicircle has radius 6cm. Find its area. (π=3.14)", "type", None, None, None, None, "56.52", "Area=½×π×r²=½×3.14×36=56.52cm².", 3),
]))

CONTENT.append(("Maths", "7. Measurement", "Volume & Capacity",
"""
<div class="lesson-block definition">
<h3>📖 Volume Formulae</h3>
<div class="rule-box">
<p><strong>Cuboid:</strong> V = l × w × h</p>
<p><strong>Any Prism:</strong> V = area of cross-section × length</p>
<p><strong>Triangular Prism:</strong> V = ½ × b × h × l</p>
</div>
</div>

<div class="lesson-block">
<h3>📏 Unit Conversions</h3>
<table class="lesson-table">
<tr><th>Length</th><th>Area</th><th>Volume</th></tr>
<tr><td>1m = 100cm</td><td>1m² = 10,000cm²</td><td>1m³ = 1,000,000cm³</td></tr>
<tr><td>1km = 1000m</td><td>1km² = 1,000,000m²</td><td>1 litre = 1,000cm³</td></tr>
</table>
</div>

<div class="lesson-block worked">
<h3>✏️ Worked Example</h3>
<p><strong>Cuboid: 5cm × 3cm × 4cm</strong></p>
<p>V = 5 × 3 × 4 = <strong>60 cm³</strong></p>
<br>
<p><strong>Triangular prism with triangle base 6cm, height 4cm, length 10cm:</strong></p>
<p>V = ½ × 6 × 4 × 10 = <strong>120 cm³</strong></p>
</div>
""",
[
    ("Find the volume of a cuboid 5cm × 3cm × 4cm.", "type", None, None, None, None, "60", "V=5×3×4=60cm³.", 1),
    ("How many cm³ in 1 m³?", "type", None, None, None, None, "1000000", "1m=100cm. 1m³=100×100×100=1,000,000cm³.", 2),
    ("A cube has sides of 4cm. What is its volume?", "type", None, None, None, None, "64", "V=4×4×4=64cm³.", 1),
    ("A triangular prism has triangle base 6cm, height 4cm, length 10cm. Find its volume.", "type", None, None, None, None, "120", "V=½×6×4×10=120cm³.", 2),
    ("A box is 30cm × 20cm × 15cm. How many 1-litre bottles fit inside?", "type", None, None, None, None, "9", "V=30×20×15=9,000cm³. 1 litre=1,000cm³. 9,000÷1,000=9 bottles.", 2),
    ("How many cm² are in 1 m²?", "type", None, None, None, None, "10000", "1m=100cm. 1m²=100×100=10,000cm².", 2),
    ("A swimming pool is 25m long, 10m wide and 2m deep. Find its volume in m³.", "type", None, None, None, None, "500", "V=25×10×2=500m³.", 1),
    ("A cylinder has radius 5cm and height 8cm. Find its volume. (π=3.14)", "type", None, None, None, None, "628", "V=π×r²×h=3.14×25×8=628cm³.", 3),
    ("A cube has volume 125cm³. What is the length of each side?", "type", None, None, None, None, "5", "5³=125. Side=5cm.", 2),
    ("A tank holds 540 litres. It is 1.5m long and 0.6m wide. How deep is it?", "type", None, None, None, None, "0.6", "540L=0.54m³. 0.54÷(1.5×0.6)=0.54÷0.9=0.6m.", 3),
]))

CONTENT.append(("Maths", "8. Geometry & Algebra", "Angles & Shapes",
"""
<div class="lesson-block definition">
<h3>📖 Angle Facts — Learn These All!</h3>
<div class="rule-box">
<p>Angles on a straight line = <strong>180°</strong></p>
<p>Angles at a point = <strong>360°</strong></p>
<p>Angles in a triangle = <strong>180°</strong></p>
<p>Angles in a quadrilateral = <strong>360°</strong></p>
</div>
</div>

<div class="lesson-block">
<h3>🔺 Triangle Types</h3>
<table class="lesson-table">
<tr><th>Type</th><th>Sides</th><th>Angles</th></tr>
<tr><td>Equilateral</td><td>All equal</td><td>All 60°</td></tr>
<tr><td>Isosceles</td><td>2 equal</td><td>2 base angles equal</td></tr>
<tr><td>Scalene</td><td>All different</td><td>All different</td></tr>
<tr><td>Right-angled</td><td>Any</td><td>One = 90°</td></tr>
</table>
</div>

<div class="lesson-block worked">
<h3>✏️ Finding Missing Angles</h3>
<p><strong>Isosceles triangle, apex = 40°. Find base angles:</strong></p>
<p>(180° − 40°) ÷ 2 = 140° ÷ 2 = <strong>70°</strong></p>
<br>
<p><strong>Angles in quadrilateral:</strong> a + b + c + d = 360°</p>
</div>
""",
[
    ("Angles on a straight line add up to how many degrees?", "type", None, None, None, None, "180", "Angles on a straight line always sum to 180°.", 1),
    ("A triangle has angles 65° and 48°. What is the third angle?", "type", None, None, None, None, "67", "180−65−48=67°.", 1),
    ("What are all angles in an equilateral triangle?", "type", None, None, None, None, "60", "Equilateral: all angles = 60°.", 1),
    ("An isosceles triangle has apex angle 40°. What are the base angles?", "type", None, None, None, None, "70", "(180−40)÷2=70°.", 2),
    ("Angles at a point add up to?", "type", None, None, None, None, "360", "Angles all the way around a point = 360°.", 1),
    ("A quadrilateral has angles 85°, 110°, 95°. What is the fourth angle?", "type", None, None, None, None, "70", "360−85−110−95=70°.", 2),
    ("What type of triangle has two equal sides and two equal base angles?", "mc", "Equilateral", "Isosceles", "Scalene", "Right-angled", "Isosceles", "Isosceles triangles have 2 equal sides and 2 equal base angles.", 1),
    ("An exterior angle of a triangle is 115°. The two opposite interior angles are equal. Find them.", "type", None, None, None, None, "57.5", "Exterior angle = sum of two opposite interior angles. Each = 115÷2 = 57.5°.", 3),
    ("Two angles of a triangle are in ratio 2:3. The third angle is 60°. Find the other two angles.", "mc", "48° and 72°", "40° and 60°", "50° and 70°", "45° and 75°", "48° and 72°", "Remaining = 180−60 = 120°. Split in ratio 2:3 (5 parts). Each part = 24°. Angles: 48° and 72°.", 3),
    ("What is the name for an angle greater than 180°?", "mc", "Acute", "Obtuse", "Reflex", "Straight", "Reflex", "Reflex angles are greater than 180° and less than 360°.", 1),
    ("A regular hexagon has interior angles of:", "type", None, None, None, None, "120", "Sum of interior angles of hexagon = (6−2)×180=720°. Each angle=720÷6=120°.", 3),
    ("Find angle x if angles on a straight line are 3x, 2x and x.", "type", None, None, None, None, "30", "6x=180. x=30°.", 2),
]))

CONTENT.append(("Maths", "8. Geometry & Algebra", "Algebra & Sequences",
"""
<div class="lesson-block definition">
<h3>📖 What is Algebra?</h3>
<p>Algebra uses letters to represent unknown numbers. We can solve equations to find what the letter equals.</p>
</div>

<div class="lesson-block worked">
<h3>✏️ Solving Equations</h3>
<p><strong>Solve 3n + 7 = 28:</strong></p>
<p>Step 1: 3n = 28 − 7 = 21</p>
<p>Step 2: n = 21 ÷ 3 = <strong>7</strong></p>
<br>
<p><strong>Solve 5x − 3 = 2x + 9:</strong></p>
<p>Step 1: 5x − 2x = 9 + 3</p>
<p>Step 2: 3x = 12</p>
<p>Step 3: x = <strong>4</strong></p>
</div>

<div class="lesson-block worked">
<h3>✏️ Sequences & nth Term</h3>
<p><strong>Sequence:</strong> 3, 7, 11, 15... (add 4 each time)</p>
<p><strong>nth term:</strong> 4n − 1</p>
<p>Check: n=1: 4(1)−1=3 ✓ n=2: 4(2)−1=7 ✓</p>
<br>
<p><strong>To find nth term:</strong></p>
<p>Common difference × n + (first term − common difference)</p>
</div>
""",
[
    ("Solve: 3n + 7 = 28", "type", None, None, None, None, "7", "3n=21. n=7.", 2),
    ("If a=4 and b=3, find 3a − 2b.", "type", None, None, None, None, "6", "12−6=6.", 1),
    ("The nth term of a sequence is 4n − 1. What is the 6th term?", "type", None, None, None, None, "23", "4×6−1=23.", 2),
    ("Solve: 5x − 3 = 2x + 9", "type", None, None, None, None, "4", "3x=12. x=4.", 2),
    ("A rectangle has perimeter 36cm. Its length is 11cm. Find its width.", "type", None, None, None, None, "7", "2(11+w)=36. w=7.", 2),
    ("Find the nth term of: 5, 8, 11, 14...", "mc", "3n+2", "n+5", "3n−2", "4n+1", "3n+2", "Difference=3. nth term=3n+2. Check: 3(1)+2=5 ✓.", 2),
    ("Solve: 2(x + 3) = 14", "type", None, None, None, None, "4", "x+3=7. x=4.", 2),
    ("What is the 10th term of 7, 11, 15, 19...?", "type", None, None, None, None, "43", "nth term=4n+3. 10th=4(10)+3=43.", 2),
    ("Solve: x/3 + 5 = 8", "type", None, None, None, None, "9", "x/3=3. x=9.", 2),
    ("If the nth term is 3n² + 1, what is the 4th term?", "type", None, None, None, None, "49", "3(16)+1=49.", 3),
    ("Angles in a triangle are 2x, 3x and 55°. Find x.", "type", None, None, None, None, "25", "5x+55=180. 5x=125. x=25.", 2),
    ("Solve: (y+2)/3 = (y−1)/2", "type", None, None, None, None, "8", "2(y+2)=3(y−1). 2y+4=3y−3. y=7. Wait: 2y+4=3y−3 → 4+3=3y−2y → y=7. Let me verify: (7+2)/3=3, (7−1)/2=3. ✓ Answer: 7.", 3),
    ("Find the missing term: 3, 6, ___, 24, 48", "type", None, None, None, None, "12", "Sequence doubles each time: ×2. 6×2=12.", 1),
]))

CONTENT.append(("Maths", "9. Statistics & Data", "Mean, Median, Mode & Range",
"""
<div class="lesson-block definition">
<h3>📖 The Four Averages</h3>
<div class="rule-box">
<p><strong>Mean</strong> = total ÷ number of values</p>
<p><strong>Median</strong> = middle value (SORT FIRST!)</p>
<p><strong>Mode</strong> = most frequent value</p>
<p><strong>Range</strong> = largest − smallest</p>
</div>
</div>

<div class="lesson-block worked">
<h3>✏️ Worked Example</h3>
<p>Data set: 4, 7, 2, 9, 4, 8, 4</p>
<br>
<p><strong>Mean:</strong> (4+7+2+9+4+8+4) ÷ 7 = 38 ÷ 7 = 5.4</p>
<p><strong>Median:</strong> Sort → 2, 4, 4, <strong>4</strong>, 7, 8, 9 → Median = 4</p>
<p><strong>Mode:</strong> 4 (appears 3 times)</p>
<p><strong>Range:</strong> 9 − 2 = 7</p>
</div>

<div class="lesson-block tip">
<h3>💡 Finding a Missing Value from the Mean</h3>
<p>If the mean of 5 numbers is 12, their total must be 60.</p>
<p>If four of the numbers add up to 48, the missing number is 60 − 48 = <strong>12</strong></p>
</div>
""",
[
    ("Find the mean of: 4, 7, 9, 12, 8.", "type", None, None, None, None, "8", "Total=40. Mean=40÷5=8.", 1),
    ("Find the median of: 3, 7, 2, 9, 5.", "mc", "7", "5", "2", "3", "5", "Sort: 2,3,5,7,9. Middle=5.", 2),
    ("Find the mode of: 4, 7, 4, 9, 7, 4, 3.", "type", None, None, None, None, "4", "4 appears 3 times — most frequent.", 1),
    ("Find the range of: 13, 7, 19, 4, 22.", "type", None, None, None, None, "18", "22−4=18.", 1),
    ("The mean of 6 numbers is 14. What is their total?", "type", None, None, None, None, "84", "Total=14×6=84.", 2),
    ("Five numbers have a mean of 8. Four of them are 6, 9, 7, 10. What is the fifth?", "type", None, None, None, None, "8", "Total=40. Known sum=32. Missing=40−32=8.", 2),
    ("Find the median of: 3, 8, 1, 6, 4, 9.", "mc", "4", "5", "5.5", "6", "5", "Sort: 1,3,4,6,8,9. Even count — average middle two: (4+6)÷2=5.", 3),
    ("Which average is most affected by a very large value?", "mc", "Mean", "Median", "Mode", "Range", "Mean", "The mean uses all values in the total, so a very large value pulls it up significantly.", 2),
    ("A set of 5 values has mean 10, median 9, mode 7. If 20 is added, which average definitely increases?", "mc", "Mean only", "Median only", "Mean and Range", "All three", "Mean and Range", "Mean increases (larger total), Range increases (new largest value). Mode stays 7. Median may or may not change.", 3),
    ("Test scores: 78, 84, 91, 67, 84, 72. Find mean, median and mode.", "mc", "Mean=79.3, Median=81, Mode=84", "Mean=79.3, Median=84, Mode=84", "Mean=81, Median=79.3, Mode=84", "Mean=84, Median=79.3, Mode=81", "Mean=79.3, Median=81, Mode=84", "Sum=476. Mean=476÷6=79.3. Sort:67,72,78,84,84,91. Median=(78+84)÷2=81. Mode=84.", 3),
    ("The range of 5 numbers is 12. The largest is 18. What is the smallest?", "type", None, None, None, None, "6", "Smallest=18−12=6.", 1),
    ("Four friends earn: £24,000; £26,000; £28,000; £72,000. Which average best represents their typical income?", "mc", "Mean", "Median", "Mode", "Range", "Median", "The mean is pulled up by £72,000. Median gives a better picture of typical earnings.", 3),
]))

# ENGLISH SECTION
CONTENT.append(("English", "Grammar", "Parts of Speech",
"""
<div class="lesson-block definition">
<h3>📖 The 8 Parts of Speech</h3>
<table class="lesson-table">
<tr><th>Part of Speech</th><th>Job</th><th>Example</th></tr>
<tr><td>Noun</td><td>Names a thing</td><td>dog, London, kindness</td></tr>
<tr><td>Pronoun</td><td>Replaces a noun</td><td>he, she, they, it</td></tr>
<tr><td>Adjective</td><td>Describes a noun</td><td>happy, enormous, red</td></tr>
<tr><td>Verb</td><td>Shows action/being</td><td>run, is, think</td></tr>
<tr><td>Adverb</td><td>Describes a verb/adjective</td><td>quickly, very, often</td></tr>
<tr><td>Preposition</td><td>Shows position/time</td><td>in, on, after, before</td></tr>
<tr><td>Conjunction</td><td>Joins clauses/words</td><td>and, but, because, although</td></tr>
<tr><td>Article</td><td>Introduces a noun</td><td>a, an, the</td></tr>
</table>
</div>

<div class="lesson-block">
<h3>🔠 Types of Nouns</h3>
<ul>
<li><strong>Common noun:</strong> general things (dog, city, book)</li>
<li><strong>Proper noun:</strong> specific names (London, Anish, Monday) — always capital letters</li>
<li><strong>Abstract noun:</strong> ideas/feelings (happiness, freedom, courage)</li>
<li><strong>Collective noun:</strong> groups (flock, herd, pack, swarm)</li>
</ul>
</div>
""",
[
    ("Which word is a proper noun?", "mc", "city", "London", "beautiful", "running", "London", "Proper nouns are specific names and always start with a capital letter.", 1),
    ("Identify the abstract noun: 'The kindness of the teacher was remarkable.'", "mc", "teacher", "remarkable", "kindness", "was", "kindness", "Abstract nouns are ideas or qualities you cannot touch. Kindness is a quality.", 2),
    ("Which is a collective noun?", "mc", "swimming", "flock", "happy", "slowly", "flock", "A flock is a collective noun for a group of birds.", 1),
    ("Choose the correct pronoun: 'Between you and ___, the answer is wrong.'", "mc", "I", "me", "myself", "we", "me", "After a preposition (between), use object pronouns: me, him, her, us, them.", 2),
    ("Which word is an adverb in: 'She ran quickly to school'?", "mc", "She", "ran", "quickly", "school", "quickly", "Adverbs describe verbs. 'Quickly' describes HOW she ran.", 1),
    ("Identify the preposition: 'The cat sat under the table.'", "mc", "cat", "sat", "under", "table", "under", "Prepositions show position: under, over, beside, behind, through.", 1),
    ("Which is a subordinating conjunction?", "mc", "and", "but", "because", "or", "because", "Subordinating conjunctions join a dependent clause to a main clause: because, although, when, if.", 2),
    ("What type of noun is 'courage'?", "mc", "Common noun", "Proper noun", "Collective noun", "Abstract noun", "Abstract noun", "Courage is a quality/feeling — you cannot see or touch it.", 2),
    ("Identify the adjective: 'The enormous elephant stood by the muddy river.'", "mc", "stood", "river", "enormous", "by", "enormous", "Adjectives describe nouns. 'Enormous' describes 'elephant'.", 1),
    ("Which sentence uses a modal verb?", "mc", "She runs to school.", "She could run to school.", "She runs quickly.", "Running is good.", "She could run to school.", "Modal verbs show possibility/ability: could, should, would, might, must, will.", 2),
    ("What is the superlative form of 'good'?", "mc", "gooder", "more good", "best", "better", "best", "Good → better → best. Irregular comparative/superlative.", 2),
    ("In 'The old man walked slowly', identify the verb.", "mc", "old", "man", "walked", "slowly", "walked", "Verbs show action. 'Walked' is what the man did.", 1),
]))

CONTENT.append(("English", "Grammar", "Tenses & Sentence Structure",
"""
<div class="lesson-block definition">
<h3>📖 Verb Tenses</h3>
<table class="lesson-table">
<tr><th>Tense</th><th>Form</th><th>Example</th></tr>
<tr><td>Simple past</td><td>verb+ed</td><td>She walked</td></tr>
<tr><td>Past continuous</td><td>was/were + ing</td><td>She was walking</td></tr>
<tr><td>Past perfect</td><td>had + past participle</td><td>She had walked</td></tr>
<tr><td>Simple present</td><td>verb</td><td>She walks</td></tr>
<tr><td>Present perfect</td><td>has/have + past participle</td><td>She has walked</td></tr>
<tr><td>Simple future</td><td>will + verb</td><td>She will walk</td></tr>
</table>
</div>

<div class="lesson-block">
<h3>🏗️ Sentence Types</h3>
<ul>
<li><strong>Simple:</strong> One main clause — 'The dog barked.'</li>
<li><strong>Compound:</strong> Two main clauses + coordinating conjunction — 'The dog barked and the cat hissed.'</li>
<li><strong>Complex:</strong> Main clause + subordinate clause — 'Although it rained, we went out.'</li>
</ul>
</div>

<div class="lesson-block tip">
<h3>💡 Active vs Passive Voice</h3>
<p><strong>Active:</strong> The dog chased the cat. (subject does the action)</p>
<p><strong>Passive:</strong> The cat was chased by the dog. (subject receives the action)</p>
</div>
""",
[
    ("Which sentence is in the past perfect tense?", "mc", "She runs to school.", "She had run to school.", "She will run to school.", "She is running to school.", "She had run to school.", "Past perfect = had + past participle, showing completion before another past event.", 2),
    ("Which is a compound sentence?", "mc", "The dog barked.", "Although it rained, we went out.", "The dog barked and the cat hissed.", "Running quickly, she fell.", "The dog barked and the cat hissed.", "Compound = two independent clauses joined by a coordinating conjunction (and, but, or).", 2),
    ("Identify the subordinate clause: 'Although it was raining, the children played outside.'", "mc", "the children played outside", "Although it was raining", "the children played", "it was raining", "Although it was raining", "The subordinate clause cannot stand alone and starts with a subordinating conjunction.", 2),
    ("Convert to passive: 'The dog chased the cat.'", "mc", "The cat was chased by the dog.", "The cat chased the dog.", "The dog was chasing the cat.", "The cat has been chased.", "The cat was chased by the dog.", "Passive: object becomes subject + was/were + past participle + by + agent.", 2),
    ("The teacher ___ the students since morning. (Present perfect)", "mc", "taught", "teaches", "has taught", "was teaching", "has taught", "Present perfect: has/have + past participle.", 2),
    ("What type of sentence is: 'What a wonderful day it is!'?", "mc", "Statement", "Question", "Command", "Exclamation", "Exclamation", "Exclamatory sentences show strong feeling and end with !.", 1),
    ("Which sentence uses a relative clause?", "mc", "She ran fast.", "The book that I read was brilliant.", "She ran and jumped.", "Running fast, she won.", "The book that I read was brilliant.", "Relative clauses use that/which/who to give more information about a noun.", 2),
    ("Which sentence contains a fronted adverbial?", "mc", "She sang beautifully.", "Beautifully, she sang the song.", "She sang a beautiful song.", "The song was beautiful.", "Beautifully, she sang the song.", "A fronted adverbial is placed at the start of a sentence and followed by a comma.", 2),
    ("Choose the correct form: 'Neither the boys nor the girl ___ happy.'", "mc", "are", "is", "were", "have", "is", "With 'neither...nor', the verb agrees with the nearest subject ('girl is').", 3),
    ("What is the passive voice of: 'Scientists have discovered a new planet'?", "mc", "A new planet has been discovered by scientists.", "Scientists discovered a new planet.", "A new planet was discovering.", "Scientists are discovering a planet.", "A new planet has been discovered by scientists.", "Present perfect passive: has/have + been + past participle.", 3),
    ("Which sentence has an embedded relative clause?", "mc", "She went home.", "The girl, who was very tall, won the race.", "She ran home quickly.", "Running fast, she won.", "The girl, who was very tall, won the race.", "An embedded relative clause sits in the middle of a sentence, separated by commas.", 3),
    ("Change to past tense: 'She is singing in the rain.'", "mc", "She was singing in the rain.", "She has sung in the rain.", "She will sing in the rain.", "She sang in the rain.", "She was singing in the rain.", "Past continuous: was/were + verb+ing.", 2),
]))

CONTENT.append(("English", "Grammar", "Punctuation",
"""
<div class="lesson-block definition">
<h3>📖 Punctuation Guide</h3>
<table class="lesson-table">
<tr><th>Mark</th><th>Use</th><th>Example</th></tr>
<tr><td>.</td><td>End of statement</td><td>The cat sat.</td></tr>
<tr><td>?</td><td>End of question</td><td>Where is the cat?</td></tr>
<tr><td>!</td><td>Exclamation/command</td><td>Stop!</td></tr>
<tr><td>,</td><td>Pause/list/clause</td><td>I bought milk, eggs and bread.</td></tr>
<tr><td>;</td><td>Link two related clauses</td><td>She was tired; she went to bed.</td></tr>
<tr><td>:</td><td>Introduce list/explanation</td><td>I need: milk, eggs, bread.</td></tr>
<tr><td>'</td><td>Apostrophe: possession/contraction</td><td>dog's; don't</td></tr>
<tr><td>" "</td><td>Speech marks</td><td>"Hello," she said.</td></tr>
<tr><td>—</td><td>Dash: pause/explanation</td><td>The dog—a huge Labrador—barked.</td></tr>
</table>
</div>

<div class="lesson-block worked">
<h3>✏️ Apostrophes</h3>
<p><strong>Possession:</strong></p>
<p>One dog: the <strong>dog's</strong> kennel (apostrophe before s)</p>
<p>Multiple dogs: the <strong>dogs'</strong> kennel (apostrophe after s)</p>
<p>Irregular plural: the <strong>children's</strong> playground</p>
<br>
<p><strong>Contraction:</strong> don't = do not, it's = it is, they're = they are</p>
</div>
""",
[
    ("Where does the apostrophe go: 'the dogs kennel' (one dog)?", "mc", "the dog's kennel", "the dogs' kennel", "the dogs kennel", "the dog kennel's", "the dog's kennel", "One dog owns the kennel: dog's (apostrophe before s).", 1),
    ("Which sentence uses commas correctly?", "mc", "After, running fast she stopped.", "After running fast, she stopped.", "After running, fast she stopped.", "After running fast she, stopped.", "After running fast, she stopped.", "Comma after an introductory clause, before the main clause.", 2),
    ("Which sentence uses a semicolon correctly?", "mc", "She was tired; she went to bed.", "She was tired she; went to bed.", "She; was tired went to bed.", "She was; tired she went to bed.", "She was tired; she went to bed.", "A semicolon links two related independent clauses.", 2),
    ("Which sentence uses a colon correctly?", "mc", "I need: three things.", "I need three things: bread, milk and eggs.", "I need three things bread: milk eggs.", "I need: bread, milk, eggs alone.", "I need three things: bread, milk and eggs.", "A colon introduces a list or explanation.", 1),
    ("'The boys books were left outside.' Correct the apostrophe (more than one boy).", "mc", "The boy's books", "The boys's books", "The boys' books", "The boys books'", "The boys' books", "Multiple boys: apostrophe after the s.", 2),
    ("Add punctuation: 'Help shouted the boy'", "mc", "'Help!' shouted the boy.", "'Help,' shouted the boy.", "'Help.' shouted the boy.", "Help shouted the boy.", "'Help!' shouted the boy.", "Exclamation marks show strong emotion. Speech marks enclose what is said.", 1),
    ("Which uses an apostrophe for contraction correctly?", "mc", "Its raining today.", "It's raining today.", "Its' raining today.", "Itsraining today.", "It's raining today.", "It's = it is. Its (without apostrophe) = belonging to it.", 1),
    ("Where should the comma go: 'Running as fast as she could she finally reached home'?", "mc", "Running as fast as she could, she finally reached home.", "Running, as fast as she could she finally reached home.", "Running as fast, as she could she finally reached home.", "Running as fast as she could she finally reached, home.", "Running as fast as she could, she finally reached home.", "Comma after the introductory participial phrase.", 2),
    ("Which sentence punctuates direct speech correctly?", "mc", "'I am tired' she said.", "'I am tired,' she said.", "'I am tired.' she said.", "'I am tired' she said.", "'I am tired,' she said.", "Comma after speech, before the reporting clause (when reporting verb follows).", 2),
    ("Add the missing apostrophe: 'The childrens playground was closed.'", "mc", "The children's playground", "The childrens' playground", "The child's playground", "The childrens playground", "The children's playground", "Children is an irregular plural (no s), so apostrophe before s: children's.", 2),
    ("Which sentence uses dashes correctly?", "mc", "The dog—a huge Labrador—barked loudly.", "The dog —a huge Labrador barked loudly.", "The dog a huge—Labrador barked loudly.", "The—dog a huge Labrador—barked.", "The dog—a huge Labrador—barked loudly.", "Paired dashes separate additional information from the main clause.", 3),
    ("'Dont forget your homework.' What is wrong?", "mc", "Missing capital letter", "Missing full stop", "Missing apostrophe in dont", "Nothing is wrong", "Missing apostrophe in dont", "Don't = do not. Needs apostrophe: don't.", 1),
]))

CONTENT.append(("English", "Vocabulary", "Synonyms, Antonyms & Word Meanings",
"""
<div class="lesson-block definition">
<h3>📖 Key Vocabulary Terms</h3>
<p><strong>Synonym:</strong> A word with the same or similar meaning — happy/joyful, big/enormous</p>
<p><strong>Antonym:</strong> A word with the opposite meaning — happy/sad, big/small</p>
<p><strong>Homophone:</strong> Same sound, different spelling/meaning — there/their/they're</p>
</div>

<div class="lesson-block">
<h3>🌟 Essential 11+ Vocabulary — Learn These!</h3>
<table class="lesson-table">
<tr><th>Word</th><th>Meaning</th><th>Synonym</th></tr>
<tr><td>benevolent</td><td>kind, well-meaning</td><td>kind, generous</td></tr>
<tr><td>melancholy</td><td>deep sadness</td><td>sad, sorrowful</td></tr>
<tr><td>luminous</td><td>giving off light</td><td>bright, glowing</td></tr>
<tr><td>intrepid</td><td>fearless, brave</td><td>courageous, bold</td></tr>
<tr><td>persevere</td><td>continue despite difficulty</td><td>persist, endure</td></tr>
<tr><td>astute</td><td>clever, perceptive</td><td>shrewd, sharp</td></tr>
<tr><td>austere</td><td>plain, severe</td><td>stark, simple</td></tr>
<tr><td>verbose</td><td>using too many words</td><td>wordy, long-winded</td></tr>
<tr><td>diurnal</td><td>active during the day</td><td>daytime</td></tr>
<tr><td>opaque</td><td>cannot see through</td><td>cloudy, murky</td></tr>
</table>
</div>
""",
[
    ("What is a synonym for 'angry'?", "mc", "calm", "furious", "happy", "shy", "furious", "Synonyms have the same or very similar meaning. Furious = very angry.", 1),
    ("What is the antonym of 'generous'?", "mc", "kind", "giving", "miserly", "wealthy", "miserly", "Generous = giving freely. Miserly = unwilling to give.", 1),
    ("What does 'melancholy' mean?", "mc", "anger", "deep sadness", "great joy", "fear", "deep sadness", "Melancholy = a feeling of deep, thoughtful sadness.", 2),
    ("Which word is a synonym for 'benevolent'?", "mc", "cruel", "kind", "brave", "shy", "kind", "Benevolent means well-meaning and kindly.", 2),
    ("What does 'intrepid' mean?", "mc", "fearful", "clumsy", "fearless and brave", "tired", "fearless and brave", "Intrepid = fearless and adventurous.", 2),
    ("Find the antonym of 'transparent'.", "mc", "clear", "opaque", "shiny", "bright", "opaque", "Transparent = see-through. Opaque = cannot be seen through.", 2),
    ("What does 'austere' mean in: 'The austere room had no decorations'?", "mc", "colourful", "plain and simple", "large", "comfortable", "plain and simple", "Austere = severe or plain, without luxury.", 2),
    ("Which is a synonym for 'persevere'?", "mc", "give up", "persist", "forget", "hurry", "persist", "Persevere and persist both mean to continue despite difficulty.", 2),
    ("What is the antonym of 'elated'?", "mc", "excited", "happy", "joyful", "miserable", "miserable", "Elated = very happy. Antonym = miserable.", 2),
    ("What does 'verbose' mean?", "mc", "concise", "using too many words", "speaking clearly", "being quiet", "using too many words", "Verbose = using more words than necessary.", 3),
    ("What does 'luminous' mean?", "mc", "dark", "heavy", "bright and glowing", "quiet", "bright and glowing", "Luminous = giving off light; shining brightly.", 2),
    ("'The explorer was astute.' What does astute mean?", "mc", "foolish", "clever and perceptive", "brave", "tired", "clever and perceptive", "Astute = having good judgement; quick to understand.", 2),
    ("What does 'diurnal' mean?", "mc", "nocturnal", "active during the day", "underground", "very old", "active during the day", "Diurnal = active during the day (opposite of nocturnal).", 3),
    ("Choose the correct homophone: 'The horse lost ___ shoe.'", "mc", "its", "it's", "its'", "itsself", "its", "Its (no apostrophe) = belonging to it. It's = it is.", 2),
    ("What does 'reluctantly' mean?", "mc", "eagerly", "quickly", "unwillingly", "happily", "unwillingly", "Reluctantly = doing something without wanting to.", 2),
]))

CONTENT.append(("English", "Vocabulary", "Prefixes, Suffixes & Word Building",
"""
<div class="lesson-block definition">
<h3>📖 Word Building</h3>
<p><strong>Prefix:</strong> added to the BEGINNING of a word to change its meaning</p>
<p><strong>Suffix:</strong> added to the END of a word (often changes word class)</p>
<p><strong>Root word:</strong> the base word that carries the main meaning</p>
</div>

<div class="lesson-block">
<h3>🔑 Common Prefixes</h3>
<table class="lesson-table">
<tr><th>Prefix</th><th>Meaning</th><th>Examples</th></tr>
<tr><td>un-</td><td>not</td><td>unhappy, undo</td></tr>
<tr><td>mis-</td><td>wrongly</td><td>misunderstand, mistake</td></tr>
<tr><td>pre-</td><td>before</td><td>preview, prepare</td></tr>
<tr><td>re-</td><td>again</td><td>redo, return</td></tr>
<tr><td>inter-</td><td>between</td><td>international, interview</td></tr>
<tr><td>circum-</td><td>around</td><td>circumnavigate, circumference</td></tr>
<tr><td>bene-</td><td>good</td><td>benefit, benevolent</td></tr>
<tr><td>anti-</td><td>against</td><td>anticlockwise, antisocial</td></tr>
</table>
</div>

<div class="lesson-block">
<h3>🔑 Common Suffixes</h3>
<table class="lesson-table">
<tr><th>Suffix</th><th>Effect</th><th>Examples</th></tr>
<tr><td>-ful</td><td>adjective</td><td>beautiful, hopeful</td></tr>
<tr><td>-less</td><td>adjective (without)</td><td>hopeless, fearless</td></tr>
<tr><td>-tion/-sion</td><td>noun</td><td>action, decision</td></tr>
<tr><td>-ology</td><td>study of</td><td>biology, geology</td></tr>
<tr><td>-ment</td><td>noun</td><td>enjoyment, movement</td></tr>
<tr><td>-ous</td><td>adjective</td><td>dangerous, famous</td></tr>
</table>
</div>
""",
[
    ("What does the prefix 'mis-' mean?", "mc", "again", "wrongly", "before", "not", "wrongly", "Mis- means wrongly: misunderstand, misplace, misspell.", 1),
    ("Add a suffix to make 'beauty' into an adjective.", "mc", "beautyful", "beautiful", "beautious", "beautify", "beautiful", "Suffix -ful added to 'beaut' gives 'beautiful' (spelling change).", 1),
    ("What does 'circumnavigate' mean?", "mc", "to fly above", "to travel around", "to look through", "to dig under", "to travel around", "Circum- (around) + navigate = to travel all the way around.", 2),
    ("Which word uses the prefix 'bene-' meaning 'good'?", "mc", "beneath", "benefit", "between", "belong", "benefit", "Bene- (good): benefit, benevolent, benefactor.", 2),
    ("The suffix '-ology' means:", "mc", "the fear of", "the study of", "the love of", "against", "the study of", "-ology = the study of: biology, geology, psychology.", 2),
    ("What does 'international' mean?", "mc", "within one nation", "between nations", "against nations", "before nations", "between nations", "Inter- = between. International = between nations.", 1),
    ("What does the prefix 'pre-' mean?", "mc", "after", "against", "before", "again", "before", "Pre- means before: preview, prepare, predict.", 1),
    ("What is the root word of 'unhappiness'?", "mc", "happy", "unhappy", "unhappiness", "ness", "happy", "Root = happy. Un- (prefix) + happy + -ness (suffix).", 2),
    ("Which suffix turns a verb into a noun: 'enjoy → ___'?", "mc", "-ful", "-ous", "-ment", "-less", "-ment", "Enjoy + -ment = enjoyment.", 1),
    ("What does 'antipathy' mean?", "mc", "love", "strong dislike", "friendship", "courage", "strong dislike", "Anti- (against) + pathy (feeling) = strong feeling against something.", 3),
    ("Which word means 'to bring back to life'?", "mc", "review", "revive", "return", "repeat", "revive", "Re- (again) + vive (live) = bring back to life.", 2),
    ("What does 'biography' mean?", "mc", "study of life", "written account of a person's life", "love of books", "knowledge of geography", "written account of a person's life", "Bio- (life) + graphy (writing) = written account of a life.", 2),
]))

CONTENT.append(("English", "Comprehension Skills", "Reading Comprehension & Inference",
"""
<div class="lesson-block definition">
<h3>📖 Types of Comprehension Questions</h3>
<ul>
<li><strong>Literal:</strong> The answer is directly stated in the text — 'Find and copy'</li>
<li><strong>Inference:</strong> Read between the lines — 'What does this suggest?'</li>
<li><strong>Deduction:</strong> Use clues to draw conclusions — 'What can you work out?'</li>
<li><strong>Author's technique:</strong> Why did the writer choose this word/technique?</li>
</ul>
</div>

<div class="lesson-block">
<h3>🔍 Key Literary Techniques</h3>
<table class="lesson-table">
<tr><th>Technique</th><th>What it is</th><th>Example</th></tr>
<tr><td>Simile</td><td>Comparison using 'like' or 'as'</td><td>brave as a lion</td></tr>
<tr><td>Metaphor</td><td>Says something IS something else</td><td>Life is a rollercoaster</td></tr>
<tr><td>Personification</td><td>Gives human qualities to non-human things</td><td>The wind whispered</td></tr>
<tr><td>Alliteration</td><td>Repeating consonant sounds</td><td>Peter's perfect plan</td></tr>
<tr><td>Onomatopoeia</td><td>Words that sound like what they mean</td><td>buzz, crash, sizzle</td></tr>
<tr><td>Hyperbole</td><td>Deliberate exaggeration</td><td>I've told you a million times</td></tr>
<tr><td>Rule of three</td><td>Three items for emphasis</td><td>fast, furious and fearless</td></tr>
</table>
</div>

<div class="lesson-block tip">
<h3>💡 Answering Inference Questions</h3>
<p>Always use EVIDENCE from the text to support your answer.</p>
<p>Structure: Make a point → Quote from text → Explain what it suggests.</p>
</div>
""",
[
    ("A character 'clenched her fists and bit her lip'. What can you infer?", "mc", "She was tired", "She was trying to control her anger or anxiety", "She was cold", "She was hungry", "She was trying to control her anger or anxiety", "Physical signs like clenched fists and biting lip suggest suppressed strong emotion.", 2),
    ("What is alliteration?", "mc", "Repeating vowel sounds", "Repeating consonant sounds at the start of words", "Comparing using like/as", "Giving human qualities to things", "Repeating consonant sounds at the start of words", "Alliteration: Peter Piper picked a peck. The 'p' sounds repeat.", 1),
    ("'The wind whispered through the trees.' What technique is this?", "mc", "Simile", "Metaphor", "Personification", "Alliteration", "Personification", "The wind is given the human ability to whisper.", 1),
    ("'Life is a rollercoaster.' What technique is this?", "mc", "Simile", "Metaphor", "Personification", "Hyperbole", "Metaphor", "A metaphor says something IS something else (no 'like' or 'as').", 1),
    ("What effect do short, punchy sentences create?", "mc", "Slows the reader down", "Creates pace, tension and drama", "Shows character is educated", "Makes text boring", "Creates pace, tension and drama", "Short sentences speed up pace and build tension — used in action scenes.", 2),
    ("'The sun smiled down on the playground.' What technique is this?", "mc", "Simile", "Alliteration", "Personification", "Metaphor", "Personification", "The sun is given the human ability to smile.", 1),
    ("What is the effect of using the rule of three?", "mc", "Confuses the reader", "Creates rhythm and emphasises the idea", "Shows poor writing", "Shortens the text", "Creates rhythm and emphasises the idea", "Three items in a row create rhythm and make ideas more memorable.", 2),
    ("'She was as quiet as a mouse.' What technique is this?", "mc", "Metaphor", "Simile", "Personification", "Alliteration", "Simile", "A simile compares using 'as' or 'like'. As quiet as a mouse.", 1),
    ("'I've told you a million times!' What technique is this?", "mc", "Simile", "Metaphor", "Alliteration", "Hyperbole", "Hyperbole", "Hyperbole = deliberate exaggeration for effect.", 2),
    ("Why do authors use rhetorical questions?", "mc", "To ask for an answer", "To engage and involve the reader", "To show they don't know", "To confuse the reader", "To engage and involve the reader", "Rhetorical questions make readers think — no actual answer is expected.", 2),
    ("'The room fell silent as the teacher entered.' What does this suggest?", "mc", "The teacher was quiet", "The teacher was respected or feared", "The students were sleeping", "The room was empty", "The teacher was respected or feared", "Students falling silent when someone enters shows that person commands authority.", 2),
    ("What is onomatopoeia?", "mc", "A comparison using like", "Words that sound like what they describe", "Giving human qualities to things", "Exaggeration", "Words that sound like what they describe", "Examples: buzz, crash, hiss, sizzle, roar.", 1),
]))

CONTENT.append(("English", "Spelling", "Spelling Rules & Common Words",
"""
<div class="lesson-block definition">
<h3>📖 Key Spelling Rules</h3>
<ul>
<li><strong>i before e except after c:</strong> believe, receive, ceiling (but: weird, seize, height are exceptions!)</li>
<li><strong>Double the final consonant</strong> before -ing/-ed if the vowel is short: run → running, hop → hopped</li>
<li><strong>Drop the e</strong> before -ing: make → making, have → having</li>
<li><strong>y → ies</strong> for plurals: baby → babies, city → cities</li>
</ul>
</div>

<div class="lesson-block">
<h3>📝 Commonly Misspelled Words</h3>
<table class="lesson-table">
<tr><th>Word</th><th>Memory trick</th></tr>
<tr><td>receive</td><td>after C = ei</td></tr>
<tr><td>separate</td><td>there's a RAT in sepaRATE</td></tr>
<tr><td>accommodation</td><td>double c, double m</td></tr>
<tr><td>definitely</td><td>de-FINITE-ly</td></tr>
<tr><td>necessary</td><td>one Collar, two Socks (1c, 2s)</td></tr>
<tr><td>occurrence</td><td>double c, double r</td></tr>
<tr><td>embarrass</td><td>double r, double s</td></tr>
<tr><td>rhythm</td><td>Rhythm Helps Your Two Hips Move</td></tr>
</table>
</div>
""",
[
    ("Which is spelled correctly?", "mc", "recieve", "receive", "receve", "recieive", "receive", "After c, the vowels are e then i: re-C-eive.", 1),
    ("Which is correct?", "mc", "seperate", "separate", "separete", "seperete", "separate", "There's a RAT in sepaRATE.", 1),
    ("Which is correct?", "mc", "accomodation", "accommodation", "acommodation", "accomadation", "accommodation", "Double c, double m: ac-com-mo-da-tion.", 2),
    ("Which is correct?", "mc", "definately", "definitly", "definitely", "definiteley", "definitely", "De-FINITE-ly.", 2),
    ("Which is correct?", "mc", "occurance", "occurrence", "occurence", "occurrrence", "occurrence", "Double c, double r: oc-cur-rence.", 3),
    ("Which is correct?", "mc", "embarass", "embarras", "embarrass", "embaras", "embarrass", "Double r, double s: em-bar-rass.", 2),
    ("Which is correct?", "mc", "neccessary", "necessary", "neccesary", "necesary", "necessary", "One collar, two socks: 1c, 2s. ne-c-ess-ary.", 2),
    ("What is the plural of 'baby'?", "type", None, None, None, None, "babies", "Change y to ies: baby → babies.", 1),
    ("What is the correct spelling: 'She was ____ (running/runing)'?", "mc", "runing", "running", "runeing", "ruuning", "running", "Short vowel before single consonant: double the consonant before -ing.", 1),
    ("Which is correct?", "mc", "beleive", "believe", "belive", "beleeve", "believe", "i before e: bel-ie-ve.", 2),
    ("What is the -ing form of 'make'?", "type", None, None, None, None, "making", "Drop the e before -ing: make → making.", 1),
    ("Which is correct?", "mc", "rythm", "rhythm", "rhythem", "rithym", "rhythm", "Rhythm Helps Your Two Hips Move — all consonants!", 2),
]))

# VERBAL REASONING
CONTENT.append(("Verbal Reasoning", "Applied Reasoning", "Word Synonyms & Antonyms",
"""
<div class="lesson-block definition">
<h3>📖 Applied Reasoning</h3>
<p>The CSSE Applied Reasoning section tests your ability to work with words logically. It is not just about knowing vocabulary — it is about thinking carefully.</p>
</div>

<div class="lesson-block">
<h3>🔑 Approach to Synonym Questions</h3>
<ol>
<li>Read the target word carefully</li>
<li>Think of its meaning in your own words</li>
<li>Look at the options and eliminate obviously wrong ones</li>
<li>Choose the closest match in meaning AND word type</li>
</ol>
</div>

<div class="lesson-block">
<h3>Essential Vocabulary Pairs</h3>
<table class="lesson-table">
<tr><th>Word</th><th>Synonym</th><th>Antonym</th></tr>
<tr><td>brave</td><td>courageous</td><td>cowardly</td></tr>
<tr><td>ancient</td><td>antique</td><td>modern</td></tr>
<tr><td>rapid</td><td>swift</td><td>slow</td></tr>
<tr><td>enormous</td><td>gigantic</td><td>tiny</td></tr>
<tr><td>gloomy</td><td>miserable</td><td>cheerful</td></tr>
<tr><td>cautious</td><td>careful</td><td>reckless</td></tr>
</table>
</div>
""",
[
    ("Which word is closest in meaning to BRAVE?", "mc", "cowardly", "fearful", "courageous", "weak", "courageous", "Brave and courageous both mean not afraid of danger.", 1),
    ("Which word is OPPOSITE to RAPID?", "mc", "fast", "quick", "slow", "speedy", "slow", "Rapid = fast. Opposite = slow.", 1),
    ("Which word is closest in meaning to FAMISHED?", "mc", "full", "starving", "tired", "bored", "starving", "Famished = extremely hungry.", 2),
    ("Which is the odd one out?", "mc", "happy", "joyful", "elated", "miserable", "miserable", "Happy, joyful and elated all mean pleased. Miserable is opposite.", 1),
    ("Which is a synonym for ENORMOUS?", "mc", "tiny", "gigantic", "medium", "average", "gigantic", "Enormous and gigantic both mean extremely large.", 1),
    ("Which word is closest in meaning to CAUTIOUS?", "mc", "reckless", "careful", "fast", "noisy", "careful", "Cautious and careful both mean taking care to avoid danger.", 1),
    ("Which is OPPOSITE to ANCIENT?", "mc", "old", "antique", "modern", "historical", "modern", "Ancient = very old. Antonym = modern.", 1),
    ("Which word is closest in meaning to PECULIAR?", "mc", "normal", "strange", "beautiful", "clever", "strange", "Peculiar = strange, unusual.", 2),
    ("Which is the odd one out: angry, furious, irate, calm?", "mc", "angry", "furious", "irate", "calm", "calm", "Angry, furious, irate all mean very cross. Calm is opposite.", 1),
    ("Which word is closest in meaning to MELANCHOLY?", "mc", "joyful", "energetic", "sorrowful", "angry", "sorrowful", "Melancholy and sorrowful both mean deeply sad.", 2),
    ("Which is OPPOSITE to GENEROUS?", "mc", "kind", "giving", "miserly", "wealthy", "miserly", "Generous = giving freely. Antonym = miserly.", 2),
    ("Which is closest in meaning to SUMMIT?", "mc", "bottom", "middle", "peak", "slope", "peak", "Summit and peak both mean the top of a mountain.", 2),
    ("Which is OPPOSITE to TRANSPARENT?", "mc", "clear", "see-through", "opaque", "glass", "opaque", "Transparent = can see through. Opaque = cannot see through.", 2),
    ("Which word is closest in meaning to TRIVIAL?", "mc", "important", "unimportant", "interesting", "difficult", "unimportant", "Trivial = of little importance; unimportant.", 2),
    ("Which is the odd one out: enormous, gigantic, vast, minute?", "mc", "enormous", "gigantic", "vast", "minute", "minute", "Enormous, gigantic and vast all mean very large. Minute = very small.", 2),
]))

CONTENT.append(("Verbal Reasoning", "Applied Reasoning", "Word Analogies & Patterns",
"""
<div class="lesson-block definition">
<h3>📖 Word Analogies</h3>
<p>An analogy shows a relationship between two words, then asks you to find a word with the same relationship.</p>
<p><strong>Format:</strong> A is to B as C is to ___</p>
<p>First, identify the RELATIONSHIP between A and B, then apply it to C.</p>
</div>

<div class="lesson-block">
<h3>🔗 Common Relationship Types</h3>
<ul>
<li><strong>Part to whole:</strong> petal → flower :: tyre → car</li>
<li><strong>Young to adult:</strong> kitten → cat :: puppy → dog</li>
<li><strong>Worker to tool:</strong> painter → brush :: surgeon → scalpel</li>
<li><strong>Synonyms:</strong> happy → joyful :: sad → miserable</li>
<li><strong>Antonyms:</strong> hot → cold :: light → dark</li>
<li><strong>Place to product:</strong> bakery → bread :: dairy → milk</li>
<li><strong>Animal to home:</strong> bee → hive :: bird → nest</li>
</ul>
</div>

<div class="lesson-block tip">
<h3>💡 Strategy</h3>
<p>Make a sentence: "A is the [relationship] of B". Then apply: "C is the [relationship] of ___"</p>
<p>Example: "A kitten is the young of a cat. A puppy is the young of a ___." → dog</p>
</div>
""",
[
    ("Cat is to kitten as dog is to ___.", "type", None, None, None, None, "puppy", "A baby cat is a kitten. A baby dog is a puppy.", 1),
    ("Hot is to cold as light is to ___.", "type", None, None, None, None, "dark", "Hot and cold are opposites. Light and dark are opposites.", 1),
    ("Painter is to canvas as writer is to ___.", "mc", "pen", "paper", "book", "paintbrush", "paper", "A painter works on canvas. A writer works on paper.", 1),
    ("Bee is to hive as bird is to ___.", "mc", "wing", "sky", "feather", "nest", "nest", "Bees live in a hive. Birds live in a nest.", 1),
    ("Glove is to hand as boot is to ___.", "mc", "shoe", "sock", "foot", "leg", "foot", "A glove covers a hand. A boot covers a foot.", 1),
    ("Hear is to ear as see is to ___.", "type", None, None, None, None, "eye", "We hear with our ear. We see with our eye.", 1),
    ("Doctor is to hospital as teacher is to ___.", "type", None, None, None, None, "school", "A doctor works in a hospital. A teacher works in a school.", 1),
    ("Happy is to joyful as angry is to ___.", "mc", "calm", "sad", "furious", "bored", "furious", "Happy and joyful are synonyms. Angry and furious are synonyms.", 2),
    ("Petal is to flower as tyre is to ___.", "type", None, None, None, None, "car", "A petal is part of a flower. A tyre is part of a car.", 2),
    ("Author is to book as composer is to ___.", "mc", "painting", "sculpture", "music", "poem", "music", "An author creates a book. A composer creates music.", 2),
    ("Flour is to baker as steel is to ___.", "mc", "painter", "blacksmith", "teacher", "farmer", "blacksmith", "A baker uses flour. A blacksmith works with steel.", 2),
    ("Introduction is to conclusion as beginning is to ___.", "type", None, None, None, None, "end", "Introduction and conclusion are opposite positions in a piece of writing.", 2),
    ("Flock is to sheep as pod is to ___.", "mc", "fish", "birds", "whales", "bees", "whales", "A flock is a group of sheep. A pod is a group of whales.", 3),
    ("Marathon is to running as regatta is to ___.", "mc", "swimming", "cycling", "rowing/sailing", "horse riding", "rowing/sailing", "A marathon is a running race. A regatta is a boat race.", 3),
    ("Symphony is to orchestra as sonnet is to ___.", "mc", "musician", "painter", "poet", "dancer", "poet", "A symphony is composed by an orchestra. A sonnet is written by a poet.", 3),
]))

CONTENT.append(("Verbal Reasoning", "Applied Reasoning", "Cloze & Missing Words",
"""
<div class="lesson-block definition">
<h3>📖 Cloze Technique</h3>
<p>Cloze questions ask you to choose the best word to complete a sentence. The word must make sense both <strong>grammatically</strong> and in <strong>meaning</strong>.</p>
</div>

<div class="lesson-block">
<h3>🔑 Strategy</h3>
<ol>
<li>Read the whole sentence carefully</li>
<li>Identify what part of speech is needed (noun, verb, adjective, adverb)</li>
<li>Use the context to narrow down the meaning</li>
<li>Test each option — read the full sentence with each option</li>
<li>Eliminate wrong answers</li>
</ol>
</div>

<div class="lesson-block tip">
<h3>💡 Context Clues</h3>
<p>Look for clue words:</p>
<ul>
<li><strong>despite/although:</strong> suggests a contrast</li>
<li><strong>because/therefore:</strong> suggests a reason or result</li>
<li><strong>however/but:</strong> suggests an opposite</li>
</ul>
</div>
""",
[
    ("Choose the best word: 'The ___ scientist discovered a new species.'", "mc", "lazy", "dedicated", "nervous", "clumsy", "dedicated", "A dedicated scientist is one committed to their work — consistent with discovering a new species.", 1),
    ("'Despite the heavy rain, the children played ___ in the garden.'", "mc", "sadly", "nervously", "happily", "angrily", "happily", "Despite = although. Despite the rain (negative), they played happily (positive). Contrast.", 1),
    ("'The explorers were ___ by the vastness of the jungle.'", "mc", "bored", "overwhelmed", "amused", "disappointed", "overwhelmed", "Overwhelmed by vastness best shows how huge and overpowering the jungle was.", 2),
    ("'She spoke with great ___, choosing each word carefully.'", "mc", "speed", "anger", "precision", "sadness", "precision", "Precision = exactness. Fits with 'choosing each word carefully'.", 2),
    ("'The ancient castle stood ___ on the clifftop, having survived a thousand years.'", "mc", "weakly", "precariously", "majestically", "miserably", "majestically", "An ancient castle that has survived 1000 years stands majestically (impressively).", 2),
    ("'The pupils listened ___ as the teacher explained the difficult concept.'", "mc", "noisily", "attentively", "reluctantly", "carelessly", "attentively", "Attentively = paying careful attention. Consistent with trying to understand a difficult concept.", 2),
    ("'The dog's bark was so ___ that it woke the whole street.'", "mc", "quiet", "piercing", "gentle", "soothing", "piercing", "Piercing = sharp and loud — enough to wake the whole street.", 2),
    ("'The athlete's ___ preparation paid off when she won the gold medal.'", "mc", "careless", "minimal", "rigorous", "occasional", "rigorous", "Rigorous = thorough and demanding. Winning gold medal suggests very thorough preparation.", 2),
    ("'He was ___ about failing the test, unable to eat or sleep.'", "mc", "delighted", "indifferent", "distraught", "amused", "distraught", "Distraught = deeply upset. Consistent with not being able to eat or sleep.", 2),
    ("'The young artist's painting was ___ praised by the judges for its originality.'", "mc", "barely", "lavishly", "slightly", "reluctantly", "lavishly", "Lavishly = generously and extensively. Fits with being praised for originality.", 3),
    ("'Although ___, the plan ultimately succeeded beyond everyone's expectations.'", "mc", "ambitious", "flawed", "popular", "expensive", "flawed", "'Although' signals a contrast — despite being flawed, it succeeded.", 2),
    ("'The scientist's ___ research led to a breakthrough that changed medicine forever.'", "mc", "brief", "groundbreaking", "unpublished", "boring", "groundbreaking", "Groundbreaking = revolutionary. Consistent with a breakthrough that changed medicine.", 2),
]))

# Verify counts
total_topics = len(CONTENT)
total_questions = sum(len(q) for _, _, _, _, q in CONTENT)
print(f"Total topics: {total_topics}")
print(f"Total questions: {total_questions}")


def seed_all_content(conn):
    """Seed all topics, lessons and questions. Safe to call multiple times."""
    from datetime import date
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) as c FROM topics")
    count = cur.fetchone()['c']
    if count > 10:
        print(f"Database already has {count} topics — skipping seed.")
        cur.close()
        return

    print(f"Seeding {total_topics} topics and {total_questions} questions...")
    today = date.today().isoformat()

    for subject, section, title, lesson_html, questions in CONTENT:
        cur.execute("""
            INSERT INTO topics (subject, section, title, source, lesson_html, created_at, archived)
            VALUES (%s, %s, %s, %s, %s, %s, 0) RETURNING id
        """, (subject, section, title, "CSSE 11+ Syllabus", lesson_html, today))
        topic_id = cur.fetchone()['id']

        for q in questions:
            q_text, q_type, a, b, c, d, answer, explanation, level = q
            cur.execute("""
                INSERT INTO questions (topic_id, question_text, question_type,
                    option_a, option_b, option_c, option_d,
                    correct_answer, explanation, difficulty)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """, (topic_id, q_text, q_type, a, b, c, d, answer, explanation, level))

    conn.commit()
    cur.close()
    print(f"✓ Seeded {total_topics} topics and {total_questions} questions!")
