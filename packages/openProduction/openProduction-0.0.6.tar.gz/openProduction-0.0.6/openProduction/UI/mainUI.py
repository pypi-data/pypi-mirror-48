# -*- coding: utf-8 -*-
"""
Created on Fri May 31 11:29:17 2019

@author: Markus
"""
from openProduction.suite import TestSuiteIO, TestSuite, TestRunnerCli
from concurrent.futures import ThreadPoolExecutor, Future
from PyQt5 import QtCore, QtQml, QtMultimedia
from openProduction.station import Station
from openProduction.common import misc
from openProduction import log
import os
import logging
import time
import subprocess
import base64
import json

class RevisionModel(QtCore.QAbstractListModel):

    IDX_NAME = QtCore.Qt.UserRole
    IDX_DATE = QtCore.Qt.UserRole+1

    def __init__(self, parent=None):
        super(RevisionModel, self).__init__(parent)
        self.items = []

    def add_item(self, item):
        #self.beginInsertRows(QtCore.QModelIndex(),
        #                     self.rowCount(),
        #                     self.rowCount())

        self.items.append(item)
        #self.endInsertRows()

    def clearModel(self):
        #call self.endResetModel() after finishing with model
        self.beginResetModel()
        self.items = []

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self.items)

    @QtCore.pyqtSlot(int, result=str)
    def getName(self, index):
        try:
            return str(self.items[index][self.IDX_NAME])
        except IndexError:
            return ""

    @QtCore.pyqtSlot(int, result=str)
    def getDate(self, index):
        try:
            return self.items[index][self.IDX_DATE]
        except IndexError:
            return ""

    def data(self, index, role=QtCore.Qt.DisplayRole):
        try:
            rv =  self.items[index.row()][role]
            return rv
        except IndexError:
            return QtCore.QVariant()

    def roleNames(self):
        return {
            self.IDX_NAME: QtCore.QByteArray(b"name"),
            self.IDX_DATE: QtCore.QByteArray(b"date")
        }

class VersionModel(QtCore.QAbstractListModel):

    IDX_NAME = QtCore.Qt.UserRole
    IDX_COMMENT = QtCore.Qt.UserRole+1
    IDX_IMAGE = QtCore.Qt.UserRole+2

    def __init__(self, parent=None):
        super(VersionModel, self).__init__(parent)
        self.items = []

    def add_item(self, item):
        self.beginInsertRows(QtCore.QModelIndex(),
                             self.rowCount(),
                             self.rowCount())

        self.items.append(item)
        self.endInsertRows()

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self.items)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        try:
            return self.items[index.row()][role]
        except IndexError:
            return QtCore.QVariant()

    def roleNames(self):
        return {
            self.IDX_NAME: QtCore.QByteArray(b"name"),
            self.IDX_COMMENT: QtCore.QByteArray(b"comment"),
            self.IDX_IMAGE: QtCore.QByteArray(b"imageSource")
        }

class ProductModel(QtCore.QAbstractListModel):

    IDX_NAME = QtCore.Qt.UserRole
    IDX_DETAILS = QtCore.Qt.UserRole+1

    def __init__(self, parent=None):
        super(ProductModel, self).__init__(parent)
        self.items = []

    def add_item(self, item):
        #self.beginInsertRows(QtCore.QModelIndex(),
        #                     self.rowCount(),
        #                     self.rowCount())

        self.items.append(item)
        #self.endInsertRows()

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self.items)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        try:
            return self.items[index.row()][role]
        except IndexError:
            return QtCore.QVariant()

    def roleNames(self):
        return {
            self.IDX_NAME: QtCore.QByteArray(b"name"),
            self.IDX_DETAILS: QtCore.QByteArray(b"details")
        }

class Helper(QtCore.QObject):
    def __init__(self):
        super(Helper,self).__init__()

    @QtCore.pyqtSlot(str)
    def openExplorer(self, folderName):
        subprocess.Popen(r'explorer /select,"%s"'%folderName)

class MyLogger(logging.Handler, QtCore.QObject):

    newLogMessage = QtCore.pyqtSignal(str, name='newLogMessage')

    def __init__(self):
        logging.Handler.__init__(self)
        QtCore.QObject.__init__(self)

        self.txt = ""

    @QtCore.pyqtSlot()
    def resetLog(self):
        self.txt = ""

    @QtCore.pyqtSlot(result=str)
    def getErrorLog(self):
        return self.txt

    def emit(self, record):
        if record.levelno < logging.WARNING:
            self.newLogMessage.emit(record.msg)
        self.txt += self.format(record) + "\n"

