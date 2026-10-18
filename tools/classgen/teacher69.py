import sys, json
sys.path.insert(0, '/tmp/claude-0/gen')
from build import img, esc, qr_svg, FONTS, B
from teacher import TCSS
from content import CSB, SITE
from content69 import WEEKS
import build69 as K

GUIDE = 'The Way Back Home · Ages 6–9 · Teacher’s guide'
def tfoot(r): return f'<div class="tfoot"><span>{GUIDE}</span><span>{r}</span></div>'

def cover():
    return (f'<div class="page">{img("gates-end", style="width:100%;height:6.9in;object-fit:cover;object-position:50% 25%;border-radius:.3in")}'
            f'<p style="font:900 12pt Grandstander;letter-spacing:.16em;color:#7b3fe4;margin:.25in 0 0">SUNDAY SCHOOL · AGES 6–9 · 7 WEEKS</p>'
            f'<h1 style="font-size:46pt;line-height:1;margin:.05in 0 .08in">The Way Back Home</h1>'
            f'<p style="font:800 18pt Grandstander;margin:0">Teacher’s guide for ages 6–9</p>'
            f'<p style="font-size:11pt;color:#5b5468;margin-top:.12in">The whole Bible story in seven Sundays, from Eden to the open gates of home, told with the pictures and clips of <b>{SITE}</b>. '
            f'Built for this age: real Bibles in their hands, a full memory verse each week, drama, small-group talk, puzzles and crafts.</p></div>')

def glance():
    rows = ''.join(f'<tr><td><span class="pill" style="background:{w["col"]}">{w["n"]}</span></td><td><b>{esc(w["title"])}</b><br><span class="small">{esc(", ".join(w["pages"]))} ({esc(w["book"])})</span></td>'
                   f'<td>“{esc(w["big"])}”</td><td>{esc(w["verse"][1])}<br><span class="small">{esc(w["skill"][0])}</span></td>'
                   f'<td class="small">{"<br>".join(esc(x) for x in w["pages_kid"])}</td></tr>' for w in WEEKS)
    return (f'<div class="page tight"><h2>Welcome, teacher!</h2>'
            f'<p>Six- to nine-year-olds are ready for more than the little ones: they can follow a longer story, hold a whole verse, find it in a real Bible, act it out, and argue about it. '
            f'They also think concretely and fairly, notice everything on your face, and lose focus after 10–20 minutes. This series gives them <b>one big idea a week</b>, one memory verse, one Bible-finding skill and one thing to live out, '
            f'and changes activity often enough to keep them with you.</p>'
            f'<p>It follows the same seven weeks and book pages as the 3–5 and 8–12 series, so families with several children hear the same part of the story on the same Sunday.</p>'
            f'<h3 style="margin-top:.1in">The series at a glance</h3>'
            f'<table class="std"><tr><th></th><th>Week</th><th>Big idea</th><th>Memory verse (CSB) · Bible skill</th><th>Kids’ pages</th></tr>{rows}</table>'
            f'<div class="grid2" style="margin-top:.12in"><div class="box line"><h3>In this guide</h3><ul style="margin:0"><li>How 6–9s learn, and what this series does about it</li><li>A Sunday morning, step by step (60 or 45 minutes)</li>'
            f'<li>Your toolbox: attention cue, class covenant, readers and non-readers, small groups</li><li>The Bible-skills ladder</li><li>Sharing the gospel with 6–9s; the harder pages</li><li>Two pages per week, answer keys, sources</li></ul></div>'
            f'<div class="box line"><h3>In the kids’ pack</h3><ul style="margin:0"><li>Letter to families; Road Home map; bookmarks and invite cards</li><li>Each week, 3 pages: <b>1</b> arrival puzzle, <b>2</b> memory verse (goes home with the “For grown-ups” box), <b>3</b> make or write</li><li>Certificate</li></ul>'
            f'<p class="small" style="margin:4pt 0 0">Pictures are real frames from the book’s clips.</p></div></div>{tfoot("Welcome")}</div>')

