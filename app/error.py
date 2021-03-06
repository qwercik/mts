from enum import Enum

class ErrorCode(Enum):
    UNRECOGNIZABLE_SYMBOL = 1
    NESTED_PREDICATE = 2,
    OPERATOR_ARGUMENT = 3
    QUANTIFIER_FIRST_ARGUMENT = 4,
    QUANTIFIER_SECOND_ARGUMENT = 5,
    INCORRECT_ARGUMENTS_NUMBER = 6
    UNKNOWN = 255
