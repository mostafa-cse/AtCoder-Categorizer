import sqlite3, json, sys

sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect('data/atcoder_problems.db')
c = conn.cursor()

with open('state/progress.json', 'r', encoding='utf-8') as f:
    evaluated = set(json.load(f).get('evaluated_problems', []))

c.execute('''
    SELECT id, contest_id, title, difficulty, url
    FROM problems
    WHERE difficulty >= 1900 AND difficulty <= 1950
      AND (contest_id LIKE 'abc%' OR contest_id LIKE 'arc%')
    ORDER BY difficulty ASC, id ASC
''')
rows = c.fetchall()

print(f"Total candidates in 1900-1950: {len(rows)}")
unprocessed = [r for r in rows if r[0] not in evaluated]
print(f"Unprocessed candidates: {len(unprocessed)}")
for idx, r in enumerate(unprocessed):
    print(f"{idx+1:2d}. {r[0]:15} | {r[1]:10} | {r[3]:4} | {r[2]}")
