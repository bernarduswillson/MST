from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from Graph import*
from Prim import*
from Kruskal import*
from Utils import*
import os
import sys
import networkx as nx


class Ui_MainWindow(object):
    # initialize ui attributes
    def __init__(self):
        self.file_path = None
        self.node1_val = None
        self.node2_val = None
        self.weight_val = None
        self.total_cost = ""
        self.route_path = None
        self.runtime = 0

    # UI design setup
    def setupUi(self, MainWindow):
        # main window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 720))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # left frame
        self.left_frame = QtWidgets.QFrame(self.centralwidget)
        self.left_frame.setGeometry(QtCore.QRect(0, 0, 351, 701))
        self.left_frame.setStyleSheet("background-color:rgb(36, 31, 49)")
        self.left_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_frame.setObjectName("left_frame")

        # upload button
        self.upload_button = QtWidgets.QPushButton(self.left_frame)
        self.upload_button.setGeometry(QtCore.QRect(60, 130, 91, 31))
        self.upload_button.clicked.connect(self.open_file)
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.upload_button.setFont(font)
        self.upload_button.setStyleSheet("QPushButton {color: rgb(255, 255, 255); background-color: rgb(61, 56, 70); border-radius: 10px} QPushButton:hover {background-color: rgb(255, 255, 255); color: rgb(61, 56, 70)} QPushButton:pressed {background-color: rgb(41, 36, 50);}")
        self.upload_button.setObjectName("upload_button")

        # "choose file" label
        self.choose_file = QtWidgets.QLabel(self.left_frame)
        self.choose_file.setGeometry(QtCore.QRect(60, 100, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.choose_file.setFont(font)
        self.choose_file.setStyleSheet("color: rgb(255, 255, 255)")
        self.choose_file.setObjectName("choose_file")

        # "filename" label
        self.filename = QtWidgets.QLabel(self.left_frame)
        self.filename.setGeometry(QtCore.QRect(60, 170, 311, 17))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setItalic(True)
        self.filename.setFont(font)
        self.filename.setStyleSheet("color: rgb(255, 255, 255)")
        self.filename.setObjectName("filename")

        # kruskal radio button
        self.kruskal_button = QtWidgets.QRadioButton(self.left_frame)
        self.kruskal_button.setGeometry(QtCore.QRect(40, 495, 311, 23))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(True)
        self.kruskal_button.setFont(font)
        self.kruskal_button.setAutoFillBackground(False)
        self.kruskal_button.setStyleSheet("color: rgb(255, 255, 255);")
        self.kruskal_button.setChecked(True)
        self.kruskal_button.setObjectName("kruskal_button")

        # prim radio button
        self.prim_button = QtWidgets.QRadioButton(self.left_frame)
        self.prim_button.setGeometry(QtCore.QRect(40, 535, 311, 23))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(True)
        self.prim_button.setFont(font)
        self.prim_button.setStyleSheet("color: rgb(255, 255, 255)")
        self.prim_button.setObjectName("prim_button")

        # search button
        self.search_button = QtWidgets.QPushButton(self.left_frame)
        self.search_button.setGeometry(QtCore.QRect(60, 580, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.search_button.setFont(font)
        self.search_button.setStyleSheet("QPushButton {color: rgb(255, 255, 255); background-color: rgb(61, 56, 70); border-radius: 10px} QPushButton:hover {background-color: rgb(255, 255, 255); color: rgb(61, 56, 70)} QPushButton:pressed {background-color: rgb(41, 36, 50);}")
        self.search_button.clicked.connect(self.update_plot)

        # "Modify Node" label
        self.modify_node = QtWidgets.QLabel(self.left_frame)
        self.modify_node.setGeometry(QtCore.QRect(60, 220, 151, 30))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.modify_node.setFont(font)
        self.modify_node.setStyleSheet("color: rgb(255, 255, 255)")
        self.modify_node.setObjectName("modify_node")

        # "node" label
        self.node = QtWidgets.QLabel(self.left_frame)
        self.node.setGeometry(QtCore.QRect(60, 265, 291, 17))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setItalic(False)
        self.node.setFont(font)
        self.node.setStyleSheet("color: rgb(255, 255, 255)")
        self.node.setObjectName("node")

        # "Modify Edge" label
        self.modify_edge = QtWidgets.QLabel(self.left_frame)
        self.modify_edge.setGeometry(QtCore.QRect(190, 220, 151, 30))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.modify_edge.setFont(font)
        self.modify_edge.setStyleSheet("color: rgb(255, 255, 255)")
        self.modify_edge.setObjectName("modify_edge")

        # "node1" label
        self.node1 = QtWidgets.QLabel(self.left_frame)
        self.node1.setGeometry(QtCore.QRect(190, 265, 291, 17))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setItalic(False)
        self.node1.setFont(font)
        self.node1.setStyleSheet("color: rgb(255, 255, 255)")
        self.node1.setObjectName("node1")

        # "node2" label
        self.node2 = QtWidgets.QLabel(self.left_frame)
        self.node2.setGeometry(QtCore.QRect(190, 305, 291, 17))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setItalic(False)
        self.node2.setFont(font)
        self.node2.setStyleSheet("color: rgb(255, 255, 255)")
        self.node2.setObjectName("node2")

        # node input box
        self.node_input = QtWidgets.QLineEdit(self.left_frame)
        self.node_input.setGeometry(QtCore.QRect(120, 263, 31, 25))
        self.node_input.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);")
        self.node_input.setObjectName("node_input")
        self.node_input.textChanged.connect(self.node_value)

        # node1 input box
        self.node1_input = QtWidgets.QLineEdit(self.left_frame)
        self.node1_input.setGeometry(QtCore.QRect(250, 263, 31, 25))
        self.node1_input.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);")
        self.node1_input.setObjectName("node1_input")
        self.node1_input.textChanged.connect(self.node1_value)

        # node2 input box
        self.node2_input = QtWidgets.QLineEdit(self.left_frame)
        self.node2_input.setGeometry(QtCore.QRect(250, 303, 31, 25))
        self.node2_input.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);")
        self.node2_input.setObjectName("node2_input")
        self.node2_input.textChanged.connect(self.node2_value)

        # "weight_label" label
        self.weight_label = QtWidgets.QLabel(self.left_frame)
        self.weight_label.setGeometry(QtCore.QRect(190, 345, 291, 17))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setItalic(False)
        self.weight_label.setFont(font)
        self.weight_label.setStyleSheet("color: rgb(255, 255, 255)")
        self.weight_label.setObjectName("weight_label")

        # weight input box
        self.weight_input = QtWidgets.QLineEdit(self.left_frame)
        self.weight_input.setGeometry(QtCore.QRect(250, 343, 31, 25))
        self.weight_input.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);")
        self.weight_input.setObjectName("weight_input")
        self.weight_input.textChanged.connect(self.weight_value)

        # remove node button
        self.removen_button = QtWidgets.QPushButton(self.left_frame)
        self.removen_button.setGeometry(QtCore.QRect(60, 390, 95, 31))
        self.removen_button.clicked.connect(self.remove_node)
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.removen_button.setFont(font)
        self.removen_button.setStyleSheet("QPushButton {color: rgb(255, 255, 255); background-color: rgb(61, 56, 70); border-radius: 10px} QPushButton:hover {background-color: rgb(255, 255, 255); color: rgb(61, 56, 70)} QPushButton:pressed {background-color: rgb(41, 36, 50);}")
        self.removen_button.setObjectName("removen_button")

        # add edge button
        self.adde_button = QtWidgets.QPushButton(self.left_frame)
        self.adde_button.setGeometry(QtCore.QRect(190, 390, 95, 31))
        # self.adde_button.clicked.connect(self.open_file)
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.adde_button.setFont(font)
        self.adde_button.setStyleSheet("QPushButton {color: rgb(255, 255, 255); background-color: rgb(61, 56, 70); border-radius: 10px} QPushButton:hover {background-color: rgb(255, 255, 255); color: rgb(61, 56, 70)} QPushButton:pressed {background-color: rgb(41, 36, 50);}")
        self.adde_button.setObjectName("adde_button")

        # remove edge button
        self.removee_button = QtWidgets.QPushButton(self.left_frame)
        self.removee_button.setGeometry(QtCore.QRect(190, 430, 95, 31))
        self.removee_button.clicked.connect(self.remove_edge)
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.removee_button.setFont(font)
        self.removee_button.setStyleSheet("QPushButton {color: rgb(255, 255, 255); background-color: rgb(61, 56, 70); border-radius: 10px} QPushButton:hover {background-color: rgb(255, 255, 255); color: rgb(61, 56, 70)} QPushButton:pressed {background-color: rgb(41, 36, 50);}")
        self.removee_button.setObjectName("removee_button")

        # right frame
        self.right_frame = QtWidgets.QFrame(self.centralwidget)
        self.right_frame.setGeometry(QtCore.QRect(350, 0, 931, 701))
        self.right_frame.setStyleSheet("background-color:rgb(61, 56, 70)")
        self.right_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.right_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.right_frame.setObjectName("right_frame")

        # title label
        self.title = QtWidgets.QLabel(self.right_frame)
        self.title.setGeometry(QtCore.QRect(0, 0, 931, 81))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet("color: rgb(255, 255, 255)")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")

        # plot place holder
        self.widget = QtWidgets.QWidget(self.right_frame)
        self.widget.setGeometry(QtCore.QRect(0, 90, 931, 611))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.widget.setObjectName("widget")

        # "cost" label
        self.cost = QtWidgets.QLabel(self.widget)
        self.cost.setGeometry(QtCore.QRect(0, 529, 931, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setItalic(False)
        self.cost.setFont(font)
        self.cost.setStyleSheet("color: rgb(255,255,255); background-color: rgb(61, 56, 70);")
        self.cost.setObjectName("cost")

        # "route" label
        self.route = QtWidgets.QLabel(self.widget)
        self.route.setGeometry(QtCore.QRect(0, 560, 931, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setItalic(False)
        self.route.setFont(font)
        self.route.setStyleSheet("color: rgb(255,255,255); background-color: rgb(61, 56, 70);")
        self.route.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.route.setObjectName("route")

        self.web_view = QWebEngineView(self.centralwidget)
        self.web_view.setGeometry(QtCore.QRect(350, 90, 930, 530))
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        # set canvas
        widget_size = self.widget.size()
        self.figure = Figure(figsize=(widget_size.width(), widget_size.height()))
        self.widget.setFixedSize(widget_size)
        self.figure.set_size_inches(widget_size.width()/100, widget_size.height()/120)
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setParent(self.widget)
        self.graph = self.figure.add_subplot(111)
        self.graph.set_axis_off()

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MST Finder"))
        self.upload_button.setText(_translate("MainWindow", "Upload"))
        self.choose_file.setText(_translate("MainWindow", "Choose File"))
        self.filename.setText(_translate("MainWindow", "Filename:"))
        self.kruskal_button.setText(_translate("MainWindow", "Kruskal"))
        self.prim_button.setText(_translate("MainWindow", "Prim"))
        self.search_button.setText(_translate("MainWindow", "Search"))
        self.modify_node.setText(_translate("MainWindow", "Node"))
        self.modify_edge.setText(_translate("MainWindow", "Edge"))
        self.node.setText(_translate("MainWindow", "Node"))
        self.node1.setText(_translate("MainWindow", "Node 1 "))
        self.node2.setText(_translate("MainWindow", "Node 2 "))
        self.removen_button.setText(_translate("MainWindow", "Remove"))
        self.adde_button.setText(_translate("MainWindow", "Add"))
        self.removee_button.setText(_translate("MainWindow", "Remove"))
        self.weight_label.setText(_translate("MainWindow", "Weight"))
        self.title.setText(_translate("MainWindow", "Minimum Spanning Tree Finder"))
        self.cost.setText(_translate("MainWindow", "     Total Cost :"))
        self.route.setText(_translate("MainWindow", "     Steps : "))

    # open file dialog
    def open_file(self):
        file_dialog = QFileDialog()
        file_pathT, _ = file_dialog.getOpenFileName(None, "Open File", "", "Text Files (*.txt);;All Files (*.*)")

        # check if file path is not empty
        if file_pathT != "":
            self.file_path = file_pathT
            self.update_filename(os.path.basename(self.file_path))
            self.init_plot()

    # update filename label
    def update_filename(self, filename):
        self.filename.setText("Filename: " + filename)

    # update cost label
    def update_cost(self):
        self.cost.setText("     Total Cost : " + str(self.total_cost))

    # update route label
    def update_route(self):
        route_result = ""
        for i in range(len(self.route_path)):
            if i != len(self.route_path) - 1:
                route_result += str(self.route_path[i]) + " -> "
            else:
                route_result += str(self.route_path[i])
        self.route.setText("     Steps : " + str(route_result))

    # node value from input
    def node_value(self):
        self.node_val = self.node_input.text()

    # node1 value from input
    def node1_value(self):
        self.node1_val = self.node1_input.text()

    # node2 value from input
    def node2_value(self):
        self.node2_val = self.node2_input.text()

    def weight_value(self):
        self.weight_val = self.weight_input.text()

    # remove node
    def remove_node(self):
        # if file has been selected
        if self.file_path != None:
            # check if node value is valid
            try:
                # create graph
                graph = Graph()

                # remove node
                graph.remove_node_file(self.file_path, int(self.node_val))

                # update graph
                self.init_plot()

                # reset input
                self.node_input.setText("")
                
            except:
                # show error message
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error")
                msg.setInformativeText("Node value is not valid.")
                msg.setWindowTitle("Error Message")
                msg.setStandardButtons(QMessageBox.Ok)

                msg.exec_()

        # if file has not been selected
        else :
            # show error message
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText("Please input a file.")
            msg.setWindowTitle("Error Message")
            msg.setStandardButtons(QMessageBox.Ok)

            msg.exec_()

    # remove edge
    def remove_edge(self):
        # if file has been selected
        if self.file_path != None:
            # check if node value is valid
            try:
                # create graph
                graph = Graph()

                # remove edge
                graph.remove_edge_file(self.file_path, int(self.node1_val), int(self.node2_val))

                # update graph
                self.init_plot()

                # reset input
                self.node1_input.setText("")
                self.node2_input.setText("")
                
            except:
                # show error message
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error")
                msg.setInformativeText("Node value is not valid.")
                msg.setWindowTitle("Error Message")
                msg.setStandardButtons(QMessageBox.Ok)

                msg.exec_()

        # if file has not been selected
        else :
            # show error message
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText("Please input a file.")
            msg.setWindowTitle("Error Message")
            msg.setStandardButtons(QMessageBox.Ok)

            msg.exec_()

    # initialize plot
    def init_plot(self):

        # initialize graph
        graph = Graph()

        # try to open file with correct format
        try :
            # clear the previous plot
            self.graph.clear()

            # create graph
            G = nx.DiGraph()
            graph.createGraph(self.file_path)

            # insert edges to G
            for node in graph.nodes:
                for neighbor in graph.nodes[node]:
                    G.add_edge(node, neighbor, weight=graph.nodes[node][neighbor])

            # draw the NetworkX graph on the Matplotlib figure using kamada-kawai layout
            pos = nx.kamada_kawai_layout(G)
            nx.draw(G, pos, with_labels=True, node_size=500, node_color='black', font_size=10, font_color='white', font_weight='bold', ax=self.graph, arrows=False)

            #unhide canvas
            self.canvas.show()
            #hide webview
            self.web_view.hide()

            # Refresh the canvas
            self.canvas.draw()
        
        # if file input is not correct
        except:
            # show error message
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText("File input is invalid.")
            msg.setWindowTitle("Error Message")
            msg.setStandardButtons(QMessageBox.Ok)
            self.filename.setText("Filename: FILE INVALID")
            self.file_path = None

            #hide webview
            self.web_view.hide()
            #hide canvas
            self.canvas.hide()

            msg.exec_()

    # update plot when search button is clicked
    def update_plot(self):
        # clear the previous plot
        self.graph.clear()

        # initialize graph
        graph = Graph()

        # if file has been selected
        if self.file_path != None:
            #unhide canvas
            self.canvas.show()

            # create graph
            G = nx.DiGraph()
            graph.createGraph(self.file_path)

            # insert edges to G
            for node in graph.nodes:
                for neighbor in graph.nodes[node]:
                    G.add_edge(node, neighbor, weight=graph.nodes[node][neighbor])

            # if UCS is selected
            if self.kruskal_button.isChecked():
                kruskal = Kruskal(graph)
                pair = kruskal.result
                self.total_cost = kruskal.cost
                self.route_path = kruskal.result

            # if A* is selected
            elif self.prim_button.isChecked():
                prim = Prim(graph)
                pair = prim.result
                self.total_cost = prim.cost
                self.route_path = prim.result


            # draw the NetworkX graph on the Matplotlib figure, using kamada-kawai layout
            pos = nx.kamada_kawai_layout(G)
            nx.draw(G, pos, with_labels=True, node_size=500, node_color='black', font_size=10, font_color='white', font_weight='bold', ax=self.graph, arrows=False)
            nx.draw_networkx_edges(G, pos, edgelist=pair, edge_color='red', width=3, ax=self.graph, arrows=False)

            # Add numbers on red edges
            edge_labels = {(u, v): i+1 for i, (u, v) in enumerate(pair)}
            nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', ax=self.graph)

            # update the canvas
            self.canvas.draw()

            # update labels
            self.update_cost()
            self.update_route()
        
        # if file has not been selected
        else :
            # show error message
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText("Please input a file.")
            msg.setWindowTitle("Error Message")
            msg.setStandardButtons(QMessageBox.Ok)

            msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())