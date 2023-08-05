class ELMOFromFile:

    def __init__(self, corpus_file, magnitude_file, corpus_name, label_name=None, num_chunks=1, save_directory="./",
                 max_length=None):
        import pymagnitude as pm
        import numpy as np
        self.max_length=max_length
        self.corpus_name = corpus_name
        self.corpus = corpus_file
        self.vectors = pm.Magnitude(magnitude_file)
        self.labels = label_name
        self.num_chunks = num_chunks
        self.save_dir = save_directory
        self.chunk_size = int(self.corpus_size/self.num_chunks)
        self.current_chunk_index = 0

    def read_and_save(self, verbose=False):
        import pandas as pd

        for chunk in pd.read_csv(self.corpus, chunksize=self.chunk_size):
            if self.labels:
                chunk_labels = chunk[self.labels]
                chunk_corpus = chunk.drop([self.labels], axis=1)
            else:
                chunk_labels = None
                chunk_corpus = chunk
            x = ELMOEmbeddedCorpus(chunk_corpus, self.corpus_name, self.vectors, labels=chunk_labels, max_length=self.max_length,
                                   num_chunks=1, file_directory=self.save_dir, chunk_value=self.current_chunk_index)
            x.save_chunk(verbose=verbose)
            self.current_chunk_index += 1
            x = None

    def fit_and_save_chunk(self, chunk_corpus, chunk_labels, verbose=False):
        import pickle
        import numpy as np

        embedding = np.zeros((len(chunk_corpus), self.max_length, self.vectors.dim))
        if verbose:
            import tqdm
            for index in tqdm.tqdm(range(self.split_dist)):
                embedding[index] = self.fit_doc(self.current_chunk[index])
        else:
            for index in range(self.split_dist):
                embedding[index] = self.fit_doc(self.current_chunk[index])

        chunk_file = self.file_dir + self.name + '__' + str(self.current_chunk_index) + '.dat'
        if self.labels:
            label_file = self.file_dir + self.name + '__' + str(self.current_chunk_index) + '_l.dat'
            pickle.dump(self.current_label_chunk, open(label_file, 'wb'), protocol=4)
        pickle.dump(self.fit_chunk(verbose=verbose), open(chunk_file, 'wb'), protocol=4)

class ELMOEmbeddedCorpus:

    def __init__(self, corpus, name, magnitude_file, labels=None, max_length=None, num_chunks=1, file_directory='./', chunk_value=0):

        # If input corpus is a TextProcessor object, transform it.  Else, treat as already processed
        try:
            self.corpus = corpus.transform()
        except:
            try:
                self.corpus = corpus.tolist()
            except:
                self.corpus = corpus

        try:
            self.labels = labels.tolist()
        except:
            self.labels = self.labels
        self.name = name

        #import pymagnitude ELMO vectors
        import pymagnitude
        self.vectors = pymagnitude.Magnitude(magnitude_file)

        #set maximum length of the documents in our corpus
        if max_length:
            self.max_length = max_length
        else:
            self.max_length = np.max([len(x) for x in self.corpus])

        self.file_dir = file_directory
        self.split_factor = num_chunks
        if self.split_factor == 1:
            self.current_chunk_index = chunk_value
            self.split_dist = len(self.corpus)
            self.current_chunk = self.corpus
            if self.labels:
                self.current_label_chunk = self.labels
        else:
            self.split_dist = int(len(self.corpus) / self.split_factor)
            self.current_chunk_index = 0
            self.current_chunk = self.corpus[self.current_chunk_index*self.split_dist:(self.current_chunk_index+1)*self.split_dist]
            if self.labels:
                self.current_label_chunk = self.labels[self.current_chunk_index*self.split_dist:(self.current_chunk_index+1)*self.split_dist]

    def fit_doc(self, doc):

        embedding = np.zeros((self.max_length, self.vectors.dim))
        doc_length = len(doc)
        embedding[:doc_length]=self.vectors.query(doc)
        return embedding

    def fit_chunk(self, verbose = True):
        embedding = np.zeros((self.split_dist, self.max_length, self.vectors.dim))
        if verbose:
            import tqdm
            for index in tqdm.tqdm(range(self.split_dist)):
                embedding[index] = self.fit_doc(self.current_chunk[index])
        else:
            for index in range(self.split_dist):
                embedding[index] = self.fit_doc(self.current_chunk[index])
        return embedding

    def save_chunk(self, verbose=False):
        import pickle

        chunk_file = self.file_dir + self.name + '__' + str(self.current_chunk_index) + '.dat'
        pickle.dump(self.fit_chunk(verbose=verbose), open(chunk_file, 'wb'), protocol=4)
        if self.labels:
            label_file = self.file_dir + self.name + '__' + str(self.current_chunk_index) + '_l.dat'
            pickle.dump(self.current_label_chunk, open(label_file, 'wb'), protocol=4)

    def change_chunk(self, new_index):
        self.current_chunk_index = new_index
        self.current_chunk = self.corpus[self.current_chunk_index * self.split_dist:(self.current_chunk_index + 1) * self.split_dist]
        self.current_label_chunk = self.labels[self.current_chunk_index * self.split_dist:(self.current_chunk_index + 1) * self.split_dist]

    def fit_and_save_all(self, verbose=False):
        if self.split_factor == 1:
            self.save_chunk(verbose=verbose)
        elif verbose:
            import tqdm
            for chunk in tqdm.tqdm(range(self.split_factor)):
                self.change_chunk(chunk)
                self.save_chunk(verbose=True)
        else:
            for chunk in range(self.split_factor):
                self.change_chunk(chunk)
                self.save_chunk()

class LoadEmbeddedCorpus:

    def __init__(self, matrix_name, file_dir='./', labels = True):

        from os import listdir
        self.labels = labels
        self.name = matrix_name + '__'
        self.file_dir = file_dir
        self.all_files = [f for f in listdir(file_dir)]
        self.chunk_files = list(filter(lambda x: x[:len(matrix_name)] == matrix_name, self.all_files))
        self.all_chunks_available = [int(x[len(self.name):-4]) for x in self.chunk_files if x[len(self.name):-4].isdigit()]
        if (2*len(self.all_chunks_available) != len(self.chunk_files)) and self.labels:
            raise ValueError('File missing label and/or corpus chunks.')

    def load(self, index):
        import pickle

        if index not in self.all_chunks_available:
            raise ValueError('Indexed slice not found in current directory.')

        file = open(self.file_dir + self.name + str(index) + '.dat', "rb")
        embedded_chunk = pickle.load(file)

        if self.labels:
            label_file = open(self.file_dir + self.name + str(index) + '_l.dat', 'rb')
            labels = pickle.load(label_file)
            return embedded_chunk, labels
        else:
            return embedded_chunk
