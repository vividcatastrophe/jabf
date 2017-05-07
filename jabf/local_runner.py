from jabf.config import config_read
from jabf.search_strategy import SearchStrategy
from jabf.target import Target
from jabf.output_method import OutputMethod
from jabf.dictionary import DictionaryRegister
from jabf.class_register import ClassRegister


class LocalRunnerBuilder(object):
    def get_runner(self):
        if hasattr(self, 'runner') and self.runner.is_valid():
            return self.runner
        else:
            raise Exception('No valid runner can be returned')

    def build(self, config_path):
        for register in [
                'dictionary_register',
                'strategy_register',
                'target_register',
                'output_register'
                ]:
            if not hasattr(self, register):
                raise Exception('Builder has no {}'.format(register))
        self.runner = LocalRunner()
        self.config = config_read(config_path)
        self.dictionary = self.dictionary_register[self.config['dictionary']]
        strategy_class = self.strategy_register[
            self.config['search strategy']['name']]
        self.runner.strategy = strategy_class(
            self.config['search strategy']['params'], self.dictionary)

        target_class = self.target_register[
            self.config['target module']['name']]
        self.runner.target = target_class(
            self.config['target module']['params'])

        output_class = self.output_register[
            self.config['output method']['name']]
        self.runner.output = output_class(
            self.config['output method']['params'])

    def register_dictionaries(self, dictionary_path):
        self.dictionary_register = DictionaryRegister()
        self.dictionary_register.register_dictionaries(dictionary_path)

    def register_strategies(self, strategy_path):
        self.strategy_register = ClassRegister(SearchStrategy)
        self.strategy_register.load_classes_from_folder(strategy_path)

    def register_targets(self, target_path):
        self.target_register = ClassRegister(Target)
        self.target_register.load_classes_from_folder(target_path)

    def register_outputs(self, output_path):
        self.output_register = ClassRegister(OutputMethod)
        self.output_register.load_classes_from_folder(output_path)


class LocalRunner(object):
    def is_valid(self):
        if all([hasattr(self, attr) for attr in
                ['strategy', 'target', 'output']]):
            return True

    def run(self):
        data_gen = self.strategy.get_generator()
        total_count = self.strategy.get_combination_count()
        print('Combinations total: {}'.format(total_count))
        current_count = 0
        found = False
        for data in data_gen:
            current_count += 1
            if not self.target.check_data(data):
                print("{}% Count:{}, Total:{}".format(
                    100.0 * current_count / total_count,
                    current_count,
                    total_count))
            else:
                self.output.write(data)
                return True
        print('Nothing found')
        return False