def learn():
    R = [('Attention runs about 10–20 minutes, longer with objects.', 'The story is told in short bursts (book pages, then drama), and no segment runs much past 8 minutes. Every week has a real object to hold. [1][2]'),
         ('They think concretely and focus on the parts and actions of a story.', 'Pause questions ask what happened and why. Comic strips, story cards and the 12-picture review make them put actions in order. [1]'),
         ('They like to take part: role-play, drama, retelling.', 'Every week has an “Act it out” scene with simple roles, and children retell the story in their own words. [1][2]'),
         ('One main point and one application works better than several lessons at once.', 'One big idea a week, and one “Live it” challenge for home. [1]'),
         ('Reading takes up much of their energy; treat the Bible as the most important book.', 'Pair readers with non-readers. Use real, large-print Bibles; each week teaches one finding skill. Never give a worksheet that asks for no response. [2]'),
         ('Early elementary Bible skills: find books, chapters and verses; Old vs New Testament; memorise verses; order events.', 'The Bible-skills ladder runs from Genesis to Revelation over seven weeks, with a tick-it-off bookmark. [3]'),
         ('Memory sticks with chunks, motions, games and repetition.', 'Each week uses a different verse game (word scramble, erase the verse, discover the verse, balloon juggle…). [4]'),
         ('Kids engage when they repeat back, move, talk in groups, help teach, and have a clear signal.', 'Small-group talk with answers for leaders; kids teach the motions; a call-and-response cue; a class covenant they write themselves. [5]')]
    rows = ''.join(f'<tr><td style="width:44%"><b>{esc(a)}</b></td><td>{esc(b)}</td></tr>' for a, b in R)
    return (f'<div class="page"><h2>How 6–9s learn, and how this series uses it</h2>'
            f'<p>The plan follows patterns common to evangelical elementary curricula and children’s-ministry guidance. Numbers point to the sources at the back.</p>'
            f'<table class="std"><tr><th>What we know about 6–9s</th><th>What this series does</th></tr>{rows}</table>'
            f'<div class="grid2" style="margin-top:.12in"><div class="box" style="background:#e3f5ea"><h3>Sixes vs nines</h3><p style="margin:0">A six-year-old may just be learning to read; a nine-year-old can read the whole verse, argue a point, and lead a small group. '
            f'Every week has a line for each. In a mixed class, put one confident reader in every group.</p></div>'
            f'<div class="box" style="background:#fdf3d6"><h3>Fairness is their superpower</h3><p style="margin:0">This age cares deeply about what is fair. Use it: it’s why the law page lands (“Is one lie enough?”), why we can’t just pretend sin never happened, and why Jesus taking our place is astonishing.</p></div></div>'
            f'{tfoot("How 6–9s learn")}</div>')

def rhythm():
    rows = [('0:00', 'Arrival puzzle', 'Kids’ page 1 on the tables. Greet each child by name. Early birds help set out Bibles.'),
            ('0:08', 'Welcome', 'Attention cue. Review the big ideas so far with the moves. Introduce today’s big idea.'),
            ('0:12', 'Hook', 'An object lesson that opens the big idea.'),
            ('0:17', 'Find it!', 'Bible skill: everyone finds the memory verse in a real Bible.'),
            ('0:21', 'Story time', 'Play this week’s book pages; stop on each picture with the pause question.'),
            ('0:28', 'Act it out', 'A short drama with simple roles. Then ask the audience one question.'),
            ('0:35', 'Talk', 'Small groups of 4–6 with a leader. Questions and answers are on the week’s page.'),
            ('0:42', 'Memory verse game', 'Learn the verse with this week’s game.'),
            ('0:48', 'Do it', 'The week’s activity: a game, an object lesson or the page 3 craft.'),
            ('0:55', 'Live it and pray', 'This week’s challenge, a sticker on the Road Home map, prayer. Page 2 goes home.')]
    tr = ''.join(f'<tr><td class="t">{a}</td><td class="what">{b}</td><td>{esc(c)}</td></tr>' for a, b, c in rows)
    return (f'<div class="page"><h2>A Sunday morning, step by step</h2><p>Same order every week, so children know what comes next and save their energy for the story. Move on while they still want more.</p>'
            f'<table class="plan">{tr}</table>'
            f'<div class="grid2" style="margin-top:.12in"><div class="box line"><h3>Only 45 minutes?</h3><ul style="margin:0"><li>Arrival puzzle 5 minutes</li><li>Alternate weeks: do either “Act it out” or the verse game</li><li>Talk in one big group</li><li>Page 3 goes home if not finished</li></ul></div>'
            f'<div class="box line"><h3>Kids’ pages</h3><ul style="margin:0"><li><b>Page 1</b>: arrival puzzle (in class)</li><li><b>Page 2</b>: memory verse + “For grown-ups” box (goes home)</li><li><b>Page 3</b>: craft or writing, done in “Do it” or at home</li></ul></div></div>'
            f'<div class="grid2"><div class="box line"><h3>Set up the room</h3><ul style="margin:0"><li>Rows or a semicircle facing the screen, with an open stage area in front for drama</li><li>Tables for puzzles and crafts</li><li>Bibles (same edition if you can, so page numbers match) in a tub</li><li>Download the book for offline use from the site’s menu, in case the Wi-Fi fails</li></ul></div>'
            f'<div class="box line"><h3>Helpers</h3><ul style="margin:0"><li>One adult per small group of 4–6 children</li><li>Two screened adults in the room at all times, per your church’s child-safety policy</li><li>Give small-group leaders the week’s two pages a week ahead</li></ul></div></div>'
            f'{tfoot("A Sunday morning")}</div>')

