from rembg import remove

input_path = "C:\Users\ÖMER\OneDrive\Masaüstü\Bot_AI\WhatsApp Image 2024-02-29 at 21.22.46.jpeg"
output_path = "output.png"

with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)