import sys
sys.path.insert(0, '/tmp/claude-0/gen')
from build import *   # noqa
from build import CARDS, CARD_ORDER, CARD_LABEL, TASK1, TASK2

TCSS = BASE_CSS + '''
body { font-family: 'Lexend', sans-serif; font-size: 9.6pt; line-height: 1.42; }
.page { height: 10.15in; }
p { margin: 0 0 5pt; }
ul, ol { margin: 0 0 5pt; padding-left: 13pt; }
li { margin-bottom: 2.5pt; }
h2 { font-size: 20pt; line-height: 1.1; margin-bottom: 6pt; }
h3 { font-size: 11.5pt; margin: 0 0 3pt; }
.band { border-radius: .2in; color: #fff; padding: .14in .2in; display: flex; gap: .16in; align-items: center; }
.band h1 { font-size: 28pt; line-height: 1.02; }
.band .meta { font-size: 9.4pt; opacity: .95; margin-top: 3pt; }
.band .th { display: flex; gap: 6pt; margin-left: auto; }
.band .th img { width: .82in; height: 1.15in; object-fit: cover; border-radius: .1in; border: 3px solid #fff; }
.wkpill { font: 900 9pt 'Grandstander'; background: #fff; border-radius: 99px; padding: 2pt 8pt; display: inline-block; }
.box { border-radius: .14in; padding: .1in .14in; margin-bottom: .1in; }
.line { border: 1.5px solid #e3dfe9; }
.grid2 { display: flex; gap: .14in; } .grid2 > div { flex: 1; }
.say { font: 900 19pt 'Grandstander'; line-height: 1.1; }
.small { font-size: 8.4pt; color: #5b5468; }
.verse { font: 800 13pt 'Grandstander'; }
table.plan { width: 100%; border-collapse: collapse; }
table.plan td { vertical-align: top; padding: 3.5pt 6pt; font-size: 9.2pt; border-bottom: 1px solid #e3dfe9; }
table.plan td.t { width: .52in; font: 900 11pt 'Grandstander'; }
table.plan td.what { width: 1.22in; font-weight: 600; }
.sayit { font-style: italic; }
table.std { width: 100%; border-collapse: collapse; font-size: 9pt; }
table.std th { text-align: left; font-family: 'Grandstander'; font-weight: 900; padding: 4pt 5pt; border-bottom: 2px solid #1d1a24; }
table.std td { padding: 4pt 5pt; border-bottom: 1px solid #e3dfe9; vertical-align: top; }
.tfoot { position: absolute; bottom: 0; left: 0; right: 0; font-size: 7pt; color: #8a8296; display: flex; justify-content: space-between; border-top: 1px solid #e3dfe9; padding-top: 3pt; }
.k { font-weight: 600; }
.tight { font-size: 9pt; line-height: 1.38; }
.tight table.std td { padding: 2.6pt 5pt; font-size: 8.3pt; line-height: 1.3; }
.tight .box { padding: .08in .14in; margin-top: .08in; }
.tight li { margin-bottom: 1.5pt; }
.pill { display: inline-block; border-radius: 99px; padding: 0 6pt; color: #fff; font: 900 8.5pt 'Grandstander'; }
'''

def tfoot(r):
    return f'<div class="tfoot"><span>The Way Back Home · Little ones (ages 3–5) · Teacher’s guide</span><span>{r}</span></div>'

def cover():
    return (f'<div class="page" style="background:#fff">'
            f'{img("cover", style="width:100%;height:6.9in;object-fit:cover;object-position:50% 22%;border-radius:.3in")}'
            f'<p style="font:900 12pt Grandstander;letter-spacing:.16em;color:#1e88e5;margin:.25in 0 0">SUNDAY SCHOOL · AGES 3–5 · 7 WEEKS</p>'
            f'<h1 style="font-size:46pt;line-height:1;margin:.05in 0 .08in">The Way Back Home</h1>'
            f'<p style="font:800 18pt Grandstander;margin:0">Little ones: teacher’s guide</p>'
            f'<p style="font-size:11pt;color:#5b5468;margin-top:.12in">From God’s good garden to the open gates of home. A true Bible story, told with the pictures and clips of <b>{SITE}</b>, '
            f'and taught the way little ones learn best: by seeing, moving, singing, making and repeating.</p></div>')

