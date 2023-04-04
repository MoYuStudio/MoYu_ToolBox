from pywinauto.application import Application
from pywinauto.keyboard import send_keys
import time

# Wait for the target window to be in focus
time.sleep(5)

# Click the 'Save As' button
app = Application().connect(title='Notepad')
dlg = app.window(title='Notepad')
dlg.MenuSelect("File->Save As...")
dlg.SaveAs.FileName.Edit.set_edit_text("test.txt")
dlg.SaveAs.Save.click()

# Type 'halo world'
send_keys('halo world', with_spaces=True)
