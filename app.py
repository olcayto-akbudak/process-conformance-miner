"""Süreç Uygunluk ve Varyant Analizi.

Problem: İşlem günlüklerinin zorunlu süreç adımlarını atlayıp atlamadığını açıklamalı biçimde ölçmek.
Method: Petri net token replay, paralel adımlar
Invariant: Eksik giriş jetonları sanal olarak eklenir ve ihlal sayılır; sonuç fit bayrağı ve fitness birlikte okunur.
Boundary: Optimal alignment algoritması değildir; zaman ve kaynak kuralları ayrıca modellenmelidir."""
from collections import Counter, defaultdict

class PetriNet:

    def __init__(self, transitions, initial, final):
        self.transitions = transitions
        self.initial = Counter(initial)
        self.final = Counter(final)
        if any((type(v) is not int or v < 0 for v in list(initial.values()) + list(final.values()))):
            raise ValueError('nonnegative markings')
        for name, t in transitions.items():
            if not t['consume'] or not t['produce']:
                raise ValueError('empty transition')
            if any((type(v) is not int or v <= 0 for v in list(t['consume'].values()) + list(t['produce'].values()))):
                raise ValueError('positive arc weights required')

    def replay(self, trace):
        marking = self.initial.copy()
        missing = 0
        consumed = 0
        produced = sum(marking.values())
        violations = []
        for index, event in enumerate(trace):
            if event not in self.transitions:
                violations.append({'position': index, 'event': event, 'reason': 'unknown_activity'})
                continue
            t = self.transitions[event]
            for place, need in t['consume'].items():
                deficit = max(0, need - marking[place])
                missing += deficit
                if deficit:
                    violations.append({'position': index, 'event': event, 'reason': 'missing_token', 'place': place, 'count': deficit})
                marking[place] = max(0, marking[place] - need)
                consumed += need
            marking.update(t['produce'])
            produced += sum(t['produce'].values())
        final_missing = sum((max(0, v - marking[k]) for k, v in self.final.items()))
        remaining = sum((max(0, v - self.final[k]) for k, v in marking.items()))
        fitness = 0.5 * (1 - (missing + final_missing) / max(1, consumed + sum(self.final.values()))) + 0.5 * (1 - remaining / max(1, produced))
        return {'fit': not violations and (not final_missing) and (not remaining), 'missing_during_replay': missing, 'missing_final': final_missing, 'remaining': remaining, 'fitness': round(max(0, fitness), 4), 'marking': dict(marking), 'violations': violations}

def analyze(net, cases):
    if len({c['id'] for c in cases}) != len(cases):
        raise ValueError('duplicate case ID')
    reports = []
    variants = defaultdict(list)
    for case in cases:
        result = net.replay(case['trace'])
        result['case_id'] = case['id']
        reports.append(result)
        variants[tuple(case['trace'])].append(case['id'])
    return {'cases': reports, 'variants': [{'activities': list(k), 'cases': len(ids), 'case_ids': ids} for k, ids in sorted(variants.items())], 'fit_pct': round(100 * sum((r['fit'] for r in reports)) / len(reports), 2) if reports else None}

def run(config):
    return analyze(PetriNet(config['transitions'], config['initial'], config['final']), config['cases'])

import argparse, json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description='Run reproducible synthetic project scenario')
    parser.add_argument('command', choices=['demo'])
    parser.add_argument('--input', default='scenario.json')
    parser.add_argument('--output', default='report.json')
    args = parser.parse_args()
    report = run(json.loads(Path(args.input).read_text(encoding='utf-8')))
    target = Path(args.output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False), encoding='utf-8')
    print(f'Report: {target}')
if __name__ == '__main__':
    main()
