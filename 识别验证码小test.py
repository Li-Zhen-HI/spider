import ddddocr
ocr=ddddocr.DdddOcr()
with open('2.jpg','rb') as f:
    hh=f.read()
res=ocr.classification(hh)
print((res))