def glance():
    rows = ''.join(f'<tr><td><span class="pill" style="background:{w["col"]}">{w["n"]}</span></td><td><b>{esc(w["title"])}</b><br><span class="small">{esc(", ".join(w["pages"]))} ({esc(w["book"])})</span></td>'
                   f'<td>“{esc(w["say"])}”</td><td>{esc(w["verse"][0])}<br><span class="small">{esc(w["verse"][1])}</span></td>'
                   f'<td class="small">{" · ".join(esc(x) for x in w["pages_kid"])}</td></tr>' for w in WEEKS)
    return (f'<div class="page tight"><h2>Welcome, teacher!</h2>'
            f'<p>Thank you for teaching our youngest. For seven Sundays, your class will walk the whole Bible story in <i>The Way Back Home</i>: God made a good home, sin locked us out, nothing we do can wash it away, '
            f'and Jesus, the door, died and rose to bring us home. Each week takes two or three pages of the book and boils them down to <b>one tiny truth</b> a three-year-old can say and do with their hands.</p>'
            f'<p>This series runs alongside the ages 6–10 and 8–12 series on the same book, week by week, so brothers and sisters learn the same story on the same Sunday and can tell it to each other at home.</p>'
            f'<h3 style="margin-top:.12in">The series at a glance</h3>'
            f'<table class="std"><tr><th></th><th>Week</th><th>Say it!</th><th>Bible words (CSB)</th><th>Kids’ pages</th></tr>{rows}</table>'
            f'<div class="grid2" style="margin-top:.14in"><div class="box line"><h3>What’s in this guide</h3><ul>'
            f'<li>How little ones learn, and how this series uses it</li><li>A Sunday morning, step by step (60 or 45 minutes)</li><li>Your classroom toolbox: attention cue, redirects, scissors by age</li>'
            f'<li>Sharing Jesus with 3–5s, and how to handle the harder pages</li><li>Supplies and prep for all 7 weeks</li><li>Two pages per week, with a timed plan and words to say</li><li>Answer keys and sources</li></ul></div>'
            f'<div class="box line"><h3>What’s in the kids’ pack</h3><p style="margin:0 0 4pt"><b>Short on paper or ink?</b> Print only <b>page 1</b> each week (black and white is fine): it has the colouring, the words to trace and the box for parents. Everything else is optional.</p><ul><li><b>Letter to families</b> (send home in week 1)</li><li><b>My Road Home</b> sticker chart (one per child, keep it in class)</li>'
            f'<li>Each week, <b>3 pages</b>: 1 colour and trace, 2 puzzle or maze (with the “For grown-ups” box), 3 cut and glue or a craft</li><li><b>Certificate</b> for week 7</li></ul>'
            f'<p class="small">The pictures and story cards are real frames from the book’s clips, so children recognise exactly what they saw on screen.</p></div></div>'
            f'{tfoot("Welcome")}</div>')

