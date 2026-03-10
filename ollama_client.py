import ollama

ctstr = '分析一下天翼云市场占有率以及未来发展趋势'
response = ollama.chat('qwen3.5:4b', [
    {'role': 'user', 'content': ctstr}
])
print(response['message']['content'])