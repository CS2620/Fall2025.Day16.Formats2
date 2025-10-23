from PIL import Image

image = Image.open('./zebra.jpg')
raster = image.load()

string = "P6\n"
string += f"{image.width}\n"
string += f"{image.height}\n"
string += "256\n"

for y in range(image.height):
    for x in range(image.width):
        pixel = raster[x,y]
        
        r = pixel[0]
        g = pixel[1]
        b = pixel[2]
        string += r.to_bytes().decode("latin-1")
        string += g.to_bytes().decode("latin-1")
        string += b.to_bytes().decode("latin-1")
    # string += "\n"
    
with open("out.ppm", "w") as f:
    f.write(string)
        

lines = string.split("\n")
assert lines[0] == "P6"
width = int(lines[1])
height = int(lines[2])
_ = int(lines[3])

remaining_string = string[len(lines[0]) + len(lines[1]) + len(lines[2]) + len(lines[3]) + 4]


# raster_lines = lines[4:]

ppm_image = Image.new("RGB", (width, height))
ppm_raster = ppm_image.load()

for y in range(height):
    # line = raster_lines[y]
    # rgb_triples = line.split()
    for x in range(width):
        index = (y*width+x)*3
        r = int(remaining_string[index+0].encode("latin-1"))
        g = int(remaining_string[index+1].encode("latin-1"))
        b = int(remaining_string[index+2].encode("latin-1"))
        ppm_raster[x,y] = (r, g, b)
        
image.save("ppm.png")

        
        
       