def toolbox():
    return (f'<div class="page"><h2>Your classroom toolbox</h2>'
            f'<div class="box" style="background:#e2f0fc"><h3>The attention cue: “Way back…” “HOME!”</h3><p style="margin:0">You say “Way back…”; they answer “HOME!” and freeze, hands on heads like a roof. Same cue, every week. Kids this age also love a countdown: “Five… four…” (they join in).</p></div>'
            f'<div class="grid2"><div class="box line"><h3>Week 1: write a class covenant</h3><p style="margin:0">Let the children make the rules (3–5 of them), then everyone signs. Kids who help set the rules are more invested in keeping them. [5] Keep it on the wall and point to it, rather than raising your voice.</p></div>'
            f'<div class="box line"><h3>Readers and non-readers</h3><ul style="margin:0"><li>Pair every pre-reader with a reader (“Bible buddies”).</li><li>Read every puzzle instruction aloud.</li><li>Word banks are on every fill-in page.</li><li>Never make a child read aloud who hasn’t volunteered.</li></ul></div></div>'
            f'<div class="grid2"><div class="box line"><h3>Quick redirects</h3><ul style="margin:0"><li><b>Freeze frame!</b> The book’s clips freeze on the last picture. Call it; everyone freezes.</li><li><b>Repeat it back:</b> “Tell your neighbour what just happened.” [5]</li>'
            f'<li><b>Give them a job:</b> narrator, prop holder, page-turner. [5]</li><li><b>Move:</b> stand up for every “yes”, sit for every “no”.</li><li><b>Name and nearness:</b> sit beside the wiggler, use their name kindly.</li></ul></div>'
            f'<div class="box line"><h3>Competition, kindly</h3><ul style="margin:0"><li>Teams, races and timers energise this age.</li><li>Mix teams every week; never boys vs girls or ages vs ages.</li><li>Celebrate effort and teamwork, not just winners.</li><li>Use a stamp or sticker on the Road Home map for finding the verse, not for “right answers”.</li></ul></div></div>'
            f'<h3>The Bible-skills ladder</h3><table class="std"><tr><th>Week</th><th>Skill</th><th>Find it</th></tr>'
            + ''.join(f'<tr><td><span class="pill" style="background:{w["col"]}">{w["n"]}</span></td><td><b>{esc(w["skill"][0])}</b></td><td>{esc(w["verse"][1])}</td></tr>' for w in WEEKS)
            + f'</table>{tfoot("Classroom toolbox")}</div>')

