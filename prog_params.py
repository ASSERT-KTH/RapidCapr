import logging
from pathlib import Path

class ProgParams:

    ### Framework related
    shell_script_folder = Path(__file__).parent / "frameworks"
    validate_patch_cache_folder=Path(__file__).parent / 'cache' / 'validate_patch_cache'
    bug_details_cache_folder=Path(__file__).parent / 'cache' / 'bug_details_cache'
    n_shot_cache_folder=Path(__file__).parent / 'cache' / 'n_shot_cache'
    # Defects4J related
    d4j_list_of_bugs = [("Chart", [i for i in range(1, 27)]),
                        ("Closure", [i for i in range(1, 177) if i != 63 and i != 93]),
                        ("Lang", [i for i in range(1, 66) if i != 2]),
                        ("Math", [i for i in range(1, 107)]),
                        ("Mockito", [i for i in range(1, 39)]),
                        ("Time", [i for i in range(1, 28) if i != 21])]

    humaneval_list_of_bugs = [("humaneval",
                            ["ADD",
                            "ADD_ELEMENTS",
                            "ADD_EVEN_AT_ODD",
                            "ALL_PREFIXES",
                            "ANTI_SHUFFLE",
                            "ANY_INT",
                            "BELOW_THRESHOLD",
                            "BELOW_ZERO",
                            "BF",
                            "BY_LENGTH",
                            "CAN_ARRANGE",
                            "CAR_RACE_COLLISION",
                            "CHANGE_BASE",
                            "CHECK_DICT_CASE",
                            "CHECK_IF_LAST_CHAR_IS_A_LETTER",
                            "CHOOSE_NUM",
                            "CIRCULAR_SHIFT",
                            "CLOSEST_INTEGER",
                            "COMMON",
                            "COMPARE",
                            "COMPARE_ONE",
                            "CONCATENATE",
                            "CORRECT_BRACKETING",
                            "COUNT_DISTINCT_CHARACTERS",
                            "COUNT_NUMS",
                            "COUNT_UPPER",
                            "COUNT_UP_TO",
                            "CYCPATTERN_CHECK",
                            "DECIMAL_TO_BINARY",
                            "DECODE_CYCLIC",
                            "DECODE_SHIFT",
                            "DERIVATIVE",
                            "DIGITS",
                            "DIGIT_SUM",
                            "DOUBLE_THE_DIFFERENCE",
                            "DO_ALGEBRA",
                            "EAT",
                            "ENCODE",
                            "ENCRYPT",
                            "EVEN_ODD_COUNT",
                            "EVEN_ODD_PALINDROME",
                            "EXCHANGE",
                            "FACTORIAL",
                            "FACTORIZE",
                            "FIB",
                            "FIB4",
                            "FIBFIB",
                            "FILE_NAME_CHECK",
                            "FILTER_BY_PREFIX",
                            "FILTER_BY_SUBSTRING",
                            "FILTER_INTEGERS",
                            "FIND_CLOSEST_ELEMENTS",
                            "FIND_ZERO",
                            "FIX_SPACES",
                            "FIZZ_BUZZ",
                            "FLIP_CASE",
                            "FRUIT_DISTRIBUTION",
                            "GENERATE_INTEGERS",
                            "GET_CLOSET_VOWEL",
                            "GET_MAX_TRIPLES",
                            "GET_ODD_COLLATZ",
                            "GET_POSITIVE",
                            "GET_ROW",
                            "GREATEST_COMMON_DIVISOR",
                            "HAS_CLOSE_ELEMENTS",
                            "HEX_KEY",
                            "HISTOGRAM",
                            "HOW_MANY_TIMES",
                            "INCR_LIST",
                            "INTERSECTION",
                            "INTERSPERSE",
                            "INT_TO_MINI_ROMAN",
                            "ISCUBE",
                            "IS_BORED",
                            "IS_EQUAL_TO_SUM_EVEN",
                            "IS_HAPPY",
                            "IS_MULTIPLY_PRIME",
                            "IS_NESTED",
                            "IS_PALINDROME",
                            "IS_PRIME",
                            "IS_SIMPLE_POWER",
                            "IS_SORTED",
                            "LARGEST_DIVISOR",
                            "LARGEST_PRIME_FACTOR",
                            "LARGEST_SMALLEST_INTEGERS",
                            "LONGEST",
                            "MAKE_A_PILE",
                            "MAKE_PALINDROME",
                            "MATCH_PARENS",
                            "MAXIMUM_K",
                            "MAX_ELEMENT",
                            "MAX_FILL",
                            "MEAN_ABSOLUTE_DEVIATION",
                            "MEDIAN",
                            "MIN_PATH",
                            "MIN_SUBARRAY_SUM",
                            "MODP",
                            "MONOTONIC",
                            "MOVE_ONE_BALL",
                            "MULTIPLY",
                            "NEXT_SMALLEST",
                            "NUMERICAL_LETTER_GRADE",
                            "ODD_COUNT",
                            "ORDER_BY_POINTS",
                            "PAIRS_SUM_TO_ZERO",
                            "PARSE_MUSIC",
                            "PARSE_NESTED_PARENS",
                            "PLUCK",
                            "PRIME_FIB",
                            "PRIME_LENGTH",
                            "PROD_SIGNS",
                            "REMOVE_DUPLICATES",
                            "REMOVE_VOWELS",
                            "RESCALE_TO_UNIT",
                            "REVERSE_DELETE",
                            "RIGHT_ANGLE_TRIANGLE",
                            "ROLLING_MAX",
                            "ROUNDED_AVG",
                            "SAME_CHARS",
                            "SEARCH",
                            "SELECT_WORDS",
                            "SEPARATE_PAREN_GROUPS",
                            "SIMPLIFY",
                            "SKJKASDKD",
                            "SMALLEST_CHANGE",
                            "SOLUTION",
                            "SOLVE",
                            "SOLVE_STRING",
                            "SORTED_LIST_SUM",
                            "SORT_ARRAY",
                            "SORT_ARRAY_BINARY",
                            "SORT_EVEN",
                            "SORT_NUMBERS",
                            "SORT_THIRD",
                            "SPECIAL_FACTORIAL",
                            "SPECIAL_FILTER",
                            "SPLIT_WORDS",
                            "STARTS_ONE_ENDS",
                            "STRANGE_SORT_LIST",
                            "STRING_SEQUENCE",
                            "STRING_TO_MD5",
                            "STRING_XOR",
                            "STRLEN",
                            "STRONGEST_EXTENSION",
                            "SUM_PRODUCT",
                            "SUM_SQUARED_NUMS",
                            "SUM_SQUARES",
                            "SUM_TO_N",
                            "TOTAL_MATCH",
                            "TRI",
                            "TRIANGLE_AREA",
                            "TRIANGLE_AREA_2",
                            "TRIPLES_SUM_TO_ZERO",
                            "TRUNCATE_NUMBER",
                            "UNIQUE",
                            "UNIQUE_DIGITS",
                            "VALID_DATE",
                            "VOWELS_COUNT",
                            "WILL_IT_FLY",
                            "WORDS_IN_SENTENCE",
                            "WORDS_STRINGS",
                            "X_OR_Y",])]
    
    ### LLM Related
    # ChatGPT related
    gpt35_model = "gpt-3.5-turbo-0301"
    gpt35_model_token_limit = 4097
    gpt35_cache_folder=Path(__file__).parent / 'cache' / 'chatgpt_cache'

    ### Algorithm Related
    stop_on_first_plausible_patch = False
    # CAPR related
    capr_SL_SH_max_tries = 200
    capr_SF_max_tries = 100
    capr_n_shot_count = 1
    capr_max_conv_length = 3
    # CigaR related
    cigar_max_fpps_try_per_mode = 5
    cigar_max_mpps_try_per_mode = 2
    cigar_prompt_token_limit = 1500
    cigar_total_token_limit_target = 3000
    cigar_max_sample_count = 10
    cigar_similarity_threshold = 0.5
    cigar_max_rounds = 13

    ### Logging Parameters ###
    logging_level=logging.INFO