def learn():
    R = [
        ('Attention lasts about one minute per year of age.', 'No part of the morning runs longer than about 5–8 minutes. We switch between sitting, moving and making all morning. [6]'),
        ('Plan to win attention back about three times in a 15-minute stretch.', 'Every plan has a built-in move break, and the toolbox lists quick redirects (motions, copy-me, call and response, touch the picture). [1]'),
        ('They learn through their senses and by doing.', 'A feely box, a sock snake, a mirror, a plate that won’t scrub clean, a door to knock on, an empty tomb box. Every hook is something to touch. [2][5]'),
        ('Repetition is how preschoolers learn.', 'One “Say it!” sentence per week, said whisper-normal-SHOUT, sung, traced and reviewed every week after. The same book, the same routine, the same chart. [2]'),
        ('Guided play is the best setting for Bible teaching.', 'Games carry the point: “God says, snake says”, “Sleepy… ALIVE!”, walking through the door. Play is never just filler. [2]'),
        ('Keep stories short and simple, avoid symbolism, show the Bible.', 'Open your Bible to the passage before every story. Play only that week’s 2–3 book pages. Explain pictures in plain words: “That’s the door. Jesus said He is the door.” [5]'),
        ('Break Bible verses into tiny phrases, add movement, keep it positive.', 'Each Bible word is a short CSB phrase with motions. Never make memorising a test. [4]'),
        ('Children imitate adults; your relationship is a “living commentary” on Scripture.', 'Teachers say “Me too” about their own wrong things, greet every child by name, and pray simply and honestly. [2]'),
        ('Avoid crafts where the adult does the work.', 'Kids’ pages are built for small hands: big shapes, straight cutting lines for threes, curves for fives, and one helper step at most (the paper fastener). [5][7]'),
    ]
    rows = ''.join(f'<tr><td style="width:46%"><b>{esc(a)}</b></td><td>{esc(b)}</td></tr>' for a, b in R)
    return (f'<div class="page"><h2>How little ones learn, and how this series uses it</h2>'
            f'<p>This plan follows patterns found across evangelical preschool curricula and children’s ministry guidance (Lifeway, Awana, Child Evangelism Fellowship and others). '
            f'Numbers in brackets point to the sources at the back of this guide.</p>'
            f'<table class="std"><tr><th>What we know about 3–5s</th><th>What this series does about it</th></tr>{rows}</table>'
            f'<div class="box" style="background:#e3f5ea;margin-top:.14in"><h3>The one-truth rule</h3><p style="margin:0">A three-year-old will take home one sentence, not five. Every week has exactly one: the <b>Say it!</b> line. '
            f'Hook, story, game, verse, craft and snack all point at that same sentence. If the morning goes sideways and you only manage one thing, make it the Say it! with the moves, three times.</p></div>'
            f'<div class="box" style="background:#fdf3d6"><h3>Threes and fives are different</h3><p style="margin:0">A three-year-old is just learning to snip forward on a line; a five-year-old can cut shapes and retell a story in order. '
            f'Each week gives you a line for each. Mixed classes work best with one table for “helpers needed” and one for “I can do it myself”.</p></div>'
            f'{tfoot("How little ones learn")}</div>')

def rhythm():
    rows = [
        ('0:00', 'Arrival table', 'Kids’ page 1 (colour and trace) and crayons are out on the table. Greet every child by name, at their eye level. Late arrivals simply join in.'),
        ('0:08', 'Circle and review', 'Use the attention cue. Review last weeks’ Say it! lines with the moves, then teach today’s: whisper it, say it, SHOUT it.'),
        ('0:12', 'Hook', 'Something to touch, see or do that opens the one truth (5 minutes).'),
        ('0:17', 'Story time', 'Open your Bible to the passage. Play this week’s book pages on a screen. Pause on each picture with one question.'),
        ('0:25', 'Wiggle and play', 'A movement game that carries the truth.'),
        ('0:32', 'Bible words', 'The short CSB phrase, with motions, said several ways (loud, quiet, fast, slow).'),
        ('0:35', 'Table time', 'Kids’ pages 2 and 3: puzzle or maze, then cut and glue or craft. Talk while they work.'),
        ('0:47', 'Snack and talk', 'A snack that ties to the story, with the talk questions.'),
        ('0:53', 'Say it, sticker, pray', 'The Say it! with the moves one last time (or a song you know), a sticker on the Road Home chart, a short prayer, pages into bags.'),
        ('0:60', 'Goodbye', 'Say it! one last time with each parent at the door.'),
    ]
    tr = ''.join(f'<tr><td class="t">{a}</td><td class="what">{b}</td><td>{esc(c)}</td></tr>' for a, b, c in rows)
    return (f'<div class="page"><h2>A Sunday morning, step by step</h2>'
            f'<p>Same order every week. Routine helps little ones feel safe and frees their attention for the story. The times are a guide, not a stopwatch: move on before they get wiggly, not after.</p>'
            f'<table class="plan">{tr}</table>'
            f'<div class="grid2" style="margin-top:.14in"><div class="box line"><h3>Only 45 minutes?</h3><ul><li>Arrival table: 5 minutes</li><li>Drop the separate Bible words slot; say the verse during the wiggle game</li>'
            f'<li>Snack only if your church normally has one</li><li>Send page 1 home unfinished if needed; pages 2 and 3 are the ones to do in class</li></ul></div>'
            f'<div class="box line"><h3>Only 30 minutes (e.g. during the sermon)?</h3><ul><li>Hook 5 · Story 7 · Wiggle 6 · Page 3 craft 8 · Say it and pray 4</li><li>Send pages 1 and 2 home</li></ul></div></div>'
            f'<div class="grid2"><div class="box line"><h3>Set up the room</h3><ul><li><b>Story rug</b> facing the screen, away from the door and the craft table</li><li><b>Craft table</b> with pages, crayons, glue sticks and scissors in a tub per table</li>'
            f'<li><b>Open floor</b> for games (push chairs back)</li><li><b>Road Home charts</b> on the wall at child height</li><li>Screen: a TV, laptop or tablet. Download the book for offline use from the site’s menu in case the Wi-Fi fails</li></ul></div>'
            f'<div class="box line"><h3>Helpers</h3><ul><li>Aim for one adult per 4–5 threes, or 6–8 fives</li><li>Two screened adults in the room at all times, following your church’s child-safety policy</li>'
            f'<li>Give helpers this page and the week’s plan the Sunday before</li><li>One helper owns the craft table so the lead teacher can keep the story moving</li></ul></div></div>'
            f'{tfoot("A Sunday morning")}</div>')

