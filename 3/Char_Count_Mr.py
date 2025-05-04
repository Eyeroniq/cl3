from mrjob.job import MRJob

class MRCharCount(MRJob):
    def mapper(self, _, line):
        for char in line.strip():
            yield char, 1

    def reducer(self, char, counts):
        yield char, sum(counts)

if __name__ == '__main__':
    MRCharCount.run()