def gospel():
    return (f'<div class="page"><h2>Sharing the gospel with 6–9s</h2>'
            f'<p>Many Christians first trust Jesus as children. At this age they can grasp sin, the cross and the resurrection, and they can respond. They also want to please adults and follow friends. '
            f'So be clear, and be patient: explain the choice in week 6, invite in week 7, and never manipulate.</p>'
            f'<div class="box" style="background:#fdeedd"><h3>The story in seven words (one per week)</h3><p style="margin:0;font-size:11pt"><b>Made</b> (God made a good home) → <b>Lied</b> (the serpent; sin entered) → <b>All</b> (everybody sins) → <b>Locked</b> (we can’t fix it) → <b>Door</b> (Jesus took our place) → <b>Alive</b> (He rose; He makes us clean) → <b>Home</b> (He welcomes us; we tell others).</p></div>'
            f'<div class="grid2"><div class="box line"><h3>Do</h3><ul style="margin:0"><li>Use the Bible’s words: sin, cross, rose, trust, Lord. Then explain them.</li><li>Explain that being good can’t save us (week 4), so grace is a gift (Ephesians 2:8).</li>'
            f'<li>Invite quietly and personally: “If you want to talk about following Jesus, find me after.”</li><li>Talk one to one with any child who responds; ask them to tell you in their own words what they believe.</li><li>Tell parents the same day.</li></ul></div>'
            f'<div class="box line"><h3>Don’t</h3><ul style="margin:0"><li>Ask for raised hands or “every head bowed, every eye closed” counts.</li><li>Use fear as leverage, or rewards for “decisions”.</li><li>Rush a child who isn’t ready, or doubt one who is.</li><li>Announce who prayed.</li></ul></div></div>'
            f'<h3>The harder pages</h3><table class="std">'
            f'<tr><td style="width:24%"><b>Week 2 · Fruit, exile</b></td><td>Lightning and thunder; animals die to make clothes. Say it plainly. It’s the first picture of a substitute, and week 5 needs it.</td></tr>'
            f'<tr><td><b>Week 3 · God’s law</b></td><td>“That makes you a liar and a thief.” Let it land, about all of us, yourself first. No public confessions.</td></tr>'
            f'<tr><td><b>Week 4 · Locked out</b></td><td>The book names hell. Read it calmly, as written, then: “That is very bad news, but it is not the end of the story.”</td></tr>'
            f'<tr><td><b>Weeks 5–6 · Cross, choice</b></td><td>One of the three children (Chase) turns away, then walks off. “He doesn’t want Jesus yet. Jesus still loves him. Jesus lets us choose.”</td></tr></table>'
            f'{tfoot("Sharing the gospel")}</div>')

def supplies():
    items = {}
    for w in WEEKS:
        for x in w['hookneed'] + w['act'][1] + w['extra']:
            items.setdefault(x, []).append(str(w['n']))
    rows = ''.join(f'<tr><td>{esc(k)}</td><td>{", ".join(dict.fromkeys(v))}</td></tr>' for k, v in items.items())
    return (f'<div class="page"><h2>Supplies and prep</h2><div class="grid2"><div><h3>Every week</h3><ul><li>Screen with <b>{SITE}</b> (downloaded for offline use)</li><li>Bibles, one per pair at least (large print helps)</li>'
            f'<li>Kids’ pages 1–3 for each child, plus spares</li><li>Pencils, crayons, scissors, glue sticks</li><li>Whiteboard or flip chart and markers</li><li>Stickers for the Road Home map</li><li>Index cards / sticky notes for verse games</li></ul>'
            f'<h3 style="margin-top:.1in">Before week 1</h3><ul><li>Print the family letter, maps, bookmarks</li><li>Test the permanent marker and rubbing alcohol on a plate (weeks 4, 6)</li>'
            f'<li>Find a box and padlock (weeks 4–5) and make the tomb box (week 6)</li><li>Recruit small-group leaders and send them weeks 1–2</li></ul></div>'
            f'<div><h3>Special items, by week</h3><table class="std"><tr><th>Item</th><th>Week</th></tr>{rows}</table></div></div>'
            f'<div class="box" style="background:#efe6fd;margin-top:.12in"><h3>Running threads</h3><ul style="margin:0"><li><b>The locked box</b>: nobody can open it in week 4; the key is Jesus in week 5.</li>'
            f'<li><b>The plate</b>: the mark won’t scrub off in week 4; wiped clean in week 6.</li><li><b>Dot stickers</b>: sin marks in week 3, checked again in week 4.</li><li><b>The Road Home map</b>: a stop coloured and a verse reference written each week.</li></ul></div>'
            f'{tfoot("Supplies")}</div>')

def review(n):
    prev = [w for w in WEEKS if w['n'] < n]
    return ('Teach the attention cue and write the class covenant.' if not prev else 'Review: ' + ' · '.join(f'“{w["big"]}”' for w in prev) + '.')

