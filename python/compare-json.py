import json
import glob
import os

with open('/root/data/muddy/all-nurbs.json') as f:
    all_nurbs = json.load(f)

joined_nurbs = {}
for fname in glob.glob('/root/data/1377*.json'):
    name = os.path.splitext(os.path.basename(fname))[0]
    with open(fname) as f:
        jjj = json.load(f)
        for k, v in list(jjj.items()):
            if k.endswith('Len'):
                del jjj[k]
        joined_nurbs[name] = jjj

with open('/root/data/muddy/a.json', 'w') as f:
    json.dump(all_nurbs, f, separators=(',\n', ': \n'), sort_keys=True)
with open('/root/data/muddy/b.json', 'w') as f:
    json.dump(joined_nurbs, f, separators=(',\n', ': \n'), sort_keys=True)
