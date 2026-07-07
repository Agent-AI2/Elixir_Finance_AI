class Validator:

    def validate(self, df):

        errors = []

        if df.empty:
            errors.append("No records extracted.")

        return errors