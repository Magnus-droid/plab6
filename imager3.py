from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
import numpy


class Imager:

    _pixel_colors_ = {'red':(255,0,0), 'green': (0,255,0), 'blue': (0,0,255), 'white': (255,255,255),
                      'black': (0,0,0)}

    def __init__(self,fid=False,image=False,width=100,height=100,background='black',mode='RGB'):
        self.fid = fid # The image file
        self.image = image # A PIL image object
        self.xmax = width; self.ymax = height # These can change if there's an input image or file
        self.mode = mode
        self.init_image(background=background)

    def init_image(self,background='black'):
        if self.fid: self.load_image()
        if self.image: self.get_image_dims()
        else: self.image = self.gen_plain_image(self.xmax,self.ymax,background)

    # Load image from file
    def load_image(self):
        self.image = Image.open(self.fid)  # the image is actually loaded as needed (automatically by PIL)
        if self.image.mode != self.mode:
            self.image = self.image.convert(self.mode)

    # Save image to a file.  Only if fid has no extension is the type argument used.  When writing to a JPEF
    # file, use the extension JPEG, not JPG, which seems to cause some problems.
    def dump_image(self,fid,type='gif'):
        fname = fid.split('.')
        type = fname[1] if len(fname) > 1 else type
        self.image.save(fname[0]+'.'+type,format=type)

    def get_image(self): return self.image
    def set_image(self,im): self.image = im

    def display(self):
        self.image.show()

    def get_image_dims(self):
         self.xmax = self.image.size[0]
         self.ymax = self.image.size[1]

    def copy_image_dims(self,im2):
        im2.xmax = self.xmax; im2.ymax = self.ymax

    def gen_plain_image(self,x,y,color,mode=None):
        m = mode if mode else self.mode
        return Image.new(m,(x,y),self.get_color_rgb(color))

    def get_color_rgb(self,colorname): return Imager._pixel_colors_[colorname]

    # This returns a resized copy of the image
    def resize(self,new_width,new_height,image=False):
        image = image if image else self.image
        return Imager(image=image.resize((new_width,new_height)))

    def scale(self,xfactor,yfactor):
        return self.resize(round(xfactor*self.xmax),round(yfactor*self.ymax))

    def get_pixel(self,x,y): return self.image.getpixel((x,y))
    def set_pixel(self,x,y,rgb): self.image.putpixel((x,y),rgb)

    def combine_pixels(self,p1,p2,alpha=0.5):
        return tuple([round(alpha*p1[i] + (1 - alpha)*p2[i]) for i in range(3)])

    # The use of Image.eval applies the func to each BAND, independently, if image pixels are RGB tuples.
    def map_image(self,func,image=False):
        # "Apply func to each pixel of the image, returning a new image"
        image = image if image else self.image
        return Imager(image=Image.eval(image,func)) # Eval creates a new image, so no need for me to do a copy.

    # This applies the function to each RGB TUPLE, returning a new tuple to appear in the new image.  So func
    # must return a 3-tuple if the image has RGB pixels.

    def map_image2(self,func,image=False):
        im2 = image.copy() if image else self.image.copy()
        for i in range(self.xmax):
            for j in range(self.ymax):
                im2.putpixel((i,j),func(im2.getpixel((i,j))))
        return Imager(image = im2)

    # WTA = winner take all: The dominant color becomes the ONLY color in each pixel.  However, the winner must
    # dominate by having at least thresh fraction of the total.
    def map_color_wta(self,image=False,thresh=0.34):
        image = image if image else self.image
        def wta(p):
            s = sum(p); w = max(p)
            if s > 0 and w/s >= thresh:
                return tuple([(x if x == w else 0) for x in p])
            else:
                return (0,0,0)
        return self.map_image2(wta,image)
    
    def contrast(self, val):
        return Imager(image=ImageEnhance.Contrast(self.image).enhance(val))

    # Note that grayscale uses the RGB triple to define shades of gray.
    def gen_grayscale(self,image=False): 
        return self.scale_colors(image=image,degree=0)
    
    def get_matrix(self):
        return self.image.convert('RGB')
    
    def saturate(self, val=2):
        return Imager(image=ImageEnhance.Color(self.image).enhance(val))

    def blur(self, r=0.8):
        return Imager(image=self.image.filter(ImageFilter.GaussianBlur(r)))

def reformat(in_fid, out_ext='jpeg',scalex=1.0,scaley=1.0):
    base, extension = in_fid.split('.')
    im = Imager(in_fid)
    im = im.scale(scalex,scaley)
    im.dump_image(base,out_ext)

height = 10
width = 20
color = 'g'

def find_color(image, height, width, color):

    processed_image = Imager(image=image).resize(width,height).map_color_wta()
    array = numpy.asarray(processed_image.get_matrix())
    
    # isoler ut fargen vi er interessert i
    d = {'r': 0, 'g': 1, 'b': 2}
    tmp = []
    for row in array:
        tmp.append(list(map(lambda l: l[d[color]], row)))

    # summer de ulike kolonnene
    tmp = numpy.transpose(tmp)
    tmp = list(map(lambda a: sum(a)/height, tmp))
    tmp = numpy.transpose(tmp).tolist()
    
    direction = sum([v*i for v, i in enumerate(tmp)])/sum(tmp)
    max_val = max(tmp)
    
    ## print(tmp)   
    ## processed_image.dump_image('nice.png')

    return ((direction-width/2)/(width/2), max_val)

bird = Image.open('shirt.jpg')
print(find_color(bird, 10, 20, 'r'))
