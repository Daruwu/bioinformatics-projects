#!/usr/bin/python3

sequence = input("Enter a sequence: ")
k = int(input("Enter a k-mer: "))
d = int(input("Enter a d: "))

complement = { 'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
def reverse_complement(kmer):
	r = ''
	for base in kmer:
		r = complement[base] + r
	return r

def enumerate_mismatches (kmer, maxdist):
	if maxdist == 0:
		return [kmer]
	else:
		r = []
		for m_kmer in enumerate_mismatches(kmer, maxdist - 1):
			for loc in range(k):
				for base in ['A', 'C', 'G', 'T']:
					new_kmer = m_kmer[:loc] + base + m_kmer[loc + 1:]
					r.append(new_kmer)
		return set(r)

kmer_counts = {}
max_kmers = []
max_kmer_count = 0
for idx in range(len(sequence) - k + 1):
	kmer = sequence[idx:idx+k]
	m_kmers = list(enumerate_mismatches(kmer, d))
	m_kmers.extend(list(enumerate_mismatches(reverse_complement(kmer), d)))
	for m_kmer in m_kmers:
		if m_kmer in kmer_counts:
			count = kmer_counts[m_kmer] + 1
		else:
			count = 1
		kmer_counts[m_kmer] = count

		if count > max_kmer_count:
			max_kmer_count = count
			max_kmers = [m_kmer]
		elif count == max_kmer_count:
			max_kmers.append(m_kmer)
            
print (" ".join(max_kmers))