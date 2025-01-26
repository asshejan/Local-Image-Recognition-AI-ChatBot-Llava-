import ollama

res = ollama.chat(
    model = 'llava',
    messages = [
        {
            'role' : 'user',
            'content' : 'Describe this image',
            'images' : ['./2 cat.jpg']
        }
    ]
)

print(res['message']['content'])