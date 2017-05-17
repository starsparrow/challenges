#!/usr/bin/env python


# Class definition

class Address:
    def __init__(self, address):
        self.address = address

    def __str__(self):
        return self.address

    def is_abba(self, segment):
        """Check to see whether supplied four-character string is ABBA and
        returns True/False."""
        if len(segment) == 4:
            letters = list(segment)
            return (
                       letters[0] == letters[3] and
                       letters[0] != letters[1] and
                       letters[1] == letters[2]
                    )
        else:
            raise ValueError('Address segment passed to is_abba() must be four \
characters long.')

    def is_aba(self, segment):
        """Check to see whether supplied four-character string is ABBA and
        returns True/False."""
        if len(segment) == 3:
            letters = list(segment)
            return (
                       letters[0] == letters[2] and
                       letters[0] != letters[1]
                    )
        else:
            raise ValueError('Address segment passed to is_aba() must be three \
characters long.')

    def contains_abba(self, sequence):
        """Checks a sequence for existence of an ABBA, returns True/False"""
        if len(sequence) < 4:
            return False
        else:
            start = 0
            end = 4
            while end < len(sequence) + 1:
                if self.is_abba(sequence[start:end]):
                    return True
                else:
                    start += 1
                    end += 1
            return False

    def get_abas(self, sequence):
        """Returns a list of all ABAs in a given sequence"""
        abas = []
        if len(sequence) < 3:
            return abas
        else:
            start = 0
            end = 3
            while end < len(sequence) + 1:
                if self.is_aba(sequence[start:end]):
                    abas.append(sequence[start:end])
                start += 1
                end += 1
            return abas

    def get_sequences(self):
        """Splits an address into supernet and hypernet sequences"""
        address = self.address
        sequences = []
        while len(address) > 0:
            next_hypernet_start_index = address.find('[')
            next_hypernet_end_index = address.find(']')
            if next_hypernet_start_index == 0:
                sequences.append(address[0:next_hypernet_end_index + 1])
            elif next_hypernet_start_index == -1:
                sequences.append(address[0:])
            elif next_hypernet_start_index > 0:
                sequences.append(address[0:next_hypernet_start_index])
                
            address = address[len(sequences[len(sequences) - 1]):]
        
        return sequences

    def supports_tls(self):
        """Returns if there is an ABBA in supernet but not in hypernet"""
        hypernet_contains_abba = False
        supernet_contains_abba = False
        for sequence in self.get_sequences():
            if (len(sequence) >= 6 and sequence[0] == '[' and
                self.contains_abba(sequence)):
                    hypernet_contains_abba = True
            if (len(sequence) >= 4 and sequence[0] != '[' and 
                self.contains_abba(sequence)):
                    supernet_contains_abba = True
        if supernet_contains_abba and not hypernet_contains_abba:
            return True
        else:
            return False

    def supports_ssl(self):
        """Returns True if ABA in supernet and corresponding BAB in hypernet"""
        hypernet_abas = []
        supernet_abas = []
        for sequence in self.get_sequences():
            if sequence[0] == '[':
                abas = self.get_abas(sequence)
                for aba in abas:
                    if aba not in hypernet_abas:
                        hypernet_abas.append(aba)
            else:
                abas = self.get_abas(sequence)
                for aba in abas:
                    if aba not in supernet_abas:
                        supernet_abas.append(aba)
        for aba in hypernet_abas:
            bab = '{}{}{}'.format(aba[1], aba[0], aba[1])
            if bab in supernet_abas:
                return True
        return False


# Main section

with open('input.txt', 'r') as f:
    data = f.readlines()
    print(len([datum.rstrip() for datum in data if Address(
        datum.rstrip()).supports_tls()]))
    print(len([datum.rstrip() for datum in data if Address(
        datum.rstrip()).supports_ssl()]))