def toolbox():
    sc = [('3', 'Snips forward; cuts a straight 6-inch line within about ½ inch', 'Pre-cut pages 3, or let them tear. They glue and tell.'),
          ('3½–4', 'Straight lines within ¼ inch; starts curves and big circles', 'Cut the story cards themselves (straight lines). Help with the stone and doors.'),
          ('4½–5', 'Squares and simple shapes within ¼ inch', 'Cut everything except the paper fastener. Retell the cards in order.')]
    sct = ''.join(f'<tr><td><b>{a}</b></td><td>{esc(b)}</td><td>{esc(c)}</td></tr>' for a, b, c in sc)
    return (f'<div class="page"><h2>Your classroom toolbox</h2>'
            f'<div class="box" style="background:#e2f0fc"><h3>The attention cue: “Way back…” “HOME!”</h3><p style="margin:0">Teach it in week 1 and use it every time you need the room. You say <b>“Way back…”</b> in a sing-song voice; children answer <b>“HOME!”</b> and put their hands on their heads (a roof). '
            f'Use the same cue every time: little ones do well with routine. [6]</p></div>'
            f'<div class="grid2"><div class="box line"><h3>Quick redirects (have three ready)</h3><ul>'
            f'<li><b>Freeze frame!</b> The book’s clips freeze on their last picture. Call “Freeze frame!” and everyone freezes like the picture.</li>'
            f'<li><b>Copy me:</b> touch nose, ears, toes, then sit.</li><li><b>Call and response:</b> “Kids, kids!” “Yes, yes!” [1]</li>'
            f'<li><b>Touch the picture:</b> invite one child at a time to come and touch Jesus on the screen, then sit down. [1]</li>'
            f'<li><b>The moves:</b> do this week’s Say it! moves together.</li><li><b>Whisper:</b> drop your voice. They lean in.</li></ul></div>'
            f'<div class="box line"><h3>When a child won’t join in</h3><ul><li>Give them a job: hold the snake, open the door, roll the stone. [6]</li><li>Seat them next to you; say their name warmly.</li>'
            f'<li>Let shy ones watch. Watching is learning at this age.</li><li>Unexpected comments are teaching moments: acknowledge, then bring it back. [1]</li></ul></div></div>'
            f'<h3>Scissors by age <span class="small" style="font-family:Lexend;font-weight:400">(averages; children vary) [7]</span></h3>'
            f'<table class="std"><tr><th>Age</th><th>Typical skill</th><th>On page 3</th></tr>{sct}</table>'
            f'<div class="grid2" style="margin-top:.12in"><div class="box line"><h3>Printing</h3><ul><li>US Letter; prints fine on A4 at “fit to page”.</li><li>Print story-card pages (weeks 2–4) and craft pages (5–7) <b>in colour</b> if you can. Everything else works in black and white.</li>'
            f'<li>Card stock helps for page 3 in weeks 5–7.</li><li>Print one Road Home chart per child for the wall, plus 2 spares for visitors.</li></ul></div>'
            f'<div class="box line"><h3>Safety</h3><ul><li>Check allergies before every snack (nuts, gluten, dairy). Swap freely.</li><li>Child-safe scissors only; collect them before snack.</li>'
            f'<li>Paper fasteners (week 6) are small: an adult fastens them.</li><li>Cut grapes lengthways for under-fives.</li><li>Follow your church’s policy on photos and check-out.</li></ul></div></div>'
            f'{tfoot("Classroom toolbox")}</div>')

