

import sys



from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QFileSystemModel, QFileIconProvider
from PyQt5.QtCore import QFileInfo

import humanfriendly






class FileAlreadyExists(object):

	# Size policy (default)
	__QSizePolicy_DEFAULT = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
	# QFont bold
	__QFont_BOLD = QtGui.QFont() ; __QFont_BOLD.setBold(True)



	def __init__(self, Dialog):

		# Main title
		self.static_QLabel_willOverwrite = QtWidgets.QLabel(Dialog)
		self.static_QLabel_willOverwrite.setSizePolicy(self.__QSizePolicy_DEFAULT)
		self.static_QLabel_willOverwrite.setObjectName("static_QLabel_willOverwrite")
		self.static_QLabel_willOverwrite.setText("This action will overwrite the destination.")
		# Warnings title
		self.QLabel_warnings = QtWidgets.QLabel(Dialog)
		self.QLabel_warnings.setSizePolicy(self.__QSizePolicy_DEFAULT)
		self.QLabel_warnings.setObjectName("QLabel_warnings")
		# Layout
		self.QVerticalLayout_header = QtWidgets.QVBoxLayout(Dialog)
		self.QVerticalLayout_header.setObjectName("QVerticalLayout_header")
		self.QVerticalLayout_header.addWidget(self.static_QLabel_willOverwrite)
		self.QVerticalLayout_header.addWidget(self.QLabel_warnings)
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		#----------------------------------------------------------------------#

		# Source
		self.QLabel_source = QtWidgets.QLabel(Dialog)
		self.QLabel_source.setObjectName("QLabel_source")
		self.QLabel_source.setSizePolicy(self.__QSizePolicy_DEFAULT)
		self.QLabel_source.setAlignment(QtCore.Qt.AlignCenter)
		self.QLabel_source.setFont(self.__QFont_BOLD)
		self.QLabel_source.setText("Source")
		# Path 1
		self.QLabel_path1 = QtWidgets.QLabel(Dialog)
		self.QLabel_path1.setObjectName("QLabel_path1")
		self.QLabel_path1.setSizePolicy(self.__QSizePolicy_DEFAULT)
		self.QLabel_path1.setAlignment(QtCore.Qt.AlignCenter)
		# Icon 1
		self.QLabel_icon1 = QtWidgets.QLabel(Dialog)
		self.QLabel_icon1.setObjectName("QLabel_icon1")
		self.QLabel_icon1.setAlignment(QtCore.Qt.AlignCenter)
		self.QLabel_icon1.setSizePolicy(self.__QSizePolicy_DEFAULT)
		# Date 1
		self.QLabel_date1 = QtWidgets.QLabel(Dialog)
		self.QLabel_date1.setSizePolicy(self.__QSizePolicy_DEFAULT)
		self.QLabel_date1.setAlignment(QtCore.Qt.AlignCenter)
		self.QLabel_date1.setObjectName("QLabel_date1")
		# Size 1
		self.QLabel_size1 = QtWidgets.QLabel(Dialog)
		self.QLabel_size1.setSizePolicy(self.__QSizePolicy_DEFAULT)
		self.QLabel_size1.setAlignment(QtCore.Qt.AlignCenter)
		self.QLabel_size1.setObjectName("QLabel_size1")
		# Layout 1
		self.QVerticalLayout_vlayout1 = QtWidgets.QVBoxLayout()
		self.QVerticalLayout_vlayout1.setObjectName("QVerticalLayout_vlayout1")
		self.QVerticalLayout_vlayout1.addWidget(self.QLabel_source)
		self.QVerticalLayout_vlayout1.addWidget(self.QLabel_path1)
		self.QVerticalLayout_vlayout1.addWidget(self.QLabel_icon1)
		self.QVerticalLayout_vlayout1.addWidget(self.QLabel_date1)
		self.QVerticalLayout_vlayout1.addWidget(self.QLabel_size1)
		self.horizontalLayout.addLayout(self.QVerticalLayout_vlayout1)
		#----------------------------------------------------------------------#

		# Source
		self.QLabel_destination = QtWidgets.QLabel(Dialog)
		self.QLabel_destination.setSizePolicy(self.__QSizePolicy_DEFAULT)
		self.QLabel_destination.setFont(self.__QFont_BOLD)
		self.QLabel_destination.setAlignment(QtCore.Qt.AlignCenter)
		self.QLabel_destination.setObjectName("QLabel_destination")
		self.QLabel_destination.setText("Destination")
		# Path 2
		self.QLabel_path2 = QtWidgets.QLabel(Dialog)
		self.QLabel_path2.setObjectName("QLabel_path2")
		self.QLabel_path2.setAlignment(QtCore.Qt.AlignCenter)
		self.QLabel_path2.setSizePolicy(self.__QSizePolicy_DEFAULT)
		# Icon 2
		self.QLabel_icon2 = QtWidgets.QLabel(Dialog)
		self.QLabel_icon2.setObjectName("QLabel_icon2")
		self.QLabel_icon2.setAlignment(QtCore.Qt.AlignCenter)
		self.QLabel_icon2.setSizePolicy(self.__QSizePolicy_DEFAULT)
		# Date 2
		self.QLabel_date2 = QtWidgets.QLabel(Dialog)
		self.QLabel_date2.setObjectName("QLabel_date2")
		self.QLabel_date2.setAlignment(QtCore.Qt.AlignCenter)
		self.QLabel_date2.setSizePolicy(self.__QSizePolicy_DEFAULT)
		# Size 2
		self.QLabel_size2 = QtWidgets.QLabel(Dialog)
		self.QLabel_size2.setObjectName("QLabel_size2")
		self.QLabel_size2.setAlignment(QtCore.Qt.AlignCenter)
		self.QLabel_size2.setSizePolicy(self.__QSizePolicy_DEFAULT)
		# Layout 2
		self.QVerticalLayout_vlayout2 = QtWidgets.QVBoxLayout()
		self.QVerticalLayout_vlayout2.setObjectName("QVerticalLayout_vlayout2")
		self.QVerticalLayout_vlayout2.addWidget(self.QLabel_destination)
		self.QVerticalLayout_vlayout2.addWidget(self.QLabel_path2)
		self.QVerticalLayout_vlayout2.addWidget(self.QLabel_icon2)
		self.QVerticalLayout_vlayout2.addWidget(self.QLabel_date2)
		self.QVerticalLayout_vlayout2.addWidget(self.QLabel_size2)
		self.horizontalLayout.addLayout(self.QVerticalLayout_vlayout2)
		#----------------------------------------------------------------------#

		# Vertical layout
		self.QVerticalLayout_header.addLayout(self.horizontalLayout)
		self.static_QLabel_rename = QtWidgets.QLabel(Dialog)
		self.static_QLabel_rename.setSizePolicy(self.__QSizePolicy_DEFAULT)
		self.static_QLabel_rename.setObjectName("static_QLabel_rename")
		self.static_QLabel_rename.setText("Rename:")
		self.QVerticalLayout_header.addWidget(self.static_QLabel_rename)
		# Suggest new name horizontal layout
		self.QHorizontalLayout_suggestNewName = QtWidgets.QHBoxLayout()
		self.QHorizontalLayout_suggestNewName.setObjectName("QHorizontalLayout_suggestNewName")
		# Rename QLineEdit
		self.QLineEdit_rename = QtWidgets.QLineEdit(Dialog)
		self.QLineEdit_rename.setSizePolicy(self.__QSizePolicy_DEFAULT)
		self.QLineEdit_rename.setObjectName("QLineEdit_rename")
		self.QHorizontalLayout_suggestNewName.addWidget(self.QLineEdit_rename)
		# Layout add
		self.QVerticalLayout_header.addLayout(self.QHorizontalLayout_suggestNewName)
		#----------------------------------------------------------------------#

		# Frame
		self.QFrame_separator = QtWidgets.QFrame(Dialog)
		self.QFrame_separator.setFrameShape(QtWidgets.QFrame.HLine)
		self.QFrame_separator.setFrameShadow(QtWidgets.QFrame.Raised)
		self.QFrame_separator.setObjectName("QFrame_separator")
		self.QVerticalLayout_header.addWidget(self.QFrame_separator)
		#----------------------------------------------------------------------#

		# Empty space for buttons
		self.QWidget_emptyButton = QtWidgets.QWidget(Dialog)
		self.QWidget_emptyButton.setSizePolicy(self.__QSizePolicy_DEFAULT)
		self.QWidget_emptyButton.setObjectName("QWidget_emptyButton")
		# Button : rename
		self.QPushButton_rename = QtWidgets.QPushButton(Dialog)
		self.QPushButton_rename.setObjectName("QPushButton_rename")
		self.QPushButton_rename.setText("Rename")
		# Button : overwrite
		self.QPushButton_overwr = QtWidgets.QPushButton(Dialog)
		self.QPushButton_overwr.setObjectName("QPushButton_overwr")
		self.QPushButton_overwr.setText("Overwrite")
		# Button : cancel
		self.QPushButton_cancel = QtWidgets.QPushButton(Dialog)
		self.QPushButton_cancel.setIcon(QtGui.QIcon.fromTheme("cancel"))
		self.QPushButton_cancel.setObjectName("QPushButton_cancel")
		self.QPushButton_cancel.setText("Cancel")
		# Layout
		self.QHorizontalLayout_buttons = QtWidgets.QHBoxLayout()
		self.QHorizontalLayout_buttons.setObjectName("QHorizontalLayout_buttons")
		self.QHorizontalLayout_buttons.addWidget(self.QWidget_emptyButton)
		self.QHorizontalLayout_buttons.addWidget(self.QPushButton_overwr)
		self.QHorizontalLayout_buttons.addWidget(self.QPushButton_rename)
		self.QHorizontalLayout_buttons.addWidget(self.QPushButton_cancel)
		self.QVerticalLayout_header.addLayout(self.QHorizontalLayout_buttons)
		#----------------------------------------------------------------------#

	############################################################################


