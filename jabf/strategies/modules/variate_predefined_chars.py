from strategies.search_strategy import SearchStrategy


class VariatePredefinedCharsStrategy(SearchStrategy):
    """
    Search strategy that takes a predefined text data and variates it according
    to the dictionary provided. Every character of data is searched for in the
    dictionary and variated with characters from dictionary groups that contain
    it.

    Example:
        data = abc
        Dictionary contains the following groups: 'Aa', 'Bb', 'Cc'
        The output of the strategy generator would be:
            abc, Abc, aBc, abC, ABc, aBC, AbC, ABC

    Mask is string representing a bitwise mask used to skip some characters
    variation.
    Mask should have the same length as data. it should consist of 0 and 1,
    where they mean:
        1 - character should be variated,
        0 - character should NOT be variated.

    Example:
        data = abc
        mask = 110
        Dictionary contains the following groups: 'Aa', 'Bb', 'Cc'
        The output of the strategy generator would be:
            abc, Abc, aBc, ABc
    """

    name = "variatepredefinedchars"
    strategy_params = [
        "data",
        "mask",
    ]

    def __init__(self, strategy_config, dictionary):
        self._validate_strategy_config(strategy_config)
        self.data = strategy_config['data']
        self.mask = strategy_config['mask']
        self.dictionary_cache = \
            list(dictionary.get_dictionary_generator())

    def get_combination_count(self):
        if len(self.data) == 0:
            return 0

        total = 1
        for i in range(len(self.data)):
            if self.mask[i] == '1':
                variation_count = len(
                    self._get_variations_for_char(self.data[i]))
                total = total * variation_count
        return total

    def get_generator(self):
        dictionary_values = ''.join(self.dictionary_cache)
        for c in self.data:
            if c not in dictionary_values:
                raise ValueError('Error in strategy parameters: data contains '
                                 'characters not present in dictionary')
        stack = []
        for char in self._get_variations_for_char(self.data[0]):
            variant = (char, self.data[1:])
            stack.append(variant)

        while(len(stack) > 0):
            variant = stack.pop()
            if len(variant[1]) == 0:
                yield variant[0]
            else:
                left_part = variant[0]
                right_part = variant[1]
                if (self.mask[len(left_part)] == '0'):
                    stack.append((
                        ''.join([left_part, right_part[0]]),
                        right_part[1:]))
                elif (self.mask[len(left_part)] == '1'):
                    for char in self._get_variations_for_char(right_part[0]):
                        stack.append((
                            ''.join([left_part, char]),
                            right_part[1:]))

    def _validate_strategy_config(self, strategy_config):
        self._validate_strategy_config_params(strategy_config)
        if len(strategy_config['data']) == 0:
            raise ValueError('Error in strategy parameters: "data" field '
                             'is empty')
        if len(strategy_config['data']) != len(strategy_config['mask']):
            raise ValueError('Error in strategy parameters: '
                             'data and mask length should be equal')
        for c in strategy_config['mask']:
            if c not in ('0', '1'):
                raise ValueError('Invalid characters in strategy mask. '
                                 'The characters allowed: 0 and 1')

    def _get_variations_for_char(self, char):
        variations = set(
            element for element in self.dictionary_cache if char in element)
        return ''.join(variations)
