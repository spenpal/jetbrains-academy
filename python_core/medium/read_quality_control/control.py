# IMPORTS #
from statistics import mean
import gzip


# FUNCTIONS #
def get_data(file):
    sequences = file.read().decode().splitlines()[1::4]
    sequences_lengths = map(len, sequences)

    gc_contents = []
    for sequence in sequences:
        gc = (sequence.count('G') + sequence.count('C')) / len(sequence)
        gc_contents.append(gc)

    ns_percents = []
    for sequence in sequences:
        n_percent = sequence.count('N') / len(sequence) * 100
        ns_percents.append(n_percent)

    data = {
        'filename': file.name,
        'reads': len(sequences),
        'avg_read_length': round(mean(sequences_lengths)),
        'repeats': len(sequences) - len(set(sequences)),
        'n_reads': sum(1 for sequence in sequences if "N" in sequence),
        'avg_gc_content': round(mean(gc_contents) * 100, 2),
        'avg_n_percent': round(mean(ns_percents), 2)
    }

    return data


def compare(*archives):
    least_repeats = list(sorted(archives, key=lambda a: a['repeats']))[0]
    least_n_reads = list(sorted(archives, key=lambda a: a['n_reads']))[0]
    least_avg_n_percent = list(sorted(archives, key=lambda a: a['avg_n_percent']))[0]
    most_gc_content = list(sorted(archives, key=lambda a: a['avg_gc_content'], reverse=True))[0]

    criteria = [least_repeats, least_n_reads, least_avg_n_percent, most_gc_content]
    return max(criteria, key=criteria.count)


# MAIN #
with gzip.open(input()) as f1, gzip.open(input()) as f2, gzip.open(input()) as f3:
    f1_data = get_data(f1)
    f2_data = get_data(f2)
    f3_data = get_data(f3)

best_data = compare(f1_data, f2_data, f3_data)

output = [
    f'Reads in the file = {best_data.get("reads")}',
    f'Reads sequence average length = {best_data.get("avg_read_length")}',
    '',
    f'Repeats = {best_data.get("repeats")}',
    f'Reads with Ns = {best_data.get("n_reads")}',
    '',
    f'GC content average = {best_data.get("avg_gc_content")}%',
    f'Ns per read sequence = {best_data.get("avg_n_percent")}%'
]
print(*output, sep='\n')