def gospel():
    return (f'<div class="page"><h2>Sharing Jesus with little ones</h2>'
            f'<p>Preschoolers can understand that God loves them, that they do wrong things, and that Jesus died and rose for them, especially when they hear it again and again at church and at home. '
            f'Think of yourself as a seed planter: share the gospel clearly and often, and trust God with the timing. [3]</p>'
            f'<div class="box" style="background:#fdeedd"><h3>The good news in little words</h3><ol style="margin:0">'
            f'<li><b>God made me and loves me.</b> He wants me home with Him. (weeks 1, 7)</li><li><b>I do wrong things. Everybody does.</b> Wrong things keep us away from God, and I can’t wash them off. (weeks 2–4)</li>'
            f'<li><b>Jesus never did wrong. He died for me and came alive again.</b> (weeks 5–6)</li><li><b>I can say sorry to God and trust Jesus.</b> He makes my heart clean and will welcome me home. (weeks 6–7)</li></ol></div>'
            f'<div class="grid2"><div class="box line"><h3>Do</h3><ul><li>Speak of sin and of Jesus simply and truly, in their words (grumpy, fibs, not sharing).</li>'
            f'<li>Invite, quietly: “If you want to talk to Jesus about this, you can talk to me after.” [3]</li><li>Talk one-to-one with a child who asks questions, and tell the parents the same day. [3]</li>'
            f'<li>Connect punishment to consequences they know: “When we do wrong at home, there’s a consequence. God is fair too.” [3]</li><li>End every hard moment with hope: “But God has a plan!”</li></ul></div>'
            f'<div class="box line"><h3>Don’t</h3><ul><li>Pressure. Little ones are eager to please adults. [3]</li><li>Ask for raised hands or for children to come forward; they copy each other. [3]</li>'
            f'<li>Ask a child directly “Do you want to trust Jesus?” unless they have shown real readiness. [3]</li><li>Make it scary, or so entertaining that the point is lost. [5]</li>'
            f'<li>Count or announce “decisions”.</li></ul></div></div>'
            f'<h3>The harder pages, and how to handle them</h3><table class="std">'
            f'<tr><td style="width:24%"><b>Week 2 · The fruit</b></td><td>A lightning flash and thunder. Lower the volume a little; sit near anyone who startles. “Uh-oh. That was a sad day.”</td></tr>'
            f'<tr><td><b>Week 2 · Out of the garden</b></td><td>Animals died to make clothes. Say it quietly and briefly. It matters in week 5: “Someone has to take our place.”</td></tr>'
            f'<tr><td><b>Week 3 · God’s law</b></td><td>“That makes you a liar and a thief.” Land on “We all do wrong. Me too.” Use yourself as the example, never a child.</td></tr>'
            f'<tr><td><b>Week 4 · Locked out</b></td><td>The book names hell. Say it once, calmly, then straight to hope (see week 4). Your church may prefer to read this page aloud yourself.</td></tr>'
            f'<tr><td><b>Weeks 5–6 · Cross, choice</b></td><td>One child in the book turns away. “He doesn’t want Jesus yet. Jesus still loves him. Jesus lets us choose.”</td></tr></table>'
            f'{tfoot("Sharing Jesus")}</div>')

