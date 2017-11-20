from antlr4.error.ErrorListener import ErrorListener


class ErrosSintaticosErrorListener(ErrorListener):

    # Tradução das mensagens de erro do analisador sintático e lançamento de exceção interrompendo a compilação
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception('Linha ' + str(line) + ': erro sintático proximo a ' + offendingSymbol.text)

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        return

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        return

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        return
