
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import msgbox
import threading
import ui.resource_rc
 
'''
    * Select folder to save video
    * @return null
''' 
def chooseDirectoryDialog():
    directory = QFileDialog.getExistingDirectory(None, "Choose a directory","", QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
    if directory:
        #Insert path into input field
        main_ui.path.setText(directory)

'''
    * Record Screen 
    * @return null
'''       
def recordScreen():
    import cv2
    import numpy as np
    import pyautogui
    #from PIL import ImageGrab
    
    path = main_ui.path.text()
    # display screen resolution, get it using pyautogui itself
    SCREEN_SIZE = tuple(pyautogui.size())
    # define the codec
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    # frames per second
    fps = 8.0
    # create the video write object
    out = cv2.VideoWriter(path + "/output.avi", fourcc, fps, (SCREEN_SIZE))
    # the time you want to record in seconds. Max 24h
    record_seconds = 86400 

    '''#Mouse
    def transparent_circle(img,center,radius,color,thickness):
        center = tuple(map(int,center))
        rgb = [255*c for c in color[:3]] # convert to 0-255 scale for OpenCV
        alpha = color[-1]
        radius = int(radius)
        if thickness > 0:
            pad = radius + 2 + thickness
        else:
            pad = radius + 3
        roi = slice(center[1]-pad,center[1]+pad),slice(center[0]-pad,center[0]+pad)

        try:
            overlay = img[roi].copy()
            cv2.circle(img,center,radius,rgb, thickness=thickness, lineType=cv2.LINE_AA)
            opacity = alpha
            cv2.addWeighted(src1=img[roi], alpha=opacity, src2=overlay, beta=1. - opacity, gamma=0, dst=img[roi])
        except:
            logger.debug("transparent_circle would have been partially outside of img. Did not draw it.")'''

    for i in range(int(record_seconds * fps)):
        
        # make a screenshot
        img = pyautogui.screenshot()  

        # convert these pixels to a proper numpy array to work with OpenCV
        frame = np.array(img)
        # convert colors from BGR to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        '''#Mouse
        im = ImageGrab.grab()
        imm=cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)
        _xs,_ys = win32api.GetCursorPos()
        transparent_circle(imm,(_xs,_ys),20,(0,255,255,0.5), -1)'''
        
        # write the frame
        out.write(frame)
        
        # show the frame
        #cv2.imshow("screenshot", frame)
        
        # Check Record Screen button text (at this moment, is hidden)
        current_text = main_ui.record_screen_btn.text()
        
        #When Stop button is clicked, text of Record Screen button will set to "Record Screen" again (was set to "Stop" just for control)
        if current_text == "Record Screen":                
            break

    # make sure everything is closed when exited
    cv2.destroyAllWindows()
    out.release()

def stopRecording():
    print("click on stop")
    main_ui.stop_record_screen_btn.hide()
    main_ui.stop_record_screen_btn.repaint()
    
    main_ui.record_screen_btn.show()
    main_ui.record_screen_btn.setText("Record Screen") 
    main_ui.record_screen_btn.repaint() 
    
def startRecordingByThread():
    #Get path in input
    path = main_ui.path.text()
    
    #If path is empty...
    if path == '':
        msgbox.showMessageBox('Ops', 'Path is missing', type = 'QMessageBox.Information', buttons = 'QMessageBox::Ok')
    
    #If path is not empty... 
    else: 
        x = threading.Thread(target=recordScreen, daemon=True)
        x.start()
        main_ui.record_screen_btn.setText("Stop")
        main_ui.record_screen_btn.repaint()        
        main_ui.record_screen_btn.hide()        
        main_ui.stop_record_screen_btn.show()
        main_ui.stop_record_screen_btn.repaint()
        MainWindow.showMinimized()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    '''Generating Windows'''
    
    #MainWindow
    from ui.main import Ui_MainWindow
    MainWindow = QtWidgets.QMainWindow()    
    main_ui = Ui_MainWindow()
    main_ui.setupUi(MainWindow)
    
    '''Clicks'''
    
    #Choose Path
    main_ui.choose_path_btn.clicked.connect(chooseDirectoryDialog)    
    #Record
    main_ui.record_screen_btn.clicked.connect(startRecordingByThread)    
    #Stop Recording
    main_ui.stop_record_screen_btn.clicked.connect(stopRecording)
    
    #Start with "Stop" hided
    main_ui.stop_record_screen_btn.hide()
    
    '''Show'''
    
    #Show
    MainWindow.show()
    
    sys.exit(app.exec_())
