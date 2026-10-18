# Sunday school packs (Little ones 3–5, Sunday school 6–9)

Python generators for resources/class/*.pdf (written 17 Oct 2026). WeasyPrint renders HTML to PDF.

- content.py / content69.py: the lessons (one dict per week). art.py: the hand-drawn SVG colouring art and puzzles.
- build.py kids → kids.pdf (Little ones children's pages); teacher.py → teacher.pdf (Little ones guide)
- build69.py → kids69.pdf; teacher69.py → teacher69.pdf

They were run from /tmp/claude-0/gen with output in /tmp/claude-0/build. To run again:
1. `pip install weasyprint segno`
2. Make a build folder with `img/` (540-px-wide JPEGs of the book stills named as in the scripts, e.g. `ffmpeg -i art/src/garden-end.jpg -vf scale=540:-1 img/garden-end.jpg`;
   plus frames: rule-point, gates-run, tomb-glow, road-mid, garden-mid from scenes/) and copy fonts/*.woff2 + fonts/fonts.css into it,
   adding @font-face rules for Lexend and Bricolage Grotesque.
3. Change the paths at the top of the scripts (`/tmp/claude-0/gen`, `B = '/tmp/claude-0/build'`) to yours.
4. Copy the four PDFs to resources/class/ as little-teacher, little-kids, sunday-teacher, sunday-kids.
5. If any page order or the "My name:" line position changes, update resources/class/classes.json (classprint.html depends on it).
