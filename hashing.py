class Hashing:
    def __init__(self, keys):
        self.keys = keys
        self.hash_map = {}
    
    def hash_keys(self):
        # initialize empty hash map
        for i in range(11):
            self.hash_map[i] = None

        # map given keys
        for key in self.keys:

            remainder = key % 11
            if self.hash_map[remainder] == None:
                self.hash_map[remainder] = key
            elif self.hash_map[remainder] != None:
                # first case using the quadratic probe
                probe_count = 0
                while True:
                    new_key = self.compute_quadratic_probe(key, remainder, probe_count)
                    if self.hash_map[new_key] == None:
                        break
                    probe_count += 1
                self.hash_map[self.compute_quadratic_probe(key, remainder, probe_count, False)] = key
    
    def compute_quadratic_probe(self,key, remainder,probe_count, show_computation = True):
        if show_computation:
            print(f"""
    A colision has been encountered with
    The key: {key}

    k mod 11: {remainder}

    Iteration: {probe_count}

    computing quadratic probe using
        h(k,i) = (h(k) + 3(i)^2 +2 )mod 11
        h(k,i) = ({key} + 3({probe_count})^2 +2 )mod 11
        h(k,i) = ({key} + {3*(probe_count**2)} +2 )mod 11
        h(k,i) = ({remainder + 3*(probe_count**2) + 2})mod 11
        h(k,i) = {(remainder + 3*(probe_count**2) + 2) % 11}
        
        """)
        return (remainder + 3*(probe_count**2) + 2) % 11
    
    def get_hash_map(self):
        return self.hash_map