def supplies():
    allneed = {}
    for w in WEEKS:
        for x in w['hookneed'] + w['extra_need']:
            allneed.setdefault(x, []).append(str(w['n']))
    rows = ''.join(f'<tr><td>{esc(k)}</td><td>{", ".join(v)}</td></tr>' for k, v in allneed.items())
    return (f'<div class="page"><h2>Supplies and prep for all 7 weeks</h2>'
            f'<div class="grid2"><div><h3>Every week</h3><ul><li>A screen (TV, laptop or tablet) with <b>{SITE}</b>, downloaded for offline use</li><li>Your Bible, bookmarked at the week’s passage</li>'
            f'<li>Kids’ pages 1–3 for each child, plus spares</li><li>Crayons, glue sticks, child-safe scissors</li><li>Round stickers for the Road Home chart</li><li>A bag or folder per child for take-home pages</li><li>Snack, wipes, allergy list</li></ul>'
            f'<h3 style="margin-top:.1in">Once, before week 1</h3><ul><li>Print the letter to families and the Road Home charts</li><li>Make the sock-snake puppet (week 2)</li>'
            f'<li>Test the permanent-marker plate and rubbing alcohol at home (weeks 4 and 6)</li><li>Make the shoebox tomb with a paper-plate stone (week 6)</li><li>Buy paper fasteners (week 6) and bubbles (week 7)</li><li>Teach helpers the attention cue and the Say it! moves</li></ul></div>'
            f'<div><h3>Special items, by week</h3><table class="std"><tr><th>Item</th><th>Week</th></tr>{rows}</table></div></div>'
            f'<div class="box" style="background:#efe6fd;margin-top:.14in"><h3>Running threads (don’t lose these!)</h3><ul style="margin:0">'
            f'<li><b>Dot stickers</b> go on in week 3 (“a spot for everyone”) and come off in week 5 when children walk through the door.</li>'
            f'<li><b>The spotty plate</b> won’t scrub clean in week 4, and is wiped clean in week 6.</li>'
            f'<li><b>The Road Home chart</b> gets one sticker every week and goes home with the certificate in week 7.</li></ul></div>'
            f'{tfoot("Supplies")}</div>')

def review_line(n):
    prev = [w for w in WEEKS if w['n'] < n]
    if not prev: return 'Teach the attention cue (“Way back…” “HOME!”).'
    return 'Review with the moves: ' + ' · '.join(f'“{w["say"]}”' for w in prev) + '.'

def week_a(w):
    th = ''.join(img(t) for t in w['thumbs'][:3])
    pause = ''.join(f'<li><b>{esc(a)}:</b> {esc(b)}</li>' for a, b in w['pause'])
    need = ''.join(f'<li>{esc(x)}</li>' for x in ['Screen with the book, your Bible'] + w['hookneed'] + w['extra_need'] + ['Kids’ pages 1–3, crayons, Road Home stickers'])
    return (f'<div class="page"><div class="band" style="background:{w["col"]}"><div><span class="wkpill" style="color:{w["col"]}">WEEK {w["n"]} OF 7</span><h1>{esc(w["title"])}</h1>'
            f'<div class="meta">Book: {esc(" · ".join(w["pages"]))} ({esc(w["book"])}) &nbsp;·&nbsp; Bible: {esc(w["bible"])}</div></div><div class="th">{th}</div></div>'
            f'<div class="box" style="background:{w["soft"]};margin-top:.12in"><h3>Teacher’s heart</h3><p style="margin:0">{esc(w["heart"])}</p></div>'
            f'<div class="box line"><h3>Today’s one truth</h3><p style="margin:0;font-size:11pt">{esc(w["aim"])}</p></div>'
            f'<div class="grid2"><div class="box" style="border:3px solid {w["col"]}"><h3>Say it!</h3><div class="say" style="color:{w["col"]}">“{esc(w["say"])}”</div><p class="small" style="margin:4pt 0 0">{esc(w["moves"])}<br>Say it three ways: whisper, normal, SHOUT.</p></div>'
            f'<div class="box" style="border:3px solid {w["col"]}"><h3>Bible words</h3><div class="verse">{esc(w["verse"][0])}</div><p class="small" style="margin:2pt 0 0"><b>{esc(w["verse"][1])}</b> (CSB). Motions: {esc(w["vmoves"])}</p></div></div>'
            f'<div class="grid2"><div class="box line"><h3>Story time: pause and ask</h3><p class="small" style="margin-bottom:3pt">Open your Bible to {esc(w["bible"])} first: “This true story comes from God’s Book.” Then play the pages at {SITE}.</p><ul style="margin:0">{pause}</ul></div>'
            f'<div class="box line" style="flex:.62"><h3>You need</h3><ul style="margin:0">{need}</ul></div></div>'
            f'<div class="box" style="background:{w["soft"]}"><h3>Talk (at snack or table time)</h3><ul style="margin:0">{"".join(f"<li>{esc(q)}</li>" for q in w["talk"])}</ul></div>'
            f'{tfoot(f"Week {w["n"]} · page 1 of 2")}</div>')

