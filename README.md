# ProjetoApiRestFlask

Em schema.py, modifiquei a linha 5046 de True para False

        if len(self._columns) == 1:
            col = list(self._columns)[0]

            if col.autoincrement is True:
                _validate_autoinc(col, False) # Jose editou de True para False

                return col
            elif col.autoincrement in (
                "auto",
                "ignore_fk",
            ) and _validate_autoinc(col, False):
                return col
            else:
                return None
