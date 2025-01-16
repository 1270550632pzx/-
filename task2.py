class CFG:
    def __init__(self):
       
        self.rules = {
            'S': [['A', 'B']],
            'A': [['a'], ['a', 'A']],
            'B': [['b'], ['b', 'B']]
        }

    def get_productions(self, non_terminal):
        return self.rules.get(non_terminal, [])

# 自顶向下语法分析器
class TopDownParser:
    def __init__(self, grammar):
        self.grammar = grammar
        self.derivations = []

    def parse(self, input_stream):
        input_stream = list(input_stream)
        self.derivations = []
        self._top_down_parse('S', input_stream)
        return self.derivations

    def _top_down_parse(self, non_terminal, input_stream):
        if non_terminal == ''.join(input_stream):
            self.derivations.append(f"{non_terminal} -> {''.join(input_stream)}")
            return True
        productions = self.grammar.get_productions(non_terminal)
        for production in productions:
            new_input_stream = input_stream[:]
            self.derivations.append(f"{non_terminal} -> {''.join(production)}")
            for symbol in production:
                if symbol.islower():
                    if new_input_stream and new_input_stream[0] == symbol:
                        new_input_stream.pop(0)
                    else:
                        return False
            if self._top_down_parse(non_terminal, new_input_stream):
                return True
        return False

# 自底向上语法分析器
class BottomUpParser:
    def __init__(self, grammar):
        self.grammar = grammar
        self.reductions = []

    def parse(self, input_stream):
        input_stream = list(input_stream)
        self.reductions = []
        while len(input_stream) > 1:
            reduced = False
            for non_terminal, productions in self.grammar.rules.items():
                for production in productions:
                    if ''.join(production) == ''.join(input_stream[:len(production)]):
                        input_stream = [non_terminal] + input_stream[len(production):]
                        self.reductions.append(f"Reduce: {''.join(production)} -> {non_terminal}")
                        reduced = True
                        break
                if reduced:
                    break
            if not reduced:
                return False
        return True

# 主程序
def main():
    input_stream = input("请输入字符流：")
    grammar = CFG()

    print("请选择语法分析方法：")
    print("1. 自顶向下分析（Top-Down）")
    print("2. 自底向上分析（Bottom-Up）")
    choice = int(input("请输入选择（1或2）："))

    if choice == 1:
        parser = TopDownParser(grammar)
        derivations = parser.parse(input_stream)
        print("自顶向下推导过程：")
        for derivation in derivations:
            print(derivation)
    elif choice == 2:
        parser = BottomUpParser(grammar)
        reductions = parser.parse(input_stream)
        if reductions:
            print("自底向下归约过程：")
            for reduction in reductions:
                print(reduction)
        else:
            print("无法完成归约")
    else:
        print("无效的选择")

if __name__ == "__main__":
    main()
