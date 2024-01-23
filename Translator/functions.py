
import torch
import numpy as np

class Vocabulary:
    PAD_token = 0   # Used for padding short sentences
    SOS_token = 1   # Start-of-sentence token
    EOS_token = 2   # End-of-sentence token
    NEW_WORD = 3
    MASK_token = 4
    # [SOS]The first token is always classification
    # [SEP]Separates two sentences
    # [END]End the sentence.
    # [PAD]Use to truncate the sentence with equal length.
    # [MASK] Use to create a mask by replacing the original word.
    # [UNK] unkown
    def __init__(self, name, tokenizer, sentence_trim=50):
      self.PAD_token = 0   # Used for padding short sentences
      self.SOS_token = 1   # Start-of-sentence token
      self.EOS_token = 2   # End-of-sentence token
      self.NEW_WORD = 3
      self.MASK_token = 4
      self.tokenizer = tokenizer
      self.name = name
      self.word2index = { "new_word" : self.NEW_WORD}
      self.word2count = { "new_word" : 1 }
      self.index2word = { self.PAD_token: "PAD", self.SOS_token: "SOS", self.EOS_token: "EOS", self.NEW_WORD : "new_word", self.MASK_token : "MASK" }
      self.num_words = 4
      self.num_sentences = 0
      self.longest_sentence = 0
      self.sentence_trim = sentence_trim

    def add_word(self, word):
      if word not in self.word2index:
        # First entry of word into vocabulary
        self.word2index[word] = self.num_words
        self.word2count[word] = 1
        self.index2word[self.num_words] = word
        self.num_words += 1
      else:
        # Word exists; increase word count
        self.word2count[word] += 1

    def add_sentence(self, sentence):
      sentence_len = 0
      for word in [tok.text.lower() for tok in self.tokenizer.tokenizer(sentence.replace('\n',''))]:
        sentence_len += 1
        self.add_word(word)
      if sentence_len > self.longest_sentence:
        # This is the longest sentence
        self.longest_sentence = sentence_len
      # Count the number of sentences
      self.num_sentences += 1

    def to_word(self, index):
      return self.index2word[index]

    def to_index(self, word):
      return self.word2index[word.lower()]

    def sentence_to_index(self, sentence, padding=False):
      array = []
      array.append(self.SOS_token)
      for tok in self.tokenizer.tokenizer(sentence.lower().replace('\n','')):
        try:
          array.append(self.to_index(tok.text))
        except:
          #self.add_word(tok.text)
          #array.append(self.to_index(tok.text))
          array.append(self.to_index("new_word"))
      array.append(self.EOS_token)
      if padding:
        for i in range(len(array),self.sentence_trim):
          array.append(self.PAD_token)
        return array[:self.sentence_trim]
      else:
        return array

def train(model, optimizer, criterion, clip, src, trg):

    model.train()

    epoch_loss = 0
    it = 0
    for i in chunks(np.arange(src.shape[1]), 64):
        it += 1
        #print(it)
        
        optimizer.zero_grad()

        output, _ = model(src[:,i], trg[:,i])

        """
        output_dim = output.shape[-1]

        output = output[1:].view(-1, output_dim)
        trg = trg[1:].view(-1)

        loss = criterion(output, trg)
        """
        loss = criterion(output.view(-1, output.shape[-1]), trg[:,i].reshape(-1,1)[:,0])
        loss.backward()

        torch.nn.utils.clip_grad_norm_(model.parameters(), clip)

        optimizer.step()

        epoch_loss += loss.item()

    return epoch_loss / 64

def evaluate(model, criterion, src, trg):

  model.eval()

  epoch_loss = 0

  with torch.no_grad():

    for i in chunks(np.arange(src.shape[1]), 64):
      
      output, _ = model(src[:,i], trg[:,i],0) #turn off teacher forcing
      """
      #trg = [trg len, batch size]
      #output = [trg len, batch size, output dim]

      output_dim = output.shape[-1]

      output = output[1:].view(-1, output_dim)
      trg = trg[1:].view(-1)

      #trg = [(trg len ) * batch size]
      #output = [(trg len ) * batch size, output dim]
      """
      loss = criterion(output.view(-1, output.shape[-1]), trg[:,i].reshape(-1,1)[:,0])

      epoch_loss += loss.item()

  return epoch_loss / 64

def epoch_time(start_time, end_time):
    elapsed_time = end_time - start_time
    elapsed_mins = int(elapsed_time / 60)
    elapsed_secs = int(elapsed_time - (elapsed_mins * 60))
    return elapsed_mins, elapsed_secs

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def count_parameters(model):
    return sum(p.numel() for p in model.parameters() if p.requires_grad)

def pretty_size(size):
  """Pretty prints a torch.Size object"""
  assert(isinstance(size, torch.Size))
  return " × ".join(map(str, size))

def dump_tensors(gpu_only=True):
  """Prints a list of the Tensors being tracked by the garbage collector."""
  import gc
  total_size = 0
  for obj in gc.get_objects():
    try:
      if torch.is_tensor(obj):
        if not gpu_only or obj.is_cuda:
          print("%s:%s%s %s" % (type(obj).__name__,
                      " GPU" if obj.is_cuda else "",
                                          " pinned" if obj.is_pinned else "",
                      pretty_size(obj.size())))
          total_size += obj.numel()
      elif hasattr(obj, "data") and torch.is_tensor(obj.data):
        if not gpu_only or obj.is_cuda:
          print("%s → %s:%s%s%s%s %s" % (type(obj).__name__,
                           type(obj.data).__name__,
                           " GPU" if obj.is_cuda else "",
                           " pinned" if obj.data.is_pinned else "",
                           " grad" if obj.requires_grad else "",
                           " volatile" if obj.volatile else "",
                           pretty_size(obj.data.size())))
          total_size += obj.data.numel()
    except Exception as e:
      print('Error:',e)
      #pass
  print("Total size:", total_size)
