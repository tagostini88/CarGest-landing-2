from PIL import Image
import os

os.chdir("/Users/tommasoagostini/Desktop/CarGest landing 2")

files = ["autoscout-1.png", "Unknown.png", "Unknown-1.png"]

for filename in files:
    try:
        img = Image.open(filename).convert("RGBA")
        
        # Rimuovi sfondo bianco
        data = img.getdata()
        new_data = []
        for item in data:
            if item[:3] == (255, 255, 255):  # Se è bianco puro
                new_data.append((255, 255, 255, 0))  # Rendi trasparente
            else:
                new_data.append(item)
        
        img.putdata(new_data)
        
        # Crop ai margini del contenuto
        img = img.crop(img.getbbox())
        
        # Normalizza altezza a 100px
        ratio = 100 / img.height
        new_width = int(img.width * ratio)
        img = img.resize((new_width, 100), Image.Resampling.LANCZOS)
        
        img.save(filename)
        print(f"✅ {filename}: {img.width}x{img.height}px")
    except Exception as e:
        print(f"❌ {filename}: {e}")