#==============================================================================#
































class QMessageBox_addons(QtWidgets.QMessageBox):




	# new_path2 = fileAlreadyExists(parent, path1, path2, paths2, date1, date2, size1, size2, qicon1, qicon2):
	#
	#	@argument <QWidget> parent : parent dialog
	#	@argument <str> path1 : path to the name to be moved from
	#	@argument <str> path2 : path to the name to be moved to
	#	@argument <list<str>> paths2 : paths in the same parent as path2
	#	@argument <int> date1 : date timestamp
	#	@argument <int> date2 : date timestamp
	#	@argument <int> size1 : number of bytes
	#	@argument <int> size2 : number of bytes
	#	@argument <QIcon> qicon1 : icon for path1
	#	@argument <QIcon> qicon2 : icon for path2
	#
	#	@description : returns the path2 renamed is required, None return is the
	#		ignore action
	#
	@staticmethod
	def fileAlreadyExists(parent, path1, path2, paths2, date1, date2, size1, size2, qicon1=None, qicon2=None):

		# Dialog
		dia = QtWidgets.QDialog()
		dia.setFixedSize(400, 550)
		dia.setWindowTitle("File Already Exists")

		# GUI
		gui = FileAlreadyExists(dia)

		# QSignal : response management
		response = None
		def __rename():
			nonlocal response
			nonlocal gui
			nonlocal warnings_msg
			nonlocal path2
			response = "/".join(path2.split("/")[:-1] + [gui.QLineEdit_rename.text()])
			if response in paths2:
				msg_renameItAgain = "Warning: the name you suggested also exists"
				if msg_renameItAgain in warnings_msg:
					pass
				else:
					warnings_msg.append(msg_renameItAgain)
				gui.QLabel_warnings.setText("\n".join(warnings_msg))
			if response == path2:
				msg_renameItAgain = "Warning: the name you suggested is the same"
				if msg_renameItAgain in warnings_msg:
					pass
				else:
					warnings_msg.append(msg_renameItAgain)
				gui.QLabel_warnings.setText("\n".join(warnings_msg))
			if response != path2 and response not in paths2:
				response = None
				dia.done(0)
		def __overwr():
			nonlocal response
			response = path2
			dia.done(0)
		def __cancel():
			nonlocal response
			response = None
			dia.done(0)

		gui.QPushButton_rename.clicked.connect(__rename)
		gui.QPushButton_overwr.clicked.connect(__overwr)
		gui.QPushButton_cancel.clicked.connect(__cancel)

		# Icons
		if qicon1 is None: qicon1 = QFileIconProvider().icon( QFileInfo("/home/d/Desktop/chocolate.txt") )
		if qicon2 is None: qicon2 = QFileIconProvider().icon( QFileInfo("/home/d/Desktop/chocolate.txt") )
		side_square_size = int(dia.size().width() / 2)-40
		gui.QLabel_icon1.resize(side_square_size,side_square_size)
		gui.QLabel_icon1.setPixmap(qicon1.pixmap(side_square_size, side_square_size))
		gui.QLabel_icon2.resize(side_square_size,side_square_size)
		gui.QLabel_icon2.setPixmap(qicon2.pixmap(side_square_size, side_square_size))

		# Clip paths
		gui.QLabel_path1.setText(QtGui.QFontMetrics(gui.QLabel_path1.font()).elidedText(path1, QtCore.Qt.ElideMiddle, int(dia.size().width() / 2)-20 ))
		gui.QLabel_path2.setText(QtGui.QFontMetrics(gui.QLabel_path2.font()).elidedText(path2, QtCore.Qt.ElideMiddle, int(dia.size().width() / 2)-20 ))

		# Dates
		gui.QLabel_date1.setText("Date:\n" + date1)
		gui.QLabel_date2.setText("Date:\n" + date2)

		# Sizes
		gui.QLabel_size1.setText("Size: " + humanfriendly.format_size(size1))
		gui.QLabel_size2.setText("Size: " + humanfriendly.format_size(size2))

		# Warnings
		warnings_msg = []
		if size2 > size1: warnings_msg.append("Warning: size destination is bigger")
		if date2 > date1: warnings_msg.append("Warning: date destination is more recent")
		gui.QLabel_warnings.setText("\n".join(warnings_msg))

		# Suggest name
		selection = path1.split("/")[-1]
		gui.QLineEdit_rename.setText(selection)
		gui.QLineEdit_rename.setSelection(0,len(selection))

		# ONLY WHEN THE MESSAGE BOX IS THE ONLY THING - TODO TODO TODO
		if not dia.exec_():
			return response

	############################################################################



if __name__ == "__main__":

	# First, create the app
	app = QtWidgets.QApplication(sys.argv)

	path2 = QMessageBox_addons.fileAlreadyExists(app, "/home/path/to/file/so/much/far/away/filename", "/home/path/to/file/so/much/far/away/filename", ["/home/path/to/file/so/much/far/away/filename"], "2019-01-01 23:59:58", "2019-01-01 23:59:59", 1, 2)
	print(path2)

	# When the dialog is closed, finish the application
	sys.exit(app.exec_())