class StepResultQML(QtCore.QObject):

    def __init__(self, stepResult):
        super(StepResultQML,self).__init__()
        self.stepResult = stepResult

    @QtCore.pyqtSlot(result=int)
    def getResult(self):
        return self.stepResult.result.value

    @QtCore.pyqtSlot(result=str)
    def getMessage(self):
        return self.stepResult.msg

    @QtCore.pyqtSlot(result=str)
    def getFullTCName(self):
        return self.stepResult.case.getFullName()

class TestRunnerQML(QtCore.QObject):

    stepStart = QtCore.pyqtSignal(str, int, int, name='stepStart')
    stepComplete = QtCore.pyqtSignal(TestSuite.SuiteState, int, str, str, int, int, name='stepComplete')
    sequenceComplete = QtCore.pyqtSignal(TestSuite.SuiteState, bool, float, str, name='sequenceComplete')
    sequenceStart = QtCore.pyqtSignal(TestSuite.SuiteState, name='sequenceStart')
    deviceIDSet = QtCore.pyqtSignal(str, name='deviceIDSet')
    errorOccured = QtCore.pyqtSignal(str, name='errorOccured')

    def __init__(self, testSuiteRunner, engine):
        super(TestRunnerQML,self).__init__()
        self.engine = engine
        self.testSuiteRunner = testSuiteRunner

        self.testSuiteRunner.sequenceStart.connect(self._onSequenceStartAsync)
        self.testSuiteRunner.sequenceComplete.connect(self._onSequenceCompleteAsync)
        self.testSuiteRunner.stepStart.connect(self._onStepStartAsync)
        self.testSuiteRunner.stepComplete.connect(self._onStepCompleteAsync)
        self.testSuiteRunner.deviceIDSet.connect(self._onDeviceIDSetAsync)
        self.testSuiteRunner.signalError.connect(self._onTestSuiteErrorAsync)
        self._stepResults = []
        self.stepTypes = TestSuite.StepType.LOAD
        self.suiteState = TestSuite.SuiteState.LOADING
        
    @QtCore.pyqtSlot()    
    def enaCliRunner(self):
        cli = TestRunnerCli.TestSuiteCliRunner(testSuiteRunner=self.testSuiteRunner)
        
    @QtCore.pyqtSlot(str)
    def setStepType(self, stepTypes):
        if stepTypes.lower() == "regular":
            self.stepTypes = TestSuite.StepType.REGULAR
            self.suiteState = TestSuite.SuiteState.REGULAR
        elif stepTypes.lower() == "load":
            self.stepTypes = TestSuite.StepType.LOAD
            self.suiteState = TestSuite.SuiteState.LOADING
        elif stepTypes.lower() == "unload":
            self.stepTypes = TestSuite.StepType.UNLOAD
            self.suiteState = TestSuite.SuiteState.UNLOADING
        else:
            raise RuntimeError("unsupported stepTypes %s"%str(stepTypes))

    @QtCore.pyqtSlot(result=bool)
    def isRunning(self):
        return self.testSuiteRunner.isExecuting

    @QtCore.pyqtSlot(result=list)
    def getTestCases(self):    
        nameOfCases = []
        cases = self.testSuiteRunner.testSuite.getTCs(self.stepTypes)
        for case in cases:
            nameOfCases.append(case.doc)
        return nameOfCases

    @QtCore.pyqtSlot()
    def loadSuite(self):
        future = self.testSuiteRunner.loadSuite()
        if self.stepTypes == TestSuite.StepType.REGULAR:
            future.result(timeout=10)
            self.testSuiteRunner.run()
    
    @QtCore.pyqtSlot(result=bool)        
    def run(self):
        rv = self.testSuiteRunner.run()
        if rv == None:
            rv = False
        else:
            rv = True
        return rv
    
    @QtCore.pyqtSlot()        
    def unloadSuite(self):
        self.testSuiteRunner.unloadSuite()
        
    def _onDeviceIDSetAsync(self, deviceID):
        self.deviceIDSet.emit(deviceID)

    def _onStepStartAsync(self, state, testCase, idx, numCases):
        if state == self.suiteState:
            self.stepStart.emit(testCase.doc, idx, numCases)

    def _onIOMessageAsync(self, msg):
        self.ioMessage.emit(msg)

    def _onSequenceCompleteAsync(self, state, suiteResult):
        if state == self.suiteState:
            success = suiteResult.isSuccessful()
            self.sequenceComplete.emit(state, success, suiteResult.executionTime, str(suiteResult.suite.values))

    def _onSequenceStartAsync(self, state):
        if state == self.suiteState:
            self.sequenceStart.emit(state)

    def _onStepCompleteAsync(self, state, stepRes, idx, numCases):
        if state == self.suiteState:
            self.stepComplete.emit(state, stepRes.result.value, stepRes.msg, stepRes.case.getFullName(), idx, numCases)
            
    def _onTestSuiteErrorAsync(self, msg):
        print("_onTestSuiteErrorAsync", msg)            
        self.errorOccured.emit(str(msg))

