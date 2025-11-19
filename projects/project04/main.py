from PIL import Image, ImageDraw, ImageFont

tasks = ["Buy groceries", "Read book", "Exercise"]
text = "\n".join(f"{i+1}. {task}" for i, task in enumerate(tasks))

# ایجاد تصویر سفید
img = Image.new("RGB", (400, 100 + 30*len(tasks)), color="white")
draw = ImageDraw.Draw(img)
draw.text((10, 10), text, fill="black")

# ذخیره تصویر
img.save("screenshots/project04.png")
print("Screenshot saved to screenshots/project04.png")
