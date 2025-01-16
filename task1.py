import re

class LexicalAnalyzer:
    def __init__(self):
        # 定义正则表达式
        self.token_patterns = {
            'KEYWORD': r'\b(?:if|else|while|for|return)\b',
            'IDENTIFIER': r'\b[a-zA-Z_][a-zA-Z0-9_]*\b',
            'NUMBER': r'\b\d+\b',
            'OPERATOR': r'[+\-*/=<>]',
            'PUNCTUATION': r'[;,.]',
            'WHITESPACE': r'\s+',
            'COMMENT': r'//.*'
        }
        self.tokens = []

    def analyze(self, input_stream):
        # 清空之前的token
        self.tokens = []
        position = 0
        while position < len(input_stream):
            match = None
            for token_type, pattern in self.token_patterns.items():
                match = re.match(pattern, input_stream[position:])
                if match:
                    if token_type != 'WHITESPACE' and token_type != 'COMMENT':
                        self.tokens.append((token_type, match.group(0)))
                    position += len(match.group(0))
                    break
            if not match:
                self.tokens.append(('ERROR', input_stream[position]))
                position += 1
        return self.tokens

# 使用LexicalAnalyzer进行分析
def main():
    input_stream = input("请输入代码流：")
    lexical_analyzer = LexicalAnalyzer()
    tokens = lexical_analyzer.analyze(input_stream)
    print("词法分析结果：")
    for token in tokens:
        print(token)

if __name__ == "__main__":
    main()
