from io import StringIO

text_buffer = StringIO()
text_buffer.write("This is the sample.")
print(text_buffer.getvalue())


from io import BytesIO

binary_buffer = BytesIO()
binary_buffer.write(b"This is the sample.")
binary_buffer.seek(0)
print(binary_buffer.read())