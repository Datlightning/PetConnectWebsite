"""
    
    The parser function lexically parses a string and returns a dictionary of what type and what content. 
    Kinda sick  

    The parser function accepts one singular line of code. 
    Returns a dictionary: 

    dictionary =  {
    
        "tag": String. Returns Type: 
            t = title
            a = author
            d = date
            b = bold
            i = italic
            bi = bold and italic
            bia = bold and italic for some phrases in text. 
            bii = bold or italic for some phrases in text. 
            img = image. 
            imgl = list of images. 
            p = pure text

        "content": 

            Includes content.
            Always a string. 
            Either word or a lsit of imageDics: 

            An ImageDic: 

                imageDic = {
                    
                    "content":"nameofImageFile"
                    "caption":"contentOfCaption" 
                }
        
    }
    

"""
def parser(inp):
    tag = ""
    content = "" 
    if inp[0] == "*":
        inp = inp.split(";")
        tag = inp[0]
        if inp[0] == 'img':
            inp = inp[1:]  
            content = []
            i = 0
            length = len(inp)
            while (i < length - 1 ):
                content.append({"content":inp[i], "caption":inp[i+1]})
                i += 2
            del(i)
            del(length)
        else: 
            content = inp[1]
        
        return {"tag":tag, "content":content}
               
    else: 
        return {"tag":"p", "content":inp}
    