def week_a(w):
    th = ''.join(img(t) for t in w['thumbs'][:3])
    pause = ''.join(f'<li><b>{esc(a)}:</b> {esc(b)}</li>' for a, b in w['pause'])
    need = ''.join(f'<li>{esc(x)}</li>' for x in ['Screen, Bibles, kids’ pages 1–3'] + w['hookneed'] + w['act'][1] + w['extra'])
    return (f'<div class="page"><div class="band" style="background:{w["col"]}"><div><span class="wkpill" style="color:{w["col"]}">WEEK {w["n"]} OF 7</span><h1>{esc(w["title"])}</h1>'
            f'<div class="meta">Book: {esc(" · ".join(w["pages"]))} ({esc(w["book"])}) · Bible: {esc(w["bible"])}</div></div><div class="th">{th}</div></div>'
            f'<div class="box" style="background:{w["soft"]};margin-top:.1in"><h3>Teacher’s heart</h3><p style="margin:0">{esc(w["heart"])}</p></div>'
            f'<div class="grid2"><div class="box" style="border:3px solid {w["col"]}"><h3>Big idea</h3><div class="say" style="color:{w["col"]};font-size:16pt">“{esc(w["big"])}”</div><p class="small" style="margin:3pt 0 0">{esc(w["moves"])}</p></div>'
            f'<div class="box" style="border:3px solid {w["col"]}"><h3>Memory verse</h3><div class="verse" style="font-size:11.5pt">“{esc(w["verse"][0])}”</div><p class="small" style="margin:2pt 0 0"><b>{esc(w["verse"][1])}</b> (CSB)</p></div></div>'
            f'<div class="grid2"><div class="box line"><h3>Find it! {esc(w["skill"][0])}</h3><p style="margin:0">{esc(w["skill"][1])}</p></div>'
            f'<div class="box line"><h3>Story time: pause and ask</h3><ul style="margin:0">{pause}</ul></div></div>'
            f'<div class="grid2"><div class="box" style="background:#f6f4f9"><h3>{esc(w["drama"][0])}</h3><p style="margin:0">{esc(w["drama"][1])}</p></div>'
            f'<div class="box line" style="flex:.6"><h3>You need</h3><ul style="margin:0">{need}</ul></div></div>'
            f'{tfoot(f"Week {w["n"]} · page 1 of 2")}</div>')

def week_b(w):
    n = w['n']
    plan = [('0:00', 'Arrival puzzle', f'Kids’ page 1: {w["pages_kid"][0]}.'),
            ('0:08', 'Welcome', f'Attention cue. {review(n)} Then today’s big idea with the moves.'),
            ('0:12', f'Hook: {w["hook"][0]}', w['hook'][1]),
            ('0:17', 'Find it!', f'{w["skill"][0]}: find {w["verse"][1]}.'),
            ('0:21', 'Story time', f'Play {", ".join(w["pages"])} ({w["book"]}); use the pause questions.'),
            ('0:28', 'Act it out', 'See page 1.'),
            ('0:35', 'Talk', 'Small groups; questions below.'),
            ('0:42', f'Verse game: {w["game"][0]}', w['game'][1]),
            ('0:48', f'Do it: {w["act"][0]}', w['act'][2]),
            ('0:55', 'Live it and pray', f'Challenge: {w["live"]} Sticker on the map. Pray: {w["pray"]}')]
    tr = ''.join(f'<tr><td class="t" style="color:{w["col"]}">{a}</td><td class="what">{esc(b)}</td><td>{esc(c)}</td></tr>' for a, b, c in plan)
    talk = ''.join(f'<li><b>{esc(q)}</b>{(" <span class=small>" + esc(a) + "</span>") if a else ""}</li>' for q, a in w['talk'])
    care = f'<div class="box" style="background:#fde7e5"><h3>Handle with care</h3><p style="margin:0">{esc(w["care"])}</p></div>' if w['care'] else ''
    return (f'<div class="page"><h2 style="color:{w["col"]};font-size:16pt">Week {n} · The plan</h2><table class="plan">{tr}</table>'
            f'<div class="box" style="background:{w["soft"]};margin-top:.08in"><h3>Small-group talk (with answers for leaders)</h3><ul style="margin:0">{talk}</ul></div>'
            f'<div class="grid2"><div class="box line"><h3>Sixes</h3><p style="margin:0">{esc(w["six"])}</p></div><div class="box line"><h3>Eights and nines</h3><p style="margin:0">{esc(w["nine"])}</p></div></div>'
            f'<div class="box line"><h3>Teacher tip</h3><p style="margin:0">{esc(w["tip"])}</p></div>{care}'
            f'{tfoot(f"Week {n} · page 2 of 2")}</div>')

