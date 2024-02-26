import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    def __init__(self):  # solo argumentos predeterminados aquí
        gr.sync_block.__init__(
            self,
            name='e_Acum',  # aparecerá en GRC
            in_sig=[np.float32],
            out_sig=[np.float32]
        )

    def work(self, input_items, output_items):
        x = input_items[0]  # Señal de entrada.
        y0 = output_items[0]  # Señal acumulada
        y0[:] = np.cumsum(x)
        return len(y0)

