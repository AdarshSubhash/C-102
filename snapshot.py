import cv2
import dropbox
import time
import random
starttime=time.time()
def takesnapshot():
    number=random.randint(0,100)
    videocapture=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videocapture.read()
        imagename="img"+str(number)+".png"
        cv2.imwrite(imagename,frame)
        starttime=time.time()
        result=False
    return imagename
    print("snapshottaken")    
    videocapture.release()
    cv2.destroyAllWindows()
def uploadfile(imagename):
    accesstoken="f2zlVBgKzSUAAAAAAAAAAQewfsWzSbU_2sN8jP7Q5edmlVRmk2p9AeaHwQKY_PyA"
    file=imagename
    filefrom=file
    fileto="/textfolder/"+imagename
    dbx=dropbox.Dropbox(accesstoken)
    with open(filefrom,"rb")as f:
        dbx.files_upload(f.read(),fileto,mode=dropbox.files.WriteMode.overwrite)
        print("fileuploaded")
def main():
    while(True):
        if((time.time()-starttime)>=5):
            name=takesnapshot()
            uploadfile(name)            
main()            