class OpenProductionQML(QtCore.QObject):
    def __init__(self, engine, workspace, stationName):
        super(OpenProductionQML,self).__init__()
        self.workspace = workspace
        self.stationName = stationName

    @QtCore.pyqtSlot(result=str)
    def getVersion(self):
        return misc.getVersion()

    @QtCore.pyqtSlot(result=str)
    def getWorkspace(self):
        return self.workspace

    @QtCore.pyqtSlot(result=str)
    def getStationName(self):
        return self.stationName

class StationQML(QtCore.QObject):

    productSaveComplete = QtCore.pyqtSignal(str, bool, int, name='productSaveComplete')
    asyncCallCompleted = QtCore.pyqtSignal(Future, QtCore.pyqtBoundSignal, name='asyncCallCompleted')
    productStationLoadCompleted = QtCore.pyqtSignal(name='productStationLoadCompleted')

    def __init__(self, engine):
        super(StationQML,self).__init__()
        self.engine = engine
        self.productVersions = None
        self.threadPool = ThreadPoolExecutor(5)
        self.revisionModel = None
        self.asyncCallCompleted.connect(self.onAsyncCallCompleted)

    def getStation(self):
        return Station.Station.getInstance()

    def _productSaveAsync(self, productName):
        ok, rev = self.productSaveChanges(productName)
        self.productSaveComplete.emit(productName, ok, rev)
        
    @QtCore.pyqtSlot(result=QtCore.QObject)
    def getLoadedProduct(self):
        station = self.getStation()
        product = None
        if station != None:
            product = station.loadedProduct
        if product != None:
            self.testRunner = TestRunnerQML(product.productRunner.suiteRunner ,self.engine)
            self.engine.setObjectOwnership(self.testRunner, QtQml.QQmlEngine.CppOwnership)
            return self.testRunner
        return None

    @QtCore.pyqtSlot(str, str, result=QtCore.QObject)
    def loadStationAsync(self, workspace, stationName):
        testRunner = Station.Station.loadStationAsync(workspace, stationName)
        self.testRunner = TestRunnerQML(testRunner ,self.engine)
        self.engine.setObjectOwnership(self.testRunner, QtQml.QQmlEngine.CppOwnership)
        return self.testRunner
    
    def onAsyncCallCompleted(self, future, successSig):
        if future.exception() == None:
            self.popup.hide()
            successSig.emit()
        else:
            self.popup.error()
    
    @QtCore.pyqtSlot(str, str, int)
    def loadProduct(self, productName, productVersion, revision):
        self.popup = BusyPopUp(self.engine)
        self.popup.setCaption("Lade %s '%s' (Rev %d)"%(productName, productVersion, revision))
        fut = self.threadPool.submit(self.getStation().loadProduct, productName, productVersion, revision)
        fut.add_done_callback(lambda future: self.asyncCallCompleted.emit(future, self.productStationLoadCompleted))

    @QtCore.pyqtSlot(result=list)
    def getProducts(self):
        start = time.time()
        rv, products = self.getStation().listProducts()
        print ("timing getProducts: ", time.time() - start)
        if products == None:
            products = []
        return products

    @QtCore.pyqtSlot(result=QtCore.QObject)
    def getProductModel(self):
        start = time.time()
        self.productModel = ProductModel()
        self.engine.setObjectOwnership(self.productModel, QtQml.QQmlEngine.CppOwnership)

        rv, products = self.getStation().listProducts()
        
        if products != None:
            for prod in products:
                item = {}
                item[ProductModel.IDX_NAME] = prod["name"]
                item[ProductModel.IDX_DETAILS] = prod["description"]
                self.productModel.add_item(item)

        print ("timing getProductModel: ", time.time() - start, self.productModel)
        return self.productModel

    @QtCore.pyqtSlot(str, result=QtCore.QObject)
    def getVersionModel(self, productName):
        start = time.time()
        self.versionModel = VersionModel()
        self.engine.setObjectOwnership(self.versionModel, QtQml.QQmlEngine.CppOwnership)

        rv, self.productVersions = self.getStation().listProductVersions(productName)
        
        if self.productVersions != None:
            for vers in self.productVersions:
                item = {}
                item[VersionModel.IDX_NAME] = vers["version"]
                item[VersionModel.IDX_COMMENT] = vers["description"]
                base64Image = base64.b64encode(vers["image"])
                item[VersionModel.IDX_IMAGE] = "data:image/png;base64,"+base64Image.decode()
                self.versionModel.add_item(item)


        print ("timing getVersionModel: ", time.time() - start, self.versionModel)

        return self.versionModel

    @QtCore.pyqtSlot(result=QtCore.QObject)
    def getRevisionModel(self):
        start = time.time()
        if self.revisionModel != None:
            del self.revisionModel
        self.revisionModel = RevisionModel()
        self.engine.setObjectOwnership(self.revisionModel, QtQml.QQmlEngine.CppOwnership)
        print ("timing getRevisionModel: ", time.time() - start, self.revisionModel)
        return self.revisionModel



    @QtCore.pyqtSlot(str, str)
    def reloadRevisionModel(self, productName, productVersion):
        start = time.time()
        if self.revisionModel != None:
            self.revisionModel.clearModel()

        rv, revisions = self.getStation().listProductRevisions(productName, productVersion)
        if revisions != None:
            for rev in revisions:
                item = {}
                item[RevisionModel.IDX_NAME] = rev["revision_id"]
                item[RevisionModel.IDX_DATE] = rev["date"].strftime('%Y-%m-%d %H:%M')
                self.revisionModel.add_item(item)

        self.revisionModel.endResetModel()
        print ("timing reloadRevisionModel: ", time.time() - start)
        
