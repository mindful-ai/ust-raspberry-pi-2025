🔧 Create the GUI with Qt Designer
-----------------------------------------------------------------------------------

Open Qt Designer

Create a Main Window

Set the window size: 640 x 480

Add the following widgets:

    QPushButton

        Object Name: uploadButton

        Text: "Upload Image"

        Font: Size 12, Bold

    QLabel

        Object Name: imageLabel

        SizePolicy: Expanding

        Set scaledContents = True

        Set a placeholder text "Image will appear here"

        Save the file as gui.ui

Convert: pyuic5 gui.ui -o gui.py