def answers():
    cw = json.load(open(f'{B}/answers69.json'))['cw']
    tt = ', '.join(f'{i+1} {a}' for i, (q, a) in enumerate(K.TT))
    lab = {'road-clip': 'Adam and Eve leave', 'road-mid': 'the road fills up', 'road-end': 'the crowd', 'test-end': 'God’s law'}
    fr = ['road-clip', 'road-mid', 'road-end', 'test-end']
    printed = ', '.join(lab[fr[k]] for k in [2, 0, 3, 1])
    story = ' '.join(str(k + 1) for k in K.ORDER12)
    rows = [('Week 1 · Creation', 'Pictures top to bottom: Day 4, Day 1, Day 6, Day 2, Day 5, Day 3. So Day 1 → 2nd picture, Day 2 → 4th, Day 3 → 6th, Day 4 → 1st, Day 5 → 5th, Day 6 → 3rd.'),
            ('Week 1 · Verse', 'saw, made, very, good · Genesis 1:31'), ('Week 2 · True or trick', tt), ('Week 2 · Code', 'EVERY WORD OF GOD IS PURE · shield · Proverbs 30:5'),
            ('Week 3 · Word search', 'All 12 words appear exactly once, across or down.'), ('Week 3 · Scramble', 'For all have sinned and fall short of the glory of God · Romans 3:23 · MIRROR'),
            ('Week 3 · Story cards', f'Printed left to right: {printed}. Order: Adam and Eve leave, the road fills up, the crowd, God’s law.'),
            ('Week 4 · Crossword', cw), ('Week 4 · Gift boxes', 'GRACE, FAITH, GIFT · Ephesians 2:8'),
            ('Week 5 · Verse', 'loved, world, Son, believes, perish, eternal · John 3:16'), ('Week 6 · Code', 'HE IS NOT HERE · JESUS IS ALIVE · WHITE AS SNOW'),
            ('Week 6 · Verse', 'Mouth: Lord · Heart: dead · confess, Lord, believe, dead, saved · Romans 10:9'),
            ('Week 7 · Story order', f'Reading the grid row by row, the numbers are: {story}.'), ('Week 7 · A-B-C', 'Admit, Believe, Choose · Revelation 21:5'),
            ('Crafts', 'Snake: cut the circle, then the spiral to the head. Door and gates: cut the thick lines, fold on the dashes, cut the top panel off, glue it over the picture. Stone: fasten through both dots.')]
    tr = ''.join(f'<tr><td style="width:24%"><b>{esc(a)}</b></td><td>{esc(b)}</td></tr>' for a, b in rows)
    return f'<div class="page"><h2>Answer keys</h2><table class="std">{tr}</table>{tfoot("Answer keys")}</div>'

def sources():
    S = ['ChurchLeaders, “Bible stories for elementary age: how children learn God’s word”. churchleaders.com',
         'BibleCharts, “Methods for teaching early elementary children (K–1)” (PDF). biblecharts.org',
         'David C Cook, “Bible Skills Plan” (2023, PDF). davidccook.org',
         'Ministry-to-Children, “19 memory verse games”. ministry-to-children.com',
         'Dale Hudson, “12 great ways to get kids to pay attention”, ChurchLeaders. churchleaders.com',
         'Awana, “Sharing the gospel with preschoolers” and “Dos and don’ts for sharing the gospel”. awana.org']
    li = ''.join(f'<li>{esc(s)}</li>' for s in S)
    verses = ''.join(f'<p style="margin:0 0 4pt"><b>{esc(w["verse"][1])}</b> “{esc(w["verse"][0])}”</p>' for w in WEEKS)
    return (f'<div class="page"><h2>All seven memory verses</h2><p class="small">Post this page by the door, or send it home in week 7.</p>{verses}'
            f'<h2 style="margin-top:.25in">Sources</h2><ol>{li}</ol>'
            f'<p class="small" style="margin-top:.15in">{CSB} “I am the door” is the book’s wording of John 10:9 (CSB has “gate”). Pictures are frames from <i>The Way Back Home</i> by Johnny Wall.</p>'
            f'{tfoot("Verses and sources")}</div>')

def build():
    pages = [cover(), glance(), learn(), rhythm(), toolbox(), gospel(), supplies()]
    for w in WEEKS: pages += [week_a(w), week_b(w)]
    pages += [answers(), sources()]
    return f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{TCSS}</style></head><body>{"".join(pages)}</body></html>'

if __name__ == '__main__':
    import weasyprint
    open(f'{B}/teacher69.html', 'w').write(build())
    weasyprint.HTML(f'{B}/teacher69.html', base_url=B).write_pdf(f'{B}/teacher69.pdf')
    print('ok')