class BusyPopUp(QtCore.QObject):

    def __init__(self, engine):
        super(BusyPopUp,self).__init__()
        self.engine = engine
        
        self.mainWindow = engine.rootObjects()[0]
        self.busyWindow = engine.rootObjects()[1]
        self.busyWindow.setProperty("visible", True)
        
        
        widthMain = self.mainWindow.property("width")
        width = self.busyWindow.property("width")
        xMain = self.mainWindow.property("x")
        x = round((widthMain - width) / 2)
        
        heightMain = self.mainWindow.property("height")
        height = self.busyWindow.property("height")
        yMain = self.mainWindow.property("y")
        y = round((heightMain - height) / 2)        
        
        self.busyWindow.setProperty("x", x+xMain)
        self.busyWindow.setProperty("y", y+yMain)
        self.busyWindow.errorBtnPressed.connect(self.onErrorButtonPressed)
        
        self.overlay = self.mainWindow.findChild(QtCore.QObject, "disableOverlay")
        self.overlay.setProperty("visible", True)
        
    @QtCore.pyqtSlot()
    def onErrorButtonPressed(self):
        self.mainWindow.onErrorOccured()
        self.hide()
        
    def setCaption(self, caption):
        self.busyWindow.setProperty("caption", caption)

    def error(self):
        self.busyWindow.setErrorState()
        
    def hide(self):
        self.busyWindow.setProperty("visible", False)
        self.overlay.setProperty("visible", False)
        
        
class PlaySound(QtCore.QObject):
    def __init__(self, rootPath):
        super(PlaySound,self).__init__()
        self.folder = os.path.join(rootPath, "ProductRun")
    
    @QtCore.pyqtSlot()    
    def playSuccess(self):
        QtMultimedia.QSound.play(os.path.join(self.folder, "success.wav"))

    @QtCore.pyqtSlot()
    def playError(self):
        QtMultimedia.QSound.play(os.path.join(self.folder, "error.wav"))
        
        
class UIRunner:
    def __init__(self, workspace):
        log.initLogger()
        
        self.logger = logging.getLogger(misc.getAppName())
        
        self.logger.info("trying to open workspace config file")
        f = open(os.path.join(workspace, "config.json"))
        workspaceCfg = json.load(f)
        f.close()
        
        stationName = workspaceCfg["station"]
        self.logger.info("station name is %s"%stationName)
        
        ioHandler = TestSuiteIO.BaseIOHandler()

        myPath = os.path.split(os.path.abspath(__file__))[0]
        qmlFolder = os.path.join(myPath, "qml")

        self.qmlEngine = QtQml.QQmlApplicationEngine()
        self.qmlStation = StationQML(self.qmlEngine)

        context = self.qmlEngine.rootContext()
        context.setContextProperty("station", self.qmlStation)

        self.openProduction = OpenProductionQML(self.qmlEngine, workspace, stationName)
        context.setContextProperty("openProduction", self.openProduction)

        self.helper = Helper()
        context.setContextProperty("helper", self.helper)


        logger = logging.getLogger(misc.getAppName())
        self.logStream = MyLogger()
        self.logStream.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        logger.addHandler(self.logStream)
        context.setContextProperty("logger", self.logStream)


        self.playSound = PlaySound(qmlFolder)
        context.setContextProperty("playSound", self.playSound)

        # Load the qml file into the engine
        f = os.path.join(qmlFolder, "main.qml")
        self.qmlEngine.load(f)

        qmlFolder = os.path.join(qmlFolder, "Common")
        f = os.path.join(qmlFolder, "BusyIndicationWindow.qml")
        self.qmlEngine.load(f)

