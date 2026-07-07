import pandas as pd


class BookBuilder:

    def build(self, rows):

        df = pd.DataFrame(rows)

        return df