def week_b(w):
    n = w['n']
    plan = [
        ('0:00', 'Arrival table', f'Kids’ page 1: “{TASK1[n]}” Greet each child by name.'),
        ('0:08', 'Circle', f'Attention cue. {review_line(n)} Then teach today’s Say it! with the moves.'),
        ('0:12', f'Hook: {w["hook"][0]}', w['hook'][1]),
        ('0:17', 'Story time', f'Bible open at {w["bible"]}. Play {", ".join(w["pages"])} ({w["book"]}). Use the pause questions on page 1.'),
        ('0:25', f'Play: {w["wiggle"][0]}', w['wiggle'][1]),
        ('0:32', 'Bible words', f'{w["verse"][0]} ({w["verse"][1]}). Break it into tiny pieces; children echo each one, then add the motions.'),
        ('0:35', 'Table time', f'Kids’ pages 2 and 3: {" and ".join(w["pages_kid"][1:])}. {w["table"]}'),
        ('0:47', f'Snack: {w["snack"][0]}', w['snack'][1] + ' Then the talk questions (page 1).'),
        ('0:53', 'Say it, sticker, pray', f'The Say it! with the moves once more (add a song you know if you like). Sticker on stop {n} of the Road Home chart. Pray: {w["pray"]}'),
        ('0:60', 'Goodbye', f'Pages 1–3 into bags. Do the Say it! with each parent at the door. Page 2’s grown-ups box asks: “{w["ask"]}”'),
    ]
    tr = ''.join(f'<tr><td class="t" style="color:{w["col"]}">{a}</td><td class="what">{esc(b)}</td><td>{esc(c)}</td></tr>' for a, b, c in plan)
    care = (f'<div class="box" style="background:#fde7e5"><h3>Handle with care</h3><p style="margin:0">{esc(w["care"])}</p></div>' if w['care'] else '')
    return (f'<div class="page"><h2 style="color:{w["col"]};font-size:17pt">Week {n} · The plan</h2><table class="plan">{tr}</table>'
            f'<div class="grid2" style="margin-top:.1in"><div><div class="box line"><h3>Threes</h3><p style="margin:0">{esc(w["three"])}</p></div>'
            f'<div class="box line"><h3>Fives</h3><p style="margin:0">{esc(w["five"])}</p></div></div>'
            f'<div>'
            f'<div class="box line"><h3>Teacher tip</h3><p style="margin:0">{esc(w["tip"])}</p></div></div></div>{care}'
            f'{tfoot(f"Week {n} · page 2 of 2")}</div>')

def answers():
    def order(n):
        shown = [CARD_LABEL[n][k] for k in CARD_ORDER[n]]
        return f'Printed left to right: {", ".join(shown)}. Correct order: 1 {CARD_LABEL[n][0]}, 2 {CARD_LABEL[n][1]}, 3 {CARD_LABEL[n][2]}.'
    rows = [('Week 1 · Count', 'Sun 1, trees 2, birds 3, fish 4, flowers 5.'), ('Week 1 · Stick-a-garden', 'Any arrangement! Talk: “Who made the sun? The fish? You?”'),
            ('Week 2 · Snakes', 'One in the left tree, one in the right tree, one on the middle bush, one in the grass at bottom right.'),
            ('Week 2 · Story cards', order(2)), ('Week 3 · Maze', 'One path only. Let children trace with a finger first.'), ('Week 3 · Story cards', order(3)),
            ('Week 4 · Soap', 'Circle the boot, plate, hands and dog. X on the heart: “Only God can make hearts clean.”'), ('Week 4 · Story cards', order(4)),
            ('Week 5 · Door craft', 'Cut the door on its three thick sides; fold along the dashed side. Cut the top panel off the page, glue it on the grey edges of the bottom panel so the door sits over the picture.'),
            ('Week 6 · Tombs', 'The middle tomb is empty.'), ('Week 6 · Stone craft', 'Push a paper fastener through the dot on the stone, then the dot beside the doorway, so the stone swings over the opening and rolls away.'),
            ('Week 7 · Gates craft', 'Same as the door: cut the middle line and the top and bottom of the gates, fold on the dashed sides, glue the top panel over the picture.')]
    tr = ''.join(f'<tr><td style="width:28%"><b>{esc(a)}</b></td><td>{esc(b)}</td></tr>' for a, b in rows)
    return f'<div class="page"><h2>Answer keys and craft help</h2><table class="std">{tr}</table>{tfoot("Answer keys")}</div>'

