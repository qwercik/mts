#!/usr/bin/env python3

import re
import sys
import string
import json
import lexer
import debug
import exitcodes
import translator

DEVELOPER_URL = 'https://github.com/qwercik/r2i'
CONFIG_FILE = 'config.json'
TRANSLATION_FILE = 'lang.json'

def readTranslations(lang):
    translations = dict(map(lambda x: (x[0], x[1][lang]), json.loads(open(TRANSLATION_FILE).read()).items()))

    return translations


def main():
    translations = None
    try:
        lang = json.loads(open(CONFIG_FILE).read())['lang']
        translations = readTranslations(lang)
    except:
        debug.error('You have not typed a valid app language in config.json', exitcodes.EXIT_INCORRECT_CONFIG)


    for line in sys.stdin:
        rpnFormula = line.strip()

        try:
            infixFormula = translator.translateRpnToInfix(rpnFormula)
            print(infixFormula)
        except lexer.IncorrectSymbolError as symbol:
            debug.error(translations['incorrect_symbol'] + ': ' + str(symbol), exitcodes.EXIT_INCORRECT_SYMBOL)
        except translator.NestedPredicateError as formula:
            debug.error(translations['predicate_nested'] + ': ' + str(formula), exitcodes.EXIT_INCORRECT_FORMULA)
        except translator.NotEnoughArguments as formula:
            debug.error(translations['not_valid_arity'] + ': ' + str(formula), exitcodes.EXIT_INCORRECT_FORMULA)
        except translator.IncorrectFormulaError as formula:
            debug.error(translations['unknown_error'] + ': ' + str(formula), exitcodes.EXIT_INCORRECT_FORMULA)
        except:
            debug.error(f'Unknown error. Report the developer ({DEVELOPER_URL})', exitcodes.EXIT_UNKNOWN_ERROR)

if __name__ == '__main__':
    main()
