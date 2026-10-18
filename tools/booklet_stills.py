#!/usr/bin/env python3
"""Extra stills for the printed booklet (booklet.html), taken from the animated scenes.

Each entry: name -> (clip in scenes/, seconds). Writes art/booklet/<name>.jpg at the clip's
full size. Stills that already exist in art/src (the -clip / -end frames from the original
uploads, which are sharper) are used directly by booklet.html and are not listed here.
When Johnny supplies sharper art for a scene, drop it in art/booklet/ with the same name.
Run from the repo root: python3 tools/booklet_stills.py
"""
import subprocess, pathlib
STILLS = {
    'garden-a':   ('garden', 0.3),    # God reaching out to Adam and Eve
    'rule-look':  ('rule', 0.2),      # Adam and Eve looking at the tree
    'serpent-a':  ('serpent', 2.5),   # the serpent whispering, Eve listening
    'fruit-bite': ('fruit', 1.0),     # Eve takes a bite
    'fruit-adam': ('fruit', 4.0),     # Adam takes some too
    'exile-kneel':('exile', 1.0),     # kneeling before God, serpent nearby
    'exile-shame':('exile', 7.5),     # faces in their hands at the gate
    'road-two':   ('road', 0.5),      # Adam and Eve alone on the road
    'road-family':('road', 3.5),      # children and grandchildren
    'road-crowd': ('road', 8.0),      # the crowd through history
    'locked-heaven':('locked', 2.0),  # heaven seen in the mirror
    'scrub-hard': ('scrub', 0.5),     # scrubbing hard
    'scrub-upset':('scrub', 5.0),     # it won't come off
    'door-point': ('door', 2.0),      # the preacher points to the door
    'choice-walk':('choice', 1.0),    # one walks away, two kneel
    'choice-move':('choice', 4.5),    # the stains move onto the cross
    'tomb-burst': ('tomb', 2.0),      # light bursts from the tomb
    'gates-open': ('gates', 3.5),     # Jesus with arms open wide
    'new-earth-talk':('new-earth', 2.2),
    'new-earth-hands':('new-earth', 6.0),
}
out = pathlib.Path('art/booklet'); out.mkdir(parents=True, exist_ok=True)
for name, (clip, t) in STILLS.items():
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', str(t), '-i', f'scenes/{clip}.mp4',
                    '-frames:v', '1', '-q:v', '2', str(out / f'{name}.jpg')], check=True)
    print(name)