def songs():
    boxes = ''.join(f'<div class="box" style="background:{w["soft"]};width:48.5%;margin-bottom:.12in"><h3><span class="pill" style="background:{w["col"]}">{w["n"]}</span> {esc(w["title"])} <span class="small" style="font-family:Lexend;font-weight:400">· tune: {esc(w["song"][0])}</span></h3>'
                    f'<p style="margin:0">{"<br>".join(esc(x) for x in w["song"][1])}</p><p class="small" style="margin:3pt 0 0">Say it! “{esc(w["say"])}” · {esc(w["moves"])}</p></div>' for w in WEEKS)
    return (f'<div class="page"><h2>All the songs and moves</h2><p>New words to tunes everyone knows (all public-domain tunes). Post this page by the door so helpers and parents can join in.</p>'
            f'<div style="display:flex;flex-wrap:wrap;justify-content:space-between">{boxes}</div>{tfoot("Songs")}</div>')

def sources():
    S = ['Awana, “11 tips to maintain preschoolers’ attention, part 2” (2017). awana.org',
         'Lifeway, “Eight ways preschoolers learn”. lifeway.com',
         'Awana, “Sharing the gospel with preschoolers” (2018). awana.org',
         'Awana, “8 tips for doing Scripture memory with preschoolers” (2018). awana.org',
         'BibleCharts, “Methods for teaching preschoolers ages 3–5” (PDF). biblecharts.org',
         'Ministry-to-Children, “6 quick classroom tips for engaging preschoolers”. ministry-to-children.com',
         'Growing Hands-On Kids, “Scissor skill development checklist for ages 2–6”. growinghandsonkids.com']
    li = ''.join(f'<li>{esc(s)}</li>' for s in S)
    return (f'<div class="page"><h2>Sources</h2><ol>{li}</ol>'
            f'<h3 style="margin-top:.2in">About the pictures</h3><p>All pictures are frames from <i>The Way Back Home</i> book and its animated clips, by Johnny Wall. Colouring pages are simple hand-drawn outlines made for small hands.</p>'
            f'<h3>Bible text</h3><p>{CSB} Short phrases are quoted from Genesis 1:31, Proverbs 30:5, Romans 3:23, Ephesians 2:8, John 3:16, Luke 24:6 and 1 John 4:19. '
            f'“I am the door” is the book’s own wording of John 10:9 (CSB has “gate”).</p>'
            f'<div class="box" style="background:#e2f0fc;margin-top:.2in"><h3>Free to read and listen</h3><p style="margin:0">The whole book, in many languages, is free at <b>{SITE}</b>. Families can scan the code on every week’s page 2.</p></div>'
            f'{tfoot("Sources")}</div>')

def build_teacher():
    pages = [cover(), glance(), learn(), rhythm(), toolbox(), gospel(), supplies()]
    for w in WEEKS: pages += [week_a(w), week_b(w)]
    pages += [answers(), sources()]
    return f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{TCSS}</style></head><body>{"".join(pages)}</body></html>'

if __name__ == '__main__':
    import weasyprint
    open(f'{B}/teacher.html', 'w').write(build_teacher())
    weasyprint.HTML(f'{B}/teacher.html', base_url=B).write_pdf(f'{B}/teacher.pdf')
    print('ok')
