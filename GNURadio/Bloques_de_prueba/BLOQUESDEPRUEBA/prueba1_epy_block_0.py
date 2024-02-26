import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    def __init__(self,): # only default arguments here
        gr.sync_block.__init__(
            self,
            name='e_Acum', # will show up in GRC
            in_sig=[np.float32],
            out_sig=[np.float32,np.float32]
        )
          
        self.acum_anterior=0
          
    def work(self, input_items, output_items):
        x = input_items[0] # Senial de entrada.
        y0 = output_items[0] # Senial acumulada
        N=len(x)
        y0[:] = self.acum_anterior+np.cumsum(x)
        self.acum_anterior=y0[N-1]
        return len(x)

