from PyQt5.QtWidgets import QMessageBox
def showMessageBox(title, message, type = 'QMessageBox.Information', buttons = 'QMessageBox::Ok'):
    msgBox = QMessageBox()        
    msgBox.setWindowTitle(title)
    msgBox.setText(message)
    
    if(type == 'QMessageBox.Question'):
        msgBox.setIcon(QMessageBox.Question)
    elif(type == 'QMessageBox.Information'):
        msgBox.setIcon(QMessageBox.Information)
    elif(type == 'QMessageBox.Warning'):
        msgBox.setIcon(QMessageBox.Warning)
    elif(type == 'QMessageBox.Critical'):
        msgBox.setIcon(QMessageBox.Critical)
    else:
        msgBox.setIcon(QMessageBox.NoIcon)
        
    
    if(buttons == 'QMessageBox::Ok'):
        msgBox.setStandardButtons(QMessageBox.Ok)
    elif(buttons == 'QMessageBox::Open'):
        msgBox.setStandardButtons(QMessageBox.Open)
    elif(buttons == 'QMessageBox::Save'):
        msgBox.setStandardButtons(QMessageBox.Save)
    elif(buttons == 'QMessageBox::Cancel'):
        msgBox.setStandardButtons(QMessageBox.Cancel)
    elif(buttons == 'QMessageBox::Close'):
        msgBox.setStandardButtons(QMessageBox.Close)    
    elif(buttons == 'QMessageBox::Discard'):
        msgBox.setStandardButtons(QMessageBox.Discard)
    elif(buttons == 'QMessageBox::Apply'):
        msgBox.setStandardButtons(QMessageBox.Apply)
    elif(buttons == 'QMessageBox::Reset'):
        msgBox.setStandardButtons(QMessageBox.Reset)
    elif(buttons == 'QMessageBox::RestoreDefaults'):
        msgBox.setStandardButtons(QMessageBox.RestoreDefaults)
    elif(buttons == 'QMessageBox::Help'):
        msgBox.setStandardButtons(QMessageBox.Help)
    elif(buttons == 'QMessageBox::SaveAll'):
        msgBox.setStandardButtons(QMessageBox.SaveAll)
    elif(buttons == 'QMessageBox::Yes'):
        msgBox.setStandardButtons(QMessageBox.Yes)
    elif(buttons == 'QMessageBox::YesToAll'):
        msgBox.setStandardButtons(QMessageBox.YesToAll)
    elif(buttons == 'QMessageBox::Abort'):
        msgBox.setStandardButtons(QMessageBox.Abort)
    elif(buttons == 'QMessageBox::Retry'):
        msgBox.setStandardButtons(QMessageBox.Retry)
    elif(buttons == 'QMessageBox::Ignore'):
        msgBox.setStandardButtons(QMessageBox.Ignore)
    elif(buttons == 'QMessageBox::NoButton'):
        msgBox.setStandardButtons(QMessageBox.NoButton) 
    
    msgBox.exec()