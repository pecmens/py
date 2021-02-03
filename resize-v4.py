from PIL import Image
import os, shutil

#Image Compress executed

def compressImage(srcPath, dstPath):
    
    # Traversal the files name in the source directory.
    for filename in os.listdir(srcPath):
    
        # Splicing complete file or folder paths.
        srcFile = os.path.join(srcPath, filename)
        dstFile = os.path.join(dstPath, filename)

        # if it's a file,executed it.
        if os.path.isfile(srcFile):
           
            try:
                
                # Open the original image and save it after compress.
                # (It can be used "if scrFile.endswith(".jpg") or split , splitext etc.. functions compression for specific files.
                sImg = Image.open(srcFile)

                w, h = sImg.size

                # Set the compression size and options. ! Alert That The Dimensions Are In BRACKETS.
                dImg = sImg.resize((int(w / 2), int(h / 2)), Image.ANTIALIAS)

                # It can be used "srcFile" orginal path to save,or change the suffix to save. 
                # After the save function,it can be add compression encoding options such as JPG.
                dImg.save(dstFile)

                print(dstFile + " :Done!")

            except Exception:
                
                print(dstFile + " :Fail!")

        # if it's a folder,Recursion.
        if os.path.isdir(srcFile):
            
            compressImage(srcFile, dstFile)


def main():

    # if the directory does not exist,make it.Keep level structure.
    if not os.path.exists("./prepare"):
        os.makedirs("./prepare")

    if not os.path.exists("./compress"):
        os.makedirs("./compress")

    if not os.path.exists("./finish"):
        os.makedirs("./finish")

    path = os.walk("./")

    for root, dirs, files in path:
        for f in files:
            if f.endswith(".png") or f.endswith(".jpg"):
                shutil.move(os.path.join(root, f), os.path.join("./prepare", f))

    # Traversal the image to be added. 
    path = os.walk("./prepare")

    for root, dirs, files in path:
        for f in files:

            # Moving the files
            shutil.move(os.path.join(root, f), os.path.join("./finish", f))


    # Traversal and Delete the image to be compression.
    path = os.walk("./compress")
    
    for root, dirs, files in path:
        for f in files:
            os.remove(os.path.join(root, f))


    # Traversal the image to be compression.
    compressImage("./finish", "./compress")


if __name__ == '__main__':

    main()
